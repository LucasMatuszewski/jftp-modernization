# Binary distribution assembly

The assembly descriptor produces zip, directory, and tar.gz distributions. See [build and dependencies](../../../docs/build-and-dependencies.md) and [resources and distribution](../../../docs/resources-and-distribution.md) for its observed layout and current launcher-path mismatch.

Preserve the project jar, resolved runtime libraries, legal notices, resource paths, and both platform launchers as a coherent distribution. Confirm actual output paths and substitutions when changing assembly logic. Update root/nested `AGENTS.md` files and both detailed documents in the same change for build, dependency, path, command, packaging, behavior, or architecture changes.
