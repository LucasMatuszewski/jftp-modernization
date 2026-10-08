# Scoped JFTP Repomix trial

Pinned tool: Repomix 1.18.1 via npx, executed under Ubuntu-26.04 WSL. No global installation. Exactly five public files were included: ResourceLoader.java, Favorite.java, LocalFile.java, RemoteHost.java, and pom.xml. Outputs were written outside the source repository.

| Pack | Wall time | o200k_base tokens | UTF-8 bytes | Files |
|---|---:|---:|---:|---:|
| Full XML | 2.102 s | 6,976 | 26,805 | 5 |
| Compressed XML | 1.830 s | 5,445 | 20,541 | 5 |

Compression saved 1,531 tokens (21.95%) and 6,264 bytes (23.37%). These are single measured runs after the package cache was populated by version/help probes. Timings include npx startup, file selection, security scanning, token counting, and writing. This is a scoped trial, not a full-repository benchmark.

Both packs parse as XML, contain only the five expected file headers, retain the source copyright headers, and retain the file/class context. Full XML retains ResourceLoader.getBundle's complete multiline signature including ClassLoader loader; compressed XML drops that continuation and stops after Locale locale, followed by an omission marker. The three compareTo methods remain associated with their respective class declarations and file paths. All five full-pack file elements equal their source text after LF/trailing-newline normalization.

The full pack exposes the behavioral difference: LocalFile.compareTo returns 1 for a null argument; Favorite.compareTo and RemoteHost.compareTo instead cast their argument and use its fields. The compressed pack omits LocalFile's null guard, early return, and cast. It also omits the other two casts, retaining one-line declarations and final comparison expressions. Compressed output contains omission markers and is useful as navigation context; full output or original source is required to verify complete multiline signatures and behavior. The compressed generic file_format header still says Full contents of the file although other header fields correctly disclose compression.

Security scanning stayed enabled and reported No suspicious files detected for both runs. SHA-256 hashes of all five source files remained unchanged before generation, after generation, and after verification. No source or repository documentation was edited.

The initial verification assertion expecting a complete ClassLoader signature in both variants failed. Inspection confirmed genuine compressed-signature loss; this is recorded as a limitation, and final verification explicitly checks full retention and compressed omission.

The CLI emitted ANSI progress-spinner sequences despite NO_COLOR; this only affects machine parsing of its log. No repository or global configuration was discovered by the CLI.

## Artifacts

- jftp-scope.full.xml
- jftp-scope.compressed.xml
- full.log and compressed.log: actual tool statistics/security reports
- version.log and help.log: pinned CLI evidence
- results.json: exact commands, timings, byte counts, hashes, per-file token statistics, parsed XML checks, and extracted compareTo snippets
- verify_trial.py: verification script

All artifacts are in /home/lucas/.cache/legacy-map-review-20261008/repomix-trial.

## Copyable scoped commands

Set repo to a public JFTP checkout and artifacts to a directory outside that checkout. Keep the explicit include list when only these public files are authorized.

~~~sh
repo=/path/to/public/jftp
artifacts=/path/outside/repository/repomix-trial
mkdir -p "$artifacts"
scope='src/main/java/com/myjavaworld/util/ResourceLoader.java,src/main/java/com/myjavaworld/jftp/Favorite.java,src/main/java/com/myjavaworld/jftp/LocalFile.java,src/main/java/com/myjavaworld/jftp/RemoteHost.java,pom.xml'

npx --yes repomix@1.18.1 "$repo"   --style xml --parsable-style --no-git-sort-by-changes   --include "$scope" --token-count-encoding o200k_base   --output "$artifacts/jftp-scope.full.xml"

npx --yes repomix@1.18.1 "$repo"   --style xml --parsable-style --no-git-sort-by-changes   --include "$scope" --token-count-encoding o200k_base   --output "$artifacts/jftp-scope.compressed.xml" --compress
~~~
