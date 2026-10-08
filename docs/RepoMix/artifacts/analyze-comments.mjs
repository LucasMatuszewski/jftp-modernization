import fs from 'node:fs';
import path from 'node:path';
import { javaParser, inspect, normalized, transformComment, hash, here } from './java-comments.mjs';

const repo = path.resolve(here, '../../..');
const packageRoot = process.argv[2];
if (!packageRoot) throw new Error('Pass the pinned Repomix package root');
const adapter = await javaParser(packageRoot);
const records = [];
const walk = dir => fs.readdirSync(dir, { withFileTypes: true }).flatMap(item =>
  item.isDirectory() ? walk(path.join(dir, item.name)) : item.name.endsWith('.java') ? [path.join(dir, item.name)] : []);
try {
  for (const file of walk(path.join(repo, 'src')).sort()) {
    const data = fs.readFileSync(file); const source = data.toString('utf8');
    for (const comment of inspect(adapter.parser, source).comments) {
      records.push({ path: path.relative(repo, file).replaceAll('\\', '/'), sha256: hash(data),
        ...comment, normalized: normalized(comment.text) });
    }
  }
} finally { await adapter.dispose(); }
const texts = Object.fromEntries(records.map(record => [hash(record.text), record.text]));
const references = records.map(({ text, normalized: unused, start, end, ...record }) =>
  ({ ...record, comment_id: hash(text) }));
fs.writeFileSync(path.join(here, 'comment-inventory.json'), JSON.stringify({
  description: 'Parser-identified original comments, with deduplicated text and original source hashes/lines.',
  texts, comments: references,
}, null, 2) + '\n');
const rules = JSON.parse(fs.readFileSync(path.join(here, 'comment-rules.json'), 'utf8'));
const repeated = records.filter(record => transformComment(record, rules).rule === 'repeated-apache-header');
const notices = [...Map.groupBy(repeated, record => record.normalized)].map(([, items]) => ({
  notice: items[0].text,
  source_files: items.map(record => ({ path: record.path, sha256: record.sha256,
    start_line: record.start_line, end_line: record.end_line })),
}));
fs.writeFileSync(path.join(here, 'license-notices.json'), JSON.stringify({
  description: 'Exact unique Java notices retained once with source-file attribution. Original source and full reference retain all notices; pom.xml retains its own XML notice.',
  notices,
}, null, 2) + '\n');
const licenses = records.filter(r => r.normalized.startsWith('Copyright'));
const groups = Map.groupBy(licenses, r => r.normalized);
console.log(JSON.stringify({ comments: records.length, javadocs: records.filter(r => r.text.startsWith('/**')).length,
  license_groups: [...groups].map(([text, rows]) => ({ count: rows.length, text })),
  metadata_author: records.filter(r => /@author\b/.test(r.text)).length,
  metadata_version: records.filter(r => /@version\b/.test(r.text)).length,
  constructors: records.filter(r => r.next_type === 'constructor_declaration').length,
}, null, 2));
console.log('constructor examples', JSON.stringify(records.filter(r => r.next_type === 'constructor_declaration').slice(0, 16).map(r => r.normalized)));
