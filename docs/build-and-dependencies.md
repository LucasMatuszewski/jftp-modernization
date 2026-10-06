# Build and dependencies

This document records the tracked build inputs as inspected on 2026-10-06. It separates repository facts from implications and proposals. No build, startup, or tests were attempted in this documentation phase. The working environment reported by the coordinator has Microsoft OpenJDK `21.0.10+7`; Maven is not recognized on its PowerShell `PATH`.

## Current build contract

The Maven project is `com.myjavaworld:jftp:5.0.2-SNAPSHOT`, packaging `jar`, with `com.myjavaworld.jftp.JFTPApplication` as the manifest main class ([pom.xml](../pom.xml), project coordinates and jar manifest configuration). The POM sets `project.build.sourceEncoding=UTF-8`, but compiler source and target are both `1.5` using `maven-compiler-plugin:2.4`. Eclipse metadata independently requests Java 6: [.classpath](../.classpath) binds JavaSE-1.6 and [.settings/org.eclipse.jdt.core.prefs](../.settings/org.eclipse.jdt.core.prefs) sets source, compliance, and target to `1.6`. These settings disagree; Maven is the declared build, Eclipse metadata is a separate legacy project configuration.

The POM explicitly declares these direct dependencies only:

| Coordinate | Version | Scope in POM | Notes |
|---|---:|---|---|
| `junit:junit` | `3.8.1` | `test` | Two tracked test resource/source placeholder files exist; no test classes are tracked. |
| `com.myjavaworld:ftpapi` | `3.0.0` | default `compile` | Project-specific FTP API; the POM names a custom HTTP repository. No jar is tracked. Its current availability and licensing were not established. |
| `javax.help:javahelp` | `2.0.05` | default `compile` | JavaHelp is needed for the bundled help set. No jar is tracked. |

No transitive dependency versions are asserted here: they are not pinned in this POM, and dependency resolution was not run. The declared repository is `jMethods` at `http://www.jMethods.com/mvn-repo`. Distribution management points to `ftp://ftp.kattare.com/jmethods_com/mvn-repo`, with `uniqueVersion=false`; SCM metadata names the historical GitHub project. Treat these as configured legacy endpoints, not verified live services (`pom.xml`, `repositories`, `distributionManagement`, and `scm`).

The exact build plugin declarations are `maven-compiler-plugin:2.4`, `maven-jar-plugin:2.4`, `maven-source-plugin:2.1.2`, `maven-assembly-plugin:2.3`, `maven-scm-plugin:1.7`, `maven-deploy-plugin:2.7`, and `maven-release-plugin:2.3`. The build extension is `org.apache.maven.wagon:wagon-ftp:2.2`. There is no Maven wrapper, parent POM, dependency management section, plugin management section, profile, toolchain declaration, or explicit Surefire configuration in the tracked POM. Maven defaults therefore remain implicit. The POM has a custom repository but no explicit plugin repository.

`maven-assembly-plugin` binds the `single` goal to `package`, using [src/main/assembly/binary.xml](../src/main/assembly/binary.xml). The descriptor produces `zip`, exploded `dir`, and `tar.gz`, includes a base directory, copies transitive dependency artifacts to `lib/`, copies project `target/*.jar` files to the distribution root excluding `*-sources.jar`, includes root `*.txt` and `*.md`, and copies/filters the configured script source directory (`binary.xml`). The jar manifest advertises `lib/` as its dependency classpath prefix and the application main class.

**Observed packaging mismatch:** [src/main/scripts/jftp.bat](../src/main/scripts/jftp.bat) and [jftp.sh](../src/main/scripts/jftp.sh) each run `java -jar lib/${project.artifactId}-${project.version}.jar`, while `binary.xml` puts the project jar at the distribution root and puts dependency jars under `lib/`. The descriptor's script source is `${project.build.scriptSourceDirectory}` and POM does not set that property. The default directory and the exact filtered archive output need to be confirmed with a later package run. Until then, the launch path and script filtering are unverified; preserve and test both Windows and Unix launch behavior before altering either.

There is no declared runtime image, OS installer, service wrapper, native launcher, or explicit Java runtime requirement beyond the stale Java source/target declarations. README describes a desktop Swing client across Windows, macOS, Linux and Unix-like systems. Its documented functions include FTP and FTPS/SSL, explicit and implicit SSL, passive/active transfers, SOCKS4/5, favorites, local/remote file tasks, recursive transfers, filters, transfer-mode detection, simultaneous sessions, certificates, and localized UI. It also mentions an applet in localization bundles, so applet removal or replacement is a compatibility decision to make explicitly rather than infer from the desktop launch path.

## Legal and availability gates

`LICENSE.txt` and the bundled JavaHelp content license state Apache License 2.0. `NOTICE.txt` carries jMethods, Inc. copyright and Apache 2.0 wording. The POM also labels the project Apache 2.0. That does not establish the license or redistribution rights for `ftpapi:3.0.0`, JavaHelp, or any future resolved transitive artifacts. Before replacing, shading, repackaging, or publishing dependencies, inventory the resolved artifacts, notices, license terms, and availability. No dependency jar is present among tracked files, and artifact resolution was not attempted. In particular, do not silently remove the custom repository or substitute another FTP implementation before confirming the existing API license and behavior contract.

## Build-related modernization boundaries

Follow the authoritative ordering and gates in [the integrated modernization plan](modernization-plan.md). These build-related boundaries are proposals, not evidence that the source compiles:

1. Design and implement the four behavioral suites before refactoring. Resolve the `ftpapi:3.0.0` legal/availability gate and establish reproducible Maven/JDK 21 tooling when implementation is authorized. Record actual resolution and failures; do not infer transitive dependencies. If compilation blocks test execution, isolate only the compiler/dependency/API bootstrap needed to make the characterization baseline executable.
2. Run the baseline suites, then repair minimum startup blockers while retaining FTP/FTPS, JavaHelp content, localized resources, manifest classpath and distribution forms. Run the same characterization cases after each change. Do not combine a source/API refactor or library replacement with this bootstrap.
3. When launcher layout prevents the intended startup route, reconcile assembly output, filtered substitutions, manifest classpath and both launchers as one isolated fix with tests before/after. Preserve zip, directory and tar.gz deliverables; final verification of every platform/archive remains a separate distribution phase.
4. After a passing test/startup checkpoint, introduce plugin and dependency upgrades individually with behavior comparisons, package checks and license review. Keep transfer/security, locale/help/resource and packaging coverage in place before replacing any old library.
5. Treat any source/API target migration as a later, separately scoped phase. On 2026-10-06, the official Oracle roadmap identifies Java 21 and 25 as LTS releases, and Maven's official download page lists Maven 3.10.0 as current. Candidate toolchain for evaluation: JDK 21 bootstrap, JDK 25 LTS target, Maven 3.10.0. Recheck current support, distribution terms, and compiler/plugin compatibility when implementation begins. ([Oracle Java SE roadmap](https://www.oracle.com/java/technologies/java-se-support-roadmap.html), [Apache Maven downloads](https://maven.apache.org/download.cgi), researched 2026-10-06.)

The riskiest assumptions are that the FTP API can still be obtained and redistributed, that moving the minimum runtime is acceptable to all users, and that legacy help, applet/localization bundles, and all three archive formats are unused. Resolve each with evidence before deleting or changing behavior. Reasoned disagreement is welcome where an assumption is supported by user or deployment evidence.

## Owned input coverage

The per-file coverage ledger is [build-resources-coverage.txt](analysis/build-resources-coverage.txt). It covers every tracked non-Java-source input, including hidden Eclipse metadata, all property bundles, all help text, scripts, and binary assets. Repository-wide contributors should keep this document, [resources and distribution](resources-and-distribution.md), and the relevant root/nested `AGENTS.md` instructions in the same change whenever build configuration, dependency choices, paths, commands, packaging, behavior, or architecture changes.
