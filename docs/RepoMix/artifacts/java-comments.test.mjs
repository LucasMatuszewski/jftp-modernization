import assert from 'node:assert/strict';
import fs from 'node:fs';
import { test, after } from 'node:test';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { javaParser, transform, here } from './java-comments.mjs';

const adapter = await javaParser(process.env.REPOMIX_PACKAGE_ROOT);
after(() => adapter.dispose());
const rules = JSON.parse(fs.readFileSync(`${here}/comment-rules.json`, 'utf8'));
const { resolveFileLevel } = await import(pathToFileURL(path.join(
  process.env.REPOMIX_PACKAGE_ROOT, 'lib/core/file/fileLevelResolve.js')).href);

test('native file patterns support brace globs and full overrides of global compression', () => {
  const config = { compress: true, patterns: [{
    pattern: 'src/main/java/com/myjavaworld/{util/ResourceLoader,jftp/LocalFile}.java', compress: false,
  }] };
  assert.equal(resolveFileLevel('src/main/java/com/myjavaworld/util/ResourceLoader.java', config), 'full');
  assert.equal(resolveFileLevel('src/main/java/com/myjavaworld/jftp/LocalFile.java', config), 'full');
  assert.equal(resolveFileLevel('src/main/java/com/myjavaworld/jftp/JFTP.java', config), 'compress');
});

test('native file-pattern order is significant and a matching unflagged entry forces full', () => {
  assert.equal(resolveFileLevel('A.java', { compress: true, patterns: [{ pattern: '*.java' }] }), 'full');
  assert.equal(resolveFileLevel('A.java', { compress: false, patterns: [
    { pattern: '*.java', compress: true }, { pattern: 'A.java', compress: false },
  ] }), 'compress');
});

test('comment-like text, escaped quotes, character literals and UTF-16 offsets remain intact', () => {
  const code = 'class A { String s = "😀 https://example.test /* not a comment */ \\\""; char c = \'/\'; /* erase */ int n = 1; }';
  const custom = { ...rules, remove_comments: [{ id: 'fixture', pattern: '^erase$' }] };
  const { output, before, after: result } = transform(adapter.parser, code, custom);
  assert.ok(output.includes('https://example.test /* not a comment */'));
  assert.ok(!output.includes('/* erase */'));
  assert.deepEqual(result.code_tokens, before.code_tokens);
});

test('removed inline comments retain lexical token boundaries', () => {
  const custom = { ...rules, remove_comments: [{ id: 'fixture', pattern: '^erase$' }] };
  const { output } = transform(adapter.parser, 'class A { int/* erase */n; }', custom);
  assert.match(output, /int\s+n/);
});

test('author/version tag continuations disappear while descriptions and parameter contracts remain', () => {
  const code = '/** Meaningful purpose.\n * @author Someone\n * affiliation\n * @version 1.0\n * @param n accepted values\n */\nclass A {}';
  const { output } = transform(adapter.parser, code, rules);
  assert.ok(output.includes('Meaningful purpose.'));
  assert.ok(output.includes('@param n accepted values'));
  assert.ok(!output.includes('@author') && !output.includes('affiliation') && !output.includes('@version'));
});

test('threading/lifecycle constraints win over aggressive custom removal rules', () => {
  const custom = { ...rules, remove_comments: [{ id: 'everything', pattern: '.*' }] };
  const code = '/** Must run after completion on the event dispatching thread. */ class A {}';
  assert.equal(transform(adapter.parser, code, custom).output, code);
});

test('identity-only constructor docs are removed only at constructor declarations', () => {
  const code = 'class A { /** Constructs an object of <code>A</code>. */ A() {} }';
  assert.ok(!transform(adapter.parser, code, rules).output.includes('Constructs'));
  const method = 'class A { /** Constructs an object of <code>A</code>. */ void helper() {} }';
  assert.equal(transform(adapter.parser, method, rules).output, method);
});

test('default date styles and meaningful class descriptions remain', () => {
  const code = '/** Default - Large theme for displaying the user interface elements enlarged.\n * @author Someone\n * @version 2.0\n */ class A { /** Both Date and Time styles are set to DateFormat.SHORT. */ A() {} }';
  const { output } = transform(adapter.parser, code, rules);
  assert.ok(output.includes('user interface elements enlarged'));
  assert.ok(output.includes('DateFormat.SHORT'));
});

test('empty and metadata-only files preserve the empty program', () => {
  assert.equal(transform(adapter.parser, '/** @author Someone */', rules).after.code_tokens.length, 0);
});

test('malformed Java and unsupported Unicode preprocessing fail instead of dropping text', () => {
  assert.throws(() => transform(adapter.parser, 'class A { void f( }', rules), /parsing failed/);
  assert.throws(() => transform(adapter.parser, 'class A {} // \\u002f', rules), /Unicode escape/);
});
