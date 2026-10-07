# Fork and upstream workflow

Modernization work is maintained in [LucasMatuszewski/jftp-modernization](https://github.com/LucasMatuszewski/jftp-modernization), a GitHub fork of [sai-pullabhotla/jftp](https://github.com/sai-pullabhotla/jftp). The existing `LucasMatuszewski/jftp` repository is separate and was not changed by this setup.

| Remote | Purpose |
|---|---|
| `origin` | Fetch and publish branches in the personal modernization fork |
| `upstream` | Fetch changes from the original author; local push URL is disabled |

`upstream` is a remote, not a development branch. The original default branch is tracked as `upstream/master`; the modernization branch is `Luna-subagents-modernization`. Publishing that branch does not merge it into the fork's default branch or create a pull request to the original repository.

## Configure a new clone

Local remote configuration is not copied between clones. After cloning the fork, configure the original repository and push target:

```sh
git clone https://github.com/LucasMatuszewski/jftp-modernization.git
cd jftp-modernization
git remote add upstream https://github.com/sai-pullabhotla/jftp.git
git config remote.upstream.pushurl DISABLED
git config remote.pushDefault origin
git fetch upstream
git switch --track origin/Luna-subagents-modernization
```

If using GitHub CLI, set its default API target with `gh repo set-default LucasMatuszewski/jftp-modernization`. Review `git remote -v` before publishing; the disabled upstream push URL is a local safeguard, not a GitHub permission change.

## Publish and review original-author changes

Publish only after verification and explicit user authorization, using `git push -u origin Luna-subagents-modernization`. Push only the intended branch; do not force-push or publish unrelated branches/tags.

Use `git fetch upstream` to update remote references without changing the working tree. Review `git log --oneline HEAD..upstream/master` and the relevant diff before deciding to merge the original author's changes into the modernization branch. Fetching does not itself integrate them. Any integration must preserve local work, resolve conflicts deliberately, and pass verification for the affected scope.
