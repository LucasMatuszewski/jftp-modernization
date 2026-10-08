# Legacy codebase workflows: first installation review

**Historical first-use evidence (2026-10-07).** Later grouped maps, timings, setup changes and validation are indexed in [repository maps](repo-maps/README.md) and recorded in the [current audit](repo-maps/artifacts/2026-10-08/review.md). Original observations below remain unchanged.

Date: 2026-10-07. Platform: Windows / PowerShell. Repository revision: `08899cc9b09a977bf33f12ebcb855ba1b4a10b29`.

This is an evidence log for the first use of the published and merged skill, not an execution backlog. Scope: installed package, repository inventory/maps, native executable availability, local build requirements, and distribution improvements. JFTP application changes and startup are outside scope.

Installed skill: `C:\Users\BiuroEdukey\.agents\skills\legacy-codebase-workflows`.

Generated artifacts and isolated tooling will be kept outside this repository. Installed skill files will not be edited.

## Outcome

The repository-map workflow works on this Windows checkout after isolated Python dependency setup. The current CI Rust mapper and frozen Python bundle both run here without a local build and produce byte-identical Java maps to the installed Python source. All 182 selected Java files parse with no reported parse failures; the 4096-unit budget selects 159 of 1,586 definitions. All 588 files under `src` retain their SHA-256 hashes after the checks.

The installed skill does **not** include either executable. CI already builds platform-specific programs, but delivery is source-only through this skill installation, with expiring Actions artifacts and a stale static CI link. At review time, the repository's Releases API returns an empty list. Downloading existing CI binaries is sufficient here; installing Rust or building locally is unnecessary for this use.

The full results include an initial missing-dependency failure, documentation defects, and six failed review expectations about a soft file limit. The latter were investigated and explicitly corrected below; they are not six mapper regressions. Real hard-failure invalidation subsequently passes for all three programs.

## Initial observations

- The user calls the executable "raster". The supplied skill entrypoint does not mention that executable name; its documented first-run command is a Python script. The native-tooling reference needs inspection before identifying the actual executable.
- The first-run example uses Bash paths and an unspecified `python` interpreter. Windows installation, interpreter selection and native executable discovery must be tested.
- This machine's repository instructions report a broken Windows sandbox launcher. Necessary shell commands use the required narrow escalation from the start; no sandbox-failure repro is needed for this skill review.

## Evidence and findings

Results will be appended as checks run, including failures immediately after observation.

### Installed distribution: source only

Observed: recursive installed-file listing contains Python scripts, references, queries and license texts; no `.exe`, Rust crate (`Cargo.toml`) or `build-legacy-tools.py`. `references/setup.md` explicitly says "No binaries are stored in the skill or the repository" and requires the separate toolbox source to build them. The installed directory is not a junction/symlink.

The documented native executable is `legacy-repo-map`, implemented in Rust. The standalone reference bundle is `legacy-tools`, implemented by freezing Python with PyInstaller. No documented program is called `raster`.

First-use friction: instructions refer to "the toolbox repository" and published build artifacts without a concrete download command or URL in the setup page. A user cannot build either program from the installed skill alone. Shipping only source is consistent with current documentation, but does not provide the zero-toolchain installation requested by the user.

### Initial runtime checks

Artifact root: `C:\Users\BiuroEdukey\AppData\Local\Temp\legacy-skill-review-20261007-05bd`.

- `python --version`: Python 3.14.3. `py -0p` lists only Python 3.14 x64.
- `legacy_tools.py info` exits successfully but reports all three displayed parser/ranking packages as `null`. This is information, not a readiness check: its success does not mean mapping will work. It also omits the separately pinned C# grammar from the displayed package list.
- Executable discovery finds Rust/Cargo and Python, but no `raster`, `legacy-repo-map`, `legacy-tools` or Windows `herdr` command.
- Inventory-only succeeds without parser installation: 691 candidates, 540 selected files, including 182 Java files. It reports `inventory-only` and `truncated: false`. The root inventory includes local agent-skill trees; selecting an application module is necessary to avoid irrelevant source context.
- Browser attempts to open the documented native CI URL and the toolbox Releases page both fail with `Cache miss`. This is a browser/access failure, not evidence that CI or releases are absent. Authenticated read-only GitHub API checks are being used to resolve publication status.

### Documentation inconsistency found during reading

`references/repo-map.md` says Python map snippets replace control characters and Unicode line/paragraph separators with spaces. `references/native-tooling.md`, under "Control characters in a mapped line", says Python copies them unchanged. Both cannot describe the same current implementation. Check actual source and a synthetic fixture before choosing which text to correct.

### First mapping failure and CI availability

- Initial source map: `python -B <skill>/scripts/repo_map.py . --output-dir <artifacts>/missing-deps --budget 4096 --subtree src/main/java` exits **2**, stderr: `repo_map: No package metadata was found for tree-sitter`. Setup has not installed parsers automatically. The diagnostic identifies the missing package but does not give the setup command or link.
- GitHub API returns **no Releases** (`[]`) for `EdukeyTeam/agent-toolbox` at review time.
- The native CI run linked in the skill, `37575414253`, completed successfully on commit `2fe394ec9a0c90acbabca12447e1ea5095596ff7`, event `pull_request`. It contains three non-expired Actions artifacts: `legacy-tools-windows-latest` (14,396,365 bytes), `legacy-tools-ubuntu-latest` (28,356,877 bytes), and `legacy-tools-macos-latest` (14,128,509 bytes).
- This establishes that CI builds already exist. It does not establish that installers download them or that they match the merged revision. The next check uses the Windows artifact, not a local Rust build.

### CI binary startup and stale download pointer

- Downloading the Windows Actions artifact succeeds using `gh run download 37575414253 --repo EdukeyTeam/agent-toolbox --name legacy-tools-windows-latest --dir <artifacts>/ci-windows`. It contains both Rust and Python-bundle ZIPs, `SHA256SUMS` and `build-manifest.json`.
- Both ZIP hashes match `SHA256SUMS`. The Rust ZIP is 2,384,690 bytes, the bundle ZIP 12,427,620 bytes.
- Extracted `legacy-repo-map.exe --help` exits 0. Extracted `legacy-tools.exe info` exits 0 with frozen Python 3.12.10 and the expected displayed package pins. No Rust build, Cargo command, global install, PATH change or VC runtime install was needed for startup on this existing Windows machine.
- **Version drift:** the static CI link in the installed native-tooling reference points to older mapping code. Bundle `repo_map.py` SHA-256 is `6b6baaa8c9db2c8a30ab1e6764925686254db888f0c3591e31bd2e6136b16275`; installed source is `a9c83150e4ae72f6b464425acdd84fa37693aacf7ee09546cc20af0b6c5a1576`. `repo_files.py` and `context7_backend.py` also differ. Do not assume this older artifact validates the merged installed skill.
- Pinned dependencies install successfully as prebuilt wheels into an external Python 3.14.3 environment, using `uv venv` followed by `uv pip install --python <env>/Scripts/python.exe -r <skill>/requirements-map.txt` (about 4 seconds reported for resolution/download/install). No local compiler was needed for this Python setup.
- Current workflow `native-artifacts` already builds Rust with `cargo test --locked`, packages both programs with `--require-parity`, tests the actual binaries, and uploads artifacts for Ubuntu, macOS and Windows. **Retention is only 14 days.** No release publication step was present in the inspected workflow. The missing piece is durable, version-matched delivery to skill users, rather than initial CI compilation.

### Interpretation of runtime checks below

The six recorded failures for `*-inventory-cap` and `*-stale-map-invalidated` are failed **review expectations**, not confirmed implementation failures. Inspection after the unexpected result shows `--max-files` is intentionally a soft selection limit: exit 0, `status: complete`, `truncated: true`, and a wildcard skip reason `max_files exceeded (1); map a subtree`. It replaces the earlier map with a fresh limited map. The diagnostic sentence in the original `*-stale-map-invalidated` log described the expected outcome; it was not observed. This interpretation supersedes that sentence.

The documentation is unintuitive here: hard discovery limits fail, while `--max-files` produces a completed but incomplete map. It should distinguish these explicitly, separate selection truncation from budget truncation, and say that `complete` describes successful processing, not exhaustive repository coverage. The recorded full Java maps are budget-truncated by design (159 of 1,586 definitions), despite successful parsing of all 182 Java files.

### Incremental runtime evidence

- **PASS — checksum-legacy-tools-windows-x86_64.zip:** legacy-tools-windows-x86_64.zip: f2b91d43e1dcefdeb6a4ff68baaf59e9b6ac5245772192232889508619e7f657

- **PASS — checksum-legacy-repo-map-windows-x86_64.zip:** legacy-repo-map-windows-x86_64.zip: b248a036847d3619742a60c4a1a5e18e9314a9ac25738e92a412c3dc75c0c22a

- **PASS — checksum-legacy-tools.exe:** legacy-tools-windows-x86_64/legacy-tools.exe: 7e6ca874edcde17012728e6a622c5d199eb701f5e18f326b47ebdedf37a394db

- **PASS — checksum-legacy-repo-map.exe:** legacy-repo-map-windows-x86_64/legacy-repo-map.exe: 104f0ffa2c10a98d23ec137c045a7215aa30f80b4c9cfe75e7ed30029fa0d3b5

- **PASS — current-bundle-info:** exit 0 (expected 0), 1.196 s.

- **PASS — bundle-source-version:** Every script hash reported by the current CI bundle matches the installed skill.

- **PASS — rust-version:** exit 0 (expected 0), 0.277 s.

- **PASS — current-source-java:** exit 0 (expected 0), 4.413 s.

- **PASS — source-metadata:** {"status": "complete", "coverage": {"candidates_seen": 196, "definitions_found": 1586, "definitions_in_map": 159, "files_with_definitions": 179, "parsed_files": 182, "selected_files": 196}, "truncated": true, "estimated_tokens": 4096}

- **PASS — current-bundle-java:** exit 0 (expected 0), 3.955 s.

- **PASS — bundle-metadata:** {"status": "complete", "coverage": {"candidates_seen": 196, "definitions_found": 1586, "definitions_in_map": 159, "files_with_definitions": 179, "parsed_files": 182, "selected_files": 196}, "truncated": true, "estimated_tokens": 4096}

- **PASS — current-rust-java:** exit 0 (expected 0), 0.913 s.

- **PASS — rust-metadata:** {"status": "complete", "coverage": {"candidates_seen": 196, "definitions_found": 1586, "definitions_in_map": 159, "files_with_definitions": 179, "parsed_files": 182, "selected_files": 196}, "truncated": true, "estimated_tokens": 4096}

- **PASS — bundle-java-parity:** Compared map bytes, source fingerprint and coverage with installed Python source.

- **PASS — rust-java-parity:** Compared map bytes, source fingerprint and coverage with installed Python source.

- **PASS — source-warm-java:** exit 0 (expected 0), 5.248 s.

- **PASS — source-focus:** exit 0 (expected 0), 2.366 s.

- **PASS — source-focus-selection:** Windows path normalization, focus selection and small-budget map: {'candidates_seen': 52, 'definitions_found': 366, 'definitions_in_map': 4, 'files_with_definitions': 49, 'parsed_files': 50, 'selected_files': 52}

- **PASS — source-missing-focus:** exit 0 (expected 0), 2.282 s.

- **PASS — source-missing-focus-metadata:** Absent symbol explicitly reported; a completed map does not prove that focus exists.

- **PASS — rust-focus:** exit 0 (expected 0), 0.562 s.

- **PASS — rust-focus-selection:** Windows path normalization, focus selection and small-budget map: {'candidates_seen': 52, 'definitions_found': 366, 'definitions_in_map': 4, 'files_with_definitions': 49, 'parsed_files': 50, 'selected_files': 52}

- **PASS — rust-missing-focus:** exit 0 (expected 0), 0.557 s.

- **PASS — rust-missing-focus-metadata:** Absent symbol explicitly reported; a completed map does not prove that focus exists.

- **FAIL — source-inventory-cap:** exit 0 (expected 2), 1.697 s.

- **FAIL — source-stale-map-invalidated:** Successful output replaced by failed status after inventory-cap failure; coverage={'candidates_seen': 2, 'definitions_found': 0, 'definitions_in_map': 0, 'files_with_definitions': 0, 'parsed_files': 0, 'selected_files': 1}.

- **PASS — source-restore-java:** exit 0 (expected 0), 3.907 s.

- **FAIL — bundle-inventory-cap:** exit 0 (expected 2), 0.768 s.

- **FAIL — bundle-stale-map-invalidated:** Successful output replaced by failed status after inventory-cap failure; coverage={'candidates_seen': 2, 'definitions_found': 0, 'definitions_in_map': 0, 'files_with_definitions': 0, 'parsed_files': 0, 'selected_files': 1}.

- **PASS — bundle-restore-java:** exit 0 (expected 0), 3.273 s.

- **FAIL — rust-inventory-cap:** exit 0 (expected 2), 0.593 s.

- **FAIL — rust-stale-map-invalidated:** Successful output replaced by failed status after inventory-cap failure; coverage={'candidates_seen': 2, 'definitions_found': 0, 'definitions_in_map': 0, 'files_with_definitions': 0, 'parsed_files': 0, 'selected_files': 1}.

- **PASS — rust-restore-java:** exit 0 (expected 0), 1.344 s.

- **PASS — source-in-repo-output-rejection:** exit 2 (expected 2), 0.313 s. repo_map: output directory must be outside the source repository

- **PASS — rejected-output-not-created:** Output inside target repository rejected without creating the requested directory.

- **PASS — source-valid-citation:** exit 0 (expected 0), 0.306 s.

- **PASS — bundle-valid-citation:** exit 0 (expected 0), 0.218 s.

- **PASS — source-invalid-citation:** exit 1 (expected 1), 0.259 s.

- **PASS — source-control-fixture:** exit 0 (expected 0), 1.631 s.

- **PASS — source-control-sanitization:** Synthetic Java definition containing C0 and Unicode line-separator characters is sanitized in the rendered map.

- **PASS — rust-control-fixture:** exit 0 (expected 0), 0.100 s.

- **PASS — rust-control-sanitization:** Synthetic Java definition containing C0 and Unicode line-separator characters is sanitized in the rendered map.

- **PASS — source-unchanged:** Compared SHA-256 of all 588 files under src before/after runtime checks.

- **PASS — source, actual hard inventory failure:** a synthetic `.gitignore` of 256,001 bytes produces exit 2, status `failed`, and replaces the previously successful map. Stderr: `repo_map: file exceeds max_file_bytes`.

- **PASS — bundle, actual hard inventory failure:** a synthetic `.gitignore` of 256,001 bytes produces exit 2, status `failed`, and replaces the previously successful map. Stderr: `repo_map: file exceeds max_file_bytes`.

- **PASS — rust, actual hard inventory failure:** a synthetic `.gitignore` of 256,001 bytes produces exit 2, status `failed`, and replaces the previously successful map. Stderr: `legacy-repo-map: cannot inventory directory .: ignore file exceeds 256000 bytes; select a smaller source tree`.

## Distribution review prompted by the user

### Why availability was not obvious immediately

This was not caused by a compiler failure or inability to run Windows binaries. The entrypoint recommends Python source, sends first-time users to a long setup reference, and never names a ready-to-run native artifact or platform selection command. Setup says no binaries are included and refers generically to the toolbox repository. Only the native reference links to one historical PR CI run. That run succeeds but embeds older scripts than this installed release.

The source-only installed-file listing and missing commands initially establish only that nothing is installed locally. To discover usable executables, the agent must find the toolbox URL in another reference, query Actions, distinguish a PR run from the merged run, download the artifact container, unpack a second archive, and compare hashes. The skill should resolve all of that during publication, before users enter it.

The user mentioned GitHub Releases. The observed storage is **GitHub Actions artifacts**, not Releases: `gh api repos/EdukeyTeam/agent-toolbox/releases` returns `[]`. The distinction matters because the current workflow retains these artifacts for only 14 days. Merely adding a "latest CI" link would still leave expiration, version matching and platform selection to every consumer.

### Current platform packages and measured sizes

All packages below are from successful merged-main run [37633697013](https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37633697013), source commit `8d922e517fe81d6fa978b37611e57bd6f1f7bfbc`. All six archive checksums were verified against their corresponding `SHA256SUMS`. Linux/macOS packages were inspected and hashed, not executed on this Windows host.

| Actual artifact platform | Native mapper archive | Python reference bundle archive |
| --- | ---: | ---: |
| Windows x86-64 | `legacy-repo-map-windows-x86_64.zip`: 2,394,627 bytes | `legacy-tools-windows-x86_64.zip`: 12,433,680 bytes |
| Linux x86-64 | `legacy-repo-map-linux-x86_64.tar.gz`: 2,379,097 bytes | `legacy-tools-linux-x86_64.tar.gz`: 26,346,170 bytes |
| macOS arm64 | `legacy-repo-map-macos-arm64.tar.gz`: 2,307,642 bytes | `legacy-tools-macos-arm64.tar.gz`: 12,116,603 bytes |

Together the three compressed native packages are **7,081,366 bytes**; the three reference packages are **50,896,453 bytes**. These archives include notices and build information, not just executables. The extracted Windows Rust executable alone is **17,121,792 bytes**, so "2.4 MB binary" describes its compressed distribution, not its installed size. Check installed sizes separately before storing raw executables for every platform.

There is no inspected artifact for Windows ARM64, Linux ARM64 or Intel macOS. WSL must select the Linux package, not the Windows package. Linux distro/libc compatibility and a fresh Windows VC-runtime prerequisite remain unverified here; existing-host execution does not establish them. CI labels such as `macos-latest` should not be used as durable platform identities: the inspected manifest identifies `macos-arm64`.

### Recommended delivery design

For the user's requirement that a normally installed skill already contains its native mapper, ship **the three compressed native archives with the skill**, generated from one pinned source revision by CI, plus notices and a platform manifest. About 7.1 MB total is a plausible tradeoff for this small platform set. Do not ship all three raw executables or all Python reference bundles in the ordinary skill. A launcher extracts only the selected archive into a versioned user cache outside both the target repository and installed skill. Windows can use PowerShell archive support; Unix can use `tar`. Mapping then requires neither Python nor Rust. This is a proposed change: today's installation does not do it.

If committing those generated archives to the main source history is undesirable, produce an installable skill distribution from CI instead: source instructions/scripts plus one matching platform archive, published as immutable versioned release assets. This is the preferred scalable approach once the platform set or update frequency grows. It needs an installer that downloads the complete skill distribution once at installation; publishing a binary Release by itself does not make a source-based `npx skills` installation include it. The current source installer has no inspected step that fetches executable assets.

Keep the large frozen reference bundles as optional versioned release assets. Provide their exact URLs and hashes in the manifest when reference behavior is required. Avoid Git LFS pointers as a transparent fix unless the actual skill installer is tested to resolve them; copying a pointer file would recreate first-use failure.

Rust remains experimental in this version. Java parity passed here, but the skill documents Python-grammar differences and incomplete real-corpus validation for other languages. Bundling it must not silently promote it as a universal reference implementation. During that transition, the entrypoint should explicitly distinguish `native` mapping for the validated scope from `reference` behavior using Python source or its frozen bundle. Promotion should follow the documented parity gates, not merely successful packaging.

### A manifest that eliminates release searching

Add a CI-generated `tool-distribution.json` inside the distributed skill. Each entry should pin the skill/source commit, tool version, exact OS/architecture, local archive path, immutable release URL for an optional absent asset, archive SHA-256, executable SHA-256, executable path, notices path, runtime prerequisites and validation status. Store the current skill's revision, not a moving `latest` URL. Native `0.1.0` alone is not enough to distinguish these two different inspected builds.

The launcher should choose and verify one manifest entry locally. It should not query "recent releases", run `cargo`, install Python packages, edit PATH globally or silently switch from reference to experimental behavior. A missing/unsupported package should produce a clear platform-specific diagnostic with the pinned optional setup route. If network fetching is a supported fallback, do it during explicit setup, then cache and verify it; ordinary map generation stays offline.

Because the manifest pins the assets, neither the human nor agent needs to check which releases were made recently. Updating the skill updates that manifest and its bundled archives together. CI should verify this relationship and run first-use tests on the **actual installed skill layout**, not only on the toolbox checkout.

### What the agent should see at skill entry

The first screen of `SKILL.md` should name `legacy-repo-map` and `legacy-tools`, state what is included in that installation, link the pinned manifest, and show one launcher command. Put OS/architecture choice in the launcher rather than asking the agent to infer archive names. For example, after implementing the proposed launcher:

```powershell
& '<installed-skill>\scripts\repo-map.ps1' '<repository>' --output-dir '<external-artifacts>' --mode native --budget 4096
```

```bash
sh '<installed-skill>/scripts/repo-map.sh' '<repository>' --output-dir '<external-artifacts>' --mode native --budget 4096
```

These launcher commands are **design examples and do not exist today**. Their contract should be: detect platform, read the pinned manifest, verify/extract the packaged archive, preserve notices, invoke the matching executable, forward arguments and exit code, and report the map's coverage/truncation. The entrypoint must clearly state when `reference` is required and explain unsupported platforms. Detailed Rust build instructions belong in maintainer documentation, not the consumer's first-use route.

## Additional concrete review findings

| Finding | Evidence and suggested correction |
| --- | --- |
| Native availability hidden at entry | Add included executable names, platform manifest and launcher command to `SKILL.md`; prioritize the installed distribution rather than an unspecified Python interpreter. |
| No durable published binary delivery | Current Actions artifacts expire after 14 days; Releases API is empty. Publish immutable versioned artifacts and couple their manifest/archives to the skill distribution. |
| Stale native CI link | Historical PR artifact scripts differ from installed scripts. Replace this as an installation route with version-pinned provenance; historical benchmarking links may remain explicitly historical. |
| Source readiness not established by `info` | Exit 0 with missing packages; C# package omitted from summary. Add a readiness/capability check and display all parser dependencies that mapping requires. |
| Missing-dependency error lacks next step | `No package metadata was found for tree-sitter` should identify the chosen mode and give the isolated setup or bundled-program command. |
| Outdated control-character difference | Installed `repo_map.py:168` sanitizes control characters. Synthetic C0/U+2028 definition tests pass in Python and Rust. Correct `native-tooling.md`'s claim that Python copies them unchanged. |
| Ambiguous `complete` and limit semantics | `--max-files 1` returns complete/truncated, unlike a hard discovery failure. Explain successful processing versus exhaustive coverage and report truncation reasons separately. |
| Hard ignore-limit diagnostic loses context in Python | A 256,001-byte `.gitignore` fails with `file exceeds max_file_bytes` despite the ordinary source limit being 2,000,000 bytes. Rust names the directory, ignore file and 256,000-byte limit. Python should name the actual admission limit and source path. |
| Root inventory admits repository-local agent skills | This checkout's full inventory contains `.agents/skills` and `.claude/skills`. Keep module selection explicit; consider an opt-in application-source preset without hiding user code by default. |
| Platform coverage easy to overread | Current artifacts cover only Windows/Linux x86-64 and macOS arm64. Name exact platforms and compatibility prerequisites; do not imply all devices are supported. |

## Reproducing the working path today

Existing CI download, without building locally:

```powershell
$reviewRoot = Join-Path $env:TEMP 'legacy-skill-review-20261007-05bd'
gh run download 37633697013 --repo EdukeyTeam/agent-toolbox --name legacy-tools-windows-latest --dir "$reviewRoot\ci-current-windows"
# Verify both archive hashes against SHA256SUMS before unpacking.
Expand-Archive -LiteralPath "$reviewRoot\ci-current-windows\legacy-repo-map-windows-x86_64.zip" -DestinationPath "$reviewRoot\ci-current-windows\unpacked"
& "$reviewRoot\ci-current-windows\unpacked\legacy-repo-map-windows-x86_64\legacy-repo-map.exe" . --output-dir "$reviewRoot\current-rust-java" --subtree src/main/java --budget 4096
```

The download/unpack commands above target fresh directories; those directories already exist from this review. This run's assets will expire according to Actions retention, so this is a reproducible description of the test, not a durable installation recommendation.

Python source setup and mapping that worked here:

```powershell
$skillRoot = 'C:\Users\BiuroEdukey\.agents\skills\legacy-codebase-workflows'
$reviewRoot = Join-Path $env:TEMP 'legacy-skill-review-20261007-05bd'
uv venv --python 3.14 "$reviewRoot\python-env"
uv pip install --python "$reviewRoot\python-env\Scripts\python.exe" -r "$skillRoot\requirements-map.txt"
& "$reviewRoot\python-env\Scripts\python.exe" -B "$skillRoot\scripts\repo_map.py" . --output-dir "$reviewRoot\current-source-java" --subtree src/main/java --budget 4096
```

On this shared Windows host, `-B`/`PYTHONDONTWRITEBYTECODE=1` was used to avoid writing bytecode into installed skill directories. `uv` was already available; it is a convenience here, not a newly required dependency of the skill.

## Evidence locations and verification limits

Artifact root holds both historical and merged CI downloads, unpacked Windows programs with notices, complete restored Java maps, focus maps, inventories, valid/invalid citation cards, synthetic fixtures, per-command JSON logs, `verification-results.json` and `hard-failure-results.json`. The one-off verification scripts were removed after use. Installed skill files and JFTP runtime code were not edited. Downloaded tooling was not added to global PATH or installed across devices.

Observed command wall times for one current-run sample: Python cold 4.413 s, bundle 3.955 s, Rust 0.913 s; Python repeat 5.248 s. These are shared-host single samples, not a benchmark or evidence that caching improves latency here. The native program's speed does not resolve its documented cross-language differences.

No JFTP build, application startup, transfer, TLS test or desktop QA was performed or required for this skill-distribution review. Linux/macOS runtime compatibility, unsupported architectures, release publishing and automatic binary installation remain unexecuted. The review identifies those delivery changes; it does not implement or roll them out.
