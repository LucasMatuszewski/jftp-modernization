# JFTP RepoMix source packs

Use [RepoMap](../repo-maps/README.md) first for paths and declaration/signature lookup. These larger packs provide implementation context across the application when reading individual files is insufficient.

Recorded snapshot: 2026-10-08. Token counts use `o200k_base`; see [manifests](artifacts/README.md) for source hashes and measurements.

| Pack | Contents | Snapshot tokens (o200k_base) |
|---|---|---:|
| [Selective full code](jftp-source.selective-full.xml) | Recommended for broad behavior analysis: all code retained, reviewed comment boilerplate removed, meaningful comments preserved, blank lines reduced | 198,551 |
| [Full source reference](jftp-source.full.xml) | Original source text, including all comments; use for comparison or original documentation | 230,673 |

Both snapshots include all 182 Java files under `src/` and `pom.xml` (183 paths). Resources, translations, images, help, launchers, third-party binaries and agent tooling are outside this scope. Read relevant sections when the entire pack would exceed the available context.

Selective-full uses comment reduction without Repomix structural compression. Its non-comment Java tokens and AST structure were verified against the originals; the full reference was compared with source text after newline normalization. These are static source checks, not a passing application build. Verify original definitions/callers before editing and regenerate after source changes; packed line numbers differ from source line numbers.

[Supporting artifacts](artifacts/README.md) contain scripts, configurations, comment/license audits, measured evidence and lossy compression experiments. Load them when regenerating or adjusting packing, rather than as routine application context.
