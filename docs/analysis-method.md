# Analysis scope and evidence

## Baseline

Inspection date: 2026-10-06. Working branch: `Luna-subagents-modernization`. Original revision: `14e62ce` (`Closes #8 - Row selection issues on Mac OS X`). The baseline has 576 tracked files, including 182 Java files and 394 other files. [The baseline manifest](analysis/repository-baseline.json) records original paths, modes and Git blob IDs. The pre-existing untracked `micro` file is outside the analysis and remains untouched.

This is a static-analysis and documentation phase. No application/build/resource file changes, test implementation, tool installation, application build, dependency resolution, application launch or test execution are authorized or performed here. Planned validation is not a passing result. Available local tooling was checked without building: Microsoft OpenJDK 21.0.10+7 LTS is on PATH; `mvn` is not recognized in the current PowerShell session.

## Coordinated GPT-6 Luna work

The coordinator inspected repository metadata, paths and instructions and reviews the generated documentation. Application source reading is delegated to GPT-6 Luna agents with `high` reasoning and self-contained briefs. Agents have disjoint write ownership and may coordinate cross-package questions. They do not commit, push, run the shared tracker, install tools, or change the application.

| Workstream | Original inputs | Documentation responsibility |
|---|---|---|
| Build/resources | All tracked non-Java files, including hidden IDE metadata, POM, scripts, assembly, properties and asset inventory | Build/dependencies, resources/distribution, corresponding nested instructions |
| Support/security | Java under `gui`, `util`, `zip`, and `jftp/ssl` | Shared support behavior, TLS/keystores, corresponding nested instructions |
| Application/workflows | Java under `jftp`, excluding `ssl` and the reassigned UI subset | Architecture, application flows, four behavioral regression designs, application/action instructions |
| UI/browser detail (reused build/resources agent) | 44 top-level `jftp` dialog/preference/browser/file-model/renderer sources | Focused UI/browser analysis and additional coverage ledger, supplied to the application writer |
| Synthesis | Completed analysis documents and cross-workstream findings | Integrated modernization phases, dependencies, validation and commit gates |

The original tracked-file set determines coverage; newly created docs and instructions are outputs rather than inputs. Each delegate fully reads owned text files in bounded batches and records them as `READ` in its coverage ledger. Binary assets are inventoried as `INVENTORIED_BINARY`, not represented as source that was read. Any omission must be reported with an explicit reason. The coordinator compares the combined ledgers against the baseline manifest, detects duplicate/missing paths, checks local documentation links, and checks the original tracked working tree for application changes.

## How to interpret the documentation

Repository facts have source paths and class/method/configuration references. Static call-flow analysis does not prove runtime correctness or dependency availability. Declared Maven dependencies are distinct from resolved transitives and runtime libraries referenced by launch scripts. An absent checked-in artifact is not proof it cannot be recovered legally from an approved source.

Modernization proposals preserve user-visible features and current data. Known bugs and unsupported external systems are recorded as risks or decisions, not silently reclassified as features to remove. External version recommendations are dated and grounded in primary sources; recheck them when implementation starts.

The design sequence is documentation, four behavioral characterization suites, strictly bounded compile/bootstrap work when needed, minimum application startup with tests passing, checkpoint commits, then separate dependency and Java refactors. This phase completes the documentation and design only. The [modernization plan](modernization-plan.md) specifies the later ordering and exit gates; the shared tracker holds execution state.

## Verification limits

The coverage ledgers are delegate attestations checked against the tracked-file inventory; they are not execution traces or a proof every inferred behavior is correct. Binary images were not visually inspected. No Maven dependency tree, passing baseline tests, working FTP connection, usable GUI, compatible serialized-data round trip, or successful modern-JDK build is claimed. These require the later execution phase and its controlled fixtures.
