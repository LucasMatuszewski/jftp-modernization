# Java source instructions

This subtree contains the existing Java application and shared packages under `com.myjavaworld`. Read the [root instructions](../../../AGENTS.md), [architecture](../../../docs/architecture.md), and the nearest package-level `AGENTS.md` before editing.

Application/session behavior belongs to `jftp`; command wiring belongs to `jftp/actions`; TLS belongs to `jftp/ssl`; reusable widgets belong to `gui`; shared file/resource/event helpers belong to `util`; archives belong to `zip`. These are source packages, not separate Maven modules. Check callers across package boundaries when changing an API. Detailed current-state descriptions belong in `/docs` and nearest instructions, not repeated here.

Preserve desktop behavior and source/resource relationships. Keep UI work on the appropriate Swing thread and characterize asynchronous error/cancellation behavior before replacing workers. Do not combine library substitution, storage migration and unrelated language cleanup in one change. Do not automatically enable preview features, modularize the application, or replace Swing as part of modernization.

**Every structural, responsibility, API, dependency or behavior change must update affected package instructions, root `AGENTS.md` and relevant docs in the same logical change.** Review parent/child scope links when moving files. Create colocated `CLAUDE.md` with `@AGENTS.md` for any new instruction scope. Follow [the test-scope guidance](../../test/AGENTS.md) for characterization tests and [Windows startup](../../../docs/windows-startup.md) for the existing bootstrap. A documentation-only task does not authorize test implementation.
