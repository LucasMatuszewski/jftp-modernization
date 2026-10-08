# Four public-file filesystem trial

Four public JFTP files copied byte-for-byte; these snapshots have no Git revision. Controlled small corpus, not a full-repository speed claim.

Both snapshots preserve the same original relative paths and byte hashes. Timings are single subprocess runs including freshness scans; no global speed ratio is claimed.

```json
{
  "scope": [
    "com/myjavaworld/util/ResourceLoader.java",
    "com/myjavaworld/jftp/LocalFile.java",
    "com/myjavaworld/jftp/Favorite.java",
    "com/myjavaworld/jftp/RemoteHost.java"
  ],
  "source": "Four public JFTP files copied byte-for-byte; these snapshots have no Git revision. Controlled small corpus, not a full-repository speed claim.",
  "files": {
    "com/myjavaworld/util/ResourceLoader.java": "987cea071f2044eddf460cf41a9688c406cf291548f144db3651688c70637dee",
    "com/myjavaworld/jftp/LocalFile.java": "8af551de8f5d16faea6a82713d8e748d2c2eaa3967731d8da715f798bfecf341",
    "com/myjavaworld/jftp/Favorite.java": "911b98c99a75607dcd9fc57c02858c06678c998ab6825f3b8a891b86738a53f0",
    "com/myjavaworld/jftp/RemoteHost.java": "451d94d3e00274b95e0f7275aaca463d9bbac9f8d989d0640f950acc6ef5bd37"
  },
  "corpora": {
    "ext4": {
      "root": "/home/lucas/.cache/legacy-map-review-20261008/context7-trial/four-file-snapshot",
      "index": {
        "libraryId": "/local/snapshot",
        "revision": "non-git",
        "corpusId": "9085f2401b340ca055dfdc1064825aae99980e421fc8a6b0d8164a1b75041a4d",
        "files": 4,
        "chunks": 20,
        "chunkChars": 1200,
        "oversizedChunks": 0,
        "changed": 4,
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
      "databaseBytes": 110592,
      "measurements": [
        {
          "label": "index",
          "seconds": 0.18039739807136357,
          "exit": 0
        },
        {
          "label": "query-resource",
          "seconds": 0.12012129882350564,
          "exit": 0
        },
        {
          "label": "query-localfile",
          "seconds": 0.1166627979837358,
          "exit": 0
        },
        {
          "label": "query-absent",
          "seconds": 0.12039969908073545,
          "exit": 0
        }
      ],
      "queries": {
        "resource": {
          "results": 2,
          "paths": [
            "com/myjavaworld/util/ResourceLoader.java",
            "com/myjavaworld/util/ResourceLoader.java"
          ]
        },
        "localfile": {
          "results": 5,
          "paths": [
            "com/myjavaworld/jftp/LocalFile.java",
            "com/myjavaworld/jftp/Favorite.java",
            "com/myjavaworld/jftp/RemoteHost.java",
            "com/myjavaworld/jftp/LocalFile.java",
            "com/myjavaworld/jftp/LocalFile.java"
          ]
        },
        "absent": {
          "results": 0,
          "paths": []
        }
      }
    },
    "windows-mounted": {
      "root": "/mnt/c/Users/BiuroEdukey/AppData/Local/Temp/legacy-skill-review-20261007-05bd/context7-four-file-snapshot",
      "index": {
        "libraryId": "/local/snapshot",
        "revision": "non-git",
        "corpusId": "9085f2401b340ca055dfdc1064825aae99980e421fc8a6b0d8164a1b75041a4d",
        "files": 4,
        "chunks": 20,
        "chunkChars": 1200,
        "oversizedChunks": 0,
        "changed": 4,
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
      "databaseBytes": 110592,
      "measurements": [
        {
          "label": "index",
          "seconds": 0.6310777920298278,
          "exit": 0
        },
        {
          "label": "query-resource",
          "seconds": 0.7454447911586612,
          "exit": 0
        },
        {
          "label": "query-localfile",
          "seconds": 1.0369218881241977,
          "exit": 0
        },
        {
          "label": "query-absent",
          "seconds": 0.6326339938677847,
          "exit": 0
        }
      ],
      "queries": {
        "resource": {
          "results": 2,
          "paths": [
            "com/myjavaworld/util/ResourceLoader.java",
            "com/myjavaworld/util/ResourceLoader.java"
          ]
        },
        "localfile": {
          "results": 5,
          "paths": [
            "com/myjavaworld/jftp/LocalFile.java",
            "com/myjavaworld/jftp/Favorite.java",
            "com/myjavaworld/jftp/RemoteHost.java",
            "com/myjavaworld/jftp/LocalFile.java",
            "com/myjavaworld/jftp/LocalFile.java"
          ]
        },
        "absent": {
          "results": 0,
          "paths": []
        }
      }
    }
  }
}
```
