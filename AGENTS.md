# JFTP agent instructions

## Authority and current phase

This is the existing JFTP Java desktop application. The current branch is `Luna-subagents-modernization`. The authorized phase is repository analysis, documentation and modernization planning. Do not implement tests, change application/build/resource files, install tools, run the application, or start the later refactor until the user requests the next phase.

The modernization must preserve existing functionality. Do not introduce new protocols, redesign the UI, remove commands or silently change transfer, persistence, archive or TLS behavior. Document existing defects separately from intended contracts. When a compatibility change would remove a legacy entry point or platform behavior, explain the choice and obtain a concrete scope decision before implementing it.

## Current repository map

This is one Maven JAR project, `com.myjavaworld:jftp:5.0.2-SNAPSHOT`, rather than a multi-module system. `pom.xml` currently requests Java 5 source/target and declares FTPAPI 3.0.0, JavaHelp 2.0.05 and test-scoped JUnit 3.8.1. These are baseline declarations, not recommended modern versions or successfully resolved dependencies. There are no implemented tests or Maven wrapper in the original tree; `src/test` contains placeholders.

Java packages live under `src/main/java/com/myjavaworld`. The desktop entry point is `jftp.JFTPApplication`; `jftp.JFTPApplet` is a separate legacy entry point. The client supports FTP/FTPS; do not confuse FTPS with SFTP or add a new protocol. Default/German/Traditional Chinese resource trees, `src/main/images`, and `src/main/help` supply classpath resources; `src/main/assembly` and `src/main/scripts` define distribution packaging and launchers. See the build documentation for the legacy repository, missing-artifact risks and launch-layout mismatch.

## Read the documentation

Start with [documentation index](docs/README.md), [architecture](docs/architecture.md), [build and dependencies](docs/build-and-dependencies.md), [modernization plan](docs/modernization-plan.md), and [four behavioral regression suites](docs/regression-test-design.md). For protocol/certificate choices, read [the brief security options](docs/security-modernization-options.md): SFTP is an optional new feature outside the behavior-preserving baseline. These describe the repository as inspected; proposed commands and versions are not evidence of successful execution.

Detailed instructions live next to the relevant code:

| Scope | Instructions |
|---|---|
| Build, resources, locale trees and distribution | [src/main/AGENTS.md](src/main/AGENTS.md) |
| Java packages and cross-package boundaries | [src/main/java/AGENTS.md](src/main/java/AGENTS.md) |
| Application/session/browser/persistence | [jftp/AGENTS.md](src/main/java/com/myjavaworld/jftp/AGENTS.md) |
| User commands | [actions/AGENTS.md](src/main/java/com/myjavaworld/jftp/actions/AGENTS.md) |
| TLS/certificates/keystores | [ssl/AGENTS.md](src/main/java/com/myjavaworld/jftp/ssl/AGENTS.md) |
| Shared Swing widgets | [gui/AGENTS.md](src/main/java/com/myjavaworld/gui/AGENTS.md) |
| Files, encoding, events and resources | [util/AGENTS.md](src/main/java/com/myjavaworld/util/AGENTS.md) |
| ZIP operations | [zip/AGENTS.md](src/main/java/com/myjavaworld/zip/AGENTS.md) |
| Default resource bundles | [resources/AGENTS.md](src/main/resources/AGENTS.md) |
| Launch scripts | [scripts/AGENTS.md](src/main/scripts/AGENTS.md) |
| Distribution assembly | [assembly/AGENTS.md](src/main/assembly/AGENTS.md) |
| Future behavioral tests and fixtures | [src/test/AGENTS.md](src/test/AGENTS.md) |
| Documentation maintenance | [docs/AGENTS.md](docs/AGENTS.md) |

Read the nearest instructions as well as their ancestors. `CLAUDE.md` imports the colocated `AGENTS.md`; do not maintain competing instruction copies.

## Mandatory documentation maintenance

**Update this root file, every affected nested `AGENTS.md`, and the relevant `/docs` files in the same logical change whenever modernization changes the actual project structure, package responsibilities, dependencies/versions, build or launch commands, persistence formats, behavior contracts or verification procedure.** Review these instructions at every phase boundary. Replace obsolete facts; do not leave them presented as current. Keep `CLAUDE.md` imports valid when moving directories. Update links, diagrams, dependency tables, test designs and compatibility decisions as appropriate. A modernization change is incomplete when its instructions or documentation disagree with the resulting code.

The analysis coverage records in `docs/analysis/` describe the original baseline, not an automatically current inventory. Preserve their baseline identity; document later changes in the relevant current-state pages. Keep execution state in the shared tracker, not duplicate Markdown task-status files. The requested modernization plan is an engineering design with ordering and validation gates.

## Workflow and verification

- Analyze and characterize behavior before changing implementations. Keep four stable behavioral suites; add edge cases within them as needed. Prefer observable output/state over private fields or algorithm details.
- Establish a runnable, minimally changed baseline and passing tests before dependency replacement or broad Java cleanup. If the original build cannot compile, record that limitation and restrict the first bootstrap changes to what makes characterization possible.
- When tests fail after an application change, investigate the changed application first. Do not loosen assertions, skip failures or regenerate expectations merely to obtain green results.
- Use small, descriptive commits by logical change, with a passing checkpoint before and after each refactor. Stage explicit paths only; never `git add .`, `git add -A` or `git commit -a`. Delegates do not commit or push.
- Agents share this checkout. Assign disjoint write ownership and never revert another actor's edits. The untracked `micro` file predates this work; leave it untouched.
- Use isolated temporary user homes/preferences/keystores, temporary directories and controlled local FTP/FTPS fixtures when later tests or startup checks are authorized. Do not test against real credentials or remote customer files.
- Report exactly what was tested, the environment, and known gaps. Static inspection is not a passing runtime test. Verify modern-version recommendations against official sources before pinning.

## Environment

This session uses the user-selected Windows checkout `C:\Users\BiuroEdukey\DEV\COURSES\Sages\jftp`; do not move it to another checkout on your own. Shared machine rules are in `C:\Users\BiuroEdukey\AGENTS.md`. Necessary Windows shell calls use narrowly justified `sandbox_permissions: require_escalated` because the native sandbox launch path is known to fail with errors 1326/1056. Do not disable approvals globally.

At inspection on 2026-10-06, `java -version` reported Microsoft OpenJDK 21.0.10+7 LTS and `mvn` was unavailable on the current PowerShell PATH. No application build, launch or tests were attempted during this documentation phase. Recheck tooling when implementation starts; this observation is not proof Maven is absent from every environment.
