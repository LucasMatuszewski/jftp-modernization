# Repository map comparisons and distribution follow-up

Review date: 2026-10-07. This continues the first-installation review after the user's request for discoverable files, timings, additional languages, setup guidance and signing analysis.

The [first-installation review](../legacy-codebase-workflows-first-run-review.md) retains the original error and binary-download evidence. Current benchmark binaries came from successful [CI run 37633697013](https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37633697013), source `8d922e517fe81d6fa978b37611e57bd6f1f7bfbc`. The checked Releases API returned an empty list; these are Actions artifacts, not Release assets. Current source instructions did not expose a durable, pinned installation route at first entry, and a historical CI link led to an older source build. That explains the discovery/search detour; it does not establish that Release binaries were silently overlooked.

## Saved maps

| Examined code | Python report | Rust report | Parsed files | Raw map equality |
| --- | --- | --- | ---: | --- |
| JFTP Java, `src/main/java` | [Python](jftp-java.python.md) | [Rust](jftp-java.rust.md) | 182 | Identical |
| Private TypeScript application | Retained locally; Git-ignored | Retained locally; Git-ignored | 416 | Identical |
| Flask 3.1.2 Python, `src/flask` | [Python](flask-python.python.md) | [Rust](flask-python.rust.md) | 24 | Different; explained below |
| Toolbox native mapper Rust, `src/legacy-repo-map` | [Python](toolbox-rust.python.md) | [Rust](toolbox-rust.rust.md) | 6 | Identical |

Each report has named `.raw.md`, `.meta.json` and `.inventory.json` sidecars. Headers show the individual measured generation time, revision, coverage, definitions, truncation, bytes/characters and approximate raw/report tokens. Header timing is the last warm sample for that exported map; the table below uses medians of all five samples. A report has more estimated tokens than its raw map because the statistics header adds text.

The scoped `.gitattributes` preserves generated Markdown/JSON bytes across Git checkouts so saved hashes remain valid. The human review index alone uses normalized LF text.

## Timing comparison

End-to-end subprocess wall time, median of **five cold-output and five warm-output runs per implementation**, budget 4096. Execution order alternates. Cold means a fresh output directory/tag cache; OS filesystem caches were not flushed. Windows and Linux figures are compared only within each row, not against each other.

| Corpus / platform | Python cold / warm | Rust cold / warm | Python time divided by Rust, cold / warm |
| --- | ---: | ---: | ---: |
| JFTP / Windows x86-64 | 5.155 / 4.970 s | 1.182 / 1.215 s | 4.36x / 4.09x |
| Edukey Payload / WSL Linux x86-64 | 1.441 / 0.938 s | 0.502 / 0.445 s | 2.87x / 2.11x |
| Flask / WSL Linux x86-64 | 0.427 / 0.415 s | 0.083 / 0.100 s | 5.13x / 4.16x |
| Native mapper crate / WSL Linux x86-64 | 0.457 / 0.416 s | 0.097 / 0.093 s | 4.72x / 4.48x |

Raw commands, all 60 public-corpus samples, min/max ranges, medians, output directories, coverage and parity checks are in [benchmark-results.json](benchmark-results.json). The 20 private-corpus samples are retained in a Git-ignored local JSON file. Rust is faster on these inputs; the Flask ratio measures differing extraction output and must not be presented as a speedup for equivalent reference results. Both tools reported no parse failures in these scopes. Their source inventories/hashes remained equal across all samples. This is map-generation verification; none of the target applications was built or run.

Inputs are pinned in each sidecar. Flask was shallow-cloned from the public Pallets repository at tag `3.1.2`, commit `2c1b30d0503cfb064f1cb252e6614a06915a362a`. The TypeScript source is the existing WSL Edukey application; its dirty working-copy fingerprint identifies the examined bytes. The Rust scope is the toolbox mapper's source, not generated dependencies or Cargo build output.

## Python parity result

Flask has 416 definitions in the reference Python map and 502 in Rust. Comparing full extracted tags found 1,584 Python tags and 1,670 Rust tags: **86 Rust-only definitions, zero Python-only tags**. Examples are assignments such as type variables, Click option objects and the Flask CLI instance. This is consistent with the documented grammar-shape difference for assignments; the compact maps consequently differ despite equal source fingerprints.

[python-tag-differences.json](python-tag-differences.json) retains sample names, source paths and original lines. These are different extraction results, not crashes. Python remains usable for navigation through either implementation, but Rust cannot be advertised as byte-equivalent to the Python reference for Python code. Exact reference behavior still selects Python source or its frozen bundle.

## Source update and output contract

The source skill is updated on `/home/lucas/DEV/Projects/agent-toolbox`, branch `skill/legacy-map-output-guidance`. Installed copies were not edited or rolled out.

Reviewable local source commits: `aa4005c` (export helper and regression tests) and `8c100ea` (output/setup/distribution instructions).

The updated entrypoint tells agents to announce a destination and link exact files afterward. The default is `<repository>/docs/repo-maps`; the user may override it. Agents ask only for genuine destination conflicts or a read-only repository. Low-level Python/Rust programs still accept `--output-dir` and generate fixed names outside the examined source tree. The new standard-library helper exports the existing result with a custom `--output-file`, while preserving the mapper's staging/cache boundary:

```bash
python /path/to/skill/scripts/export_repo_map.py /path/to/repository --artifact-dir /path/to/staging --implementation rust --output-file /path/to/repository/docs/repo-maps/module.rust.md --elapsed-seconds 0.42
```

`0.42` is illustrative; the real elapsed time must come from a measured generation. Omit it to show "not measured". Existing files require explicit `--force`. The helper verifies complete status, source identity, raw-map hash, revision/fingerprint consistency and coverage before creating reports. It retains the original raw `map_sha256`; report-specific hashes/stats are under the metadata's `export` namespace. The exporter itself uses Python's standard library, even for a map generated by the Rust standalone program.

Sixteen focused tests pass on both Windows and Linux. The toolbox Node structure suite passes all 37 tests. Tests cover defaults/custom names, hashes/token statistics, source preservation, failed/incomplete input, bad timing, collision handling and interrupted publication. No Cargo build was needed for these benchmarks. Existing CI binaries were checksum-verified; the new export helper and guidance are source-branch changes and are not present in those older binaries.

Export publication is not a transaction across all four files. Normal hard-link publication and explicit replacement are atomic per file; filesystems without hard-link support use exclusive creation, which prevents overwriting but exposes partial bytes while copying. Forced updates invalidate the old report after staging, before replacing evidence, and publish the report last. An interrupted update therefore cannot leave an old readable report beside mixed-generation evidence. Concurrent exports to the same destination are unsupported. Independent re-review confirmed that all three original helper findings are addressed.

## Preferred installation and publication

Final recommendation: keep binaries out of Git history. Build each supported platform in CI, then publish **versioned release assets** with notices, SHA-256 checksums, build provenance and a distribution manifest. GitHub Releases are intended to package downloadable binaries independently of source history. [GitHub release documentation](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases).

Ship a small `tool-distribution.json` with the skill, pinning compatible source/tool versions and exact asset URLs/hashes. A setup script detects the executing OS/CPU, downloads one compatible package, verifies/extracts it into a versioned user cache and performs a smoke check. Updating the skill updates its manifest; ordinary map generation uses the installed pinned version offline. Avoid automatically choosing "latest" on every run because grammar/query/policy behavior may drift. An explicit update operation can resolve a newer approved release and record that choice.

Keep machine-specific setup status in the user cache, not in shared `SKILL.md`: `missing`, `ready`, `stale` or `unsupported`, plus executable path/version and verification result. The entrypoint should tell the agent to run this local check and choose setup only if necessary. A static "To do" in installed instructions becomes inaccurate across machines and reinstallations.

The source update documents this installer/manifest design honestly as **proposed**. It does not yet implement an automatic downloader, release workflow, setup-status command, signing integration or fleet rollout. Current binary delivery remains expiring Actions artifacts, with source-only installation as the fallback. A reviewable source branch comes before publishing; no releases or pushes were made during this task.

## Unsigned executables and platform delivery

The actual Windows EXE tested here is unsigned. Download used authenticated `gh run download`, followed by checksum verification and ZIP extraction. Its inspected file streams had no `Zone.Identifier`. The native CLI ran normally; no policy change, certificate bypass, `Unblock-File` or security disabling was performed.

That local result does not establish browser-download behavior. Windows reputation and managed-device controls can warn or block; signing helps identify the publisher but does not guarantee zero warnings. [Microsoft's signing and SmartScreen guidance](https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/smartscreen-reputation). A signing service/certificate can be evaluated later; it was not required for this host's test. If a user's policy blocks unsigned code, the agent should use Python source or an approved installation route.

Linux native execution was actually tested in WSL. It needs matching architecture, executable permissions and a compatible loader/libc; checksums are still required. This establishes this Linux environment, not all distributions.

No consumer Mac was available. macOS ARM64 CI success proves build/runner execution but does not prove that a quarantined user download passes Gatekeeper. Broad delivery should use Developer ID signing and notarization, plus a fresh-download consumer test; offer Python source until native delivery is verified. [Apple signing guidance](https://developer.apple.com/documentation/xcode/creating-distribution-signed-code-for-the-mac/), [Apple notarization guidance](https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution). The skill should not automatically disable Gatekeeper or remove quarantine.

## Parser and tokenizer design

The Rust mapper uses existing pinned Tree-sitter grammar crates, with the same vendored Aider definition/reference queries embedded at compilation. It does not contain hand-written parsers for each language. Custom/adapted code handles selection, safe reads, tag extraction orchestration, hashing, Aider/NetworkX PageRank and rendering. Bare-name relationships are navigation evidence, not resolved types, overloads or a compiler call graph.

Source-supported query categories are **Java, Python, JavaScript/JSX, TypeScript, TSX, C, C++, C#, Go and Rust**. TypeScript and TSX use two grammar variants from one crate. Scope evidence here covers Java, TypeScript/TSX, Python and Rust; do not call the remaining languages comprehensively validated solely because their queries compile. `.h` currently selects C; `.pyi`, `.mts`, `.cts` and `.hxx` are not symbol-parsed by the extension policy. XML/properties/build configuration remains inventory-only and must be read directly for wiring.

For current token statistics, `ceil(Unicode characters / 4)` is sufficient as a clearly labeled heuristic. GitHub's [`bpe-openai`](https://github.com/github/rust-gems/tree/main/crates/bpe-openai) is a suitable candidate for optional named-tokenizer counts; it supports offline dictionaries and efficient counting. Exact-tokenizer mode should be separate from heuristic selection budgeting. Binary-size/startup cost has not been measured, so no size-impact claim is made and no new crate was added.

## Original map locations

The first review generated maps outside the source repository, as the installed skill required:

- Python: `%TEMP%\legacy-skill-review-20261007-05bd\current-source-java\repo-map.md`.
- Rust: `%TEMP%\legacy-skill-review-20261007-05bd\current-rust-java\repo-map.md`.
- Frozen Python: `%TEMP%\legacy-skill-review-20261007-05bd\current-bundle-java\repo-map.md`.

Each directory contains `inventory.json` and `map.meta.json`. Single-run timings existed in the first review, but were not a repeated benchmark. This review has published named report copies here with their measurement details and preserved raw maps/sidecars.

## Findings recorded as observed

- The Windows Rust EXE's Authenticode status is `NotSigned`; its signer certificate is absent. The file has only the normal `:$DATA` stream and no observed `Zone.Identifier`. It ran after checksum verification through `gh` download and ZIP extraction. No execution-policy change, security-feature disabling, certificate bypass, or unblocking command was used. Its successful CLI execution does not prove that browser downloads on fresh/managed endpoints will run without warnings.
- A source-research lookup for an assumed `vendor/tree_sitter_tags.py` failed with `No such file or directory`. That assumed helper does not exist; Python tag extraction is in `scripts/repo_map.py`. This is an exploratory lookup error, not a mapper runtime defect.
- `herdr workspace list --json` is not supported by this installed runner; it returns usage. `workspace list` already emits JSON. Calling `herdr` through a non-login WSL command also misses the user PATH; its verified absolute path is `/home/lucas/.local/bin/herdr`.
- The source checkout was clean on the unrelated `skill/write-agents-md` branch. That branch and its unmerged commits were preserved; this work uses a new `skill/legacy-map-output-guidance` branch based on current `origin/main`.
- The user refined the distribution preference: avoid accumulating binary versions in Git history. This review now favors versioned release assets, a pinned install manifest, platform-aware setup and a local readiness check. The earlier compressed-in-skill proposal remains historical context, not the final recommendation.
- Linux first setup attempt failed: `python3 -m venv` could not run because `ensurepip` / `python3.14-venv` is unavailable. The documented isolated `pip --target` fallback is being used; no system package installation is required.
- A delegate's initial `wsl -d Ubuntu` command failed because this machine's actual distribution is named `Ubuntu-26.04`. This is environment discovery, not a mapper failure.
- Python-tag comparison initially failed with `KeyError: 'path'`: the Rust debug output groups tags by source path and omits that path from each tag. The comparison adapter must retain the dictionary key when flattening. This is a review-script schema assumption, not an error from either mapper.
- Independent exporter review reproduced three helper robustness defects in temporary fixtures: both absent fingerprint fields compared equal (`None == None`); normal publication depended on hard-link support; an injected failure during `--force` could leave an old report beside partly replaced evidence. These are exporter defects, not Python/Rust mapper failures. All three are fixed with regression tests; the existing eight real exports have valid hashes/fingerprints.
- A Windows regression test initially decoded Unicode with the default system locale; its read now explicitly uses UTF-8. The helper already used UTF-8; this was a test portability defect.
- A final tracker-reference lookup assumed `references/beads.md` and failed with `Cannot find path`. The actual reference was located from the skill's file list. This was a guessed documentation path, not a tracker or mapper runtime failure.
- The documentation-index edit produced mixed LF/CRLF line endings and a Git conversion warning. The touched index was restored to CRLF before staging. Generated raw/annotated map bytes were not normalized because their saved hashes identify the original bytes.
- Staged source checks flagged a trailing carriage return on the final line of the new exporter and test file after Windows edits. Both source files were normalized to the toolbox's LF convention, then restaged and checked. This was a formatting defect, not a test or mapper failure.
- This checkout has `core.autocrlf=true`; automatic conversion on future checkout could invalidate raw/report SHA-256 values. A scoped `.gitattributes` now preserves generated evidence bytes, and staged blobs are checked against their recorded hashes. The source instructions also explain this when exports are committed.
- The first staged evidence whitespace check flagged CRLF endings in the separately assembled benchmark JSON after byte preservation was enabled. That review-generated JSON was normalized to LF; the hash-bearing raw maps, annotated reports and original inventory copies stayed byte-identical.
- The completion-note tool call initially failed before shell execution with JavaScript `SyntaxError: Invalid or unexpected token`: a multiline shell string was passed as a single-line JavaScript string literal. It was retried with a proper multiline literal. No tracker write or artifact change occurred from the failed call.
- A one-line review validation command failed with `SyntaxError` because its intended line breaks reached Python as literal `\n` escapes. The check was moved to a temporary script; exported maps were not affected.

- **Benchmark complete — jftp-java (Windows x86-64):** five cold-output and five repeat-output runs per implementation, alternating order. `{"cold": {"medians": {"python": 5.154987999936566, "rust": 1.182366699911654}, "min_max": {"python": [4.465791600057855, 5.824442599900067], "rust": [1.1038408000022173, 1.2653915998525918]}, "python_over_rust": 4.3598893645446415, "rust_time_reduction_percent": 77.06363817090936}, "warm": {"medians": {"python": 4.970142799895257, "rust": 1.2152543999254704}, "min_max": {"python": [4.276483200024813, 5.264316499931738], "rust": [1.1550534998532385, 1.3556966001633555]}, "python_over_rust": 4.08979617782093, "rust_time_reduction_percent": 75.54890374676798}}`. Parity: `{"map_bytes_equal": true, "fingerprint_equal": true, "coverage_equal": true}`.

- **Benchmark complete — edukey-typescript (Ubuntu-26.04 WSL2 x86-64):** five cold-output and five repeat-output runs per implementation, alternating order. `{"cold": {"medians": {"python": 1.440895926207304, "rust": 0.5016182139515877}, "min_max": {"python": [1.2915093021001667, 1.6696557451505214], "rust": [0.4336778009310365, 0.5271676010452211]}, "python_over_rust": 2.87249522870469, "rust_time_reduction_percent": 65.18706140894321}, "warm": {"medians": {"python": 0.9376807052176446, "rust": 0.44523730082437396}, "min_max": {"python": [0.8475979010108858, 0.95939652598463], "rust": [0.4320514118298888, 0.46653301315382123]}, "python_over_rust": 2.106024592911449, "rust_time_reduction_percent": 52.51717366616495}}`. Parity: `{"map_bytes_equal": true, "fingerprint_equal": true, "coverage_equal": true}`.

- **Benchmark complete — flask-python (Ubuntu-26.04 WSL2 x86-64):** five cold-output and five repeat-output runs per implementation, alternating order. `{"cold": {"medians": {"python": 0.4273715098388493, "rust": 0.08338750107213855}, "min_max": {"python": [0.3936319090425968, 0.4438374100718647], "rust": [0.0774707009550184, 0.0998427018057555]}, "python_over_rust": 5.125126719760196, "rust_time_reduction_percent": 80.48828732088815}, "warm": {"medians": {"python": 0.41495110909454525, "rust": 0.0998110028449446}, "min_max": {"python": [0.37356970901601017, 0.45816081017255783], "rust": [0.07639060192741454, 0.11679580202326179]}, "python_over_rust": 4.15736839894463, "rust_time_reduction_percent": 75.94632219136858}}`. Parity: `{"map_bytes_equal": false, "fingerprint_equal": true, "coverage_equal": false}`.

- **Benchmark complete — toolbox-rust (Ubuntu-26.04 WSL2 x86-64):** five cold-output and five repeat-output runs per implementation, alternating order. `{"cold": {"medians": {"python": 0.45722031011246145, "rust": 0.09693850390613079}, "min_max": {"python": [0.4328628091607243, 0.6492460248991847], "rust": [0.08008650317788124, 0.1317653029691428]}, "python_over_rust": 4.716601677236582, "rust_time_reduction_percent": 78.79829444096937}, "warm": {"medians": {"python": 0.41557381581515074, "rust": 0.092765002977103}, "min_max": {"python": [0.35663550812751055, 0.4514747099019587], "rust": [0.07557100220583379, 0.1556265060789883]}, "python_over_rust": 4.4798555756822, "rust_time_reduction_percent": 77.6778518167359}}`. Parity: `{"map_bytes_equal": true, "fingerprint_equal": true, "coverage_equal": true}`.
