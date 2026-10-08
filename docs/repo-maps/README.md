# JFTP repository maps

For unfamiliar Java source navigation, start with [the native overview](jftp-java.rust.md). Search [the complete captured-definition index](jftp-java.full.rust.md) when a symbol is omitted from the overview. Read original bodies, callers and configuration before editing or documenting behavior. A known-file task can start with direct search instead.

The grouped renderer shows each path once, original line numbers, enclosing class/implementation headers and multiline declarations. It deliberately omits bodies. The overview uses a 16,384 estimated-token budget; the full index was requested with 65,536 and contains all 1,586 captured Java definitions, without declaration clipping. Its raw text is about 27,213 estimated tokens, so a 1M context window does not require truncating this particular index to 4K. Larger budgets remain optional; reserve context for the task and relevant source bodies.

Each report states source scope, revision/fingerprint, selected/omitted definitions, clipping, budget, file counts, size, token estimator and measured generation time. These are snapshots, not a compiler-resolved call graph. Refresh after relevant source paths/declarations change, check current provenance and update this pointer when report paths change. Generation caches/staging belong outside the repository; exported evidence belongs under `artifacts` and is excluded from the Java-only scans.

The canonical files were regenerated on native Windows using the package from [final CI run 37711387112](https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37711387112), for reviewed head `03a538c`. [Final consumer evidence](artifacts/2026-10-08/windows-final/final-report.md) records its distinct build checkout, package hashes and the named report paths. Individual overview/full runs took **0.742 / 0.699 seconds**; their whole annotated reports estimate **16,745 / 27,582 tokens**. Both raw maps match the archived WSL outputs byte for byte. These individual Windows runs are separate from the repeated comparison below. The examined revision is `990545c`, with documentation work dirty; Java source hashes remain unchanged by subsequent documentation commits.
## Measured Python/native comparison

The [60-sample comparison](artifacts/2026-10-08/benchmark-results.json) used the same source/scope and grouped 16,384-token budget, alternating implementation order, with five fresh-output and five reused-output samples per implementation/corpus. OS caches were not flushed. These measurements preceded the final PR fixes to complete-output and source-retention memory accounting; they are preserved as measured evidence rather than relabeled as a later binary run.

| Public corpus | Python fresh-output median | Rust fresh-output median | Ratio | Definitions found/selected (Python; Rust) |
| --- | ---: | ---: | ---: | --- |
| JFTP Java | 38.177 s | 18.947 s | 2.01× | 1,586/869; 1,586/869 |
| Flask Python | 0.551 s | 0.096 s | 5.73× | 416/416; 502/502 |
| Mapper Rust source | 0.390 s | 0.078 s | 4.98× | 169/169; 169/169 |

Reused-output median ratios were 1.95×, 4.47× and 4.52× respectively. Java was read from a Windows mount inside WSL; Flask and Rust were on native ext4. WSL could not resolve this Windows worktree's `.git` pointer, so the measured Java exports honestly report null revision. Do not extrapolate a hardware-independent or huge-repository speedup. Individual map export timings and sample ranges remain in the reports/JSON.

Flask's 86 additional Rust tags are assignment definitions: named constants, aliases or class/module variables captured by the native grammar/query combination. They are not 86 extra functions. Under the previous 4K line renderer, extra ranked assignment rows competed with existing definitions for text space, so Rust found more but selected fewer. The new default selects all 416 Python and 502 native Flask tags in this tested scope. Repeated `to_python` methods are real methods of different classes; grouped parent headers now expose those owners. All-definitions still means captured eligible definitions: unsupported constructs and admission/parser limits remain visible.

The mapper adapts Aider's ranking and audited Tree-sitter queries; it is not an exact port of Aider's TreeContext renderer, focus logic or tokenizer. Existing grammar packages/crates parse Java, Python, JavaScript, TypeScript/TSX, C/C++, C#, Go and Rust. Tests cover those query languages; real repository comparisons here cover Java, Python and Rust. Some TypeScript const-arrow definitions are not captured by the current query. Estimated tokens use `ceil(Unicode characters / 4)`, not a model tokenizer.

## Complementary workflows and review

- [Repomix trial](artifacts/2026-10-08/repomix/review.md): full five-file source pack preserved signatures and bodies. Compression saved 21.95% of its measured tokens but dropped a Java parameter continuation and a null guard; use full source for behavior/edit evidence.
- [Local Context7 trial](artifacts/2026-10-08/context7/trial-report.md): the pinned real client returned verified source ranges/hashes; changed/deleted source/revision and hostile Host tests passed. This establishes local lexical compatibility, not semantic quality or production-scale retrieval.
- [Skill audit](artifacts/2026-10-08/review.md): setup failures, confusing behavior, review findings and corrections recorded as they occurred. Skill changes are reviewed in [Agent Toolbox PR #11](https://github.com/EdukeyTeam/agent-toolbox/pull/11).
- [Previous evidence](artifacts/2026-10-07/README.md): old 4K one-line maps and comparisons, retained for historical interpretation. Current comparative maps and raw/inventory/metadata are under [2026-10-08 artifacts](artifacts/2026-10-08/).

Private Edukey maps and client-specific feedback/review remain local and ignored. They are not public examples or agent navigation inputs for this repository. This directory does not claim a working JFTP build, GUI or network behavior.
