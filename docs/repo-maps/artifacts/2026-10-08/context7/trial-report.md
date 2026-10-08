# Public JFTP local Context7 trial

The lexical backend and real pinned `ctx7` 0.5.13 client passed the integrated trial. Original JFTP source was unchanged; all returned paths, line ranges and SHA-256 hashes matched, and the complete multiline `getBundle(..., ClassLoader loader)` signature was retained. `LocalFile.compareTo` was the top direct-query result; `syntheticabsentApi` returned no evidence.

| Measurement | Observed single run |
| --- | ---: |
| JFTP files / chunks / skips | 196 / 966 / 0 |
| SQLite database | 2,985,984 bytes |
| Index wall time | 18.462 s |
| Direct lexical queries | 16.918–19.804 s |
| Loopback server startup | 0.107 s |
| Real ctx7 library / docs | 0.264 s / 17.781 s |

Host rejection returned HTTP 403. Changed/deleted fixture files and a changed fixture Git revision returned HTTP 409; fresh evidence returned HTTP 200. Both owned servers stopped, and their ports were independently confirmed closed. Invalid CLI limits returned exit 2; an oversized synthetic file was skipped explicitly.

The source lives on a Windows mount. WSL cannot resolve this Windows Git worktree's absolute gitdir pointer, so the backend records `non-git`; Windows independently resolves HEAD `d6c208403099b90a2e0890a9ac3d8e132c215f0b`. Hash freshness remains checked, but these JFTP responses do not claim that commit as backend revision metadata. A disposable ext4 Git fixture separately verified real revision rejection.

This verifies lexical workflow and client compatibility, not semantic RAG quality. No models were downloaded. Timings include full freshness checks and are individual runs, not medians. Byte-identical four-file snapshots isolate a small filesystem comparison in `four-file-snapshot-comparison.md`; do not extrapolate a global speed ratio.

Trial harness/setup errors are retained below and in attempt logs. They were corrected without backend, client or repository changes.

Lexical retrieval only; this does not measure semantic RAG quality.

Source: `/mnt/c/Users/BiuroEdukey/.codex/worktrees/05bd/jftp/src/main/java`. Windows Git HEAD: `d6c208403099b90a2e0890a9ac3d8e132c215f0b`. Backend records `non-git` because WSL cannot resolve the Windows worktree gitdir pointer. Source hashes, original paths and LF-based line ranges were checked.

Client: pinned `ctx7` 0.5.13, isolated pnpm install with `--ignore-scripts`. HOME/CODEX_HOME unchanged; scoped XDG credentials `{}` prevent legacy-home credential migration/reads. `CTX7_TELEMETRY_DISABLED=1`, explicit loopback root base URL and JSON/noninteractive invocation avoid telemetry/update checks.

Index/files/chunks/database and timings:

```json
{
  "index": {
    "libraryId": "/local/jftp",
    "revision": "non-git",
    "corpusId": "ee8166181a71135b486bedaaa98f5e1c36d4c9d247c0de6786fd7ee559758003",
    "files": 196,
    "chunks": 966,
    "chunkChars": 1200,
    "oversizedChunks": 0,
    "changed": 196,
    "deleted": 0,
    "skippedCount": 0,
    "skipped": [],
    "embeddingModel": null,
    "modelRevision": null,
    "rerankerModel": null,
    "rerankerRevision": null,
    "vectorEngine": "stdlib",
    "excludes": []
  },
  "databaseBytes": 2985984,
  "measurements": [
    {
      "label": "index-jftp",
      "command": [
        "python3",
        "/home/lucas/DEV/Projects/agent-toolbox/skills/legacy-codebase-workflows/scripts/context7_backend.py",
        "index",
        "/mnt/c/Users/BiuroEdukey/.codex/worktrees/05bd/jftp/src/main/java",
        "--database",
        "/home/lucas/.cache/legacy-map-review-20261008/context7-trial/jftp.sqlite",
        "--library-id",
        "/local/jftp"
      ],
      "seconds": 18.461786642903462,
      "exit": 0,
      "stderr": ""
    },
    {
      "label": "query-resource",
      "command": [
        "python3",
        "/home/lucas/DEV/Projects/agent-toolbox/skills/legacy-codebase-workflows/scripts/context7_backend.py",
        "query",
        "--database",
        "/home/lucas/.cache/legacy-map-review-20261008/context7-trial/jftp.sqlite",
        "--query",
        "ResourceLoader getBundle ClassLoader",
        "--limit",
        "5"
      ],
      "seconds": 19.80356059106998,
      "exit": 0,
      "stderr": ""
    },
    {
      "label": "query-localfile",
      "command": [
        "python3",
        "/home/lucas/DEV/Projects/agent-toolbox/skills/legacy-codebase-workflows/scripts/context7_backend.py",
        "query",
        "--database",
        "/home/lucas/.cache/legacy-map-review-20261008/context7-trial/jftp.sqlite",
        "--query",
        "LocalFile compareTo",
        "--limit",
        "5"
      ],
      "seconds": 16.91757334303111,
      "exit": 0,
      "stderr": ""
    },
    {
      "label": "query-absent",
      "command": [
        "python3",
        "/home/lucas/DEV/Projects/agent-toolbox/skills/legacy-codebase-workflows/scripts/context7_backend.py",
        "query",
        "--database",
        "/home/lucas/.cache/legacy-map-review-20261008/context7-trial/jftp.sqlite",
        "--query",
        "syntheticabsentApi",
        "--limit",
        "5"
      ],
      "seconds": 18.025316975079477,
      "exit": 0,
      "stderr": ""
    }
  ],
  "queries": {
    "resource": {
      "query": "ResourceLoader getBundle ClassLoader",
      "results": 5,
      "checked": [
        {
          "path": "com/myjavaworld/util/ResourceLoader.java",
          "startLine": 31,
          "endLine": 61,
          "hash_matches": true,
          "text_matches": true,
          "revision": "non-git"
        },
        {
          "path": "com/myjavaworld/util/ResourceLoader.java",
          "startLine": 1,
          "endLine": 38,
          "hash_matches": true,
          "text_matches": true,
          "revision": "non-git"
        },
        {
          "path": "com/myjavaworld/jftp/LocalSystemMenu.java",
          "startLine": 25,
          "endLine": 54,
          "hash_matches": true,
          "text_matches": true,
          "revision": "non-git"
        },
        {
          "path": "com/myjavaworld/jftp/RemoteSystemMenu.java",
          "startLine": 24,
          "endLine": 52,
          "hash_matches": true,
          "text_matches": true,
          "revision": "non-git"
        },
        {
          "path": "com/myjavaworld/jftp/RemoteSystemMenu.java",
          "startLine": 45,
          "endLine": 78,
          "hash_matches": true,
          "text_matches": true,
          "revision": "non-git"
        }
      ],
      "resource_multiline_signature": true
    },
    "localfile": {
      "query": "LocalFile compareTo",
      "results": 5,
      "checked": [
        {
          "path": "com/myjavaworld/jftp/LocalFile.java",
          "startLine": 233,
          "endLine": 280,
          "hash_matches": true,
          "text_matches": true,
          "revision": "non-git"
        },
        {
          "path": "com/myjavaworld/jftp/Favorite.java",
          "startLine": 35,
          "endLine": 55,
          "hash_matches": true,
          "text_matches": true,
          "revision": "non-git"
        },
        {
          "path": "com/myjavaworld/jftp/RemoteHost.java",
          "startLine": 205,
          "endLine": 252,
          "hash_matches": true,
          "text_matches": true,
          "revision": "non-git"
        },
        {
          "path": "com/myjavaworld/jftp/LocalFileComparator.java",
          "startLine": 134,
          "endLine": 159,
          "hash_matches": true,
          "text_matches": true,
          "revision": "non-git"
        },
        {
          "path": "com/myjavaworld/jftp/LocalFile.java",
          "startLine": 33,
          "endLine": 80,
          "hash_matches": true,
          "text_matches": true,
          "revision": "non-git"
        }
      ],
      "resource_multiline_signature": false
    },
    "absent": {
      "query": "syntheticabsentApi",
      "results": 0,
      "checked": [],
      "resource_multiline_signature": false
    }
  }
}
```

Client/server/freshness results:

```json
{
  "commands": [
    {
      "label": "ctx7-version",
      "command": [
        "node",
        "/home/lucas/.cache/legacy-map-review-20261008/context7-trial/client/node_modules/ctx7/dist/index.js",
        "--version"
      ],
      "seconds": 0.23559649800881743,
      "exit": 0,
      "stderr": ""
    },
    {
      "label": "ctx7-library",
      "command": [
        "node",
        "/home/lucas/.cache/legacy-map-review-20261008/context7-trial/client/node_modules/ctx7/dist/index.js",
        "--base-url",
        "http://127.0.0.1:45175",
        "library",
        "jftp",
        "ResourceLoader getBundle",
        "--json"
      ],
      "seconds": 0.26431269804015756,
      "exit": 0,
      "stderr": ""
    },
    {
      "label": "ctx7-docs",
      "command": [
        "node",
        "/home/lucas/.cache/legacy-map-review-20261008/context7-trial/client/node_modules/ctx7/dist/index.js",
        "--base-url",
        "http://127.0.0.1:45175",
        "docs",
        "/local/jftp",
        "ResourceLoader getBundle ClassLoader",
        "--json"
      ],
      "seconds": 17.78118439298123,
      "exit": 0,
      "stderr": ""
    },
    {
      "label": "fixture-index",
      "command": [
        "python3",
        "/home/lucas/DEV/Projects/agent-toolbox/skills/legacy-codebase-workflows/scripts/context7_backend.py",
        "index",
        "/home/lucas/.cache/legacy-map-review-20261008/context7-trial/freshness-fixture",
        "--database",
        "/home/lucas/.cache/legacy-map-review-20261008/context7-trial/freshness.sqlite",
        "--library-id",
        "/local/fixture"
      ],
      "seconds": 0.1490393050480634,
      "exit": 0,
      "stderr": ""
    },
    {
      "label": "fixture-reindex-change",
      "command": [
        "python3",
        "/home/lucas/DEV/Projects/agent-toolbox/skills/legacy-codebase-workflows/scripts/context7_backend.py",
        "index",
        "/home/lucas/.cache/legacy-map-review-20261008/context7-trial/freshness-fixture",
        "--database",
        "/home/lucas/.cache/legacy-map-review-20261008/context7-trial/freshness.sqlite",
        "--library-id",
        "/local/fixture"
      ],
      "seconds": 0.13246940495446324,
      "exit": 0,
      "stderr": ""
    },
    {
      "label": "fixture-reindex-restored",
      "command": [
        "python3",
        "/home/lucas/DEV/Projects/agent-toolbox/skills/legacy-codebase-workflows/scripts/context7_backend.py",
        "index",
        "/home/lucas/.cache/legacy-map-review-20261008/context7-trial/freshness-fixture",
        "--database",
        "/home/lucas/.cache/legacy-map-review-20261008/context7-trial/freshness.sqlite",
        "--library-id",
        "/local/fixture"
      ],
      "seconds": 0.13198370416648686,
      "exit": 0,
      "stderr": ""
    }
  ],
  "servers": [
    {
      "label": "jftp-server",
      "pid": 1109284,
      "port": 45175,
      "startupSeconds": 0.10688079916872084,
      "announcement": "Local Context7 endpoint: http://127.0.0.1:45175 mode=lexical rerank=None"
    },
    {
      "label": "fixture-server",
      "pid": 1109550,
      "port": 45251,
      "startupSeconds": 0.09068670310080051,
      "announcement": "Local Context7 endpoint: http://127.0.0.1:45251 mode=lexical rerank=None"
    }
  ],
  "checks": {
    "library-selected-local-id": true,
    "ctx7-source-provenance": [
      {
        "path": "com/myjavaworld/util/ResourceLoader.java",
        "startLine": 31,
        "endLine": 61,
        "hash_matches": true,
        "text_matches": true,
        "revision": "non-git"
      },
      {
        "path": "com/myjavaworld/util/ResourceLoader.java",
        "startLine": 1,
        "endLine": 38,
        "hash_matches": true,
        "text_matches": true,
        "revision": "non-git"
      },
      {
        "path": "com/myjavaworld/jftp/LocalSystemMenu.java",
        "startLine": 25,
        "endLine": 54,
        "hash_matches": true,
        "text_matches": true,
        "revision": "non-git"
      },
      {
        "path": "com/myjavaworld/jftp/RemoteSystemMenu.java",
        "startLine": 24,
        "endLine": 52,
        "hash_matches": true,
        "text_matches": true,
        "revision": "non-git"
      },
      {
        "path": "com/myjavaworld/jftp/RemoteSystemMenu.java",
        "startLine": 45,
        "endLine": 78,
        "hash_matches": true,
        "text_matches": true,
        "revision": "non-git"
      }
    ],
    "ctx7-multiline-signature": true,
    "nonloopback-host-rejected": {
      "status": 403,
      "body": "{\"error\": \"Only loopback Host authorities are supported\"}",
      "seconds": 0.004907499998807907
    },
    "fixture-index": {
      "libraryId": "/local/fixture",
      "revision": "f27d85202cf8092f4fe2255c6149c95e20ac59c4",
      "corpusId": "6285455c7f16295f6a9ae8845cf5b05f2487ed590d180fed2b78656be8259af8",
      "files": 1,
      "chunks": 1,
      "chunkChars": 1200,
      "oversizedChunks": 0,
      "changed": 1,
      "deleted": 0,
      "skippedCount": 0,
      "skipped": [],
      "embeddingModel": null,
      "modelRevision": null,
      "rerankerModel": null,
      "rerankerRevision": null,
      "vectorEngine": "stdlib",
      "excludes": []
    },
    "fixture-before-change": {
      "status": 200,
      "body": "{\"codeSnippets\": [{\"codeTitle\": \"code:FreshFixture.java:L1-L3 sha256:7bbf5a9e143d38feff66b4eecc8a907f7f3084d6da79c3d0d9a2dff4bb2dc2a7 revision:f27d85202cf8092f4fe2255c6149c95e20ac59c4 corpus:6285455c7f16295f6a9ae8845cf5b05f2487ed590d180fed2b78656be8259af8\", \"codeDescription\": \"code:FreshFixture.java:L1-L3 sha256:7bbf5a9e143d38feff66b4eecc8a907f7f3084d6da79c3d0d9a2dff4bb2dc2a7 revision:f27d85202cf8092f4fe2255c6149c95e20ac59c4 corpus:6285455c7f16295f6a9ae8845cf5b05f2487ed590d180fed2b78656be8259af8\", \"codeLanguage\": \"java\", \"codeTokens\": 17, \"codeId\": \"code:FreshFixture.java:L1-L3 sha256:7bbf5a9e143d38feff66b4eecc8a907f7f3084d6da79c3d0d9a2dff4bb2dc2a7 revision:f27d85202cf8092f4fe2255c6149c95e20ac59c4 corpus:6285455c7f16295f6a9ae8845cf5b05f2487ed590d180fed2b78656be8259af8\", \"pageTitle\": \"FreshFixture.java\", \"codeList\": [{\"language\": \"java\", \"code\": \"class FreshFixture {\\n  String getValue(String key) { return key; }\\n}\"}]}], \"infoSnippets\": []}",
      "seconds": 0.013667599996551871
    },
    "changed-file-rejected": {
      "status": 409,
      "body": "{\"error\": \"Indexed files changed, appeared, or disappeared; reindex before querying\"}",
      "seconds": 0.011502400040626526
    },
    "deleted-file-rejected": {
      "status": 409,
      "body": "{\"error\": \"Indexed files changed, appeared, or disappeared; reindex before querying\"}",
      "seconds": 0.011905701132491231
    },
    "revision-change-rejected": {
      "status": 409,
      "body": "{\"error\": \"Repository revision changed; reindex before querying\"}",
      "seconds": 0.006666500121355057
    }
  },
  "errors": [],
  "success": true,
  "ownedServersStopped": true
}
```

Limits: 10,000 files; 30,000 chunks; 100,000 source candidates/root; default 1,200 Unicode characters and 48 lines/chunk, 8 overlap; selected query limit5. No embedding/model downloads. Actual JFTP index reports 0 skips/oversized chunks. Query latency includes repeated full freshness scans over mounted Windows source; timings are individual runs, not medians.

Setup issue: local pnpm is Corepack; first attempt waited for its download prompt. Retained `client-install-prompt.log`; retry used scoped `COREPACK_ENABLE_DOWNLOAD_PROMPT=0`. Initial evidence checker included terminal LF in comparisons; corrected to LF-joined exact source lines used by backend. One read-only shell inspection had quoting SyntaxError; retried via Python stdin. The first real-client harness assumed library JSON was an object; ctx7 actually returns a list. Both client commands succeeded; corrected the harness and preserved attempt1 evidence. A helper named http initially shadowed Python http.client in the fixture phase; renamed it and preserved attempt2 client/provenance evidence. These were harness issues, not backend failures.

Exact stdout/stderr and JSON measurements are adjacent to this report. All owned trial servers were stopped; JFTP source was never changed.

## Additional limits and filesystem checks

The one-file byte cap is 256,000. Query result limits are 1–10 and question length is 1–500 characters. Invalid result/chunk settings were rejected with exit2 and plain stderr diagnostics; HTTP failures use JSON. A synthetic 256,001-byte Java file was explicitly skipped while the admitted fixture remained indexed. These are expected validation failures. A supplementary harness first expected exit1; corrected to the actual exit2 and retained stderr logs.

The same four byte-identical public files were indexed on ext4 and a mounted Windows temporary directory; both produced 4 files / 20 chunks and 110,592-byte databases. See `four-file-snapshot-comparison.md` and JSON. Ext4 index 0.180 s, queries 0.117–0.120 s; mounted index 0.631 s, queries 0.633–1.037 s. Single-run controlled small-corpus evidence; no full-repository ratio is claimed.

Both final owned server ports 45175/45251 were independently checked closed (connection refused) after cleanup. Full limits/results in `trial-results.json`.
