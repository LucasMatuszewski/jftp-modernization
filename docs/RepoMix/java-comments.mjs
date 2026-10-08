/** Local comment-only preprocessing and AST verification; never edits input files. */
import fs from 'node:fs';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { pathToFileURL, fileURLToPath } from 'node:url';

export const here = path.dirname(fileURLToPath(import.meta.url));
export const hash = value => createHash('sha256').update(value).digest('hex');

export async function javaParser(packageRoot) {
  const metadata = JSON.parse(fs.readFileSync(path.join(packageRoot, 'package.json'), 'utf8'));
  if (metadata.name !== 'repomix' || metadata.version !== '1.18.1') {
    throw new Error('This adapter requires the verified Repomix 1.18.1 package');
  }
  const { LanguageParser } = await import(pathToFileURL(
    path.join(packageRoot, 'lib/core/treeSitter/languageParser.js')).href);
  const languages = new LanguageParser();
  await languages.init();
  return { parser: await languages.getParserForLang('java'), dispose: () => languages.dispose() };
}

const isComment = node => node.type === 'block_comment' || node.type === 'line_comment';

export function inspect(parser, source) {
  // Java translates these before lexing. This corpus contains none; refuse an
  // unsupported preprocessing case rather than trusting different parser semantics.
  if (/\\u+[0-9a-fA-F]{4}/.test(source)) throw new Error('Unicode escape preprocessing is unsupported');
  const tree = parser.parse(source);
  if (!tree || tree.rootNode.hasError) {
    tree?.delete();
    throw new Error('Java parsing failed; do not transform uncertain syntax');
  }
  const comments = [];
  const codeTokens = [];
  const structure = [];
  const visit = node => {
    if (isComment(node)) {
      if (source.slice(node.startIndex, node.endIndex) !== node.text) {
        throw new Error('Parser offsets do not match source text');
      }
      let next = node.nextNamedSibling;
      while (next && isComment(next)) next = next.nextNamedSibling;
      comments.push({
        type: node.type, text: node.text,
        start: node.startIndex, end: node.endIndex,
        start_line: node.startPosition.row + 1, end_line: node.endPosition.row + 1,
        next_type: next?.type ?? null,
        next_name: next?.childForFieldName('name')?.text ?? null,
      });
      return;
    }
    structure.push(`(${node.type}`);
    if (node.childCount === 0 && node.type !== 'program') codeTokens.push([node.type, node.text]);
    for (const child of node.children) visit(child);
    structure.push(')');
  };
  try { visit(tree.rootNode); } finally { tree.delete(); }
  return {
    comments, code_tokens: codeTokens,
    code_sha256: hash(JSON.stringify(codeTokens)),
    structure_sha256: hash(structure.join('')),
  };
}

export function bodyLines(comment) {
  if (comment.startsWith('//')) return [comment.slice(2).trim()];
  return comment.replace(/^\/\*\*?/, '').replace(/\*\/$/, '')
    .split(/\r?\n/).map(line => line.replace(/^\s*\* ?/, '').trim());
}

export const normalized = comment => bodyLines(comment).join(' ').replace(/\s+/g, ' ').trim();

function stripTags(lines, tags) {
  const out = [];
  let skipping = false;
  for (const line of lines) {
    const tag = /^@([a-zA-Z]+)\b/.exec(line);
    if (tag) skipping = tags.includes(tag[1]);
    if (!skipping) out.push(line);
  }
  return out;
}

export function transformComment(comment, rules) {
  const original = normalized(comment.text);
  // Retention wins over every removal rule, including metadata cleanup.
  for (const rule of rules.keep_comments) {
    if (new RegExp(rule.pattern, rule.flags ?? '').test(original)) {
      return { text: comment.text, action: 'keep', rule: rule.id };
    }
  }
  for (const rule of rules.remove_comments) {
    if (rule.next_type && rule.next_type !== comment.next_type) continue;
    if (new RegExp(rule.pattern, rule.flags ?? '').test(original)) {
      return { text: '', action: 'remove', rule: rule.id };
    }
  }
  if (comment.text.startsWith('/**')) {
    const lines = bodyLines(comment.text);
    const cleaned = stripTags(lines, rules.remove_javadoc_tags);
    const meaningful = cleaned.filter(line => line.trim());
    if (!meaningful.length) return { text: '', action: 'remove', rule: 'empty-javadoc' };
    if (cleaned.join('\n') !== lines.join('\n')) {
      return {
        text: '/**\n' + meaningful.map(line => ` * ${line}`).join('\n') + '\n */',
        action: 'rewrite', rule: 'javadoc-metadata',
      };
    }
  }
  return { text: comment.text, action: 'keep', rule: 'default-retain' };
}

export function transform(parser, source, rules) {
  const before = inspect(parser, source);
  const edits = before.comments.map(comment => ({
    ...comment, ...transformComment(comment, rules), original_text: comment.text,
  }));
  let output = source;
  for (const edit of [...edits].reverse()) {
    if (edit.action === 'keep') continue;
    // A space prevents tokens joining; retain newlines for removed comments.
    const replacement = edit.text || ' ' + '\n'.repeat((edit.original_text.match(/\n/g) ?? []).length);
    output = output.slice(0, edit.start) + replacement + output.slice(edit.end);
  }
  const after = inspect(parser, output);
  if (before.code_sha256 !== after.code_sha256 || before.structure_sha256 !== after.structure_sha256) {
    throw new Error('Comment filtering changed non-comment tokens or AST structure');
  }
  return { output, edits, before, after };
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  // Repomix processors receive a temporary input path. Only stdout is packed.
  const [input, explicitPackage, rulesFile = path.join(here, 'comment-rules.json')] = process.argv.slice(2);
  const packageRoot = explicitPackage ?? process.env.REPOMIX_PACKAGE_ROOT;
  if (!input || !packageRoot) throw new Error('Pass FILE and set REPOMIX_PACKAGE_ROOT to the pinned package');
  const adapter = await javaParser(packageRoot);
  try {
    const rules = JSON.parse(fs.readFileSync(rulesFile, 'utf8'));
    process.stdout.write(transform(adapter.parser, fs.readFileSync(input, 'utf8'), rules).output);
  } finally { await adapter.dispose(); }
}
