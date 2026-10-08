import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { javaParser, inspect, transform, normalized, hash, here } from './java-comments.mjs';

const [packageRoot, stagedContents] = process.argv.slice(2);
const repo = path.resolve(here, '../../..');
const packs = JSON.parse(fs.readFileSync(stagedContents, 'utf8'));
const rules = JSON.parse(fs.readFileSync(path.join(here, 'comment-rules.json'), 'utf8'));
const adapter = await javaParser(packageRoot);
const { resolveFileLevel } = await import(pathToFileURL(path.join(
  packageRoot, 'lib/core/file/fileLevelResolve.js')).href);
const hybridConfig = JSON.parse(fs.readFileSync(path.join(here, 'repomix.hybrid.config.json'), 'utf8'));
const counts = {};
const audit = [];
const sources = [];
const retainedExamples = [];
let overridesVerified = 0;
try {
  for (const [relative, packed] of Object.entries(packs['selective-full'])) {
    if (!relative.endsWith('.java')) continue;
    const bytes = fs.readFileSync(path.join(repo, relative));
    const original = bytes.toString('utf8');
    const filtered = transform(adapter.parser, original, rules);
    const actual = inspect(adapter.parser, packed);
    if (actual.code_sha256 !== filtered.before.code_sha256 ||
        actual.structure_sha256 !== filtered.before.structure_sha256) {
      throw new Error(`Optimized pack lost executable code/structure: ${relative}`);
    }
    const expectedComments = filtered.after.comments.map(comment => normalized(comment.text));
    const actualComments = actual.comments.map(comment => normalized(comment.text));
    if (JSON.stringify(expectedComments) !== JSON.stringify(actualComments)) {
      throw new Error(`Optimized pack lost or changed retained comment text: ${relative}`);
    }
    // Independently exercise the built-in strip-all option on the complete corpus.
    const stripped = inspect(adapter.parser, packs['builtin-no-comments-full'][relative]);
    if (stripped.code_sha256 !== actual.code_sha256 || stripped.structure_sha256 !== actual.structure_sha256) {
      throw new Error(`Built-in removal changed Java code/structure: ${relative}`);
    }
    sources.push({ path: relative, source_sha256: hash(bytes),
      non_comment_tokens: actual.code_tokens.length,
      executable_tokens_sha256: actual.code_sha256,
      ast_structure_sha256: actual.structure_sha256 });
    for (const edit of filtered.edits) {
      counts[`${edit.action}:${edit.rule}`] = (counts[`${edit.action}:${edit.rule}`] ?? 0) + 1;
      audit.push({ path: relative, source_sha256: hash(bytes), start_line: edit.start_line,
        end_line: edit.end_line, action: edit.action, rule: edit.rule,
        comment_sha256: hash(edit.original_text),
        ...(edit.rule === 'repeated-apache-header' ? {} : { text: edit.original_text }) });
      if (edit.action === 'keep' && /event dispatching|must be called|Let's not try|Returns.*null/is.test(edit.original_text)) {
        retainedExamples.push({ path: relative, source_sha256: hash(bytes),
          start_line: edit.start_line, end_line: edit.end_line,
          quote: edit.original_text.replaceAll('\r\n', '\n').replace(/\r$/, ''),
          retained_in_selective_full: actualComments.includes(normalized(edit.original_text)) });
      }
    }
  }
  // File-level hybrid overrides must preserve *all* code in the two nominated files.
  const overrides = Object.keys(packs.hybrid).filter(relative => relative.endsWith('.java') &&
    resolveFileLevel(relative, hybridConfig.output) === 'full');
  for (const relative of overrides) {
    const full = inspect(adapter.parser, packs['selective-full'][relative]);
    const hybrid = inspect(adapter.parser, packs.hybrid[relative]);
    if (full.code_sha256 !== hybrid.code_sha256 || full.structure_sha256 !== hybrid.structure_sha256) {
      throw new Error(`First-match file override failed: ${relative}`);
    }
  }
  overridesVerified = overrides.length;
} finally { await adapter.dispose(); }
const report = { java_files_verified: sources.length, comments: audit.length, counts,
  non_comment_token_count: sources.reduce((sum, source) => sum + source.non_comment_tokens, 0),
  selective_full_preserves_all_non_comment_tokens_and_ast: true,
  selective_full_preserves_all_retained_comment_text_after_whitespace_normalization: true,
  builtin_no_comments_full_preserves_all_non_comment_tokens_and_ast: true,
  hybrid_overrides_verified: overridesVerified, sources, retained_examples: retainedExamples };
fs.writeFileSync(path.join(here, 'optimization-verification.json'), JSON.stringify(report, null, 2) + '\n');
fs.writeFileSync(path.join(here, 'comment-audit.json'), JSON.stringify(audit, null, 2) + '\n');
fs.writeFileSync(path.join(here, 'optimization-citations.json'), JSON.stringify({
  citations: retainedExamples.map(example => ({ path: example.path, sha256: example.source_sha256,
    start_line: example.start_line, end_line: example.end_line, quote: example.quote,
    claim: 'Comment retained after whitespace normalization; contract text preserved, not runtime verified.' })),
}, null, 2) + '\n');
console.log(JSON.stringify({ java_files: sources.length, comments: audit.length, counts,
  tokens_verified: report.non_comment_token_count, retained_examples: retainedExamples.length }));
