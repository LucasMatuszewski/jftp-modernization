#!/usr/bin/env python3
"""Offline Codex rollout audit. Never uploads logs or exports their raw text.

Recorded API usage is exact as reported. Text token counts are estimates; even
with tiktoken they exclude request framing, unrecorded tool schemas and hidden
reasoning. Historical text volume is not an instantaneous context snapshot.
"""
import argparse
import collections
import hashlib
import json
import math
from pathlib import Path
import re
import sqlite3
import sys


class TokenMeter:
    def __init__(self, encoding="chars"):
        self.encoding_name = encoding
        self.encoder = None
        if encoding != "chars":
            try:
                import tiktoken
            except ImportError as exc:
                raise ValueError("Install tiktoken in an isolated tool environment, or use --encoding chars.") from exc
            self.encoder = tiktoken.get_encoding(encoding)

    def count(self, text):
        if self.encoder is None:
            return math.ceil(len(text) / 4)
        return len(self.encoder.encode(text, disallowed_special=()))

    def measure(self, text):
        return {"characters": len(text), "utf8_bytes": len(text.encode("utf-8")), "estimated_tokens": self.count(text)}


def read_records(path):
    """Snapshot a live log; tolerate only an incomplete, unterminated last line."""
    path = Path(path)
    lines = path.read_bytes().splitlines(keepends=True)
    records = []
    for ordinal, raw in enumerate(lines):
        try:
            record = json.loads(raw)
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            if ordinal == len(lines) - 1 and not raw.endswith(b"\n"):
                break
            raise ValueError(f"Malformed record in {path.name}, line {ordinal + 1}") from exc
        if not isinstance(record, dict) or not isinstance(record.get("payload"), dict):
            raise ValueError(f"Unsupported record in {path.name}, line {ordinal + 1}")
        record.update(_source=str(path), _line=ordinal + 1, _ordinal=ordinal)
        records.append(record)
    return records


def find_session(sessions_dir, session_id):
    if not re.fullmatch(r"[A-Za-z0-9_-]+", session_id):
        raise ValueError("Unsafe session identifier")
    matches = list(Path(sessions_dir).rglob(f"*{session_id}.jsonl"))
    if len(matches) != 1:
        raise ValueError(f"Expected one rollout for {session_id}, found {len(matches)}")
    return matches[0]


def load_lineage(path, sessions_dir, seen=None, limit=None):
    """Reconstruct fork inheritance using recorded exclusive rollout ordinals."""
    seen = set() if seen is None else seen
    path = Path(path).resolve()
    if path in seen:
        raise ValueError("Cycle in session ancestry")
    seen.add(path)
    records = read_records(path)
    if limit is not None:
        if not isinstance(limit, int) or limit < 1 or limit > len(records):
            raise ValueError("Inherited rollout prefix is missing or has invalid bounds")
        records = records[:limit]
    meta = next((r["payload"] for r in records if r["type"] == "session_meta"), None)
    if meta is None:
        raise ValueError(f"No session metadata in {path.name}")
    parent = meta.get("history_base") or {}
    parent_id = parent.get("thread_id", meta.get("forked_from_id"))
    parent_limit = parent.get("end_ordinal_exclusive", meta.get("forked_from_ordinal_exclusive"))
    previous, sources = [], []
    if parent_id:
        if parent_limit is None:
            raise ValueError("Fork ancestry has no recorded cutoff; refusing to include later parent activity")
        previous, sources = load_lineage(find_session(sessions_dir, parent_id), sessions_dir, seen, parent_limit)
    sources.append({"session_id": meta.get("id"), "log_file": path.name, "records_included": len(records),
                    "log_bytes_on_disk": path.stat().st_size, "included_log_sha256": hashlib.sha256(
                        b"".join(path.read_bytes().splitlines(keepends=True)[:len(records)])).hexdigest(),
                    "source": meta.get("source"), "forked_from": parent_id})
    return previous + records, sources


def text_of(value):
    """Only visible text. Never tokenize encrypted reasoning or media bytes."""
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return "\n".join(text_of(v) for v in value)
    if isinstance(value, dict):
        if isinstance(value.get("text"), str):
            return value["text"]
        if isinstance(value.get("content"), list):
            return text_of(value["content"])
    return ""


def add_size(target, size):
    for key in ("characters", "utf8_bytes", "estimated_tokens"):
        target[key] = target.get(key, 0) + size[key]
    target["items"] = target.get("items", 0) + 1


def message_parts(role, text):
    if role == "user":
        category = "user_messages"
        if text.startswith("# AGENTS.md instructions"):
            category = "repository_and_environment_instructions"
        elif "<skill>" in text:
            category = "invoked_skill_instructions"
        return [(category, text)]
    if role == "assistant":
        return [("assistant_messages", text)]
    if role not in ("developer", "system"):
        return [("other_messages", text)]
    parts, cursor = [], 0
    for match in re.finditer(r"<skills_instructions>.*?</skills_instructions>", text, re.S):
        before = text[cursor:match.start()]
        if before:
            parts.append(("memory_instructions" if before.lstrip().startswith("## Memory") else "developer_and_system_instructions", before))
        parts.append(("skill_catalog", match.group()))
        cursor = match.end()
    rest = text[cursor:]
    if rest:
        parts.append(("memory_instructions" if rest.lstrip().startswith("## Memory") else "developer_and_system_instructions", rest))
    return parts


def call_commands(code):
    commands = []
    for match in re.finditer(r'\b(?:"cmd"|cmd)\s*:\s*("(?:\\.|[^"\\])*")', code):
        try:
            commands.append(json.loads(match.group(1)))
        except json.JSONDecodeError:
            pass
    return commands


def skill_reads(code, output, meter):
    """Secondary attribution: match logged Markdown reads against visible stdout.

    This estimates decoded content, not its surrounding JSON escaping. It is a
    subset diagnostic, not an additional row in the main context totals.
    """
    stdout = []
    for block in output if isinstance(output, list) else [{"text": text_of(output)}]:
        text = text_of(block)
        try:
            obj = json.loads(text)
            if isinstance(obj, dict) and isinstance(obj.get("output"), str):
                stdout.append(obj["output"])
        except json.JSONDecodeError:
            pass
    visible = "\n".join(stdout).replace("\r\n", "\n")
    # Some shell adapters preserve literal escaped CR/LF in their stdout.
    visible = visible.replace("\\r\\n", "\n")
    attributed, occupied = [], []
    for command in call_commands(code):
        for match in re.finditer(r"Get-Content\s+-LiteralPath\s+['\"]([^'\"]+)['\"](?:\s+-TotalCount\s+(\d+))?", command, re.I):
            path, count = match.groups()
            normalized = path.replace("\\", "/")
            if "/skills/" not in normalized or not normalized.lower().endswith(".md"):
                continue
            suffix = normalized.split("/skills/", 1)[1]
            if ".." in normalized.split("/") or not re.fullmatch(r"[^/]+/(?:SKILL\.md|references/.+\.md)", suffix):
                continue
            try:
                source = Path(path).read_bytes().decode("utf-8").replace("\r\n", "\n")
            except (OSError, UnicodeDecodeError):
                continue
            if count:
                source = "".join(source.splitlines(keepends=True)[:int(count)])
            if not source:
                continue
            start = visible.find(source[:min(100, len(source))])
            if start < 0:
                continue
            length = 0
            for a, b in zip(source, visible[start:]):
                if a != b:
                    break
                length += 1
            if length < min(100, len(source)) or any(start < end and start + length > begin for begin, end in occupied):
                continue
            occupied.append((start, start + length))
            attributed.append({"document": normalized.split("/skills/", 1)[1],
                               "matched_current_file_prefix": True, "complete_excerpt": length >= len(source.rstrip()),
                               **meter.measure(visible[start:start + length])})
    return attributed


def tool_inventory(tools, meter):
    groups, largest = {}, []
    for tool in tools or []:
        name, description = tool.get("name", "unknown"), tool.get("description", "")
        if not isinstance(description, str):
            continue
        namespace = "__".join(name.split("__")[:2]) if "__" in name else "builtins"
        add_size(groups.setdefault(namespace, {}), meter.measure(description))
        largest.append({"name": name, **meter.measure(description)})
    return {"proves_prompt_inclusion": False,
            "interpretation": "Available code-mode descriptions only; not loaded request schemas or measured prompt cost.",
            "groups": groups, "largest_descriptions": sorted(largest, key=lambda x: x["estimated_tokens"], reverse=True)[:15]}


def analyze(records, meter, tool_catalog=None, attribute_reads=False):
    categories, entries, catalog_entries, calls, usages, fallback_usages = {}, [], [], {}, [], []
    seen_responses, seen_fallback, world, encrypted_chars, compactions = set(), set(), {}, 0, []
    thread_id, tools_called = None, collections.Counter()
    window = None
    base = next((r["payload"].get("base_instructions", {}).get("text", "") for r in reversed(records) if r["type"] == "session_meta"), "")

    def add(category, text, record, **extra):
        if not text:
            return
        size = meter.measure(text)
        add_size(categories.setdefault(category, {}), size)
        entries.append({"category": category, "line": record.get("_line"),
                        "log_file": Path(record.get("_source", "")).name, "timestamp": record.get("timestamp"),
                        **size, **extra})
        return entries[-1]

    if base:
        add("base_instructions", base, {})
    for record in records:
        kind, payload = record["type"], record["payload"]
        if kind == "session_meta":
            thread_id = payload.get("id")
        elif kind == "world_state":
            if payload.get("full"):
                world = {}
            world.update(payload.get("state", {}))
        elif kind == "compacted":
            compactions.append({"line": record.get("_line"), "timestamp": record.get("timestamp")})
        elif kind == "event_msg":
            if payload.get("type") == "token_count" and payload.get("info"):
                info = payload["info"]
                window = info.get("model_context_window") or window
                if info.get("last_token_usage"):
                    signature = (thread_id, json.dumps(info.get("total_token_usage", info["last_token_usage"]), sort_keys=True))
                    if signature not in seen_fallback:
                        seen_fallback.add(signature)
                        fallback_usages.append({"timestamp": record.get("timestamp"), "line": record.get("_line"),
                                                "thread_id": thread_id, "usage": info["last_token_usage"]})
            elif payload.get("type") == "task_started":
                window = payload.get("model_context_window") or window
        elif kind == "token_usage_record":
            thread_id = payload.get("thread_id") or thread_id
            identity = payload.get("response_id")
            if identity and identity in seen_responses:
                continue
            seen_responses.add(identity)
            usages.append({"timestamp": record.get("timestamp"), "line": record.get("_line"),
                           "thread_id": payload.get("thread_id"), "turn_id": payload.get("turn_id"),
                           "usage": payload.get("usage", {}), "reported_thread_total": payload.get("thread_token_usage")})
        elif kind == "response_item":
            item_type = payload.get("type")
            if item_type == "message":
                for category, text in message_parts(payload.get("role"), text_of(payload.get("content", []))):
                    add(category, text, record)
                    if category == "skill_catalog":
                        for line in text.splitlines():
                            if re.match(r"^- [^:]+:.*\(file:", line):
                                catalog_entries.append({"name": line[2:].split(": ", 1)[0], **meter.measure(line)})
            elif item_type in ("custom_tool_call", "function_call"):
                code = payload.get("input", payload.get("arguments", ""))
                if not isinstance(code, str):
                    code = json.dumps(code, ensure_ascii=False)
                calls[payload.get("call_id")] = code
                nested = re.findall(r"\btools\.([A-Za-z0-9_]+)\s*\(", code)
                tools_called.update(nested or [payload.get("name", "unknown")])
                add("tool_call_arguments", code, record, tool=payload.get("name"),
                    nested_tools=sorted(set(nested)))
            elif item_type in ("custom_tool_call_output", "function_call_output"):
                entry = add("tool_results", text_of(payload.get("output", "")), record, call_id=payload.get("call_id"))
                if attribute_reads and entry:
                    code = calls.get(payload.get("call_id"), "")
                    entry["skill_read_content_subset"] = skill_reads(code, payload.get("output", ""), meter)
            elif item_type == "reasoning":
                encrypted_chars += len(payload.get("encrypted_content") or "")
                add("visible_reasoning_summaries", text_of(payload.get("summary", [])), record)
    # Newer forks may have per-response records while their ancestors only have
    # token_count events. Keep both versions without counting their mirrors.
    direct_threads = {u.get("thread_id") for u in usages}
    usages += [u for u in fallback_usages if u.get("thread_id") not in direct_threads]
    usages.sort(key=lambda u: u.get("timestamp") or "")
    sums = {key: sum(u["usage"].get(key, 0) for u in usages) for key in
            ("input_tokens", "cached_input_tokens", "cache_write_input_tokens", "output_tokens", "reasoning_output_tokens")}
    inputs = [u["usage"].get("input_tokens", 0) for u in usages]
    total = sum(v["estimated_tokens"] for v in categories.values())
    for size in categories.values():
        size["percent_of_recorded_text_estimate"] = round(100 * size["estimated_tokens"] / total, 2) if total else 0
    world_sizes = {}
    for key, value in world.items():
        text = value.get("body", value.get("text", "")) if isinstance(value, dict) else (value if isinstance(value, str) else "")
        if text:
            world_sizes[key] = meter.measure(text)
    skill_totals = {}
    for entry in entries:
        for read in entry.get("skill_read_content_subset", []):
            add_size(skill_totals.setdefault(read["document"], {}), read)
    return {
        "estimator": meter.encoding_name,
        "interpretation": "Historical visible text volume, not an instantaneous reconstructed API prompt; percentages use only these estimated text tokens.",
        "categories": categories, "visible_text_estimated_tokens": total,
        "usage": {"calls": len(usages), "context_window_tokens": window,
                  "first_input_tokens": inputs[0] if inputs else None,
                  "last_input_tokens": inputs[-1] if inputs else None,
                  "peak_input_tokens": max(inputs) if inputs else None,
                  "peak_input_percent_of_window": round(100 * max(inputs) / window, 2) if inputs and window else None,
                  "cumulative_input_tokens": sums["input_tokens"],
                  "cumulative_cached_input_tokens": sums["cached_input_tokens"],
                  "cumulative_cache_write_input_tokens": sums["cache_write_input_tokens"],
                  "cached_fraction_percent": round(100 * sums["cached_input_tokens"] / sums["input_tokens"], 2) if sums["input_tokens"] else None,
                  "cumulative_uncached_input_tokens": sums["input_tokens"] - sums["cached_input_tokens"],
                  "cumulative_output_tokens": sums["output_tokens"],
                  "cumulative_reasoning_output_tokens": sums["reasoning_output_tokens"],
                  "output_includes_reasoning_do_not_add_twice": True,
                  "timeline": usages},
        "skill_catalog_entries": sorted(catalog_entries, key=lambda x: x["estimated_tokens"], reverse=True),
        "skill_read_content_subset": skill_totals,
        "largest_items": sorted(entries, key=lambda x: x["estimated_tokens"], reverse=True)[:20],
        "entries": entries,
        "available_tools": tool_inventory(tool_catalog, meter),
        "tool_names_in_call_code_counts": dict(tools_called),
        "tool_call_count_policy": "Syntactic calls inside orchestration code, not proof of nested execution success.",
        "world_state_diagnostics": world_sizes,
        "world_state_not_added_to_text_total": True,
        "encrypted_reasoning_characters_not_tokenized": encrypted_chars,
        "compactions": compactions,
        "limitations": [
            "No full request payload/schema snapshot in rollout: exact attribution of MCP/tool definitions is unavailable.",
            "Available/deferred tool descriptions are not proof of prompt inclusion; description sizes exclude parameter schemas.",
            "World state, UI item_completed events and token_count mirrors are not additional conversation messages.",
            "Encrypted reasoning payload size is not a token count; reasoning usage is already a subset of reported output.",
            "Input usage sums measure repeated processing, not occupied context; cached inputs still belong to processed input.",
            "No reliable live-context reconstruction after compaction or instruction replacement from text volume alone.",
            "Text estimates omit message framing and internal formatting; o200k_base is a proxy, not a verified model tokenizer.",
            "Files created on disk do not occupy context unless their content or summaries are included in a request.",
        ],
    }


def db_diagnostics(codex_home, session_ids):
    """Read-only, session-filtered diagnostics. Export counts and safe numeric fields."""
    result = {"logs": {}, "dynamic_tools": {}, "errors": []}
    for name in ("logs_2.sqlite", "state_5.sqlite", "thread_history_1.sqlite"):
        path = Path(codex_home) / name
        if not path.exists():
            continue
        try:
            with sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True) as db:
                db.execute("PRAGMA query_only=ON")
                for sid in session_ids:
                    if name == "logs_2.sqlite":
                        rows = db.execute("SELECT target,feedback_log_body FROM logs WHERE thread_id=? ORDER BY id", (sid,)).fetchall()
                        stats = collections.Counter(target for target, _ in rows)
                        metrics, omitted_servers = [], set()
                        for target, body in rows:
                            if target.endswith("render_observability") or target.endswith("session::turn"):
                                numbers = dict((key, int(value)) for key, value in re.findall(
                                    r"\b(budget_limit|total_skills|included_skills|omitted_skills|truncated_skill_descriptions|total_usage_tokens|full_context_window_limit|auto_compact_scope_limit)=(?:Some\()?(\d+)(?![\w-])", body))
                                if numbers:
                                    metrics.append({"target": target, "numbers": numbers})
                            if "omitting MCP server without an exact ready client" in body:
                                match = re.search(r"server_name=([A-Za-z0-9_-]+)", body)
                                if match:
                                    omitted_servers.add(match.group(1))
                        result["logs"][sid] = {"target_record_counts": dict(stats), "context_and_skill_metrics": metrics,
                                               "not_ready_mcp_servers_omitted": sorted(omitted_servers)}
                    elif name == "state_5.sqlite":
                        rows = db.execute("SELECT namespace,defer_loading,count(*),sum(length(description)),sum(length(input_schema)) FROM thread_dynamic_tools WHERE thread_id=? GROUP BY namespace,defer_loading", (sid,)).fetchall()
                        result["dynamic_tools"][sid] = [{"namespace": r[0], "deferred": r[1], "count": r[2], "description_characters": r[3], "schema_characters": r[4]} for r in rows]
                    else:
                        count = db.execute("SELECT count(*) FROM thread_items WHERE thread_id=?", (sid,)).fetchone()[0]
                        result.setdefault("history_projection_counts_not_added", {})[sid] = count
        except sqlite3.Error as exc:
            result["errors"].append({"database": name, "error_type": type(exc).__name__})
    return result


def config_metadata(path):
    import tomllib
    with Path(path).open("rb") as stream:
        config = tomllib.load(stream)
    # Never export commands, arguments, URLs, environment or authentication fields.
    return {"mcp_servers": {name: {"enabled": value.get("enabled", True),
                                   "enabled_tools": value.get("enabled_tools"), "disabled_tools": value.get("disabled_tools")}
                            for name, value in config.get("mcp_servers", {}).items()},
            "features": {key: value for key, value in config.get("features", {}).items() if isinstance(value, bool)},
            "configuration_does_not_prove_session_loading": True}


def markdown_report(report):
    analysis = report["analysis"]
    usage = analysis["usage"]
    lines = ["# Codex session context audit", "", "Offline snapshot. Numeric aggregates only; no raw conversation or command text.", "",
             "## Recorded model usage", "", "| Metric | Value |", "|---|---:|"]
    for key in ("calls", "context_window_tokens", "first_input_tokens", "last_input_tokens", "peak_input_tokens",
                "peak_input_percent_of_window", "cumulative_input_tokens", "cumulative_cached_input_tokens",
                "cached_fraction_percent", "cumulative_uncached_input_tokens", "cumulative_output_tokens", "cumulative_reasoning_output_tokens"):
        lines.append(f"| {key} | {usage[key]} |")
    lines += ["", "Input totals include repeated history. Cached input is a subset, not extra context. Output includes reasoning.", "",
              "## Estimated recorded text volume", "", f"Estimator: `{analysis['estimator']}`. Historical recorded text, not instantaneous context.", "",
              "| Component | Characters | Estimated text tokens | Share of text estimate |", "|---|---:|---:|---:|"]
    for key, value in sorted(analysis["categories"].items(), key=lambda kv: kv[1]["estimated_tokens"], reverse=True):
        lines.append(f"| {key} | {value['characters']} | {value['estimated_tokens']} | {value['percent_of_recorded_text_estimate']}% |")
    lines += ["", "## Skill content read through commands", "", "Secondary decoded-content subset; already part of tool results. Do not add it again.", "",
              "| Document | Matching reads | Estimated decoded text tokens |", "|---|---:|---:|"]
    for key, value in sorted(analysis["skill_read_content_subset"].items(), key=lambda kv: kv[1]["estimated_tokens"], reverse=True):
        lines.append(f"| {key} | {value['items']} | {value['estimated_tokens']} |")
    lines += ["", "## Largest tool results", "", "| Log line | Estimated tokens |", "|---|---:|"]
    for entry in sorted((e for e in analysis["entries"] if e["category"] == "tool_results"), key=lambda e: e["estimated_tokens"], reverse=True)[:10]:
        lines.append(f"| {entry['log_file']}:{entry['line']} | {entry['estimated_tokens']} |")
    if analysis["available_tools"]["groups"]:
        lines += ["", "## Available tool description inventory", "", "Availability does not establish prompt inclusion. Schemas and framing are excluded.", "",
                  "| Namespace | Descriptions | Potential description tokens |", "|---|---:|---:|"]
        for key, value in sorted(analysis["available_tools"]["groups"].items(), key=lambda kv: kv[1]["estimated_tokens"], reverse=True):
            lines.append(f"| {key} | {value['items']} | {value['estimated_tokens']} |")
    if report.get("auxiliary_sessions"):
        lines += ["", "## Separate auxiliary contexts", "", "These API inputs belong to separate contexts; do not add them to root-window occupancy.", ""]
        for aux in report["auxiliary_sessions"]:
            u = aux["analysis"]["usage"]
            lines.append(f"- {aux['session_id']}: {u['calls']} calls, {u['cumulative_input_tokens']} cumulative input tokens, {u['peak_input_tokens']} peak input.")
    lines += ["", "## Limitations", ""] + [f"- {line}" for line in analysis["limitations"]]
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("session", type=Path, help="Current root/fork rollout JSONL; follows inherited prefixes")
    parser.add_argument("--sessions-dir", type=Path, help="Ancestor lookup root; defaults to the input file's directory")
    parser.add_argument("--end-ordinal", type=int, help="Exclusive record cutoff in the selected log, for a reproducible snapshot")
    parser.add_argument("--encoding", default="chars", help="chars (stdlib), or explicit tiktoken encoding such as o200k_base")
    parser.add_argument("--output-dir", type=Path, required=True, help="Local output directory, outside publishable source")
    parser.add_argument("--tool-catalog", type=Path, help="Optional [{name, description}] available-tool metadata snapshot")
    parser.add_argument("--attribute-skill-reads", action="store_true", help="Match visible logged reads against current local skill Markdown")
    parser.add_argument("--codex-home", type=Path, help="Optional read-only, session-filtered SQLite diagnostics")
    parser.add_argument("--config", type=Path, help="Optional TOML: export only MCP names/enable flags and Boolean features")
    parser.add_argument("--auxiliary-session", type=Path, action="append", default=[], help="Separate approval/subagent context; never added to root occupancy")
    parser.add_argument("--artifact-file", type=Path, action="append", default=[], help="Record a related disk file's size without reading its content or adding it to context")
    args = parser.parse_args(argv)
    try:
        meter = TokenMeter(args.encoding)
        records, sources = load_lineage(args.session, args.sessions_dir or args.session.parent, limit=args.end_ordinal)
        catalog = json.loads(args.tool_catalog.read_text(encoding="utf-8")) if args.tool_catalog else None
        if catalog is not None and (not isinstance(catalog, list) or any(not isinstance(t, dict) for t in catalog)):
            raise ValueError("Tool catalog must be an array of tool metadata objects")
        report = {"format_version": 1, "sources": sources, "analysis": analyze(records, meter, catalog, args.attribute_skill_reads)}
        report["auxiliary_sessions"] = []
        for path in args.auxiliary_session:
            aux_records = read_records(path)
            meta = next(r["payload"] for r in aux_records if r["type"] == "session_meta")
            report["auxiliary_sessions"].append({"session_id": meta.get("id"), "source": meta.get("source"),
                                                 "analysis": analyze(aux_records, meter)})
        if args.codex_home:
            report["database_diagnostics"] = db_diagnostics(args.codex_home, [s["session_id"] for s in sources])
        if args.config:
            report["current_configuration_metadata"] = config_metadata(args.config)
        report["disk_artifacts_not_added_to_context"] = [{"filename": path.name, "bytes_on_disk": path.stat().st_size}
                                                       for path in args.artifact_file]
        args.output_dir.mkdir(parents=True, exist_ok=True)
        (args.output_dir / "context-audit.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (args.output_dir / "context-audit.md").write_text(markdown_report(report), encoding="utf-8")
        print(json.dumps({"report": str(args.output_dir / "context-audit.md"), "data": str(args.output_dir / "context-audit.json"),
                          "estimated_recorded_text_tokens": report["analysis"]["visible_text_estimated_tokens"],
                          "recorded_peak_input_tokens": report["analysis"]["usage"]["peak_input_tokens"]}))
    except (OSError, ValueError, KeyError, StopIteration) as exc:
        print(f"Audit failed ({type(exc).__name__}): {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
