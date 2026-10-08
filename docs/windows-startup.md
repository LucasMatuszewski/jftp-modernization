# Windows startup bootstrap

The user authorized a minimal Windows build/startup attempt and useful basic
regression tests on 2026-10-08. This slice retains the existing FTPAPI and JavaHelp,
Swing UI, applet source, resource roots and serialized data formats. Application
implementation bodies were not changed. It does not complete the four regression
suites or the broader modernization plan.

## Toolchain and build boundary

- Verified runtime: Windows 11, Microsoft OpenJDK 21.0.10+7-LTS, amd64.
- Maven Wrapper 3.3.4, `only-script`, downloads Maven 3.10.0 over HTTPS and checks
  its SHA-256. The initial Apache download also matched the published SHA-512.
- Compiler plugin 3.13.0 uses `release=8`; this is a bootstrap bytecode/API target,
  not proof that the application has been tested on Java 8.
- The automatically activated `windows-bootstrap` profile excludes only
  `com/myjavaworld/jftp/OSXAdapterOld.java`. Its source is retained. A scoped search
  of all application Java sources found references only inside that file;
  `JFTPApplication` uses the separate reflective `OSXAdapter`. macOS is untested.
- JUnit 4.13.2 remains test-scoped; the initial characterization uses its compatible
  `junit.framework.TestCase` API. Surefire 3.6.0 is pinned explicitly.
- Build output is ignored under `target/`.

## Reproducible Windows commands

Run PowerShell from the repository root with JDK 21 on PATH. These commands use
an external Maven cache, empty settings and a synthetic application profile:

```powershell
$run = Join-Path $env:TEMP 'jftp-windows-startup'
New-Item -ItemType Directory -Path $run -Force | Out-Null
$env:MAVEN_USER_HOME = Join-Path $run 'wrapper-cache'
Set-Content -LiteralPath (Join-Path $run 'settings.xml') -Value '<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"/>'
.\mvnw.cmd -B -ntp "-Dmaven.repo.local=$run\repository" -s "$run\settings.xml" test org.apache.maven.plugins:maven-dependency-plugin:3.8.1:copy-dependencies -DincludeScope=test
if ($LASTEXITCODE -ne 0) { throw 'JFTP build/tests failed' }
$profile = Join-Path $run 'profile'
New-Item -ItemType Directory -Path $profile -Force | Out-Null
java "-Duser.home=$profile" -cp 'target\test-classes;target\classes;target\dependency\*' com.myjavaworld.jftp.StartupStateProbe desktop-seed
if ($LASTEXITCODE -ne 0) { throw 'Synthetic profile setup failed' }
java "-Duser.home=$profile" -cp 'target\classes;target\dependency\*' com.myjavaworld.jftp.JFTPApplication
```

Test-scope dependency copying supports the synthetic-profile fixture; it does not
change application dependency scopes or distribution contents. The fixture creates
`files/hello.txt`, selects that directory, uses English UI and disables automatic
update checks only in the synthetic preferences. It rejects homes outside the OS
temporary directory before loading application state. Start a new JVM after seeding
because legacy classes snapshot `user.home` and preferences statically.

## Dependency provenance

The original FTPAPI 3.0.0 JAR, POM and source JAR were downloaded from the
[publisher's HTTPS Maven repository](https://www.jmethods.com/ftpapi/download.html).
The POM declares Apache License 2.0 and SCM tag `ftpapi-3.0.0`; the inspected
`FTPClient.java` source carries the matching Apache notice. The JAR contains the
publisher's Maven metadata. SHA-256 values and build evidence are recorded in the
bootstrap evidence directory. No FTP library was replaced or vendored.

This establishes provenance for this local bootstrap. Distribution verification
must still inventory final dependency notices and licenses before publishing.

## Verification evidence

The initial failures were recorded independently: HTTP repository blocked by Maven;
unsupported Java 5 source/target; 12 compiler errors from Apple's legacy EAWT API;
JUnit 3.8.1 rejected by Surefire. Each received a bounded build/test configuration
change. These are bootstrap failures, not behavioral red tests.

The runner was checked with a temporary deliberately failing assertion: exactly
three tests were discovered, one failed with `Test discovery canary`, and none
were skipped. The assertion was then removed. The behavioral checks cover:

1. First-run preference creation, readable defaults and an empty favorites list.
2. Settings and synthetic password-bearing favorites surviving a separate JVM.
3. Base/German/Traditional Chinese bundles, icon, help-set location and configured
   FTP client/parser classes on the classpath.

These checks use a fresh temporary home per test and bounded child JVMs. They do
not prove browser operations, transfers, FTPS trust decisions or migration from
every historical saved-state variant.

Desktop QA uses the real `JFTPApplication.main`, synthetic state and AWT Robot
mouse/keyboard input. Logs and screenshots are retained outside the repository
under `%TEMP%/jftp-bootstrap-20261008/`. The execution report in
`windows-startup-evidence/` records observed outcomes and file hashes.

## Remaining boundaries

The old batch/shell distribution launchers and assembly layout are unchanged and
remain unverified. The verified command above starts compiled classes outside an
IDE. No release archives were built or published. Java 8, macOS, Linux, real FTP
transfers, FTPS handshakes, full help-topic navigation and the complete four-suite
baseline need their own verification before related refactors or release claims.

Legacy deprecation/unchecked warnings and the bootstrap Java 8 target warning
remain visible; they are not suppressed or resolved by this slice. Preserve the
immutable original analysis records under `docs/analysis/`.
