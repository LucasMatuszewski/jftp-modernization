# JFTP documentation

This documentation describes the legacy application at revision `14e62ce` and a proposed modernization that preserves its functionality. Inspection date: 2026-10-06. Work is on `Luna-subagents-modernization`.

**Only analysis, documentation and planning are authorized in this phase.** Tests, build repairs, startup and the larger refactor are future work. No passing build or working application is claimed.

## Read in this order

| Document | Purpose |
|---|---|
| [Modernization plan](modernization-plan.md) | Ordered phases, prerequisites, validation gates, commit checkpoints and open decisions |
| [Fork and upstream workflow](git-workflow.md) | Clone setup, publishing to the personal fork and reviewing original-author changes |
| [Architecture](architecture.md) | Entry points, package boundaries, dependencies, threading and state |
| [Build and dependencies](build-and-dependencies.md) | Exact declared Java/library/plugin versions, repositories and build constraints |
| [Application workflows](application-workflows.md) | Desktop/session/browser/transfer actions, preferences, favorites and auxiliary features |
| [UI and browser details](ui-and-browser-details.md) | Dialog validation, local/remote browser models, filtering, selection and preference controls |
| [Four behavioral regression suites](regression-test-design.md) | Detailed implementation-independent examples and fixture/validation strategy |
| [Shared support libraries](support-libraries.md) | Swing helpers, utilities, filesystem/event behavior and ZIP contracts |
| [TLS and persistence](tls-and-persistence.md) | Trust/key/certificate flows, storage compatibility and security limitations |
| [Security modernization options](security-modernization-options.md) | Brief FTP/FTPS/SFTP comparison, certificate inventory and researched version candidates |
| [Resources and distribution](resources-and-distribution.md) | Locales, assets, help, assembly, launch scripts and platform packaging |
| [Analysis method](analysis-method.md) | Delegate ownership, original inventory, evidence rules and verification limits |

## Instructions for agents

Read [root AGENTS.md](../AGENTS.md), then the nearest instructions in the source subtree you are working on. Every instruction scope has a `CLAUDE.md` that imports its colocated `AGENTS.md`. Detailed code descriptions live in these documentation pages; specialized editing instructions live next to the code.

**Keep root/nested instructions and these pages aligned with application changes in the same logical change.** After modernization, update descriptions and commands to the actual resulting system, rather than leaving proposals presented as implemented behavior.

## Original analysis records

The [baseline manifest](analysis/repository-baseline.json) records 576 original tracked paths and blob IDs, including 182 Java sources. Delegate coverage records are [build/resources](analysis/build-resources-coverage.txt), [support/security](analysis/support-security-coverage.txt), [application/workflows](analysis/application-workflows-coverage.txt) and [UI details](analysis/ui-details-coverage.txt). Text reading and binary inventory are distinct. These records describe the original baseline, not successful builds or an automatically current inventory.

Execution state is held in the shared tracker under **Document JFTP architecture and design behavior-preserving modernization (sacs-qy7v)**. This index and the modernization plan provide engineering context, not a second task-status list.

The [documentation-phase verification report](analysis/verification.md) records coverage, instruction/link checks, unchanged application files and the limits of this static analysis.
