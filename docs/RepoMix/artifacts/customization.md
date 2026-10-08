# Comment-aware JFTP packing

Inspected and measured on 2026-10-08 with **Repomix 1.18.1**, using all 182 Java files and `pom.xml`. The original source and installed Repomix package were not edited. Everything authored by this task is in `docs/RepoMix/`. Source hashes, individual subprocess timings, commands and token counts are in [the optimization manifest](optimization-manifest.json).

## What configuration can and cannot do

Repomix supports a persistent `repomix.config.json` supplied with `--config`. These mechanisms serve different purposes:

| Mechanism | Meaning in the inspected version |
|---|---|
| `output.removeComments` | Remove comments wholesale for supported languages. There is no native comment-content keep/remove regex list. |
| `include`, `ignore.customPatterns`, default ignore settings | Select **files** with globs. They do not select comment text or statements. Custom file exclusions augment enabled default ignores; defaults can be disabled as a group. |
| `output.patterns` | Ordered **file globs** controlling full, compressed or directory-only output. First match wins. `compress: false`, or a matching entry with neither flag, forces full content even when global compression is enabled. |
| `input.processors` | Run a local command on a temporary file and consume stdout before packing. This is the supported extension point used here for selective comment filtering. It does not edit the source file. |
| Java Tree-sitter query customization | Not exposed by the 1.18.1 configuration schema. Adding a JSON regex does not replace/add/subtract the built-in syntax captures. |

These configuration features are described in [official configuration documentation](https://repomix.com/guide/configuration), [comment removal](https://repomix.com/guide/comment-removal) and [code compression](https://repomix.com/guide/code-compression). Current online documentation can drift; the tested installed module identities are recorded in [implementation evidence](repomix-implementation.json).

The installed Java query captures every line/block comment. Its default strategy retains complete comment rows but uses identifier rows for declarations/references. Consequently, a multiline method's parameter continuation may disappear while an entire license comment remains. A null guard without a selected capture also disappears. This is structural extraction, not a statement-preserving minifier. A file override preserves the whole nominated file; it cannot selectively restore one method body through a JSON content pattern.

## What the JFTP inspection found

The parser found **912 Java comments**, including **408 Javadocs**, **180 identical Java copyright/license headers**, **174 comments containing `@author`**, and **124 containing `@version`**. The XML notice in `pom.xml` accounts for the additional occurrence in the original pack's 181 copyright comments. See [deduplicated comment inventory](comment-inventory.json) and [per-comment decisions](comment-audit.json).

The static [comment policy](comment-rules.json) applies regexes only to AST-identified comments. It normalizes comment markers/whitespace for matching, uses case flags only when explicitly configured, gives retention rules precedence and keeps unrecognized text. It currently makes these decisions:

| Decision | Comments | Reason |
|---|---:|---|
| Consolidate exact repeated Apache notice | 180 | One exact common notice is included in each selective pack's header; [the notice index](license-notices.json) preserves per-file attribution. `pom.xml` retains its own XML notice. Original source and the original full reference retain all notices. |
| Remove metadata-only Javadocs | 53 | No description/contract remains after removing author/version tag blocks. Eclipse template instructions following an author tag are also metadata continuations. |
| Remove constructor identity templates | 23 | Anchored “constructs/creates an instance of Class” descriptions immediately preceding actual constructor declarations. Parameterized descriptions are not broadly matched. |
| Remove the supplied DateCellRenderer style template | 1 | Exact supplied generic wording and parameter descriptions. The separate constructor documentation specifying locale/default `DateFormat.SHORT` is retained. |
| Remove copied action prose | 12 | Exact repeated “uploading a signle file with a different name” paragraph found on multiple different action classes, including print/open/edit actions. The repetition and class names suggest stale copied prose; no runtime behavior is inferred from that sentence. |
| Remove empty/decorative comments | 11 | Anchored empty/separator-only text. |
| Rewrite author/version metadata, keep description | 107 | Includes the supplied large-theme example: its purpose remains, author/version disappear. |
| Keep comments unchanged | 525 | 43 match the conservative behavior-contract retention rule; the other 482 are retained by default. |

No generic rule deletes all `@param`, `@return` or `@throws` text. There are 152 apparently empty tag **lines**, but some have meaningful multiline continuations, as the supplied constructor example illustrates. Removing them by a line-only regex would be unreliable. The inventory also contains many commented-out code fragments: these remain by default because distinguishing obsolete alternatives from useful history requires review.

Retained examples include SwingWorker completion on the event dispatch thread, interrupt/null-result contracts, Zip.open/close sequencing, and excluding the destination archive from its own contents. Unknown purpose summaries and default-value documentation remain. Add narrower reviewed rules rather than treating every description understandable from code as redundant.

## Measured profiles

All packs cover the same **183 paths**. Tokens below use Repomix's **o200k_base** encoding; these are individual cached-package runs, not a benchmark or a model-independent context count.

| Profile | Tokens | Both previously flagged code fragments retained? | All Java code preserved? |
|---|---:|---|---|
| Original full reference | 230,673 | Yes | Full-source text comparison |
| Original structural compression | 146,244 | No | No |
| Built-in remove-all-comments, full code | 182,982 | Yes | Verified non-comment tokens + AST |
| Built-in remove-all-comments, compressed | 98,697 | No | No |
| **Selective comments, full code** | **198,551** | **Yes** | **Verified non-comment tokens + AST** |
| Selective comments, structural compression | 113,395 | No | No |
| Selective hybrid, two full-file overrides | 114,182 | Yes, in those two files | Only the two overridden files were verified as complete; other files remain structurally compressed |

For behavior analysis, use [selective full code](../jftp-source.selective-full.xml): **13.93% fewer tokens** than the original full reference while preserving useful comments and every non-comment Java token/AST structure. The strip-all alternative saves 20.67% but removes contract/rationale documentation too.

For navigation, [selective structural compression](jftp-source.selective-compressed.xml) is **22.46% smaller** than the original compressed pack. It still loses method details. [The hybrid example](jftp-source.hybrid.xml) costs 787 extra tokens and restores the two known examples, with the same limitation in other files. Restoring those examples is not proof that all other useful logic survived.

Built-in alternative packs remain in external measurement staging; their configs, logs and statistics are saved here. Selective-full is published in the parent directory; the two lossy selective variants are archived here. No application compilation, execution or modernization was performed.

## Edit and reproduce

1. Edit [comment-rules.json](comment-rules.json): add/remove narrowly anchored `remove_comments` regex entries, `keep_comments` retention entries, metadata tags, or `full_file_patterns` globs. Optional `next_type` restricts a removal rule to a neighboring declaration such as `constructor_declaration`. Keep rules win. Regex flags are explicit. The normalized text includes HTML tags such as `<code>`; it is original Java comment text, before XML escaping.
2. Use `output.patterns` in a persistent Repomix config to protect complete files. The tested hybrid config is [repomix.hybrid.config.json](repomix.hybrid.config.json). Place specific exceptions before broad rules:

```json
{
  "output": {
    "compress": true,
    "patterns": [
      { "pattern": "src/main/java/com/myjavaworld/util/ResourceLoader.java", "compress": false },
      { "pattern": "src/main/java/com/myjavaworld/jftp/LocalFile.java", "compress": false },
      { "pattern": "**/*.java", "compress": true }
    ]
  }
}
```

3. Regenerate from the repository root:

```powershell
npx --yes repomix@1.18.1 --version
python docs/RepoMix/artifacts/generate.py
python docs/RepoMix/artifacts/optimize.py
```

The optimizer rebuilds its experiment configs from the original base config and the policy; edits to generated variant configs are for direct CLI trials and are overwritten by the optimizer. To change persistent file exceptions, edit `full_file_patterns` in the JSON policy. Its globs become full-file overrides preceding the compressed Java catch-all. Brace expansion was tested against both known file paths. The comment part of this policy is implemented by our external adapter; it is not a native Repomix query override.

For a single selective profile, set `REPOMIX_PACKAGE_ROOT` to the cached pinned npm **package directory**, then run the local CLI with [repomix.selective-full.config.json](repomix.selective-full.config.json) or [repomix.selective-compressed.config.json](repomix.selective-compressed.config.json). The configured command is `node docs/RepoMix/artifacts/java-comments.mjs {file}`. The Python optimizer discovers the pinned package and supplies the environment variable automatically. The adapter uses the installed parser without modifying its queries or source. Processor errors fail packing.

## Verification boundaries

[Verification evidence](optimization-verification.json) records **182 Java files**, **141,001 non-comment AST leaf tokens**, matching token-sequence hashes, matching non-comment AST structure, and original source hashes. This checks actual generated selective-full and built-in-full output, not only a preprocessing intermediate. All retained comment text also matches after whitespace normalization, and [five source citations](optimization-citations.json) identify example contracts. Every original byte hash remains unchanged. Both full-file hybrid overrides were checked independently.

Ten [behavioral tests](java-comments.test.mjs) cover native brace globs/first-match priority as well as comment-looking strings/URLs, escaped quotes, character literals, non-ASCII offsets, token adjacency, multiline metadata, retention precedence, constructor scoping, default/description retention, empty programs, and failing uncertain syntax. Run `node --test docs/RepoMix/artifacts/java-comments.test.mjs` with `REPOMIX_PACKAGE_ROOT` set. The adapter deliberately rejects Java Unicode escape preprocessing, which does not occur in these sources, rather than assume its parser handles Java's pre-lexing rules.

The repeated common license text and all removal/rewrite decisions are auditable. These checks prove parser-token/structure retention within the measured corpus, not a passing JFTP build or resolution of legacy defects. Structural/hybrid files remain navigation artifacts. Original source lines/hashes are used for evidence; removal and blank-line cleanup change packed line numbering.
