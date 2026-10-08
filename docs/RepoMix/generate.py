"""Generate and verify pinned Repomix packs; writes only this report directory.

Populate the npm cache first: npx --yes repomix@1.18.1 --version
Then run: python docs/RepoMix/generate.py
Requires Python 3.12+ and Node.js. No application build or startup is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import time
import xml.etree.ElementTree as ET


VERSION = "1.18.1"
OUTPUT = Path(__file__).resolve().parent
REPOSITORY = OUTPUT.parent.parent


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_snapshot() -> dict[str, dict]:
    paths = sorted((REPOSITORY / "src").rglob("*.java"))
    paths.append(REPOSITORY / "pom.xml")
    return {
        path.relative_to(REPOSITORY).as_posix(): {
            "sha256": sha256(path.read_bytes()),
            "bytes": path.stat().st_size,
        }
        for path in paths
    }


def locate_cli(explicit: str | None) -> Path:
    if explicit:
        candidates = [Path(explicit).resolve()]
    else:
        cache = (
            Path(os.environ["LOCALAPPDATA"]) / "npm-cache" / "_npx"
            if os.name == "nt"
            else Path.home() / ".npm" / "_npx"
        )
        candidates = []
        for package in sorted(cache.glob("*/node_modules/repomix/package.json")):
            metadata = json.loads(package.read_text(encoding="utf-8"))
            if metadata["version"] == VERSION:
                entry = metadata["bin"]
                candidates.append(package.parent / (entry if isinstance(entry, str) else entry["repomix"]))
    node = shutil.which("node")
    if not node:
        raise RuntimeError("Node.js is required")
    for cli in candidates:
        if cli.is_file():
            probe = subprocess.run(
                [node, str(cli), "--version"], capture_output=True, text=True, check=True
            )
            if probe.stdout.strip() == VERSION:
                return cli
    raise RuntimeError(
        f"Repomix {VERSION} unavailable. Run npx --yes repomix@{VERSION} --version, "
        "or provide --repomix-cli /path/to/repomix/bin/repomix.cjs."
    )


def normalize(text: str) -> str:
    return text.replace("\r\n", "\n").rstrip("\n")


def parse_pack(path: Path, expected: set[str]) -> dict[str, str]:
    tree = ET.parse(path)
    elements = tree.findall(".//file")
    paths = [element.attrib["path"] for element in elements]
    if len(paths) != len(set(paths)) or set(paths) != expected:
        raise RuntimeError(f"Pack coverage mismatch: {path.name}")
    return {element.attrib["path"]: element.text or "" for element in elements}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repomix-cli", help="Pinned package's JavaScript entrypoint")
    args = parser.parse_args()
    cli = locate_cli(args.repomix_cli)
    node = shutil.which("node")
    before = source_snapshot()
    revision = subprocess.check_output(
        ["git", "-C", str(REPOSITORY), "rev-parse", "HEAD"], text=True
    ).strip()
    source_status = subprocess.check_output(
        ["git", "-C", str(REPOSITORY), "status", "--porcelain", "--", "src", "pom.xml"],
        text=True,
    ).splitlines()
    # Fixed scope, regardless of any config/history edits by other repository agents.
    config_path = OUTPUT / "repomix.config.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))
    if config["include"] != ["src/**/*.java", "pom.xml"]:
        raise RuntimeError("Unexpected include scope; update verification before changing it")
    staging = Path(tempfile.mkdtemp(prefix="jftp-repomix-"))
    if staging.is_relative_to(REPOSITORY):
        raise RuntimeError("Generation staging must remain outside the repository")
    result = {
        "tool": "Repomix",
        "version": VERSION,
        "date": time.strftime("%Y-%m-%d"),
        "source_revision": revision,
        "source_working_copy_status": source_status,
        "source_files": before,
        "scope": config["include"],
        "config_sha256": sha256(config_path.read_bytes()),
        "token_encoding": config["tokenCount"]["encoding"],
        "security_check_enabled": config["security"]["enableSecurityCheck"],
        "runs": {},
    }
    pack_contents = {}
    for mode in ("full", "compressed"):
        pack = staging / f"jftp-source.{mode}.xml"
        command = [
            node, str(cli), str(REPOSITORY), "--config", str(config_path),
            "--include", "src/**/*.java,pom.xml", "--style", "xml",
            "--parsable-style", "--no-git-sort-by-changes",
            "--token-count-encoding", "o200k_base", "--output", str(pack),
        ]
        if mode == "compressed":
            command.append("--compress")
        start = time.perf_counter()
        process = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        elapsed = time.perf_counter() - start
        log = re.sub(r"\x1b\[[0-?]*[ -/]*[@-~]", "", process.stdout + process.stderr)
        (staging / f"{mode}.log").write_text(log, encoding="utf-8")
        if process.returncode:
            raise RuntimeError(f"{mode} failed; inspect {staging / (mode + '.log')}")
        token_matches = re.findall(r"Total Tokens:\s*([\d,]+)", log)
        file_matches = re.findall(r"Total Files:\s*([\d,]+)", log)
        if not token_matches or not file_matches:
            raise RuntimeError(f"Missing measured statistics in {mode} log: {staging}")
        files = parse_pack(pack, set(before))
        pack_contents[mode] = files
        if int(file_matches[-1].replace(",", "")) != len(before):
            raise RuntimeError(f"Unexpected reported file count: {mode}")
        if mode == "full":
            for path, text in files.items():
                original = (REPOSITORY / path).read_text(encoding="utf-8")
                if normalize(text) != normalize(original):
                    raise RuntimeError(f"Full-source content mismatch: {path}")
        data = pack.read_bytes()
        result["runs"][mode] = {
            "command": command,
            "elapsed_seconds": elapsed,
            "files": len(files),
            "tokens": int(token_matches[-1].replace(",", "")),
            "utf8_bytes": len(data),
            "characters": len(data.decode("utf-8")),
            "sha256": sha256(data),
            "xml_valid": True,
            "exact_file_coverage": True,
            "full_contents_match_source": mode == "full",
            "security_log_no_suspicious_files": "No suspicious files detected" in log,
        }
        print(f"{mode}: {len(files)} files, {result['runs'][mode]['tokens']:,} tokens", flush=True)
    after = source_snapshot()
    if before != after:
        raise RuntimeError(f"Sources changed during packing; regenerate. Staging: {staging}")
    result["sources_unchanged_during_generation"] = True
    full = result["runs"]["full"]["tokens"]
    compressed = result["runs"]["compressed"]["tokens"]
    result["tokens_saved"] = full - compressed
    result["token_reduction_percent"] = (full - compressed) * 100 / full
    result["citations"] = []
    for path, quote in (
        ("src/main/java/com/myjavaworld/util/ResourceLoader.java", "ClassLoader loader) {"),
        ("src/main/java/com/myjavaworld/jftp/LocalFile.java", "if (obj == null) {"),
    ):
        original = (REPOSITORY / path).read_text(encoding="utf-8")
        matches = [i for i, line in enumerate(original.splitlines(), 1) if quote in line]
        if len(matches) == 1:
            result["citations"].append({
                "path": path, "sha256": before[path]["sha256"],
                "start_line": matches[0], "end_line": matches[0], "quote": quote,
                "in_full_pack": quote in pack_contents["full"][path],
                "in_compressed_pack": quote in pack_contents["compressed"][path],
                "claim": "Observed retention/omission in these generated packs only",
            })
    # Publish only after both outputs, source retention and coverage checks succeed.
    for mode in ("full", "compressed"):
        for filename in (f"jftp-source.{mode}.xml", f"{mode}.log"):
            shutil.copyfile(staging / filename, OUTPUT / filename)
    (OUTPUT / "manifest.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    rows = []
    for mode in ("full", "compressed"):
        stats = result["runs"][mode]
        rows.append(
            f"| {mode.capitalize()} | {stats['files']} | {stats['tokens']:,} | "
            f"{stats['utf8_bytes']:,} | {stats['elapsed_seconds']:.3f} s |"
        )
    readme = (
        "# JFTP Repomix source packs\n\n"
        f"Generated {result['date']} from revision `{revision}` using Repomix **{VERSION}**. "
        "All Java sources below `src/` plus `pom.xml` are included. "
        f"This snapshot contains {sum(path.endswith('.java') for path in before)} "
        "Java sources and one Maven descriptor. "
        "Resources, images, help, assembly/launcher files, third-party binaries, agent tooling "
        "and documentation are outside this source-code scope.\n\n"
        "- [Compressed source](jftp-source.compressed.xml): reduced structural context.\n"
        "- [Full source reference](jftp-source.full.xml): complete text for behavior/signature checks.\n"
        "- [Manifest](manifest.json): original paths/hashes, commands, measured statistics and verification.\n\n"
        "| Pack | Files | o200k_base tokens | UTF-8 bytes | Generation wall time |\n"
        "|---|---:|---:|---:|---:|\n" + "\n".join(rows) + "\n\n"
        f"Compression saved **{result['tokens_saved']:,} tokens "
        f"({result['token_reduction_percent']:.2f}%)** in this source scope. "
        "Counts are reported by Repomix using `o200k_base`; they are not model-independent "
        "billing/context counts. Timings are individual subprocess measurements with the npm "
        "package cache already populated, not a benchmark.\n\n"
        "## Verification and compression limits\n\n"
        "Both packs parse as XML, contain each expected path exactly once, and omit no "
        "selected file. Every full-pack file equals its original after CRLF-to-LF and "
        "trailing-newline normalization. Original byte hashes were unchanged before and "
        "after packing. Security scanning remained enabled; inspect [full.log](full.log) "
        "and [compressed.log](compressed.log) for the actual CLI reports.\n\n"
        "Compression is lossy within files. The manifest records source-hash/line evidence "
        "and retention checks for `ResourceLoader.getBundle`'s `ClassLoader loader` "
        "parameter continuation and `LocalFile.compareTo`'s null guard. In this snapshot "
        "both are retained in the full pack and omitted from the compressed pack. "
        "Other logic can also disappear; file coverage does not prove declaration or "
        "behavior coverage. Use original source/full XML for edits and behavior analysis. "
        "Packed output line numbers are not original-source line numbers.\n\n"
        "## Reproduce\n\n"
        "From the repository root with Node.js and Python 3.12+ available:\n\n"
        "```powershell\n"
        f"npx --yes repomix@{VERSION} --version\n"
        "python docs/RepoMix/generate.py\n"
        "```\n\n"
        "The first command obtains the pinned npm package when absent. The generator "
        "uses that cached package's Node entrypoint, validates its version, and applies "
        "[the explicit configuration](repomix.config.json). For a custom npm cache, pass "
        "`--repomix-cli /path/to/repomix/bin/repomix.cjs`. Generation stages outside the "
        "repository and publishes artifacts here only after source/coverage validation. "
        "It never builds or launches JFTP. Concurrent edits outside the source scope "
        "are excluded; source changes during generation fail verification. Regeneration "
        "updates these files and this measured report.\n\n"
        "Only `docs/RepoMix/` is owned by this task; RepoMap work remains separate. "
        "Generated XML and JSON bytes are preserved by this directory's Git attributes "
        "so hashes survive platform checkout.\n"
    )
    (OUTPUT / "README.md").write_text(readme, encoding="utf-8")
    print(f"Token reduction: {result['token_reduction_percent']:.2f}%", flush=True)
    print(f"Verified packs saved in {OUTPUT}; generation staging: {staging}", flush=True)


if __name__ == "__main__":
    main()
