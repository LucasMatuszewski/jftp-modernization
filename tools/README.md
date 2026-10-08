# Offline Codex context audit

`analyze_codex_context.py` analyzes a selected local Codex rollout and its
recorded fork ancestry. It produces `context-audit.json` and `context-audit.md`
with aggregate statistics, log line references and token-usage timelines.
Raw messages, commands, credentials and encrypted reasoning are not exported.
It does not call an API, start JFTP or change Codex configuration.

Python 3.11+ suffices for the standard-library character estimate. For a better
plain-text estimate, install `tiktoken` into an isolated tools environment and
pass `--encoding o200k_base`. That encoding is a proxy: neither local tokenizer
mode reproduces full model-request token accounting. The tokenizer may fetch
its encoding data on first use; subsequent analysis is offline.

```powershell
python tools/analyze_codex_context.py '<selected-rollout.jsonl>' `
  --output-dir "$env:TEMP/codex-context-audit" `
  --codex-home "$env:USERPROFILE/.codex" `
  --config "$env:USERPROFILE/.codex/config.toml" `
  --attribute-skill-reads
```

Useful options:

- `--sessions-dir`: ancestor lookup root when logs are in different dated folders.
  Without it, ancestors must exist below the selected log's own directory.
- `--auxiliary-session`: record approval-review/subagent usage in a separate
  context; repeat it for multiple auxiliary logs.
- `--tool-catalog`: optional JSON array of `{name, description}` entries for
  available code-mode tools. Availability does **not** establish prompt inclusion.
- `--artifact-file`: related file sizes without reading or tokenizing contents.
- `--attribute-skill-reads`: match recorded Markdown reads to current local
  skill-file prefixes; these decoded-content subtotals are already within tool
  results and must not be added again.
- `--codex-home`: read-only SQLite diagnostics, filtered to the selected session
  and inherited ancestors. UI/history projections are not counted as extra text.
- `--config`: export only MCP names/enable flags and Boolean feature flags;
  current configuration is not proof of historical loading.

Fork cutoffs exclude later parent activity. The parser tolerates a live log's
unterminated final record but rejects corruption earlier in the file. Recorded
per-response usage and mirrored `token_count` UI events are deduplicated.

Interpret the main measurements separately:

1. Recorded input-token usage is the actual reported API input for each call.
   Its maximum is a useful observed occupancy boundary; sums count repeated
   processing of history. Cached inputs remain a subset of input tokens.
2. The component table measures historical visible text once. Its percentages
   describe that text estimate, **not** a full instantaneous request snapshot.
3. Tool-description inventory, world-state diagnostics, on-disk files and
   auxiliary contexts are separate from that component table. Unlogged schemas,
   message framing, instruction replacement and compaction prevent exact
   reconstruction of live context from a rollout alone.

Store reports outside publishable source. Aggregates can still identify local
sessions, filenames and installed integrations. Inspect them before sharing.

Verification uses synthetic logs and temporary directories:

```powershell
python -m unittest discover -s tools/tests -p 'test_analyze_codex_context.py'
```
