# Default application resources

This directory owns the default English `.properties` bundles under package-matching paths. See [resources and distribution](../../../docs/resources-and-distribution.md) for locale, encoding, and packaging details. Sibling locale roots `resources_de` and `resources_zh_TW` are covered by [the parent main-tree guidance](../AGENTS.md), not this file.

Preserve bundle base names, keys, placeholders, newlines, and Java Properties escaping. Compare localized keys with Properties continuation semantics. Any resource path, encoding, lookup, or behavior change must update root/nested `AGENTS.md` files and the detailed docs in the same change.
