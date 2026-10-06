# Launch scripts

The Windows batch and POSIX shell scripts currently launch `com.myjavaworld.jftp.JFTPApplication` indirectly through the executable jar manifest. See [build and dependencies](../../../docs/build-and-dependencies.md) and [resources and distribution](../../../docs/resources-and-distribution.md).

Keep both launchers aligned with the assembled jar location, manifest `lib/` classpath, and filtered Maven substitutions. Check quoting and path handling on each platform when changing commands. Update root/nested `AGENTS.md` files and both detailed documents in the same change whenever launch paths, commands, dependencies, packaging, or behavior change.
