# Main tree guidance

This scope contains application resources, locale bundles, help, images, scripts, and assembly packaging. Use [build and dependencies](../../docs/build-and-dependencies.md) and [resources and distribution](../../docs/resources-and-distribution.md) as the detailed references.

The [Windows bootstrap](../../docs/windows-startup.md) preserves these roots and launches compiled classes; it does not verify the existing distribution launchers.

Preserve classpath-relative resource names and the default, German, and Traditional Chinese bundle trees. When changing resource roots, encodings, images, help paths, packaging, launch commands, or dependencies, update the root and applicable nested `AGENTS.md` files and both detailed documents in the same change. Do not remove applet-era bundles, legacy image variants, help topics, or archive formats without evidence that the behavior is unused. For sibling routing: locale trees, images, help, assembly, and scripts are covered by this guidance; [resources/AGENTS.md](resources/AGENTS.md) applies only to default `src/main/resources`.
