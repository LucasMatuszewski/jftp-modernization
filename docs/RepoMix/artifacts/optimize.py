"""Measure selective comment policies and verify actual Repomix output.

All repository writes stay in docs/RepoMix; temporary staging is external.
Run after the pinned npm package is cached: python docs/RepoMix/artifacts/optimize.py
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import time

from generate import VERSION, ARTIFACTS, OUTPUT, REPOSITORY, locate_cli, parse_pack, source_snapshot


def main():
    cli = locate_cli(None)
    # Entry is package/bin/repomix.cjs; resolve without changing installed code.
    package = cli.parent.parent
    node = shutil.which('node')
    env = {**os.environ, 'REPOMIX_PACKAGE_ROOT': str(package)}
    before = source_snapshot()
    subprocess.run([node, str(ARTIFACTS / 'analyze-comments.mjs'), str(package)], env=env, check=True)
    revision = subprocess.check_output(['git', '-C', str(REPOSITORY), 'rev-parse', 'HEAD'], text=True).strip()
    staging = Path(tempfile.mkdtemp(prefix='jftp-repomix-optimization-'))
    if staging.is_relative_to(REPOSITORY):
        raise RuntimeError('Staging must be outside the source repository')
    baseline = json.loads((ARTIFACTS / 'manifest.json').read_text(encoding='utf-8'))
    if baseline['source_files'] != before:
        raise RuntimeError('Baseline pack is stale; regenerate it before comparing')
    config = json.loads((ARTIFACTS / 'repomix.config.json').read_text(encoding='utf-8'))
    policy = json.loads((ARTIFACTS / 'comment-rules.json').read_text(encoding='utf-8'))
    notices = json.loads((ARTIFACTS / 'license-notices.json').read_text(encoding='utf-8'))['notices']
    notice = '\n\n'.join(item['notice'] for item in notices)
    variants = ['builtin-no-comments-full', 'builtin-no-comments-compressed',
                'selective-full', 'selective-compressed', 'hybrid']
    reports = {}
    contents = {}
    for mode in variants:
        current = json.loads(json.dumps(config))
        current['output']['compress'] = mode.endswith('compressed') or mode == 'hybrid'
        current['output']['removeEmptyLines'] = True
        if mode.startswith('builtin'):
            current['output']['removeComments'] = True
        else:
            current['output']['headerText'] = (
                'Java notices are consolidated here; original attribution is indexed in '
                'docs/RepoMix/artifacts/license-notices.json. Original source and the full reference retain all notices.\n' + notice
            )
            current['input']['processors'] = [{
                'pattern': '**/*.java',
                'command': 'node docs/RepoMix/artifacts/java-comments.mjs {file}',
                'timeout': 30000, 'onError': 'fail',
            }]
        if mode == 'hybrid':
            current['output']['patterns'] = [
                {'pattern': pattern, 'compress': False}
                for pattern in policy['full_file_patterns']
            ] + [{'pattern': '**/*.java', 'compress': True}]
        config_path = ARTIFACTS / f'repomix.{mode}.config.json'
        config_path.write_text(json.dumps(current, indent=2) + '\n', encoding='utf-8', newline='\n')
        pack = staging / f'jftp-source.{mode}.xml'
        command = [node, str(cli), str(REPOSITORY), '--config', str(config_path), '--output', str(pack)]
        start = time.perf_counter()
        process = subprocess.run(command, cwd=REPOSITORY, env=env, capture_output=True, text=True, encoding='utf-8')
        elapsed = time.perf_counter() - start
        log = re.sub(r'\x1b\[[0-?]*[ -/]*[@-~]', '', process.stdout + process.stderr)
        (staging / f'{mode}.log').write_text(log, encoding='utf-8', newline='\n')
        if process.returncode:
            raise RuntimeError(f'{mode} failed; inspect {staging / (mode + ".log")}')
        contents[mode] = parse_pack(pack, set(before))
        counts = re.findall(r'Total Tokens:\s*([\d,]+)', log)
        if not counts or 'No suspicious files detected' not in log:
            raise RuntimeError(f'Missing statistics or unexpected security result: {staging}')
        data = pack.read_bytes()
        tokens = int(counts[-1].replace(',', ''))
        reports[mode] = {'command': command, 'elapsed_seconds': elapsed, 'tokens': tokens,
                         'utf8_bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                         'files': len(contents[mode]), 'xml_valid': True, 'file_coverage_exact': True,
                         'security_no_suspicious_files': True,
                         'published': not mode.startswith('builtin')}
        print(f'{mode}: {tokens:,} tokens, {elapsed:.2f}s', flush=True)
    content_path = staging / 'pack-contents.json'
    content_path.write_text(json.dumps(contents), encoding='utf-8', newline='\n')
    subprocess.run([node, str(ARTIFACTS / 'validate-optimization.mjs'), str(package), str(content_path)],
                   env=env, check=True)
    if before != source_snapshot():
        raise RuntimeError('Original source changed during optimization; regenerate')
    flags = {}
    for mode, files in contents.items():
        flags[mode] = {
            'ClassLoader_parameter_retained': 'ClassLoader loader' in files['src/main/java/com/myjavaworld/util/ResourceLoader.java'],
            'LocalFile_null_guard_retained': 'if (obj == null)' in files['src/main/java/com/myjavaworld/jftp/LocalFile.java'],
        }
    manifest = {'version': VERSION, 'source_revision': revision, 'source_files': before,
                'sources_unchanged': True, 'token_encoding': 'o200k_base',
                'baseline_tokens': {mode: stats['tokens'] for mode, stats in baseline['runs'].items()},
                'variants': reports, 'known_boundary_checks': flags,
                'rules_sha256': hashlib.sha256((ARTIFACTS / 'comment-rules.json').read_bytes()).hexdigest()}
    for mode in variants:
        shutil.copyfile(staging / f'{mode}.log', ARTIFACTS / f'{mode}.log')
        if reports[mode]['published']:
            destination = OUTPUT if mode == 'selective-full' else ARTIFACTS
            shutil.copyfile(staging / f'jftp-source.{mode}.xml', destination / f'jftp-source.{mode}.xml')
    (ARTIFACTS / 'optimization-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(f'Optimization verified; staged measurements: {staging}', flush=True)


if __name__ == '__main__':
    main()
