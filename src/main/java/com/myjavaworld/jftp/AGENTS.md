# JFTP application package instructions

This package contains the desktop/applet launch paths, the main window, session orchestration, menus, local/remote browser integration, preferences, favorites, transfer dialogs and per-session UI. Read [application workflows](../../../../../../docs/application-workflows.md), [architecture](../../../../../../docs/architecture.md), and [regression test design](../../../../../../docs/regression-test-design.md) before changing public behavior or moving responsibilities. TLS implementation is under `ssl/`; reusable Swing widgets, utilities and archive logic live in sibling `gui`, `util`, and `zip` packages.

## Key contracts

- `JFTPApplication.main` is the executable desktop entry point; `JFTPApplet` is a separate legacy applet launcher and an explicit compatibility question. Do not remove it or claim modern browser support without a target decision.
- `JFTP` owns global preferences, top-level menus/toolbars, tab management, window lifecycle and current-session routing. Keep selected-tab state and actions aligned.
- `FTPSession` owns connection/session state, FTP callbacks, directory panes, per-session filters and transfer-mode selection, recursive transfers, abort handling, status output, and temporary-file edit monitoring. It adapts to the external FTPAPI `FTPClient` / `ListParser` contract; the protocol is FTP or FTPS, not SFTP.
- `RemoteHost`/`Favorite` are serialized connection data. `FavoritesManager` and `JFTP.savePreferences/loadPreferences` own legacy local state formats. Preserve migration compatibility and never use real user-home credentials as test fixtures.
- Menus, toolbar and action classes are the user-visible command boundary. Preserve menu availability, keyboard accelerators, modal confirmations, active-session targeting, Desktop handoffs, drag/drop, and local versus remote filesystem effects.
- `JFTPPreferences`, connection dialogs and preference panels define transfer mapping/defaults, proxy, certificate store paths, security options, locale/theme and update settings. Do not conflate FTPS with SSH/SFTP or silently remove platform-specific behavior.

## Change and verification guidance

The [Windows bootstrap](../../../../../../docs/windows-startup.md) compiles the retained desktop/app source with a Windows-only exclusion for the unreferenced `OSXAdapterOld`. Its startup-state checks and visible desktop smoke do not establish the four-suite baseline or macOS compatibility.

Keep application changes no-feature-change until the four suites in the regression design exist and pass against the baseline. Exercise transfers through an application session/action against an isolated controlled FTP/FTPS server and temporary local/user-home directories; assert output bytes, server state, visible session result and callbacks rather than helper algorithms or private fields. Keep separate unit, integration and UI-smoke coverage. Treat unsafe TLS validation, ZIP extraction, updater endpoints, old macOS APIs, serialized passwords, and the applet as explicit security/compatibility decisions instead of desired regression behavior.

Do not install tools, build, run the app or tests in a documentation-only phase. When implementation is authorized, first resolve the declared FTPAPI artifact's availability and redistribution terms, then bootstrap only enough compiler/tooling to establish an executable baseline.

Whenever source structure, implementation responsibilities, commands, dependencies, public behavior or test boundaries change, update the root and applicable nested `AGENTS.md`/`CLAUDE.md` files and all affected documents under `docs/` in the same change. Keep both agent instruction files in sync; `CLAUDE.md` imports this file.
