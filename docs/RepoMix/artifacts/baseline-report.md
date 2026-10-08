# JFTP Repomix source packs

Generated 2026-10-08 from revision `c823596cc017cd858326292c7de8976a1e71fbcc` using Repomix **1.18.1**. All Java sources below `src/` plus `pom.xml` are included. This snapshot contains 184 Java sources and one Maven descriptor. Resources, images, help, assembly/launcher files, third-party binaries, agent tooling and documentation are outside this source-code scope.

- [Compressed source](jftp-source.compressed.xml): reduced structural context.
- [Full source reference](../jftp-source.full.xml): complete text for behavior/signature checks.
- [Manifest](manifest.json): original paths/hashes, commands, measured statistics and verification.

For comment-aware optimization, read [customization and measured profiles](customization.md). Use [selective full code](../jftp-source.selective-full.xml) when behavior matters; [selective structural compression](jftp-source.selective-compressed.xml) and [the hybrid example](jftp-source.hybrid.xml) still omit implementation outside explicit full-file overrides.

| Pack | Files | o200k_base tokens | UTF-8 bytes | Generation wall time |
|---|---:|---:|---:|---:|
| Full | 185 | 232,658 | 914,073 | 3.534 s |
| Compressed | 185 | 147,913 | 599,608 | 4.641 s |

Compression saved **84,745 tokens (36.42%)** in this source scope. Counts are reported by Repomix using `o200k_base`; they are not model-independent billing/context counts. Timings are individual subprocess measurements with the npm package cache already populated, not a benchmark.

## Verification and compression limits

Both packs parse as XML, contain each expected path exactly once, and omit no selected file. Every full-pack file equals its original after CRLF-to-LF and trailing-newline normalization. Original byte hashes were unchanged before and after packing. Security scanning remained enabled; inspect [full.log](full.log) and [compressed.log](compressed.log) for the actual CLI reports.

Compression is lossy within files. The manifest records source-hash/line evidence and retention checks for `ResourceLoader.getBundle`'s `ClassLoader loader` parameter continuation and `LocalFile.compareTo`'s null guard. In this snapshot both are retained in the full pack and omitted from the compressed pack. Other logic can also disappear; file coverage does not prove declaration or behavior coverage. Use original source/full XML for edits and behavior analysis. Packed output line numbers are not original-source line numbers.

## Reproduce

From the repository root with Node.js and Python 3.12+ available:

```powershell
npx --yes repomix@1.18.1 --version
python docs/RepoMix/artifacts/generate.py
python docs/RepoMix/artifacts/optimize.py
```

The first command obtains the pinned npm package when absent. The generator uses that cached package's Node entrypoint, validates its version, and applies [the explicit configuration](repomix.config.json). For a custom npm cache, pass `--repomix-cli /path/to/repomix/bin/repomix.cjs`. Generation stages outside the repository and publishes packs and evidence only after source/coverage validation. It never builds or launches JFTP. Concurrent edits outside the source scope are excluded; source changes during generation fail verification. Regeneration updates these files and this measured report.

Only `docs/RepoMix/` is owned by this task; RepoMap work remains separate. Generated XML and JSON bytes are preserved by this directory's Git attributes so hashes survive platform checkout.
