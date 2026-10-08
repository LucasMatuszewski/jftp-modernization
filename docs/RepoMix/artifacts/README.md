# RepoMix supporting artifacts

Agents normally start with [RepoMap](../../repo-maps/README.md), then the two source packs described in the [RepoMix guide](../README.md). This directory holds regeneration tools, customization research and evidence; load these only when adjusting packing or auditing a snapshot.

| Material | Entry points |
|---|---|
| Customization and measured profiles | [customization.md](customization.md), [baseline-report.md](baseline-report.md) |
| Regeneration | [generate.py](generate.py), [optimize.py](optimize.py) |
| Comment policy and processor | [comment-rules.json](comment-rules.json), [java-comments.mjs](java-comments.mjs), [tests](java-comments.test.mjs) |
| Pack configurations | [base](repomix.config.json), [selective full](repomix.selective-full.config.json), [hybrid](repomix.hybrid.config.json); other `repomix.*.config.json` files are comparison profiles |
| Verification and provenance | [baseline manifest](manifest.json), [optimization manifest](optimization-manifest.json), [verification](optimization-verification.json), [citations](optimization-citations.json), [implementation evidence](repomix-implementation.json), [layout checks](layout-verification.json) |
| Comment/license audit | [inventory](comment-inventory.json), [decisions](comment-audit.json), [license notices and attribution](license-notices.json) |
| Lossy experimental packs | [original structural](jftp-source.compressed.xml), [selective structural](jftp-source.selective-compressed.xml), [hybrid](jftp-source.hybrid.xml) |

Structural compression omits implementation details. The hybrid restores only nominated full files; it does not preserve all logic elsewhere. Logs (`*.log`) record the measured CLI runs. Built-in remove-all-comment packs remain in external measurement staging.

From the repository root, with Python 3.12+ and Node.js:

```powershell
npx --yes repomix@1.18.1 --version
python docs/RepoMix/artifacts/generate.py
python docs/RepoMix/artifacts/optimize.py
```

The generator publishes the full reference in the parent directory and the baseline report, compressed experiment, logs and manifest here. The optimizer publishes selective-full in the parent directory and its other outputs here. Both stage outside the repository and verify source/coverage before publishing; neither builds nor launches JFTP. They leave the short parent guide intact. See [customization](customization.md) for policy changes and processor tests.

The reorganization preserved all five existing XML packs byte for byte. Paths embedded in their headers and measured commands in historical manifests/logs reflect the layout at generation time. Use the current paths above and the updated configurations for regeneration; the license-attribution file is now [license-notices.json](license-notices.json). Measured token counts and hashes continue to describe those original snapshots.
