# Codex context configuration

Observed on 2026-10-08, Windows Codex CLI 0.160.1, OpenAI provider,
`gpt-6.1-sol`. This config changes agent context management, not JFTP runtime
behavior. Model catalogs and client behavior can change.

## Repository preference and current limit

[`.codex/config.toml`](../.codex/config.toml) requests:

```toml
model_context_window = 1000000
model_auto_compact_token_limit = 800000
```

The first value is a requested window, not a guarantee of server capacity.
The second controls when history is automatically compacted; it does not
increase model capacity. The current client caps the requested window using
the model catalog and reserves 5% of that capped window:

| Observation | Tokens |
|---|---:|
| Catalog default `context_window` | 272,000 |
| Existing session's reported window: 272,000 x 95% | 258,400 |
| Catalog `max_context_window` | 872,000 |
| Repository request | 1,000,000 |
| New verification thread's reported window: 872,000 x 95% | 828,400 |
| Configured automatic compaction threshold | 800,000 |

Both the installed bundled catalog and the user's fetched model cache had
the same default, maximum, and effective percentage. The fetched catalog
also reported `supports_experimental_context = false`.

Verification used the installed app-server protocol with strict config
validation. `config/read` attributed both context keys to this repository's
`.codex` directory. An ephemeral thread completed a short real model turn
with MCP servers and hooks disabled for the probe. Its
`thread/tokenUsage/updated` event reported `modelContextWindow = 828400`.
That verifies the effective client window and successful small request;
it does not prove acceptance of an 828,400-token server request.
Afterward, the compaction preference was reduced from the initial probe's
900,000 to 800,000 so it sits below the effective window.

The [API model page](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
advertises 1,050,000 tokens. API capacity and the Codex catalog's usable
window are different observations. This installed Codex client did not
expose the full advertised API window with a config override.

The previous global user config contained neither context key. Existing
JFTP logs show 258,400 with client 0.160.0. Available evidence does not
identify the exact release or catalog update that changed an earlier
million-token experience. The official changelog documents experimental
1M support for GPT-5.4 on 2026-03-05; that is not evidence of an unconditional
million-token default for the current model.

## Global, project, and CLI controls

For a global preference, put the same two keys at the root of
`~/.codex/config.toml`, before any table headers. On this Windows host that
file is `C:\Users\BiuroEdukey\.codex\config.toml`. It was not changed by
this task. A WSL CLI has a separate configuration home, normally
`/home/lucas/.codex`; do not assume Windows config also configures that CLI.

For a project preference, use `.codex/config.toml` in the repository.
Project layers load only for trusted projects; JFTP is already trusted in
the inspected Windows profile. Closer project layers override parent
layers. No model is pinned by this file, so a later model selection can
have a different maximum.

For a one-run override in PowerShell:

```powershell
codex -C 'C:\Users\BiuroEdukey\DEV\COURSES\Sages\jftp' -c model_context_window=1000000 -c model_auto_compact_token_limit=800000
```

Relevant precedence is CLI flags, trusted project config, selected profile
file, user config, and then remaining managed/system/default layers.
Managed requirements can constrain settings. These are documented config
keys; no separate CLI `--context-window` option is required.

## Desktop and activation

The current official desktop settings documentation does not describe a
numeric context-window control. It documents opening Settings with
`Ctrl+,` on Windows. The model/reasoning chooser is below the composer;
selecting a model is not the same as setting a numeric window.
Use the config file for this preference. The installed desktop Settings
screen was not inspected, so an undocumented or version-specific control
has not been ruled out.

Start a new JFTP thread after the config change; restart the client/backend
if it retained old settings. Do not assume the already running thread
grows automatically. Check the new thread's reported window (CLI `/status`
or token-usage/session telemetry). The existing
[context auditor](../tools/README.md) can read persisted session token
events. Do not edit the model cache to fabricate a larger server limit.

## Official references

- [Configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)
- [Configuration precedence](https://learn.chatgpt.com/docs/config-file/config-basic)
- [CLI reference](https://learn.chatgpt.com/docs/cli/reference)
- [Desktop settings](https://learn.chatgpt.com/docs/app/settings)
- [Model selection](https://learn.chatgpt.com/docs/models)
- [Release history](https://learn.chatgpt.com/docs/changelog)
