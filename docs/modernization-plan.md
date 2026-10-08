---
approval: draft
goal: user-requested behavior-preserving JFTP modernization
beads: sacs-qy7v
---

# JFTP modernization plan

This is a proposed engineering sequence for the existing JFTP desktop application at baseline revision `14e62ce`, on branch `Luna-subagents-modernization`. The original authorization covered documentation and planning. On 2026-10-08 the user authorized the first Windows build/startup attempt, minimal necessary repairs and useful basic tests. The [Windows startup guide](windows-startup.md) records this bounded execution slice. The rest of this plan remains a draft; this instruction does not authorize broad modernization, protocol replacement or state migration, and the limited startup checks do not establish the four-suite gates.

## Objective and completion boundary

Modernize the existing Java Swing FTP/FTPS application while preserving its useful desktop workflows, transfer semantics, user data, locales, help, and distribution forms. Keep the existing `FTPClient` adapter boundary until artifact availability, API behavior, licensing, and a replacement decision are evidenced. Keep startup/build repair, the four behavioral suites, application behavior fixes, dependency upgrades, Java API refactoring, security corrections, and packaging in separate reviewable changes.

The proposed compatibility path is JDK 21 as the initial bootstrap because it is available on the current Windows checkout; JDK 25 LTS is the candidate end target. JDK 26 is a non-LTS release and removes `java.applet` and `javax.swing.JApplet`; retaining and compiling `JFTPApplet` therefore constrains the proposed ceiling to JDK 25 unless the owner explicitly decides to remove or replace that entry point. Browser applet deployment is already unsupported by current browser/JDK deployment technology and is not implied by keeping the source. Recheck tool versions, licenses, support, and platform needs when implementation begins. ([Oracle Java SE roadmap](https://www.oracle.com/java/technologies/java-se-support-roadmap.html), [Oracle removed APIs in JDK 26](https://docs.oracle.com/en/java/javase/26/migrate/removed-apis.html), researched 2026-10-06.)

## Original baseline evidence and authority

The baseline has 576 tracked files: 182 Java sources and 394 non-Java paths. The three source-reading ledgers cover 79 support/security, 59 application/workflow, and 44 UI/browser Java files; the build/resources ledger records the remaining inventory and binary assets. The analysis and current-state pages are in [the documentation index](README.md). Analysis was static. The current environment report says Microsoft OpenJDK 21.0.10+7 is available and `mvn` is not recognized on this PowerShell `PATH`; no Maven wrapper exists in the repository. Maven dependency resolution, compilation, startup, test execution, GUI behavior, network behavior, and distribution launch remain unverified. The untracked `micro` file predates this work and stays untouched.

Use only synthetic preferences, favorites, certificates, keystores, local trees, and FTP server state in future verification. The real profile data directory is `${user.home}/.jftp/data`; preferences and favorites use Java serialization, preference passwords are serialized as char arrays, favorites wrap a password-bearing host list in fixed-key AES `SealedObject` with a plaintext fallback, and certificate stores default to JKS files under that directory. These are compatibility facts, not acceptable secret-storage goals. See [TLS and persistence](tls-and-persistence.md) before changing storage.

Protocol/source and repository-asset evidence, plus primary-source options for TLS, FTP client maintenance, and optional SFTP, are summarized in [security modernization options](security-modernization-options.md). In this checkout, built-in support evidenced by source is FTP/FTPS; no runtime TLS version is proven, and SFTP would be a separate new feature outside this plan.

## Original dependency and compatibility map

| Dependency or blocker | What it blocks | Required evidence or gate |
|---|---|---|
| Maven is not on the reported `PATH`; there is no wrapper or documented Maven profile | Reproducible compile, test, package, and distribution checks | In a later authorized phase, establish one approved Maven installation or project wrapper, record version and checksums/source, then run with isolated local repository/settings if needed. Do not download or install tools in this planning phase. |
| POM source/target `1.5`, `maven-compiler-plugin:2.4`, old Maven plugins/extensions and implicit lifecycle defaults | JDK 21 compilation and modern test execution may fail before application code is assessed | Capture the first reproducible failure. If required, make the smallest compiler/plugin/bootstrap change that allows current source and the tests to compile. Keep it separate from broad Java cleanup and document every intentional build-model change. |
| `com.myjavaworld:ftpapi:3.0.0` from the configured legacy HTTP repository; no jar is tracked and availability/license are unknown | Main application compilation and all real FTP/FTPS integration suites | Resolve provenance, artifact bytes, API surface, transitive dependencies, repository availability, and redistribution rights before replacement or distribution. Do not assume the original artifact is unavailable merely because it is not checked in. Do not replace it with a utility-only fake or direct FTPAPI tests. |
| `javax.help:javahelp:2.0.05` and the bundled help set | Compilation, help-dialog startup, help IDs and topic navigation | Verify resolution and license, then smoke-test `JFTPHelp2`, help IDs, map/TOC links, and all delivered help resources. The local-open map path appears inconsistent with the tracked HTML path and needs a launch-backed correction. |
| Legacy direct macOS EAWT import in `OSXAdapterOld`; active reflective `OSXAdapter` path | Standard-JDK compilation may fail, while macOS menu actions are compatibility behavior | Verify exact compile failure and whether old adapter is referenced. Make only the necessary source/build adjustment; retain and verify About, Preferences, Quit, and full-screen behavior on supported macOS before removing any platform path. |
| `JFTPApplet` and applet localization/resource references | Java 26 compile compatibility and unresolved legacy deployment support | Decide whether the source entry point remains supported. If retained, validate on JDK 25 or earlier. If removed/replaced, scope an explicit user decision and update documentation/resources together; do not infer that source presence means a modern browser can run it. |
| JUnit 3.8.1, no tracked test classes, empty test placeholders, no explicit Surefire configuration | Four new suites and reliable red/green evidence | JUnit 6.1.3 is a candidate as of 2026-10-06 and requires Java 17 or higher at runtime, so it can run on the reported JDK 21. Verify exact Jupiter, Surefire/Failsafe, server-fixture, GUI-display, and JDK compatibility together before pinning. Keep all JUnit artifact versions aligned. ([JUnit user guide](https://docs.junit.org/6.1.3/overview.html), researched 2026-10-06.) |
| Old compiler/build plugins, `wagon-ftp:2.2`, legacy HTTP artifact repository, custom assembly and filtered script paths | Resolution, POM validation, packaging, release/archive reproducibility | Separate core Maven upgrade from plugin upgrades and packaging fixes. Inventory resolved artifacts, notices, licenses, and script inputs; do not treat legacy endpoints as live or legally redistributable without verification. |
| Assembly layout versus `jftp.bat`/`jftp.sh` jar path, unset script-source property, manifest classpath | End-user launch from ZIP, directory and tar.gz packages | Compare actual packaged file paths, filtering, executable bits, classpath and both launchers. Preserve all three archive types unless owners/consumers decide otherwise. Do not claim assembly output before an authorized package run. |
| Java object serialization for preferences/favorites and explicit JKS stores | Existing user settings, favorite credentials and imported trust on upgrade | Preserve readable existing formats and configured paths until isolated compatibility tests, backup/migration behavior, and explicit credential/storage decisions exist. Never test against or rewrite a real user home. |
| Legacy TLS trust manager and certificate-only UI import; unsafe ZIP extraction/path naming | FTPS security and archive safety | Keep current defects distinct from intended contracts. Add fail-first correction cases within suites 3 and 4. Decide visible TLS prompt/override policy explicitly; correct archive path traversal before treating rejection as green. Do not disable TLS globally or silently drop old-server connections. |
| Swing worker and FTP callback threading, dialog creation during TLS validation | UI responsiveness, ordering, cancellation, status and thread safety | Characterize operation-level output first. Refactor worker replacement and EDT callback marshaling separately, with visible/session assertions and a real display for UI paths. Do not preserve thread counts or private worker implementation as product contracts. |

Security modernization candidates are deliberately narrow: preserve the FTP/FTPS boundary while verifying FTPAPI 3.0.0 provenance and rights; Apache Commons Net 3.13.0 is a Java 8+ FTP/FTPS candidate, not yet selected. Prefer TLS 1.3 and retain TLS 1.2 interoperability; disable TLS 1.0/1.1. Apache MINA SSHD 2.20.0 is an optional SFTP/SSH candidate only if separately authorized as new functionality. This repository scan found zero tracked certificate/key/store assets, and the coordinator's dated existence-only check found the two default profile JKS files absent; no trust-store contents or custom paths were read. See [the full concise options and source links](security-modernization-options.md).

As of 2026-10-06, Apache lists Maven 3.10.0 as a GA release and 3.9.16 as the maintained prior series; Maven 4 remains pre-GA. Maven 3.10.0 tightens POM validation and changes dependency classpath ordering, so use 3.10.0 as the candidate tool and 3.9.16 as a controlled comparator only if a reproducible resolver/core issue blocks the candidate. Fix invalid project metadata rather than masking it with downgrade or validation escape hatches. ([Maven 3.10.0 release notes](https://maven.apache.org/docs/3.10.0/release-notes.html), [Maven release history](https://maven.apache.org/docs/history.html), researched 2026-10-06.)

## Safe parallel work and serialized changes

The completed source analyses were disjoint. During implementation, independent synthetic fixture preparation and read-only compatibility research may run concurrently. Keep changes to the shared `pom.xml`, compiler/test plugins, application startup/session core, serialized state, TLS trust policy, and package layout serialized. A contributor changing one of these must land or checkpoint before the next dependent change starts. Do not allow parallel Maven edits or simultaneous test failures to obscure attribution.

| Work may run concurrently | Must remain serialized |
|---|---|
| Synthetic fixture design for the four suites; official documentation/license research; source-to-test traceability review; per-platform launcher inventory | POM/compiler/Surefire/Maven-wrapper changes; shared `FTPSession` or `JFTP` code; any change to preference/favorite/keystore formats; TLS prompt/validation policy; ZIP extraction path policy; assembly/script path correction |
| Independent review of locale/help maps and asset references | Shared resource path or localization rewrite; broad Java API/source-level migration |
| Test design for a suite whose dependencies are settled | Changes to common Swing worker, shared event contracts, or `FTPClient` adapter while another suite is being re-baselined |

## Ordered phases and gates

### Phase 0 — Baseline documentation and design

This was the original documentation phase. Its deliverables are the architecture, dependency, workflow, UI/browser, support/security, regression design, resources/distribution, analysis-method pages, root and nested instructions, and coverage ledgers. The baseline identity remains `14e62ce`; the per-file ledgers are read/inventory evidence, not runtime verification.

**Validation artifact:** coordinator checks the combined ledgers against the 576-path baseline manifest, confirms 182 Java reads and 394 non-Java inventory paths with no duplicate/omitted owned files, checks all relative documentation links, and checks that only the authorized docs/instruction outputs changed. Report tool facts and all runtime gaps plainly.

**Gate:** no implementation proceeds under this phase authorization. Phase 1 requires a new user instruction. The coordinator owns any commit/checkpoint; delegates do not commit or push.

**Rollback:** documentation-only edits are reversible by explicit path and do not touch application data. Preserve the original baseline manifest/identity and do not delete unrelated untracked files.

### Phase 1 — Build bootstrap and four behavioral suites

**Prerequisites:** a new user instruction authorizes test/build work; verify the current branch and worktree; create per-run temporary `user.home`, local files, remote fixture tree, certificate stores, ports and display; resolve the FTPAPI source/artifact and licensing gate; identify the supported OS/JDK matrix. Install or invoke a pinned Maven only after that instruction. Maven 3.10.0 GA is the current candidate, with 3.9.16 as the evidence-based comparator. No project Maven wrapper exists today, so future command examples depend on which wrapper/tool path the owner approves.

Start by attempting a clean current-source build with JDK 21 and capturing exact command, environment, stdout/stderr, resolved artifact coordinates and POM warnings/errors. If source cannot compile, make the narrowest reproducible bootstrap adjustment needed to execute characterization tests—such as a compiler plugin/source-level setting or a proven platform import blocker—then record that this was not an untouched runnable baseline. Do not relabel bootstrap fixes as application regressions, substitute mock-only transfer tests for the application, or claim baseline green before each suite runs.

Implement exactly the four suites specified in [behavioral regression design](regression-test-design.md), in this order. Start each with its smallest demonstrable case; expand to the listed edge cases before risky refactors:

1. **Startup, session selection, preferences and favorites:** launch JFTP with isolated `user.home`; verify first-start defaults and one session; add/select multiple sessions; save/reload representative preference and favorite values; verify duplicate handling and synthetic password-bearing favorite persistence.
2. **Local and remote browser behavior:** on temporary local and controlled remote trees, cover pane navigation, roots/breadcrumbs, refresh, selection before/after sorting, selected-row versus blank-area context menus, filters (including hidden-file/exclusion inversion and lenient dates), create/rename/delete confirm and cancel, and visible listings. Add spaces, Unicode, and case-sensitive names where platform/server permits.
3. **Transfer and archive workflows:** invoke actual JFTP `FTPSession` transfer/archive actions, not FTPAPI-only helpers. First upload/download a binary fixture and assert exact bytes. Expand to ASCII conversion, renamed targets, recursion/filtering, manual/default mode, progress/status, permission/data-channel failures, and gated abort. Exercise archive temp/chosen destinations, deletion option, and traversal rejection. ZIP traversal rejection is an intended security correction and must remain tracked as expected-failing until fixed; do not claim all suites green by skipping or disabling it.
4. **FTPS certificate and trust decisions:** use loopback explicit/implicit FTPS and generated certificates; cover trusted connection, the untrusted host-matching prompt accept/reject path, expired/not-yet-valid, hostname mismatch, separately installed trust across restart, and handshake failure. Mark modern hostname/PKIX enforcement as a pending correction; unsafe acceptance is a defect, not a desired stable contract. Choose visible prompt/override policy explicitly.

UI-dependent cases must assert user-visible/session outcomes and relevant file or saved-state changes. Include Preferences panel validation and save/cancel/default behavior (noting that Software Updates “Check Now” begins immediately), connection field trim-to-validate but raw-value persistence, command/session selection routing, recursive remote-property working-directory restoration, and cancellation/close behavior where safe and deterministic. See [UI/browser details](ui-and-browser-details.md) for the source-grounded edge-case catalog; it refines these four suites and does not add a fifth.

These four are whole-application suites: unit assertions may support their deterministic data transformations, but suites 2–4 must cross the application/session/action or visible UI boundary when the behavior depends on FTP, browser, archive, or TLS orchestration. Assert destination bytes and paths, visible/session output, prompts, cancellation/status, or persisted compatibility—not helper classes, private fields, internal loops or thread counts. Use deterministic loopback servers, isolated homes and unique ports; no public servers, real secrets, remote customer files, or developer profile state.

For each change, preserve the failing report as red evidence, apply the smallest fix, then run the same case for green evidence. Keep baseline characterization and deliberate correctness/security fixes distinguishable inside the four suites. Never skip, weaken or regenerate expected results just to accommodate a changed-code regression. Record test counts, command, JDK, Maven, fixture versions, failure output and known exclusions.

**Validation artifacts:** baseline build/resolution log; one fixture design and execution report per suite; isolated serialized-state fixtures; local FTP server logs/state; prompt decision evidence; test counts; build/test reports; red/green evidence for deliberate fixes.

**Gate:** all four suites have at least a deterministic vertical-slice case and are runnable; the transfer slice exercises actual app orchestration; legacy-safe characterization passes on the isolated baseline; known unsafe ZIP/TLS expectations remain tracked as pending corrections, not disabled or omitted to claim an all-green result. If FTPAPI cannot be obtained/licensed or required server/UI fixtures cannot be made deterministic, stop at that blocker and report the evidence rather than swapping protocol libraries silently.

**Rollback:** checkpoint test harness and each suite independently. Revert only the specific bootstrap/test commit if it makes the already-established build less reproducible. Never mutate live preferences, stores or files as rollback state.

### Phase 2 — Minimum application startup, one blocker at a time

With the suite harness in place, repair only what is necessary for the desktop application to compile and start on the bootstrap JDK. Follow actual failures in dependency order: Maven/core model and source level; missing/legal dependency; direct Apple API compile blockers; classpath/resources/help; then startup. Keep the active reflective macOS path and menu behavior while evaluating `OSXAdapterOld`; preserve help IDs, locale bundles, applet entry point and resource paths until explicit compatibility choices are made.

Verify first startup, close/reopen settings from a fresh temporary home, visible main window and one session, help/resource lookup, and no destructive changes to profile state. Run the four suite smoke slices after each source/build change. Fix the help map mismatch only with a JavaHelp lookup check. Do not combine packaging, library replacement, secret-storage work or Swing redesign with startup repair.

**Validation artifacts:** exact compile/startup failure snapshots and corrections; dependency-resolution and license inventory; isolated first-run files; GUI/display and help smoke record; unchanged synthetic preference/favorite/JKS compatibility; updated tests.

**Gate:** JDK 21 compile/package and desktop startup succeed from a clean temporary home; no original feature was removed; the suites still pass except named fail-first corrections; every bootstrap change is attributable and documented.

**Rollback:** one commit per blocker/fix. Revert only the change that introduces a new failure; keep the test evidence and earlier known-good bootstrap checkpoint. Do not delete/migrate existing user data during rollback.

### Phase 3 — Passing-test, GUI and transfer checkpoint

After startup repair, complete the non-security and non-archive-defect characterization ranges in all four suites. Run at least one real visible GUI smoke on an authorized desktop and an actual loopback FTP transfer through JFTP actions in both directions. Verify selected-tab command routing, transcript/status output, progress completion, local/remote destination state, cancellation boundary and synthetic settings persistence. Capture application/server logs and exact environment.

Fix only failures caused by changes in Phases 1–2. Classify pre-existing behavior defects, platform gaps, uncertain external-system results, and intended security corrections separately. Do not require every correction to be green before the baseline checkpoint; do require that its test exists in suite 3 or 4 and that later work cannot hide it.

**Validation artifacts:** all four suite reports; GUI smoke evidence; two-way FTP file comparison; status/transcript and server logs; dependency/legal status; known fail-first defect list; a clean diff and baseline commit hash.

**Gate:** maintain a reviewed, passing characterization checkpoint on JDK 21, with only the explicitly named archive/TLS correction cases red. No broad dependency or Java refactor begins before this checkpoint. Root and nested instructions plus affected docs must agree with any source change.

**Rollback:** preserve a tagged/hash checkpoint for the passing application and four suites. A phase regression returns to that specific commit; do not reset the shared checkout or discard another agent's changes.

### Phase 4 — Dependency and build-tool upgrades, separately

With the checkpoint passing, upgrade Maven core, build plugins, test engine, and application dependencies in separate changes. Start by pinning Maven/compiler/resources/jar/Surefire/assembly plugin behavior currently implicit or obsolete. Evaluate Maven 3.10.0 POM validation and dependency classpath ordering before changing dependency declarations; compare with 3.9.16 only if needed to localize a core/resolver incompatibility. Do not use Maven 4 previews, floating versions, blanket latest upgrades, broad BOM imports, or version changes bundled with source cleanup.

For every artifact, record current resolved version, candidate version, source repository, license/notice, transitive additions/removals, Java baseline and test/package results. Verify FTPAPI provenance before deciding to keep or replace it; verify JavaHelp compatibility and content; update JUnit/Jupiter and Surefire/Failsafe together after a small test can run. Preserve supported dependency API behavior and distribution contents while moving one boundary at a time.

**Validation artifacts:** dependency trees before/after; artifact hashes, origin and license/notice review; plugin-resolution/build logs; all four suites; package inventory; clean-diff checkpoint per dependency group.

**Gate:** each upgrade passes the same four suites and package structure comparison before the next dependency changes. Unknown licensing, API incompatibility or unavailable artifacts are owner decisions, not invitations to drop behavior.

**Rollback:** revert the single dependency/plugin change, restore its exact prior coordinate and lock/checksum record if introduced, and rerun the prior checkpoint. Do not “solve” dependency failures by excluding a user-visible feature.

### Phase 5 — Modern Java and behavior/security corrections

Modernize Java APIs and internal structure one area at a time against the passing checkpoint. Pin an explicit supported compiler JDK/toolchain and `--release` target, and run tests on the declared supported runtime(s); do not let the local JDK silently define the release target. Candidate cleanup includes generics, deprecated standard methods, the custom `SwingWorker` boundary, thread/EDT marshaling, filesystem utilities, resource failure handling and dialog APIs. Apply try-with-resources only where close timing does not alter event ordering, cancellation, or transfer completion. Introduce generics without changing serialized field types or `serialVersionUID` behavior until compatibility fixtures prove safe. Remove obsolete APIs in favor of supported `java.awt.Desktop` APIs where feasible, retaining platform behavior and guarded fallbacks. Avoid preview features and a framework rewrite; do not convert serialized state to records without a separate compatibility decision. The support source scan found no `sun.*`/`com.sun.*` usage in the owned support packages; the broader compatibility inventory must also check the application and build/resource surfaces. Do not assume a deprecated API is the current build blocker. JDK 26 applet API removal is a concrete ceiling if retaining `JFTPApplet`.

Keep corrections with materially different behavior in isolated commits and make the corresponding test fail first. Required review areas include:

- **TLS:** implement standards-based path validation and hostname verification, including SAN, correct validity and chain checks. Decide what the user can do for unknown, expired or mismatched identities; do not let a generic Yes silently override every failure. Preserve separately visible certificate review/install/manage features and configured trust store compatibility. If modern TLS defaults reject an old server, document the exact server/cipher/version gap and obtain a supported-scope decision; do not globally weaken TLS or silently drop that connection.
- **ZIP:** ensure extracted canonical paths remain under the target; reject traversal and absolute entry paths. Preserve ordinary nested extraction, timestamps, overwrite policy, partial-file cleanup, progress and error visibility deliberately. Correct `Zip.setRelativeTo` prefix handling separately and test out-of-root/sibling-prefix inputs.
- **Persistence and credentials:** preserve `preferences.ser`, `favorites.ser`, serial UIDs, user-selected store paths, existing JKS stores, aliases and readable favorites until compatibility fixtures and explicit migration/backup behavior are approved. Preference password chars are serialized plainly and favorite AES wrapping uses an embedded fixed key with plaintext fallback; changing these is a security/storage migration, not automatic cleanup. Never rewrite a real user home in a test.
- **Transfers and threads:** preserve ASCII/binary conversion, extension mapping, recursive filters, renamed destinations, errors, completion and abort behavior. Marshal callbacks to the EDT only with tested ordering and completion effects. Do not substitute direct FTPAPI unit coverage for actual app actions.
- **Updater, help and OS integration:** the updater currently uses HTTP and lexical version comparison; determine endpoint ownership and update policy before changing them. Verify help references and macOS callbacks. Retain locale text, menu behaviors and supported distribution platforms.

**Validation artifacts:** one change-level before/after report; red/green case within the same four suites; JDK 21 and JDK 25 compiler/test reports; serialized-state comparison; synthetic TLS/ZIP fixtures; thread/display logs where relevant; refreshed architecture, behavior, test and instruction docs.

**Gate:** JDK 25 LTS compiles and passes the declared regression baseline; known security-correction cases have explicit expected behavior and are green after their fixes, rather than skipped or excluded. Every behavior-changing correction is explicit, tested and documented; supported old-server, platform, locale and state-migration limitations have an owner decision. No unrelated API cleanup remains coupled to a security/storage correction.

**Rollback:** keep one commit per API area and per policy correction. A failed case reverts that area to the previous passing checkpoint while preserving red evidence; do not restore unsafe behavior by weakening assertions. Data migrations must be tested on copied synthetic inputs and have an explicit backup/restore path before release.

### Phase 6 — Distribution verification and handoff

Fix and verify the final executable JAR, manifest classpath, project-jar location, dependency `lib/`, script filtering, executable permissions, base directory and all three formats: ZIP, exploded directory and TAR.GZ. Run Windows and POSIX launchers from extracted packages outside an IDE. Test first-run and saved-state startup under a fresh isolated home, then execute one visible connection/session smoke and one loopback upload/download using the packaged application. Check help contents, representative locales, toolbar/menu actions, cancellation/status and certificate-store path loading. If macOS is in supported scope, verify native menu behavior on macOS rather than inferring it from the Windows result.

Inventory the final artifacts and dependencies, notices/licenses, runtime/JDK requirement, install/launch instructions, known compatibility limits, migration behavior and reproducible build/test commands. The current POM does not provide a wrapper; any future documented command must match the actual chosen wrapper or Maven installation. Preserve the baseline coverage ledgers as immutable snapshots; if implementation scope later changes, record new execution/change coverage separately instead of rewriting those original-snapshot counts. Update affected instructions, relevant docs, index, and release notes in the same logical change.

**Validation artifacts:** packaged archive manifests and checksums; launcher logs from extracted packages; dependency/license inventory; fresh-home startup record; four-suite report on the final JDK; transfer evidence; unresolved limitations and decision record.

**Gate:** all formats launch from outside the IDE on the selected supported platforms; the visible desktop app and real JFTP transfer flow work; all four suites pass, including approved security-correction expectations; no required UI, locale, help, archive format or persisted user setting was silently removed; documentation describes the resulting release accurately.

**Rollback:** retain the prior package/checkpoint and preserve user data untouched. If a launcher or package correction fails, revert only that distribution change and restore the last verified archive set. Do not replace previously supported formats without a consumer decision.

## Commit checkpoints and verification discipline

The coordinator owns commits and tracker updates. Delegates do not commit or push; the coordinator reviews and may commit their scoped outputs. Keep each logical step reviewable with explicit changed paths and descriptive commit messages: current-state documentation; test/fixture harness; each compile/bootstrap blocker; startup/resource correction; passing-test checkpoint; each Maven/plugin/dependency group; each Java API area; each TLS/archive/storage policy correction; and distribution assembly/launch fixes. Stage paths explicitly. Never bundle “cleanup everything” into one commit, and checkpoint before and after refactors. Use one execution record per change with command, environment, test count, outcome, output artifact/log path, and rollback hash.

The original baseline had no Maven wrapper or verified test command. The Windows bootstrap now provides both; see [the verified commands and limits](windows-startup.md). After a new execution instruction and after Maven/profile/toolchain setup, illustrative future commands could be `mvn -version`, `mvn -f pom.xml clean test`, and `mvn -f pom.xml clean package`; they are examples only, have not been executed, and are not established as working until prerequisites and profiles exist. Substitute the approved wrapper/tool path when selected. Distinguish unit, loopback integration, and visible GUI smoke evidence. A passing unit test cannot stand in for file transfer, FTPS prompting, packaged startup, or UI state.

## Phase dependency gates

| Dependency | Gate before next phase |
|---|---|
| 0 → 1 | Current-state docs and immutable original coverage ledgers reviewed; new user instruction authorizes test/build work. |
| 1 → 2 | Exactly four app-level suites have deterministic initial cases; narrow bootstrap limitations and FTPAPI provenance/license blocker are evidenced. |
| 2 → 3 | JDK 21 compiles and the desktop starts from isolated state; no feature/data format was silently removed. |
| 3 → 4 | Visible GUI and real bidirectional JFTP transfer checkpoint passes; only named pending security fixes remain red. |
| 4 → 5 | Each dependency/build-tool change has passed same suites and package comparisons; FTPAPI/JavaHelp rights and compatibility are resolved. |
| 5 → 6 | Modern-Java checkpoint and explicit security/storage policy corrections pass on target JDK; serialization and user-visible behavior evidence is recorded. |
| 6 complete | Extracted distributions launch outside the IDE on declared platforms; app and transfer flows work; docs and known limitations match artifacts. |

## Decision points before risky changes

The next implementation slice is the isolated JDK 21 baseline attempt and the smallest vertical case for the four suites, after the user authorizes execution. Before reaching later phases, resolve: FTPAPI availability/licensing and API replacement scope; whether `JFTPApplet` source must remain; supported JDK/vendor/platform matrix; JavaHelp and all packaged formats' consumers; the TLS policy for expired, mismatched and unknown certificates; the migration and protection policy for saved passwords/favorites/keystores; ZIP overwrite/partial-file policy while adding traversal rejection; and updater endpoint ownership/security. These are concrete product or compatibility decisions, not implied permission to remove functionality.

Reasoned disagreement is welcome when supported by user/deployment evidence. Record the alternative and its observable consequences in the relevant decision section and tests. Do not ask the user to authorize implementation as part of this planning deliverable.
