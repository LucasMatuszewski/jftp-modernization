# Whole JFTP repository structure

Historical tracked-path snapshot: 2026-10-08; source revision `3e1b7afe048ac1baa40d7ad515f1140d7fd8e3f8`. The inventory and table below retain that original snapshot; they are not a refreshed count of today's checkout.

The historical inventory covers **691 tracked files**, including images, fonts, legacy-encoded resources, launch scripts and agent tooling. See [all historical file paths and index blob IDs](artifacts/jftp.structure/files.json).

The current compact symbol snapshots separately select **539 UTF-8 text files**, parse **182 Java + 12 JavaScript files**, and capture **1,658 declarations**. JavaScript declarations come from the tracked `.agents/skills` and `.claude/skills` trees. Later, separately authored `tools` and `docs/RepoMix` trees are explicitly excluded. Current source revision, dirty state and working-copy fingerprint are recorded in [compact overview metadata](artifacts/jftp.compact.rust/jftp.compact.rust.meta.json) and [complete-index metadata](artifacts/jftp.full.compact.rust/jftp.full.compact.rust.meta.json).

| Path group | Tracked files |
|---|---:|
| `.agent-briefs` | 5 |
| `.agents/skills` | 22 |
| `.claude/skills` | 22 |
| `.settings` | 6 |
| `<root>` | 10 |
| `assets` | 6 |
| `assets/fonts` | 9 |
| `docs` | 17 |
| `docs/analysis` | 6 |
| `src/main/AGENTS.md` | 1 |
| `src/main/CLAUDE.md` | 1 |
| `src/main/assembly` | 3 |
| `src/main/help` | 155 |
| `src/main/images` | 50 |
| `src/main/java` | 196 |
| `src/main/resources` | 59 |
| `src/main/resources_de` | 57 |
| `src/main/resources_zh_TW` | 58 |
| `src/main/scripts` | 4 |
| `src/test` | 4 |

## Navigation

- [Ranked compact root overview](jftp.compact.rust.md): 16,384 raw estimated-token budget; 975 declarations selected and 683 omitted.
- [Complete compact captured-definition index](jftp.full.compact.rust.md): all 1,658 captured declarations; 25,275 raw estimated tokens, no declaration clipping, syntax-error files or parser failures.
- [Documentation index](../README.md), [build/dependency wiring](../build-and-dependencies.md), [resources/distribution](../resources-and-distribution.md), and [architecture](../architecture.md) explain the non-symbol configuration and resources.
- [Archived grouped reports](artifacts/2026-10-08/readable/README.md) retain the earlier output unchanged.

## Coverage boundaries

The current root scans have no subtree restriction and use all four recursive exclusions: `--exclude "docs/repo-maps/**" --exclude ".codex/**" --exclude "tools/**" --exclude "docs/RepoMix/**"`. These remove saved reports, local profile state, separate context-audit tooling and packed source context from the symbol scan. A bare directory name is not a recursive file exclusion; a single `*` matches only one path segment.

The native policy also excludes symlinks, binary files, oversized files and non-UTF-8 content. The current complete run records 109 binary skips, 41 non-UTF-8 skips, one symlink skip, and one size-limit skip (`assets/homepage.png`), separately from explicit exclusions. Historical tracked paths remain in the structure inventory; symbol-map omission does not establish absence from JFTP. Consult the current sidecars for the actual admitted/skipped paths rather than treating the historical table as current scan coverage.

XML/properties/JSON and other readable text are inventoried, not parsed as declarations. A complete captured-definition index is a navigation aid, not a resolved call graph or runtime verification. Refresh after path/declaration changes.

## Reproduction

The compact reports used the Windows x86-64 native **0.3.0** package from [CI run 37752937879](https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37752937879), for reviewed source head `49d43e6` and its distinct clean merge build `b612871c5e93f7df2ee3c32d5bee5165a0f9a823`. All 15 jobs passed. Exact installation/status, generation/export arguments, hashes and measured subprocess times are in [the current compact consumer evidence](artifacts/2026-10-08/compact-windows-results.json). The unsigned EXE ran without changing Windows security policy. Release publication remains pending; the verified CI package was used instead of a local Rust build.

Use the current skill's setup workflow, then obtain the verified `program` from `setup_native.py status`. An older installed 0.2.0 copy does not provide these compact controls. From the repository root, run that program with a fresh external staging directory and the following arguments. Replace the placeholders with actual paths; compact is the default format.

```text
<verified-program> . --output-dir <external-staging>/overview --budget 16384 --exclude "docs/repo-maps/**" --exclude ".codex/**" --exclude "tools/**" --exclude "docs/RepoMix/**"
<verified-program> . --output-dir <external-staging>/full --budget 65536 --all-definitions --exclude "docs/repo-maps/**" --exclude ".codex/**" --exclude "tools/**" --exclude "docs/RepoMix/**"
```

Measure each mapper subprocess separately. Export with the current skill's `scripts/export_repo_map.py`, using `--implementation rust`, `--artifact-dir <external-staging>/overview` or `/full`, and the corresponding `--output-file docs/repo-maps/jftp.compact.rust.md` or `docs/repo-maps/jftp.full.compact.rust.md`. Pass each measured duration through `--elapsed-seconds`. The exporter also requires the repository root as its positional argument. Existing reports require an explicit `--force` when intentionally refreshing them; avoid overwriting unreviewed evidence.

These commands refresh the current working copy. Exact published fingerprints/hashes require the same input bytes and tool build; metadata truthfully records later revisions and changes. Keep generated bytes unchanged so raw/report hashes remain valid. The [original 0.2.0 generation evidence](artifacts/jftp.structure/generation.json) and [original verification](artifacts/jftp.structure/verification.json) remain unchanged historical evidence for the archived grouped maps and tracked-path snapshot, not provenance for the compact reports.
