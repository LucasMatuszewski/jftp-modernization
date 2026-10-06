# JFTP action instructions

Actions under this package connect menus and toolbar gestures to `JFTP`, the selected `FTPSession`, dialogs and file/remote operations. Read [application workflows](../../../../../../../docs/application-workflows.md) and [regression test design](../../../../../../../docs/regression-test-design.md) before changing a user-visible action.

Preserve each action's active-session selection, connection/selection preconditions, cancellation behavior, confirmation prompts, destination-name handling, worker completion refresh and status/error reporting. Remote open/edit/print downloads a temporary file; monitored edits can upload a changed file to the original remote path. Archive actions bridge `FTPSession` with the sibling `zip` package. `AbortAction` sets the session abort flag and calls `FTPClient.abort()`; recursive transfer loops check between items. The API is FTP/FTPS; do not substitute SFTP semantics.

Prefer tests at the application action/session boundary. Use temporary user homes and local roots plus deterministic controlled FTP/FTPS fixtures. Assert resulting local/server files, user-visible state, cancellation/error outcomes and callbacks, not action internals or thread classes. Separate existing behavior characterization from explicit bug-fix expectations for security defects.

Whenever source structure, implementation responsibilities, commands, dependencies or public behavior change, update the applicable root/package/action `AGENTS.md` and `CLAUDE.md` instructions and affected `docs/` files in the same change. `CLAUDE.md` imports this file.
