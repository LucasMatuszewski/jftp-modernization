# Shared Swing components

This package contains reusable Swing components, document models, renderers, themes, and the legacy worker used by application and certificate screens. These are source packages in one desktop application, not an independent module. Read the [repository instructions](../../../../../../AGENTS.md), [Java boundary instructions](../../../AGENTS.md), and [support-library behavior notes](../../../../../../docs/support-libraries.md) before changing this package.

Keep Swing component construction and mutation on the event dispatch thread. The custom SwingWorker is an app-owned API; characterize `construct`, `finished`, blocking `get`, and interrupt timing before replacing it. Preserve text document maximum-length, case, single-line, selection, clipboard, popup-menu, undo-limit, and password cut/copy behavior. Password field cut/copy remain disabled for security. Preserve `MDialog` hide-on-close/Escape semantics and `ProgressDialog` cancellation wiring until callers are migrated and tested.

Review call sites in `jftp` and `jftp/ssl` when changing constructors, event order, text contracts, renderer values, or public methods. Keep UI resource bundle keys aligned with the corresponding `src/main/resources` files. Do not use appearance-only cleanup to silently alter keyboard behavior, localization, theme names, modal behavior, or selected-row behavior.

When an authorized implementation change alters package structure, responsibilities, APIs, dependencies, or behavior, update this file, the root and Java-parent instructions, and [support-library documentation](../../../../../../docs/support-libraries.md) in the same logical change. Add behavior coverage before replacement; no implementation tests are authorized in the present analysis phase.
