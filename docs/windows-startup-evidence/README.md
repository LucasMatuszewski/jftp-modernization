# Windows bootstrap evidence

See [the startup guide](../windows-startup.md) for scope and reproducible commands.
[verification.json](verification.json) records source citations, dependency hashes,
test outcomes, observed desktop steps and limitations.

The build logs preserve each independent bootstrap failure, the temporary runner
canary and the final passing wrapper build. [startup-state-tests.xml](startup-state-tests.xml)
contains the final three-test result with environment properties removed.

The desktop checks used synthetic state and real input. Window activation and
rendering were synchronized before capture; the initial keyboard attempt without
foreground focus did not add a session and is retained in the raw desktop log.
Escape did not close About; native window-close input was used subsequently.
Normal standalone close was confirmed by process termination within five seconds;
its exit code was not available and is not reported as zero.

- [Restarted standalone application](restart.png): one disconnected session,
  synthetic local file and empty remote listing.
- [Two sessions](two-sessions.png): real session creation through keyboard input.
- [Preferences](preferences.png): synthetic local-directory setting.
- [Save information](preferences-save.png): existing restart notice after Save.
- [About](about.png): Windows 11 and Microsoft Java 21.0.10. The unchanged UI still
  reports application version 5.0.1/build 20120623 while Maven uses 5.0.2-SNAPSHOT.

No screenshots or logs establish FTP/FTPS transfer behavior or packaged launch.
