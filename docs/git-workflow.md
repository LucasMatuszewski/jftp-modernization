# Fork and upstream workflow

Course work is published in [LucasMatuszewski/jftp-modernization](https://github.com/LucasMatuszewski/jftp-modernization), a fork of [sai-pullabhotla/jftp](https://github.com/sai-pullabhotla/jftp). The separate `LucasMatuszewski/jftp` repository is not the target.

| Reference | Purpose |
|---|---|
| `main` / `origin/main` | Default course branch with the demonstrated modernization and Windows bootstrap |
| `upstream-baseline` / `origin/upstream-baseline` | Pristine original-author baseline, published for comparison |
| `upstream/master` | Fetch-only reference to the original author's current default branch |

The local `upstream-baseline` branch tracks `upstream/master`; its push target is `origin`. `upstream` remains a remote, and its push URL is disabled. Publishing a baseline to the fork does not update it automatically when the original author commits. Preserve the full history in `main`; compare using [upstream-baseline...main](https://github.com/LucasMatuszewski/jftp-modernization/compare/upstream-baseline...main).

## Configure a new clone

Remote configuration and tracking relationships are local to each clone:

```sh
git clone https://github.com/LucasMatuszewski/jftp-modernization.git
cd jftp-modernization
git remote add upstream https://github.com/sai-pullabhotla/jftp.git
git config remote.upstream.pushurl DISABLED
git config remote.pushDefault origin
git fetch upstream
git branch --track upstream-baseline upstream/master
git config branch.upstream-baseline.pushRemote origin
```

The default checkout is `main`. Use [Windows startup](windows-startup.md) for the verified isolated build/launch procedure. With GitHub CLI, set the API target using `gh repo set-default LucasMatuszewski/jftp-modernization`.

## Publish course work

Create a focused branch from current `main`, verify the affected scope, and publish to `origin` only when authorized. Integrate verified history into `main`; use fast-forward when possible, preserving the checkpoints participants need to compare. Confirm the fork's default branch is `main`. Never force-push or publish unrelated branches/tags.

Before deleting a branch, fetch current refs and prove its commits are reachable from `main`. Patch-equivalent commits alone do not establish full ancestry. Preserve branches with unique work or open pull requests until their disposition is decided. After an authorized merge, delete obsolete local refs with `git branch -d` and their fork refs with an explicit `git push origin --delete <branch>`. Keep `main` and `upstream-baseline`; the first Windows bootstrap checkpoints remain available as commits `e8b1558` and `e5ddfc0`. PR #2 was merged into `main` as `cd6f32a`, preserving its reviewed history and all later bootstrap/context work.

## Review original-author changes

Fetch without changing the working tree, then inspect the new commits and relevant diff:

```sh
git fetch upstream
git log --oneline upstream-baseline..upstream/master
git diff upstream-baseline upstream/master
```

After review authorizes advancing the pristine baseline:

```sh
git switch upstream-baseline
git merge --ff-only upstream/master
git push origin upstream-baseline
git switch main
```

If fast-forward fails, stop and inspect the divergence; do not replace the baseline by force. Separately review `git log --oneline main..upstream-baseline` and the affected files before integrating original-author changes into `main`. Resolve conflicts deliberately and run checks for the affected application scope. Never push to the original author's remote.
