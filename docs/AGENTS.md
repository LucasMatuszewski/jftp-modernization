# Documentation instructions

This directory holds the requested current-state analysis and modernization design. Read [the root instructions](../AGENTS.md). Maintain the [index](README.md) as the entry point. Keep architecture, build/dependencies, application flows, support libraries, TLS/persistence, resources/distribution, four behavioral test designs and modernization phases in focused pages.

Use English, relative links, and concrete source class/method/configuration references. Separate observed repository facts, runtime-verified results, known defects, inferences and future proposals. Date externally researched version recommendations and link primary official sources. Do not present unexecuted commands, unresolved dependency trees, planned tests or compatibility hypotheses as verified results.

**Update affected documentation and root/nested `AGENTS.md` in the same change as the application modernization.** Verify links and eliminate conflicting descriptions after each phase. Preserve the original identity of baseline coverage ledgers under `analysis/`; a ledger records delegate reading/inventory of the baseline rather than runtime correctness.

The modernization design must include step dependencies, minimal-startup boundaries, four behavioral regression suites, validation and rollback gates, granular commit checkpoints, unresolved decisions and the user's current authority boundary. Do not turn these pages into a second execution tracker. Keep live work state in the shared tracker.
