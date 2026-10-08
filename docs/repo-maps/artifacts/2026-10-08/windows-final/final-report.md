# Final Windows native consumer and Java maps

No signature, execution-policy, MOTW or global PATH changes. CI/build identity comes from the downloaded authenticated artifact index. Individual Windows generation times are separate from archived 60-sample WSL measurements. Full commands, original revision/fingerprint, hashes, coverage and comparison follow.

```json
{
  "expected_head": "03a538c5db5ddcbbf7bc4377d380106343bf9177",
  "run_id": "37711387112",
  "root": "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp",
  "commands": [
    {
      "label": "ci-run",
      "command": [
        "gh",
        "run",
        "view",
        "37711387112",
        "--repo",
        "EdukeyTeam/agent-toolbox",
        "--json",
        "status,conclusion,headSha,jobs,url"
      ],
      "elapsed_seconds": 1.459680800093338,
      "exit": 0,
      "stdout": "{\"conclusion\":\"success\",\"headSha\":\"03a538c5db5ddcbbf7bc4377d380106343bf9177\",\"jobs\":[{\"completedAt\":\"2026-10-08T01:08:20Z\",\"conclusion\":\"success\",\"databaseId\":113097869123,\"name\":\"workflow-validation\",\"startedAt\":\"2026-10-08T01:08:16Z\",\"status\":\"completed\",\"steps\":[{\"completedAt\":\"2026-10-08T01:08:17Z\",\"conclusion\":\"success\",\"name\":\"Set up job\",\"number\":1,\"startedAt\":\"2026-10-08T01:08:17Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:18Z\",\"conclusion\":\"success\",\"name\":\"Run actions/checkout@v6\",\"number\":2,\"startedAt\":\"2026-10-08T01:08:17Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:18Z\",\"conclusion\":\"success\",\"name\":\"Validate workflow expressions with pinned actionlint\",\"number\":3,\"startedAt\":\"2026-10-08T01:08:18Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:19Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/checkout@v6\",\"number\":6,\"startedAt\":\"2026-10-08T01:08:18Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:19Z\",\"conclusion\":\"success\",\"name\":\"Complete job\",\"number\":7,\"startedAt\":\"2026-10-08T01:08:19Z\",\"status\":\"completed\"}],\"url\":\"https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37711387112/job/113097869123\"},{\"completedAt\":\"2026-10-08T01:09:00Z\",\"conclusion\":\"success\",\"databaseId\":113097897491,\"name\":\"semantic-retrieval (ubuntu-latest)\",\"startedAt\":\"2026-10-08T01:08:23Z\",\"status\":\"completed\",\"steps\":[{\"completedAt\":\"2026-10-08T01:08:25Z\",\"conclusion\":\"success\",\"name\":\"Set up job\",\"number\":1,\"startedAt\":\"2026-10-08T01:08:24Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:25Z\",\"conclusion\":\"success\",\"name\":\"Run actions/checkout@v6\",\"number\":2,\"startedAt\":\"2026-10-08T01:08:25Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:26Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-node@v7\",\"number\":3,\"startedAt\":\"2026-10-08T01:08:25Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:26Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-python@v7\",\"number\":4,\"startedAt\":\"2026-10-08T01:08:26Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:31Z\",\"conclusion\":\"success\",\"name\":\"Run pnpm/action-setup@v6\",\"number\":5,\"startedAt\":\"2026-10-08T01:08:26Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:33Z\",\"conclusion\":\"success\",\"name\":\"Prepare optional inference runtime\",\"number\":6,\"startedAt\":\"2026-10-08T01:08:31Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:35Z\",\"conclusion\":\"success\",\"name\":\"Install optional vector adapter and pinned Context7 client\",\"number\":7,\"startedAt\":\"2026-10-08T01:08:33Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:57Z\",\"conclusion\":\"success\",\"name\":\"Test actual local embeddings and hybrid retrieval\",\"number\":8,\"startedAt\":\"2026-10-08T01:08:35Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:58Z\",\"conclusion\":\"success\",\"name\":\"Post Run pnpm/action-setup@v6\",\"number\":13,\"startedAt\":\"2026-10-08T01:08:57Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:58Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-python@v7\",\"number\":14,\"startedAt\":\"2026-10-08T01:08:58Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:58Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-node@v7\",\"number\":15,\"startedAt\":\"2026-10-08T01:08:58Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:58Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/checkout@v6\",\"number\":16,\"startedAt\":\"2026-10-08T01:08:58Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:58Z\",\"conclusion\":\"success\",\"name\":\"Complete job\",\"number\":17,\"startedAt\":\"2026-10-08T01:08:58Z\",\"status\":\"completed\"}],\"url\":\"https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37711387112/job/113097897491\"},{\"completedAt\":\"2026-10-08T01:10:06Z\",\"conclusion\":\"success\",\"databaseId\":113097897511,\"name\":\"native-artifacts (ubuntu-latest)\",\"startedAt\":\"2026-10-08T01:08:23Z\",\"status\":\"completed\",\"steps\":[{\"completedAt\":\"2026-10-08T01:08:26Z\",\"conclusion\":\"success\",\"name\":\"Set up job\",\"number\":1,\"startedAt\":\"2026-10-08T01:08:24Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:28Z\",\"conclusion\":\"success\",\"name\":\"Run actions/checkout@v6\",\"number\":2,\"startedAt\":\"2026-10-08T01:08:26Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:28Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-python@v7\",\"number\":3,\"startedAt\":\"2026-10-08T01:08:28Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:30Z\",\"conclusion\":\"success\",\"name\":\"Run dtolnay/rust-toolchain@stable\",\"number\":4,\"startedAt\":\"2026-10-08T01:08:28Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:48Z\",\"conclusion\":\"success\",\"name\":\"Test native repository mapper\",\"number\":5,\"startedAt\":\"2026-10-08T01:08:30Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:40Z\",\"conclusion\":\"success\",\"name\":\"Build standalone tools with licenses and smoke checks\",\"number\":6,\"startedAt\":\"2026-10-08T01:08:48Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:40Z\",\"conclusion\":\"success\",\"name\":\"Locate host-specific binaries\",\"number\":7,\"startedAt\":\"2026-10-08T01:09:40Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:00Z\",\"conclusion\":\"success\",\"name\":\"Test actual binaries against the Python source\",\"number\":8,\"startedAt\":\"2026-10-08T01:09:40Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:01Z\",\"conclusion\":\"success\",\"name\":\"Prepare a source-identified per-platform CI install index\",\"number\":9,\"startedAt\":\"2026-10-08T01:10:00Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:03Z\",\"conclusion\":\"success\",\"name\":\"Retain reviewable native artifacts\",\"number\":10,\"startedAt\":\"2026-10-08T01:10:01Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:03Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-python@v7\",\"number\":19,\"startedAt\":\"2026-10-08T01:10:03Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:03Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/checkout@v6\",\"number\":20,\"startedAt\":\"2026-10-08T01:10:03Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:03Z\",\"conclusion\":\"success\",\"name\":\"Complete job\",\"number\":21,\"startedAt\":\"2026-10-08T01:10:03Z\",\"status\":\"completed\"}],\"url\":\"https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37711387112/job/113097897511\"},{\"completedAt\":\"2026-10-08T01:09:47Z\",\"conclusion\":\"success\",\"databaseId\":113097897537,\"name\":\"semantic-retrieval (windows-latest)\",\"startedAt\":\"2026-10-08T01:08:24Z\",\"status\":\"completed\",\"steps\":[{\"completedAt\":\"2026-10-08T01:08:26Z\",\"conclusion\":\"success\",\"name\":\"Set up job\",\"number\":1,\"startedAt\":\"2026-10-08T01:08:25Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:30Z\",\"conclusion\":\"success\",\"name\":\"Run actions/checkout@v6\",\"number\":2,\"startedAt\":\"2026-10-08T01:08:26Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:35Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-node@v7\",\"number\":3,\"startedAt\":\"2026-10-08T01:08:30Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:35Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-python@v7\",\"number\":4,\"startedAt\":\"2026-10-08T01:08:35Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:52Z\",\"conclusion\":\"success\",\"name\":\"Run pnpm/action-setup@v6\",\"number\":5,\"startedAt\":\"2026-10-08T01:08:35Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:54Z\",\"conclusion\":\"success\",\"name\":\"Prepare optional inference runtime\",\"number\":6,\"startedAt\":\"2026-10-08T01:08:52Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:02Z\",\"conclusion\":\"success\",\"name\":\"Install optional vector adapter and pinned Context7 client\",\"number\":7,\"startedAt\":\"2026-10-08T01:08:54Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:43Z\",\"conclusion\":\"success\",\"name\":\"Test actual local embeddings and hybrid retrieval\",\"number\":8,\"startedAt\":\"2026-10-08T01:09:02Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:44Z\",\"conclusion\":\"success\",\"name\":\"Post Run pnpm/action-setup@v6\",\"number\":13,\"startedAt\":\"2026-10-08T01:09:43Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:44Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-python@v7\",\"number\":14,\"startedAt\":\"2026-10-08T01:09:44Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:44Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-node@v7\",\"number\":15,\"startedAt\":\"2026-10-08T01:09:44Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:45Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/checkout@v6\",\"number\":16,\"startedAt\":\"2026-10-08T01:09:44Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:45Z\",\"conclusion\":\"success\",\"name\":\"Complete job\",\"number\":17,\"startedAt\":\"2026-10-08T01:09:45Z\",\"status\":\"completed\"}],\"url\":\"https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37711387112/job/113097897537\"},{\"completedAt\":\"2026-10-08T01:10:45Z\",\"conclusion\":\"success\",\"databaseId\":113097897572,\"name\":\"native-artifacts (windows-latest)\",\"startedAt\":\"2026-10-08T01:08:23Z\",\"status\":\"completed\",\"steps\":[{\"completedAt\":\"2026-10-08T01:08:25Z\",\"conclusion\":\"success\",\"name\":\"Set up job\",\"number\":1,\"startedAt\":\"2026-10-08T01:08:24Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:29Z\",\"conclusion\":\"success\",\"name\":\"Run actions/checkout@v6\",\"number\":2,\"startedAt\":\"2026-10-08T01:08:25Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:30Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-python@v7\",\"number\":3,\"startedAt\":\"2026-10-08T01:08:29Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:47Z\",\"conclusion\":\"success\",\"name\":\"Run dtolnay/rust-toolchain@stable\",\"number\":4,\"startedAt\":\"2026-10-08T01:08:30Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:12Z\",\"conclusion\":\"success\",\"name\":\"Test native repository mapper\",\"number\":5,\"startedAt\":\"2026-10-08T01:08:47Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:12Z\",\"conclusion\":\"success\",\"name\":\"Build standalone tools with licenses and smoke checks\",\"number\":6,\"startedAt\":\"2026-10-08T01:09:12Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:12Z\",\"conclusion\":\"success\",\"name\":\"Locate host-specific binaries\",\"number\":7,\"startedAt\":\"2026-10-08T01:10:12Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:40Z\",\"conclusion\":\"success\",\"name\":\"Test actual binaries against the Python source\",\"number\":8,\"startedAt\":\"2026-10-08T01:10:12Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:40Z\",\"conclusion\":\"success\",\"name\":\"Prepare a source-identified per-platform CI install index\",\"number\":9,\"startedAt\":\"2026-10-08T01:10:40Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:42Z\",\"conclusion\":\"success\",\"name\":\"Retain reviewable native artifacts\",\"number\":10,\"startedAt\":\"2026-10-08T01:10:40Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:42Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-python@v7\",\"number\":19,\"startedAt\":\"2026-10-08T01:10:42Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:44Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/checkout@v6\",\"number\":20,\"startedAt\":\"2026-10-08T01:10:42Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:44Z\",\"conclusion\":\"success\",\"name\":\"Complete job\",\"number\":21,\"startedAt\":\"2026-10-08T01:10:44Z\",\"status\":\"completed\"}],\"url\":\"https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37711387112/job/113097897572\"},{\"completedAt\":\"2026-10-08T01:09:58Z\",\"conclusion\":\"success\",\"databaseId\":113097897601,\"name\":\"test (windows-latest, 3.12)\",\"startedAt\":\"2026-10-08T01:08:23Z\",\"status\":\"completed\",\"steps\":[{\"completedAt\":\"2026-10-08T01:08:25Z\",\"conclusion\":\"success\",\"name\":\"Set up job\",\"number\":1,\"startedAt\":\"2026-10-08T01:08:24Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:30Z\",\"conclusion\":\"success\",\"name\":\"Run actions/checkout@v6\",\"number\":2,\"startedAt\":\"2026-10-08T01:08:25Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:40Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-node@v7\",\"number\":3,\"startedAt\":\"2026-10-08T01:08:30Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:41Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-python@v7\",\"number\":4,\"startedAt\":\"2026-10-08T01:08:40Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:45Z\",\"conclusion\":\"success\",\"name\":\"Run npm ci\",\"number\":5,\"startedAt\":\"2026-10-08T01:08:41Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:50Z\",\"conclusion\":\"success\",\"name\":\"Run npm test\",\"number\":6,\"startedAt\":\"2026-10-08T01:08:45Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:00Z\",\"conclusion\":\"success\",\"name\":\"Install local map dependencies\",\"number\":7,\"startedAt\":\"2026-10-08T01:08:50Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:02Z\",\"conclusion\":\"success\",\"name\":\"Install optional vector adapter on each platform\",\"number\":8,\"startedAt\":\"2026-10-08T01:09:00Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:55Z\",\"conclusion\":\"success\",\"name\":\"Test local mapping and retrieval\",\"number\":9,\"startedAt\":\"2026-10-08T01:09:02Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:55Z\",\"conclusion\":\"skipped\",\"name\":\"Require native vector adapter with compatible macOS SQLite\",\"number\":10,\"startedAt\":\"2026-10-08T01:09:55Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:55Z\",\"conclusion\":\"skipped\",\"name\":\"Build and verify Claude plugin ZIP\",\"number\":11,\"startedAt\":\"2026-10-08T01:09:55Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:55Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-python@v7\",\"number\":20,\"startedAt\":\"2026-10-08T01:09:55Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:55Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-node@v7\",\"number\":21,\"startedAt\":\"2026-10-08T01:09:55Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:57Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/checkout@v6\",\"number\":22,\"startedAt\":\"2026-10-08T01:09:55Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:57Z\",\"conclusion\":\"success\",\"name\":\"Complete job\",\"number\":23,\"startedAt\":\"2026-10-08T01:09:57Z\",\"status\":\"completed\"}],\"url\":\"https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37711387112/job/113097897601\"},{\"completedAt\":\"2026-10-08T01:08:50Z\",\"conclusion\":\"success\",\"databaseId\":113097897605,\"name\":\"test (ubuntu-latest, 3.13)\",\"startedAt\":\"2026-10-08T01:08:23Z\",\"status\":\"completed\",\"steps\":[{\"completedAt\":\"2026-10-08T01:08:25Z\",\"conclusion\":\"success\",\"name\":\"Set up job\",\"number\":1,\"startedAt\":\"2026-10-08T01:08:24Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:26Z\",\"conclusion\":\"success\",\"name\":\"Run actions/checkout@v6\",\"number\":2,\"startedAt\":\"2026-10-08T01:08:25Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:27Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-node@v7\",\"number\":3,\"startedAt\":\"2026-10-08T01:08:26Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:27Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-python@v7\",\"number\":4,\"startedAt\":\"2026-10-08T01:08:27Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:28Z\",\"conclusion\":\"success\",\"name\":\"Run npm ci\",\"number\":5,\"startedAt\":\"2026-10-08T01:08:27Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:30Z\",\"conclusion\":\"success\",\"name\":\"Run npm test\",\"number\":6,\"startedAt\":\"2026-10-08T01:08:28Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:34Z\",\"conclusion\":\"success\",\"name\":\"Install local map dependencies\",\"number\":7,\"startedAt\":\"2026-10-08T01:08:30Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:34Z\",\"conclusion\":\"skipped\",\"name\":\"Install optional vector adapter on each platform\",\"number\":8,\"startedAt\":\"2026-10-08T01:08:34Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:48Z\",\"conclusion\":\"success\",\"name\":\"Test local mapping and retrieval\",\"number\":9,\"startedAt\":\"2026-10-08T01:08:34Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:48Z\",\"conclusion\":\"skipped\",\"name\":\"Require native vector adapter with compatible macOS SQLite\",\"number\":10,\"startedAt\":\"2026-10-08T01:08:48Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:48Z\",\"conclusion\":\"skipped\",\"name\":\"Build and verify Claude plugin ZIP\",\"number\":11,\"startedAt\":\"2026-10-08T01:08:48Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:48Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-python@v7\",\"number\":20,\"startedAt\":\"2026-10-08T01:08:48Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:48Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-node@v7\",\"number\":21,\"startedAt\":\"2026-10-08T01:08:48Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:48Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/checkout@v6\",\"number\":22,\"startedAt\":\"2026-10-08T01:08:48Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:48Z\",\"conclusion\":\"success\",\"name\":\"Complete job\",\"number\":23,\"startedAt\":\"2026-10-08T01:08:48Z\",\"status\":\"completed\"}],\"url\":\"https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37711387112/job/113097897605\"},{\"completedAt\":\"2026-10-08T01:13:26Z\",\"conclusion\":\"success\",\"databaseId\":113097897608,\"name\":\"test (macos-latest, 3.13)\",\"startedAt\":\"2026-10-08T01:08:31Z\",\"status\":\"completed\",\"steps\":[{\"completedAt\":\"2026-10-08T01:08:34Z\",\"conclusion\":\"success\",\"name\":\"Set up job\",\"number\":1,\"startedAt\":\"2026-10-08T01:08:33Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:36Z\",\"conclusion\":\"success\",\"name\":\"Run actions/checkout@v6\",\"number\":2,\"startedAt\":\"2026-10-08T01:08:34Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:37Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-node@v7\",\"number\":3,\"startedAt\":\"2026-10-08T01:08:36Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:38Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-python@v7\",\"number\":4,\"startedAt\":\"2026-10-08T01:08:37Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:38Z\",\"conclusion\":\"success\",\"name\":\"Run npm ci\",\"number\":5,\"startedAt\":\"2026-10-08T01:08:38Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:40Z\",\"conclusion\":\"success\",\"name\":\"Run npm test\",\"number\":6,\"startedAt\":\"2026-10-08T01:08:38Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:45Z\",\"conclusion\":\"success\",\"name\":\"Install local map dependencies\",\"number\":7,\"startedAt\":\"2026-10-08T01:08:40Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:45Z\",\"conclusion\":\"skipped\",\"name\":\"Install optional vector adapter on each platform\",\"number\":8,\"startedAt\":\"2026-10-08T01:08:45Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:13:20Z\",\"conclusion\":\"success\",\"name\":\"Test local mapping and retrieval\",\"number\":9,\"startedAt\":\"2026-10-08T01:08:45Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:13:20Z\",\"conclusion\":\"skipped\",\"name\":\"Require native vector adapter with compatible macOS SQLite\",\"number\":10,\"startedAt\":\"2026-10-08T01:13:20Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:13:20Z\",\"conclusion\":\"skipped\",\"name\":\"Build and verify Claude plugin ZIP\",\"number\":11,\"startedAt\":\"2026-10-08T01:13:20Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:13:21Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-python@v7\",\"number\":20,\"startedAt\":\"2026-10-08T01:13:20Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:13:21Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-node@v7\",\"number\":21,\"startedAt\":\"2026-10-08T01:13:21Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:13:22Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/checkout@v6\",\"number\":22,\"startedAt\":\"2026-10-08T01:13:21Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:13:24Z\",\"conclusion\":\"success\",\"name\":\"Complete job\",\"number\":23,\"startedAt\":\"2026-10-08T01:13:22Z\",\"status\":\"completed\"}],\"url\":\"https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37711387112/job/113097897608\"},{\"completedAt\":\"2026-10-08T01:09:40Z\",\"conclusion\":\"success\",\"databaseId\":113097897622,\"name\":\"test (windows-latest, 3.14)\",\"startedAt\":\"2026-10-08T01:08:24Z\",\"status\":\"completed\",\"steps\":[{\"completedAt\":\"2026-10-08T01:08:26Z\",\"conclusion\":\"success\",\"name\":\"Set up job\",\"number\":1,\"startedAt\":\"2026-10-08T01:08:25Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:30Z\",\"conclusion\":\"success\",\"name\":\"Run actions/checkout@v6\",\"number\":2,\"startedAt\":\"2026-10-08T01:08:26Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:37Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-node@v7\",\"number\":3,\"startedAt\":\"2026-10-08T01:08:30Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:37Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-python@v7\",\"number\":4,\"startedAt\":\"2026-10-08T01:08:37Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:42Z\",\"conclusion\":\"success\",\"name\":\"Run npm ci\",\"number\":5,\"startedAt\":\"2026-10-08T01:08:37Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:48Z\",\"conclusion\":\"success\",\"name\":\"Run npm test\",\"number\":6,\"startedAt\":\"2026-10-08T01:08:42Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:57Z\",\"conclusion\":\"success\",\"name\":\"Install local map dependencies\",\"number\":7,\"startedAt\":\"2026-10-08T01:08:48Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:57Z\",\"conclusion\":\"skipped\",\"name\":\"Install optional vector adapter on each platform\",\"number\":8,\"startedAt\":\"2026-10-08T01:08:57Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:37Z\",\"conclusion\":\"success\",\"name\":\"Test local mapping and retrieval\",\"number\":9,\"startedAt\":\"2026-10-08T01:08:57Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:37Z\",\"conclusion\":\"skipped\",\"name\":\"Require native vector adapter with compatible macOS SQLite\",\"number\":10,\"startedAt\":\"2026-10-08T01:09:37Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:37Z\",\"conclusion\":\"skipped\",\"name\":\"Build and verify Claude plugin ZIP\",\"number\":11,\"startedAt\":\"2026-10-08T01:09:37Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:37Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-python@v7\",\"number\":20,\"startedAt\":\"2026-10-08T01:09:37Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:37Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-node@v7\",\"number\":21,\"startedAt\":\"2026-10-08T01:09:37Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:39Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/checkout@v6\",\"number\":22,\"startedAt\":\"2026-10-08T01:09:37Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:39Z\",\"conclusion\":\"success\",\"name\":\"Complete job\",\"number\":23,\"startedAt\":\"2026-10-08T01:09:39Z\",\"status\":\"completed\"}],\"url\":\"https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37711387112/job/113097897622\"},{\"completedAt\":\"2026-10-08T01:10:54Z\",\"conclusion\":\"success\",\"databaseId\":113097897628,\"name\":\"native-artifacts (macos-latest)\",\"startedAt\":\"2026-10-08T01:08:27Z\",\"status\":\"completed\",\"steps\":[{\"completedAt\":\"2026-10-08T01:08:29Z\",\"conclusion\":\"success\",\"name\":\"Set up job\",\"number\":1,\"startedAt\":\"2026-10-08T01:08:27Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:31Z\",\"conclusion\":\"success\",\"name\":\"Run actions/checkout@v6\",\"number\":2,\"startedAt\":\"2026-10-08T01:08:29Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:31Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-python@v7\",\"number\":3,\"startedAt\":\"2026-10-08T01:08:31Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:40Z\",\"conclusion\":\"success\",\"name\":\"Run dtolnay/rust-toolchain@stable\",\"number\":4,\"startedAt\":\"2026-10-08T01:08:31Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:16Z\",\"conclusion\":\"success\",\"name\":\"Test native repository mapper\",\"number\":5,\"startedAt\":\"2026-10-08T01:08:40Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:21Z\",\"conclusion\":\"success\",\"name\":\"Build standalone tools with licenses and smoke checks\",\"number\":6,\"startedAt\":\"2026-10-08T01:09:16Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:21Z\",\"conclusion\":\"success\",\"name\":\"Locate host-specific binaries\",\"number\":7,\"startedAt\":\"2026-10-08T01:10:21Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:48Z\",\"conclusion\":\"success\",\"name\":\"Test actual binaries against the Python source\",\"number\":8,\"startedAt\":\"2026-10-08T01:10:21Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:48Z\",\"conclusion\":\"success\",\"name\":\"Prepare a source-identified per-platform CI install index\",\"number\":9,\"startedAt\":\"2026-10-08T01:10:48Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:50Z\",\"conclusion\":\"success\",\"name\":\"Retain reviewable native artifacts\",\"number\":10,\"startedAt\":\"2026-10-08T01:10:48Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:50Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-python@v7\",\"number\":19,\"startedAt\":\"2026-10-08T01:10:50Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:51Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/checkout@v6\",\"number\":20,\"startedAt\":\"2026-10-08T01:10:50Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:52Z\",\"conclusion\":\"success\",\"name\":\"Complete job\",\"number\":21,\"startedAt\":\"2026-10-08T01:10:51Z\",\"status\":\"completed\"}],\"url\":\"https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37711387112/job/113097897628\"},{\"completedAt\":\"2026-10-08T01:13:22Z\",\"conclusion\":\"success\",\"databaseId\":113097897642,\"name\":\"test (macos-latest, 3.14)\",\"startedAt\":\"2026-10-08T01:08:31Z\",\"status\":\"completed\",\"steps\":[{\"completedAt\":\"2026-10-08T01:08:33Z\",\"conclusion\":\"success\",\"name\":\"Set up job\",\"number\":1,\"startedAt\":\"2026-10-08T01:08:32Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:35Z\",\"conclusion\":\"success\",\"name\":\"Run actions/checkout@v6\",\"number\":2,\"startedAt\":\"2026-10-08T01:08:33Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:37Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-node@v7\",\"number\":3,\"startedAt\":\"2026-10-08T01:08:35Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:37Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-python@v7\",\"number\":4,\"startedAt\":\"2026-10-08T01:08:37Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:38Z\",\"conclusion\":\"success\",\"name\":\"Run npm ci\",\"number\":5,\"startedAt\":\"2026-10-08T01:08:37Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:41Z\",\"conclusion\":\"success\",\"name\":\"Run npm test\",\"number\":6,\"startedAt\":\"2026-10-08T01:08:38Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:47Z\",\"conclusion\":\"success\",\"name\":\"Install local map dependencies\",\"number\":7,\"startedAt\":\"2026-10-08T01:08:41Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:47Z\",\"conclusion\":\"skipped\",\"name\":\"Install optional vector adapter on each platform\",\"number\":8,\"startedAt\":\"2026-10-08T01:08:47Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:13:18Z\",\"conclusion\":\"success\",\"name\":\"Test local mapping and retrieval\",\"number\":9,\"startedAt\":\"2026-10-08T01:08:47Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:13:18Z\",\"conclusion\":\"skipped\",\"name\":\"Require native vector adapter with compatible macOS SQLite\",\"number\":10,\"startedAt\":\"2026-10-08T01:13:18Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:13:18Z\",\"conclusion\":\"skipped\",\"name\":\"Build and verify Claude plugin ZIP\",\"number\":11,\"startedAt\":\"2026-10-08T01:13:18Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:13:18Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-python@v7\",\"number\":20,\"startedAt\":\"2026-10-08T01:13:18Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:13:18Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-node@v7\",\"number\":21,\"startedAt\":\"2026-10-08T01:13:18Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:13:19Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/checkout@v6\",\"number\":22,\"startedAt\":\"2026-10-08T01:13:18Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:13:19Z\",\"conclusion\":\"success\",\"name\":\"Complete job\",\"number\":23,\"startedAt\":\"2026-10-08T01:13:19Z\",\"status\":\"completed\"}],\"url\":\"https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37711387112/job/113097897642\"},{\"completedAt\":\"2026-10-08T01:08:57Z\",\"conclusion\":\"success\",\"databaseId\":113097897650,\"name\":\"test (ubuntu-latest, 3.12)\",\"startedAt\":\"2026-10-08T01:08:23Z\",\"status\":\"completed\",\"steps\":[{\"completedAt\":\"2026-10-08T01:08:25Z\",\"conclusion\":\"success\",\"name\":\"Set up job\",\"number\":1,\"startedAt\":\"2026-10-08T01:08:24Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:25Z\",\"conclusion\":\"success\",\"name\":\"Run actions/checkout@v6\",\"number\":2,\"startedAt\":\"2026-10-08T01:08:25Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:26Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-node@v7\",\"number\":3,\"startedAt\":\"2026-10-08T01:08:25Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:26Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-python@v7\",\"number\":4,\"startedAt\":\"2026-10-08T01:08:26Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:28Z\",\"conclusion\":\"success\",\"name\":\"Run npm ci\",\"number\":5,\"startedAt\":\"2026-10-08T01:08:26Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:29Z\",\"conclusion\":\"success\",\"name\":\"Run npm test\",\"number\":6,\"startedAt\":\"2026-10-08T01:08:28Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:34Z\",\"conclusion\":\"success\",\"name\":\"Install local map dependencies\",\"number\":7,\"startedAt\":\"2026-10-08T01:08:29Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:35Z\",\"conclusion\":\"success\",\"name\":\"Install optional vector adapter on each platform\",\"number\":8,\"startedAt\":\"2026-10-08T01:08:34Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:50Z\",\"conclusion\":\"success\",\"name\":\"Test local mapping and retrieval\",\"number\":9,\"startedAt\":\"2026-10-08T01:08:35Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:50Z\",\"conclusion\":\"skipped\",\"name\":\"Require native vector adapter with compatible macOS SQLite\",\"number\":10,\"startedAt\":\"2026-10-08T01:08:50Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:54Z\",\"conclusion\":\"success\",\"name\":\"Build and verify Claude plugin ZIP\",\"number\":11,\"startedAt\":\"2026-10-08T01:08:50Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:54Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-python@v7\",\"number\":20,\"startedAt\":\"2026-10-08T01:08:54Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:55Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-node@v7\",\"number\":21,\"startedAt\":\"2026-10-08T01:08:54Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:55Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/checkout@v6\",\"number\":22,\"startedAt\":\"2026-10-08T01:08:55Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:55Z\",\"conclusion\":\"success\",\"name\":\"Complete job\",\"number\":23,\"startedAt\":\"2026-10-08T01:08:55Z\",\"status\":\"completed\"}],\"url\":\"https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37711387112/job/113097897650\"},{\"completedAt\":\"2026-10-08T01:08:54Z\",\"conclusion\":\"success\",\"databaseId\":113097897657,\"name\":\"test (ubuntu-latest, 3.14)\",\"startedAt\":\"2026-10-08T01:08:23Z\",\"status\":\"completed\",\"steps\":[{\"completedAt\":\"2026-10-08T01:08:25Z\",\"conclusion\":\"success\",\"name\":\"Set up job\",\"number\":1,\"startedAt\":\"2026-10-08T01:08:24Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:26Z\",\"conclusion\":\"success\",\"name\":\"Run actions/checkout@v6\",\"number\":2,\"startedAt\":\"2026-10-08T01:08:25Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:29Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-node@v7\",\"number\":3,\"startedAt\":\"2026-10-08T01:08:26Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:29Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-python@v7\",\"number\":4,\"startedAt\":\"2026-10-08T01:08:29Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:30Z\",\"conclusion\":\"success\",\"name\":\"Run npm ci\",\"number\":5,\"startedAt\":\"2026-10-08T01:08:29Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:34Z\",\"conclusion\":\"success\",\"name\":\"Run npm test\",\"number\":6,\"startedAt\":\"2026-10-08T01:08:30Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:40Z\",\"conclusion\":\"success\",\"name\":\"Install local map dependencies\",\"number\":7,\"startedAt\":\"2026-10-08T01:08:34Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:40Z\",\"conclusion\":\"skipped\",\"name\":\"Install optional vector adapter on each platform\",\"number\":8,\"startedAt\":\"2026-10-08T01:08:40Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:51Z\",\"conclusion\":\"success\",\"name\":\"Test local mapping and retrieval\",\"number\":9,\"startedAt\":\"2026-10-08T01:08:40Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:51Z\",\"conclusion\":\"skipped\",\"name\":\"Require native vector adapter with compatible macOS SQLite\",\"number\":10,\"startedAt\":\"2026-10-08T01:08:51Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:51Z\",\"conclusion\":\"skipped\",\"name\":\"Build and verify Claude plugin ZIP\",\"number\":11,\"startedAt\":\"2026-10-08T01:08:51Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:51Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-python@v7\",\"number\":20,\"startedAt\":\"2026-10-08T01:08:51Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:51Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-node@v7\",\"number\":21,\"startedAt\":\"2026-10-08T01:08:51Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:52Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/checkout@v6\",\"number\":22,\"startedAt\":\"2026-10-08T01:08:51Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:52Z\",\"conclusion\":\"success\",\"name\":\"Complete job\",\"number\":23,\"startedAt\":\"2026-10-08T01:08:52Z\",\"status\":\"completed\"}],\"url\":\"https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37711387112/job/113097897657\"},{\"completedAt\":\"2026-10-08T01:10:16Z\",\"conclusion\":\"success\",\"databaseId\":113097897658,\"name\":\"test (windows-latest, 3.13)\",\"startedAt\":\"2026-10-08T01:08:23Z\",\"status\":\"completed\",\"steps\":[{\"completedAt\":\"2026-10-08T01:08:25Z\",\"conclusion\":\"success\",\"name\":\"Set up job\",\"number\":1,\"startedAt\":\"2026-10-08T01:08:24Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:31Z\",\"conclusion\":\"success\",\"name\":\"Run actions/checkout@v6\",\"number\":2,\"startedAt\":\"2026-10-08T01:08:25Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:38Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-node@v7\",\"number\":3,\"startedAt\":\"2026-10-08T01:08:31Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:38Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-python@v7\",\"number\":4,\"startedAt\":\"2026-10-08T01:08:38Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:44Z\",\"conclusion\":\"success\",\"name\":\"Run npm ci\",\"number\":5,\"startedAt\":\"2026-10-08T01:08:38Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:54Z\",\"conclusion\":\"success\",\"name\":\"Run npm test\",\"number\":6,\"startedAt\":\"2026-10-08T01:08:44Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:16Z\",\"conclusion\":\"success\",\"name\":\"Install local map dependencies\",\"number\":7,\"startedAt\":\"2026-10-08T01:08:54Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:09:16Z\",\"conclusion\":\"skipped\",\"name\":\"Install optional vector adapter on each platform\",\"number\":8,\"startedAt\":\"2026-10-08T01:09:16Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:13Z\",\"conclusion\":\"success\",\"name\":\"Test local mapping and retrieval\",\"number\":9,\"startedAt\":\"2026-10-08T01:09:16Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:13Z\",\"conclusion\":\"skipped\",\"name\":\"Require native vector adapter with compatible macOS SQLite\",\"number\":10,\"startedAt\":\"2026-10-08T01:10:13Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:13Z\",\"conclusion\":\"skipped\",\"name\":\"Build and verify Claude plugin ZIP\",\"number\":11,\"startedAt\":\"2026-10-08T01:10:13Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:13Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-python@v7\",\"number\":20,\"startedAt\":\"2026-10-08T01:10:13Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:13Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-node@v7\",\"number\":21,\"startedAt\":\"2026-10-08T01:10:13Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:15Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/checkout@v6\",\"number\":22,\"startedAt\":\"2026-10-08T01:10:13Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:10:15Z\",\"conclusion\":\"success\",\"name\":\"Complete job\",\"number\":23,\"startedAt\":\"2026-10-08T01:10:15Z\",\"status\":\"completed\"}],\"url\":\"https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37711387112/job/113097897658\"},{\"completedAt\":\"2026-10-08T01:17:41Z\",\"conclusion\":\"success\",\"databaseId\":113097897731,\"name\":\"test (macos-latest, 3.12)\",\"startedAt\":\"2026-10-08T01:08:32Z\",\"status\":\"completed\",\"steps\":[{\"completedAt\":\"2026-10-08T01:08:35Z\",\"conclusion\":\"success\",\"name\":\"Set up job\",\"number\":1,\"startedAt\":\"2026-10-08T01:08:33Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:38Z\",\"conclusion\":\"success\",\"name\":\"Run actions/checkout@v6\",\"number\":2,\"startedAt\":\"2026-10-08T01:08:35Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:41Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-node@v7\",\"number\":3,\"startedAt\":\"2026-10-08T01:08:38Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:41Z\",\"conclusion\":\"success\",\"name\":\"Run actions/setup-python@v7\",\"number\":4,\"startedAt\":\"2026-10-08T01:08:41Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:43Z\",\"conclusion\":\"success\",\"name\":\"Run npm ci\",\"number\":5,\"startedAt\":\"2026-10-08T01:08:41Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:47Z\",\"conclusion\":\"success\",\"name\":\"Run npm test\",\"number\":6,\"startedAt\":\"2026-10-08T01:08:43Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:52Z\",\"conclusion\":\"success\",\"name\":\"Install local map dependencies\",\"number\":7,\"startedAt\":\"2026-10-08T01:08:47Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:08:54Z\",\"conclusion\":\"success\",\"name\":\"Install optional vector adapter on each platform\",\"number\":8,\"startedAt\":\"2026-10-08T01:08:52Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:13:29Z\",\"conclusion\":\"success\",\"name\":\"Test local mapping and retrieval\",\"number\":9,\"startedAt\":\"2026-10-08T01:08:54Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:17:35Z\",\"conclusion\":\"success\",\"name\":\"Require native vector adapter with compatible macOS SQLite\",\"number\":10,\"startedAt\":\"2026-10-08T01:13:29Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:17:35Z\",\"conclusion\":\"skipped\",\"name\":\"Build and verify Claude plugin ZIP\",\"number\":11,\"startedAt\":\"2026-10-08T01:17:35Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:17:36Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-python@v7\",\"number\":20,\"startedAt\":\"2026-10-08T01:17:35Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:17:36Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/setup-node@v7\",\"number\":21,\"startedAt\":\"2026-10-08T01:17:36Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:17:37Z\",\"conclusion\":\"success\",\"name\":\"Post Run actions/checkout@v6\",\"number\":22,\"startedAt\":\"2026-10-08T01:17:36Z\",\"status\":\"completed\"},{\"completedAt\":\"2026-10-08T01:17:39Z\",\"conclusion\":\"success\",\"name\":\"Complete job\",\"number\":23,\"startedAt\":\"2026-10-08T01:17:37Z\",\"status\":\"completed\"}],\"url\":\"https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37711387112/job/113097897731\"}],\"status\":\"completed\",\"url\":\"https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37711387112\"}\n",
      "stderr": ""
    },
    {
      "label": "download-index-artifact",
      "command": [
        "gh",
        "run",
        "download",
        "37711387112",
        "--repo",
        "EdukeyTeam/agent-toolbox",
        "--name",
        "legacy-tools-windows-latest",
        "--dir",
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\index-artifact"
      ],
      "elapsed_seconds": 3.2796773000154644,
      "exit": 0,
      "stdout": "",
      "stderr": ""
    },
    {
      "label": "install-from-ci",
      "command": [
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\python-env\\Scripts\\python.exe",
        "\\\\wsl.localhost\\Ubuntu-26.04\\home\\lucas\\DEV\\Projects\\agent-toolbox\\skills\\legacy-codebase-workflows\\scripts\\setup_native.py",
        "install",
        "--from-ci",
        "37711387112",
        "--expected-source",
        "d0181792fba3026c20f5b4fbc1595f7d38abc688",
        "--cache-dir",
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\cache"
      ],
      "elapsed_seconds": 6.798513600137085,
      "exit": 0,
      "stdout": "{\"cache_directory\": \"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-final-37711387112\\\\cache\\\\native\\\\0.2.0\\\\windows-x86_64\", \"consumer_verified\": false, \"platform\": \"windows-x86_64\", \"program\": \"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-final-37711387112\\\\cache\\\\native\\\\0.2.0\\\\windows-x86_64\\\\package\\\\legacy-repo-map.exe\", \"publication\": \"pending-first-release\", \"release_tag\": \"legacy-tools-v0.2.0\", \"setup_command\": [\"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\python-env\\\\Scripts\\\\python.exe\", \"\\\\\\\\wsl.localhost\\\\Ubuntu-26.04\\\\home\\\\lucas\\\\DEV\\\\Projects\\\\agent-toolbox\\\\skills\\\\legacy-codebase-workflows\\\\scripts\\\\setup_native.py\", \"install\", \"--cache-dir\", \"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-final-37711387112\\\\cache\"], \"source_commit\": \"d0181792fba3026c20f5b4fbc1595f7d38abc688\", \"source_dirty\": false, \"source_kind\": \"ci\", \"state\": \"ready\", \"version\": \"0.2.0\"}\n",
      "stderr": ""
    },
    {
      "label": "status-revalidation",
      "command": [
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\python-env\\Scripts\\python.exe",
        "\\\\wsl.localhost\\Ubuntu-26.04\\home\\lucas\\DEV\\Projects\\agent-toolbox\\skills\\legacy-codebase-workflows\\scripts\\setup_native.py",
        "status",
        "--cache-dir",
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\cache"
      ],
      "elapsed_seconds": 0.7125233998522162,
      "exit": 0,
      "stdout": "{\"cache_directory\": \"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-final-37711387112\\\\cache\\\\native\\\\0.2.0\\\\windows-x86_64\", \"consumer_verified\": false, \"platform\": \"windows-x86_64\", \"program\": \"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-final-37711387112\\\\cache\\\\native\\\\0.2.0\\\\windows-x86_64\\\\package\\\\legacy-repo-map.exe\", \"publication\": \"pending-first-release\", \"release_tag\": \"legacy-tools-v0.2.0\", \"setup_command\": [\"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\python-env\\\\Scripts\\\\python.exe\", \"\\\\\\\\wsl.localhost\\\\Ubuntu-26.04\\\\home\\\\lucas\\\\DEV\\\\Projects\\\\agent-toolbox\\\\skills\\\\legacy-codebase-workflows\\\\scripts\\\\setup_native.py\", \"install\", \"--cache-dir\", \"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-final-37711387112\\\\cache\"], \"source_commit\": \"d0181792fba3026c20f5b4fbc1595f7d38abc688\", \"source_dirty\": false, \"source_kind\": \"ci\", \"state\": \"ready\", \"version\": \"0.2.0\"}\n",
      "stderr": ""
    },
    {
      "label": "authenticode-current-host",
      "command": [
        "C:\\Program Files\\PowerShell\\7\\pwsh.exe",
        "-NoProfile",
        "-Command",
        "Get-AuthenticodeSignature -LiteralPath 'C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\cache\\native\\0.2.0\\windows-x86_64\\package\\legacy-repo-map.exe' | ForEach-Object { [PSCustomObject]@{Status=$_.Status.ToString();SignerPresent=($null -ne $_.SignerCertificate);StatusMessage=$_.StatusMessage} } | ConvertTo-Json"
      ],
      "elapsed_seconds": 0.6881741001270711,
      "exit": 0,
      "stdout": "{\n  \"Status\": \"NotSigned\",\n  \"SignerPresent\": false,\n  \"StatusMessage\": \"The file C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-final-37711387112\\\\cache\\\\native\\\\0.2.0\\\\windows-x86_64\\\\package\\\\legacy-repo-map.exe is not digitally signed. You cannot run this script on the current system. For more information about running scripts and setting execution policy, see about_Execution_Policies at https://go.microsoft.com/fwlink/?LinkID=135170\"\n}\n",
      "stderr": ""
    },
    {
      "label": "native-version",
      "command": [
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\cache\\native\\0.2.0\\windows-x86_64\\package\\legacy-repo-map.exe",
        "--version"
      ],
      "elapsed_seconds": 0.01451819995418191,
      "exit": 0,
      "stdout": "legacy-repo-map 0.2.0 (experimental)\n",
      "stderr": ""
    },
    {
      "label": "native-class-multiline-smoke",
      "command": [
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\cache\\native\\0.2.0\\windows-x86_64\\package\\legacy-repo-map.exe",
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\smoke-source",
        "--output-dir",
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\smoke-output",
        "--all-definitions",
        "--budget",
        "512"
      ],
      "elapsed_seconds": 0.07426969986408949,
      "exit": 0,
      "stdout": "{\"coverage\":{\"candidates_seen\":1,\"definitions_found\":4,\"definitions_in_map\":4,\"definitions_omitted\":0,\"files_with_definitions\":1,\"parsed_files\":1,\"selected_files\":1},\"estimated_tokens\":84,\"inventory_summary\":{\"languages\":{\"java\":1},\"modules\":[{\"files\":1,\"path\":\"<root>\"}],\"modules_omitted\":0},\"map\":\"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-final-37711387112\\\\smoke-output\\\\repo-map.md\",\"metadata\":\"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-final-37711387112\\\\smoke-output\\\\map.meta.json\",\"status\":\"complete\",\"truncated\":false}\n",
      "stderr": ""
    },
    {
      "label": "jftp-revision-before",
      "command": [
        "git",
        "-C",
        "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp",
        "rev-parse",
        "HEAD"
      ],
      "elapsed_seconds": 0.045071500120684505,
      "exit": 0,
      "stdout": "990545cc101a3bab96d8a2e3c5d3b926d0638c26\n",
      "stderr": ""
    },
    {
      "label": "generate-overview",
      "command": [
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\cache\\native\\0.2.0\\windows-x86_64\\package\\legacy-repo-map.exe",
        "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp",
        "--subtree",
        "src/main/java",
        "--output-dir",
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\staging-overview",
        "--budget",
        "16384"
      ],
      "elapsed_seconds": 0.7415352000389248,
      "exit": 0,
      "stdout": "{\"coverage\":{\"candidates_seen\":196,\"definitions_found\":1586,\"definitions_in_map\":869,\"definitions_omitted\":717,\"files_with_definitions\":179,\"parsed_files\":182,\"selected_files\":196},\"estimated_tokens\":16384,\"inventory_summary\":{\"languages\":{\"java\":182,\"other\":14},\"modules\":[{\"files\":196,\"path\":\"src/main\"}],\"modules_omitted\":0},\"map\":\"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-final-37711387112\\\\staging-overview\\\\repo-map.md\",\"metadata\":\"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-final-37711387112\\\\staging-overview\\\\map.meta.json\",\"status\":\"complete\",\"truncated\":true}\n",
      "stderr": ""
    },
    {
      "label": "generate-full",
      "command": [
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\cache\\native\\0.2.0\\windows-x86_64\\package\\legacy-repo-map.exe",
        "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp",
        "--subtree",
        "src/main/java",
        "--output-dir",
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\staging-full",
        "--budget",
        "65536",
        "--all-definitions"
      ],
      "elapsed_seconds": 0.6994857001118362,
      "exit": 0,
      "stdout": "{\"coverage\":{\"candidates_seen\":196,\"definitions_found\":1586,\"definitions_in_map\":1586,\"definitions_omitted\":0,\"files_with_definitions\":179,\"parsed_files\":182,\"selected_files\":196},\"estimated_tokens\":27213,\"inventory_summary\":{\"languages\":{\"java\":182,\"other\":14},\"modules\":[{\"files\":196,\"path\":\"src/main\"}],\"modules_omitted\":0},\"map\":\"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-final-37711387112\\\\staging-full\\\\repo-map.md\",\"metadata\":\"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-final-37711387112\\\\staging-full\\\\map.meta.json\",\"status\":\"complete\",\"truncated\":false}\n",
      "stderr": ""
    },
    {
      "label": "jftp-revision-after",
      "command": [
        "git",
        "-C",
        "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp",
        "rev-parse",
        "HEAD"
      ],
      "elapsed_seconds": 0.04065189999528229,
      "exit": 0,
      "stdout": "990545cc101a3bab96d8a2e3c5d3b926d0638c26\n",
      "stderr": ""
    },
    {
      "label": "export-overview",
      "command": [
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\python-env\\Scripts\\python.exe",
        "\\\\wsl.localhost\\Ubuntu-26.04\\home\\lucas\\DEV\\Projects\\agent-toolbox\\skills\\legacy-codebase-workflows\\scripts\\export_repo_map.py",
        "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp",
        "--artifact-dir",
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\staging-overview",
        "--implementation",
        "rust",
        "--output-file",
        "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp\\docs\\repo-maps\\jftp-java.rust.md",
        "--evidence-dir",
        "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp\\docs\\repo-maps\\artifacts\\2026-10-08\\windows-final\\overview",
        "--elapsed-seconds",
        "0.7415352000389248",
        "--force"
      ],
      "elapsed_seconds": 0.34024800010956824,
      "exit": 0,
      "stdout": "{\"inventory\": \"C:\\\\Users\\\\BiuroEdukey\\\\.codex\\\\worktrees\\\\05bd\\\\jftp\\\\docs\\\\repo-maps\\\\artifacts\\\\2026-10-08\\\\windows-final\\\\overview\\\\jftp-java.rust.inventory.json\", \"metadata\": \"C:\\\\Users\\\\BiuroEdukey\\\\.codex\\\\worktrees\\\\05bd\\\\jftp\\\\docs\\\\repo-maps\\\\artifacts\\\\2026-10-08\\\\windows-final\\\\overview\\\\jftp-java.rust.meta.json\", \"raw\": \"C:\\\\Users\\\\BiuroEdukey\\\\.codex\\\\worktrees\\\\05bd\\\\jftp\\\\docs\\\\repo-maps\\\\artifacts\\\\2026-10-08\\\\windows-final\\\\overview\\\\jftp-java.rust.raw.md\", \"report\": \"C:\\\\Users\\\\BiuroEdukey\\\\.codex\\\\worktrees\\\\05bd\\\\jftp\\\\docs\\\\repo-maps\\\\jftp-java.rust.md\"}\n",
      "stderr": ""
    },
    {
      "label": "export-full",
      "command": [
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\python-env\\Scripts\\python.exe",
        "\\\\wsl.localhost\\Ubuntu-26.04\\home\\lucas\\DEV\\Projects\\agent-toolbox\\skills\\legacy-codebase-workflows\\scripts\\export_repo_map.py",
        "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp",
        "--artifact-dir",
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\staging-full",
        "--implementation",
        "rust",
        "--output-file",
        "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp\\docs\\repo-maps\\jftp-java.full.rust.md",
        "--evidence-dir",
        "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp\\docs\\repo-maps\\artifacts\\2026-10-08\\windows-final\\full",
        "--elapsed-seconds",
        "0.6994857001118362",
        "--force"
      ],
      "elapsed_seconds": 0.3510971001815051,
      "exit": 0,
      "stdout": "{\"inventory\": \"C:\\\\Users\\\\BiuroEdukey\\\\.codex\\\\worktrees\\\\05bd\\\\jftp\\\\docs\\\\repo-maps\\\\artifacts\\\\2026-10-08\\\\windows-final\\\\full\\\\jftp-java.full.rust.inventory.json\", \"metadata\": \"C:\\\\Users\\\\BiuroEdukey\\\\.codex\\\\worktrees\\\\05bd\\\\jftp\\\\docs\\\\repo-maps\\\\artifacts\\\\2026-10-08\\\\windows-final\\\\full\\\\jftp-java.full.rust.meta.json\", \"raw\": \"C:\\\\Users\\\\BiuroEdukey\\\\.codex\\\\worktrees\\\\05bd\\\\jftp\\\\docs\\\\repo-maps\\\\artifacts\\\\2026-10-08\\\\windows-final\\\\full\\\\jftp-java.full.rust.raw.md\", \"report\": \"C:\\\\Users\\\\BiuroEdukey\\\\.codex\\\\worktrees\\\\05bd\\\\jftp\\\\docs\\\\repo-maps\\\\jftp-java.full.rust.md\"}\n",
      "stderr": ""
    }
  ],
  "phase": "complete",
  "ci": {
    "headSha": "03a538c5db5ddcbbf7bc4377d380106343bf9177",
    "status": "completed",
    "conclusion": "success",
    "url": "https://github.com/EdukeyTeam/agent-toolbox/actions/runs/37711387112",
    "jobs": [
      {
        "name": "workflow-validation",
        "conclusion": "success"
      },
      {
        "name": "semantic-retrieval (ubuntu-latest)",
        "conclusion": "success"
      },
      {
        "name": "native-artifacts (ubuntu-latest)",
        "conclusion": "success"
      },
      {
        "name": "semantic-retrieval (windows-latest)",
        "conclusion": "success"
      },
      {
        "name": "native-artifacts (windows-latest)",
        "conclusion": "success"
      },
      {
        "name": "test (windows-latest, 3.12)",
        "conclusion": "success"
      },
      {
        "name": "test (ubuntu-latest, 3.13)",
        "conclusion": "success"
      },
      {
        "name": "test (macos-latest, 3.13)",
        "conclusion": "success"
      },
      {
        "name": "test (windows-latest, 3.14)",
        "conclusion": "success"
      },
      {
        "name": "native-artifacts (macos-latest)",
        "conclusion": "success"
      },
      {
        "name": "test (macos-latest, 3.14)",
        "conclusion": "success"
      },
      {
        "name": "test (ubuntu-latest, 3.12)",
        "conclusion": "success"
      },
      {
        "name": "test (ubuntu-latest, 3.14)",
        "conclusion": "success"
      },
      {
        "name": "test (windows-latest, 3.13)",
        "conclusion": "success"
      },
      {
        "name": "test (macos-latest, 3.12)",
        "conclusion": "success"
      }
    ]
  },
  "archives": {
    "overview": {
      "report": "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp\\docs\\repo-maps\\artifacts\\2026-10-08\\jftp-java.wsl-benchmark.rust.md",
      "raw": "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp\\docs\\repo-maps\\artifacts\\2026-10-08\\sidecars\\jftp-java.wsl-benchmark.rust\\jftp-java.wsl-benchmark.rust.raw.md",
      "metadata": "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp\\docs\\repo-maps\\artifacts\\2026-10-08\\sidecars\\jftp-java.wsl-benchmark.rust\\jftp-java.wsl-benchmark.rust.meta.json",
      "raw_sha256": "09ea057a8cee9ef85cfbf3c5fea66ca604039e750fa983b7fb7fd7080f788ba9",
      "original_elapsed_seconds": 17.239781256997958,
      "revision": null,
      "fingerprint": "c981ce97fec27912208abd6d6d92bce8838933b21d300f3e4290c261cff3bd2d"
    },
    "full": {
      "report": "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp\\docs\\repo-maps\\artifacts\\2026-10-08\\jftp-java.full.wsl-benchmark.rust.md",
      "raw": "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp\\docs\\repo-maps\\artifacts\\2026-10-08\\sidecars\\jftp-java.full.wsl-benchmark.rust\\jftp-java.full.wsl-benchmark.rust.raw.md",
      "metadata": "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp\\docs\\repo-maps\\artifacts\\2026-10-08\\sidecars\\jftp-java.full.wsl-benchmark.rust\\jftp-java.full.wsl-benchmark.rust.meta.json",
      "raw_sha256": "eef199e8d18b7cceddd706220a1ab4acf9696cfff991d2ba0afb2cde209bcd74",
      "original_elapsed_seconds": 20.08179550198838,
      "revision": null,
      "fingerprint": "c981ce97fec27912208abd6d6d92bce8838933b21d300f3e4290c261cff3bd2d"
    }
  },
  "build_source_commit": "d0181792fba3026c20f5b4fbc1595f7d38abc688",
  "status": {
    "cache_directory": "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\cache\\native\\0.2.0\\windows-x86_64",
    "consumer_verified": false,
    "platform": "windows-x86_64",
    "program": "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\cache\\native\\0.2.0\\windows-x86_64\\package\\legacy-repo-map.exe",
    "publication": "pending-first-release",
    "release_tag": "legacy-tools-v0.2.0",
    "setup_command": [
      "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\python-env\\Scripts\\python.exe",
      "\\\\wsl.localhost\\Ubuntu-26.04\\home\\lucas\\DEV\\Projects\\agent-toolbox\\skills\\legacy-codebase-workflows\\scripts\\setup_native.py",
      "install",
      "--cache-dir",
      "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\cache"
    ],
    "source_commit": "d0181792fba3026c20f5b4fbc1595f7d38abc688",
    "source_dirty": false,
    "source_kind": "ci",
    "state": "ready",
    "version": "0.2.0"
  },
  "authenticode": {
    "Status": "NotSigned",
    "SignerPresent": false,
    "StatusMessage": "The file C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\cache\\native\\0.2.0\\windows-x86_64\\package\\legacy-repo-map.exe is not digitally signed. You cannot run this script on the current system. For more information about running scripts and setting execution policy, see about_Execution_Policies at https://go.microsoft.com/fwlink/?LinkID=135170"
  },
  "receipt": {
    "source_commit": "d0181792fba3026c20f5b4fbc1595f7d38abc688",
    "run_head_commit": "03a538c5db5ddcbbf7bc4377d380106343bf9177",
    "run_id": "37711387112",
    "source_kind": "ci",
    "files_verified": 89,
    "binary_sha256": "96b9a780921e977fe1cb399c04b20f1682bf64d1253835d0ae292b6abf8fd085",
    "archive_sha256": "e59fe8cbcd98172198e1c3176a96d90a2f5dc939e7618b8f218e31ea62b33d21"
  },
  "smoke": {
    "coverage": {
      "candidates_seen": 1,
      "definitions_found": 4,
      "definitions_in_map": 4,
      "definitions_omitted": 0,
      "files_with_definitions": 1,
      "parsed_files": 1,
      "selected_files": 1
    },
    "rendering": {
      "clipped_declarations": [],
      "declaration_character_limit": 8000,
      "declaration_line_limit": 80,
      "format": "grouped"
    },
    "map_sha256": "3798cb15f93b44e89891fb492c58c1c77552759de3529f76beaac73efb593a36",
    "complete_multiline_and_owners": true,
    "bodies_excluded": true
  },
  "generated": {
    "overview": {
      "staging": "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\staging-overview",
      "elapsed_seconds": 0.7415352000389248,
      "budget": 16384,
      "revision": "990545cc101a3bab96d8a2e3c5d3b926d0638c26",
      "fingerprint": "101dbfcc1c7aeff75e2680eb1c734b205a263bd72c8ccdd2b1a0aa27a662dd4d",
      "coverage": {
        "candidates_seen": 196,
        "definitions_found": 1586,
        "definitions_in_map": 869,
        "definitions_omitted": 717,
        "files_with_definitions": 179,
        "parsed_files": 182,
        "selected_files": 196
      },
      "rendering": {
        "clipped_declarations": [],
        "declaration_character_limit": 8000,
        "declaration_line_limit": 80,
        "format": "grouped"
      },
      "truncated": true,
      "raw_sha256": "09ea057a8cee9ef85cfbf3c5fea66ca604039e750fa983b7fb7fd7080f788ba9",
      "same_raw_bytes_as_wsl_benchmark": true,
      "archived_wsl_raw_sha256": "09ea057a8cee9ef85cfbf3c5fea66ca604039e750fa983b7fb7fd7080f788ba9",
      "original_wsl_elapsed_seconds": 17.239781256997958,
      "report": "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp\\docs\\repo-maps\\jftp-java.rust.md",
      "evidence_dir": "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp\\docs\\repo-maps\\artifacts\\2026-10-08\\windows-final\\overview",
      "report_sha256": "cbe7c9ccf0c1638c296df2f0e0e80c852f7585f15e4b93d1b2046c6595915816"
    },
    "full": {
      "staging": "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-final-37711387112\\staging-full",
      "elapsed_seconds": 0.6994857001118362,
      "budget": 65536,
      "revision": "990545cc101a3bab96d8a2e3c5d3b926d0638c26",
      "fingerprint": "101dbfcc1c7aeff75e2680eb1c734b205a263bd72c8ccdd2b1a0aa27a662dd4d",
      "coverage": {
        "candidates_seen": 196,
        "definitions_found": 1586,
        "definitions_in_map": 1586,
        "definitions_omitted": 0,
        "files_with_definitions": 179,
        "parsed_files": 182,
        "selected_files": 196
      },
      "rendering": {
        "clipped_declarations": [],
        "declaration_character_limit": 8000,
        "declaration_line_limit": 80,
        "format": "grouped"
      },
      "truncated": false,
      "raw_sha256": "eef199e8d18b7cceddd706220a1ab4acf9696cfff991d2ba0afb2cde209bcd74",
      "same_raw_bytes_as_wsl_benchmark": true,
      "archived_wsl_raw_sha256": "eef199e8d18b7cceddd706220a1ab4acf9696cfff991d2ba0afb2cde209bcd74",
      "original_wsl_elapsed_seconds": 20.08179550198838,
      "report": "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp\\docs\\repo-maps\\jftp-java.full.rust.md",
      "evidence_dir": "C:\\Users\\BiuroEdukey\\.codex\\worktrees\\05bd\\jftp\\docs\\repo-maps\\artifacts\\2026-10-08\\windows-final\\full",
      "report_sha256": "3a628ffc023a312b9a6cb580943b06ba9a6628e4ad802735ccff9c08b79d7cf4"
    }
  },
  "success": true
}
```
