# Windows native CI consumer check

Successful verification of CI run 37704966686's pre-review package. The source installer downloaded and verified the Windows artifact into an isolated cache; status returned ready. All 89 packaged file hashes matched. The unsigned EXE ran version and grouped/all-definition commands without unblocking files, clearing origin metadata, changing execution policy or disabling security checks.

Build source (read from actual index): d8cb3924609dd82aff9a65735428035931eeeb17. Authenticated CI run head: 3df435987fe7da0bf9c4407b43a4ef35ad962ad1. Native 0.2.0; reference repo_map.py 1.1.0; clean source.

Legacy powershell.exe failed to autoload Microsoft.PowerShell.Security during the first signature inspection. Install/status had already succeeded. Current PowerShell 7 independently reported NotSigned and no signer; its generic StatusMessage mentions scripts but is not an EXE execution result. Subsequent native execution succeeded. The helper failure remains in logs/results. A final report-formatting shell command had a quoting ParserError before execution; retried via Python without changing verified results.

This proves execution on this permitted host through this CI download path, not browser-download SmartScreen reputation or other consumer policies. Repeat with the final matching package after pending renderer fixes.

```json
{
  "phase": "pre-review CI package verification",
  "run_id": "37704966686",
  "build_source_commit": "d8cb3924609dd82aff9a65735428035931eeeb17",
  "run_head_commit": "3df435987fe7da0bf9c4407b43a4ef35ad962ad1",
  "native_version": "0.2.0",
  "source_contract": "repo_map.py 1.1.0",
  "source_dirty": false,
  "commands": [
    {
      "label": "install-from-ci",
      "command": [
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\python-env\\Scripts\\python.exe",
        "\\\\wsl.localhost\\Ubuntu-26.04\\home\\lucas\\DEV\\Projects\\agent-toolbox\\skills\\legacy-codebase-workflows\\scripts\\setup_native.py",
        "install",
        "--from-ci",
        "37704966686",
        "--expected-source",
        "d8cb3924609dd82aff9a65735428035931eeeb17",
        "--cache-dir",
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-37704966686\\cache"
      ],
      "elapsed_seconds": 6.924645899794996,
      "exit": 0,
      "stdout": "{\"cache_directory\": \"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-37704966686\\\\cache\\\\native\\\\0.2.0\\\\windows-x86_64\", \"consumer_verified\": false, \"platform\": \"windows-x86_64\", \"program\": \"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-37704966686\\\\cache\\\\native\\\\0.2.0\\\\windows-x86_64\\\\package\\\\legacy-repo-map.exe\", \"publication\": \"pending-first-release\", \"release_tag\": \"legacy-tools-v0.2.0\", \"setup_command\": [\"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\python-env\\\\Scripts\\\\python.exe\", \"\\\\\\\\wsl.localhost\\\\Ubuntu-26.04\\\\home\\\\lucas\\\\DEV\\\\Projects\\\\agent-toolbox\\\\skills\\\\legacy-codebase-workflows\\\\scripts\\\\setup_native.py\", \"install\", \"--cache-dir\", \"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-37704966686\\\\cache\"], \"source_commit\": \"d8cb3924609dd82aff9a65735428035931eeeb17\", \"source_dirty\": false, \"source_kind\": \"ci\", \"state\": \"ready\", \"version\": \"0.2.0\"}\n",
      "stderr": ""
    },
    {
      "label": "status-revalidation",
      "command": [
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\python-env\\Scripts\\python.exe",
        "\\\\wsl.localhost\\Ubuntu-26.04\\home\\lucas\\DEV\\Projects\\agent-toolbox\\skills\\legacy-codebase-workflows\\scripts\\setup_native.py",
        "status",
        "--cache-dir",
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-37704966686\\cache"
      ],
      "elapsed_seconds": 0.7449244998861104,
      "exit": 0,
      "stdout": "{\"cache_directory\": \"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-37704966686\\\\cache\\\\native\\\\0.2.0\\\\windows-x86_64\", \"consumer_verified\": false, \"platform\": \"windows-x86_64\", \"program\": \"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-37704966686\\\\cache\\\\native\\\\0.2.0\\\\windows-x86_64\\\\package\\\\legacy-repo-map.exe\", \"publication\": \"pending-first-release\", \"release_tag\": \"legacy-tools-v0.2.0\", \"setup_command\": [\"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\python-env\\\\Scripts\\\\python.exe\", \"\\\\\\\\wsl.localhost\\\\Ubuntu-26.04\\\\home\\\\lucas\\\\DEV\\\\Projects\\\\agent-toolbox\\\\skills\\\\legacy-codebase-workflows\\\\scripts\\\\setup_native.py\", \"install\", \"--cache-dir\", \"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-37704966686\\\\cache\"], \"source_commit\": \"d8cb3924609dd82aff9a65735428035931eeeb17\", \"source_dirty\": false, \"source_kind\": \"ci\", \"state\": \"ready\", \"version\": \"0.2.0\"}\n",
      "stderr": ""
    },
    {
      "label": "authenticode-check",
      "command": [
        "powershell",
        "-NoProfile",
        "-Command",
        "Get-AuthenticodeSignature -LiteralPath 'C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-37704966686\\cache\\native\\0.2.0\\windows-x86_64\\package\\legacy-repo-map.exe' | Select-Object Status,StatusMessage | ConvertTo-Json"
      ],
      "elapsed_seconds": 0.5343612001743168,
      "exit": 1,
      "stdout": "",
      "stderr": "Get-AuthenticodeSignature : The 'Get-AuthenticodeSignature' command was found in the module \n'Microsoft.PowerShell.Security', but the module could not be loaded. For more information, run 'Import-Module \nMicrosoft.PowerShell.Security'.\nAt line:1 char:1\n+ Get-AuthenticodeSignature -LiteralPath 'C:\\Users\\BiuroEdukey\\AppData\\ ...\n+ ~~~~~~~~~~~~~~~~~~~~~~~~~\n    + CategoryInfo          : ObjectNotFound: (Get-AuthenticodeSignature:String) [], CommandNotFoundException\n    + FullyQualifiedErrorId : CouldNotAutoloadMatchingModule\n \n"
    },
    {
      "label": "native-version",
      "command": [
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-37704966686\\cache\\native\\0.2.0\\windows-x86_64\\package\\legacy-repo-map.exe",
        "--version"
      ],
      "elapsed_seconds": 0.01673650019802153,
      "exit": 0,
      "stdout": "legacy-repo-map 0.2.0 (experimental)\n",
      "stderr": ""
    },
    {
      "label": "native-grouped-map",
      "command": [
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-37704966686\\cache\\native\\0.2.0\\windows-x86_64\\package\\legacy-repo-map.exe",
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-37704966686\\grouped-smoke-source",
        "--output-dir",
        "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-37704966686\\grouped-smoke-output",
        "--format",
        "grouped",
        "--all-definitions",
        "--budget",
        "256"
      ],
      "elapsed_seconds": 0.08274980005808175,
      "exit": 0,
      "stdout": "{\"coverage\":{\"candidates_seen\":1,\"definitions_found\":2,\"definitions_in_map\":2,\"definitions_omitted\":0,\"files_with_definitions\":1,\"parsed_files\":1,\"selected_files\":1},\"estimated_tokens\":57,\"inventory_summary\":{\"languages\":{\"java\":1},\"modules\":[{\"files\":1,\"path\":\"<root>\"}],\"modules_omitted\":0},\"map\":\"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-37704966686\\\\grouped-smoke-output\\\\repo-map.md\",\"metadata\":\"C:\\\\Users\\\\BiuroEdukey\\\\AppData\\\\Local\\\\Temp\\\\legacy-skill-review-20261007-05bd\\\\native-consumer-windows\\\\run-37704966686\\\\grouped-smoke-output\\\\map.meta.json\",\"status\":\"complete\",\"truncated\":false}\n",
      "stderr": ""
    }
  ],
  "status": {
    "cache_directory": "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-37704966686\\cache\\native\\0.2.0\\windows-x86_64",
    "consumer_verified": false,
    "platform": "windows-x86_64",
    "program": "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-37704966686\\cache\\native\\0.2.0\\windows-x86_64\\package\\legacy-repo-map.exe",
    "publication": "pending-first-release",
    "release_tag": "legacy-tools-v0.2.0",
    "setup_command": [
      "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\python-env\\Scripts\\python.exe",
      "\\\\wsl.localhost\\Ubuntu-26.04\\home\\lucas\\DEV\\Projects\\agent-toolbox\\skills\\legacy-codebase-workflows\\scripts\\setup_native.py",
      "install",
      "--cache-dir",
      "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-37704966686\\cache"
    ],
    "source_commit": "d8cb3924609dd82aff9a65735428035931eeeb17",
    "source_dirty": false,
    "source_kind": "ci",
    "state": "ready",
    "version": "0.2.0"
  },
  "success": true,
  "signature_helper_error": "Traceback (most recent call last):\n  File \"C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-37704966686\\verify-windows-consumer.py\", line 20, in <module>\n    signature=json.loads(run('authenticode-check',['powershell','-NoProfile','-Command',\"Get-AuthenticodeSignature -LiteralPath '\"+str(program).replace(\"'\",\"''\")+\"' | Select-Object Status,StatusMessage | ConvertTo-Json\"]).stdout)\n                         ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-37704966686\\verify-windows-consumer.py\", line 13, in run\n    if p.returncode: raise RuntimeError(f'{label} failed exit{p.returncode}: {p.stderr or p.stdout}')\n                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nRuntimeError: authenticode-check failed exit1: Get-AuthenticodeSignature : The 'Get-AuthenticodeSignature' command was found in the module \n'Microsoft.PowerShell.Security', but the module could not be loaded. For more information, run 'Import-Module \nMicrosoft.PowerShell.Security'.\nAt line:1 char:1\n+ Get-AuthenticodeSignature -LiteralPath 'C:\\Users\\BiuroEdukey\\AppData\\ ...\n+ ~~~~~~~~~~~~~~~~~~~~~~~~~\n    + CategoryInfo          : ObjectNotFound: (Get-AuthenticodeSignature:String) [], CommandNotFoundException\n    + FullyQualifiedErrorId : CouldNotAutoloadMatchingModule\n \n\n",
  "authenticode": {
    "status": "NotSigned",
    "status_message": "The file C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-37704966686\\cache\\native\\0.2.0\\windows-x86_64\\package\\legacy-repo-map.exe is not digitally signed. You cannot run this script on the current system. For more information about running scripts and setting execution policy, see about_Execution_Policies at https://go.microsoft.com/fwlink/?LinkID=135170",
    "signer_present": false,
    "powershell_host": "C:\\Program Files\\PowerShell\\7\\pwsh.exe"
  },
  "receipt_hashes": {
    "files_checked": 89,
    "all_match": true,
    "binary_sha256": "74d05ee1297b7c8ec87c6565d54f814f4645c7a382eacb75887606107d530694",
    "archive_sha256": "45a111e7c11f04444c31f6b982a91f6b560a99ac351fab996c28784660925de8"
  },
  "receipt_provenance": {
    "source_commit": "d8cb3924609dd82aff9a65735428035931eeeb17",
    "ci_run_head_commit": "3df435987fe7da0bf9c4407b43a4ef35ad962ad1",
    "ci_run_id": "37704966686",
    "source_kind": "ci",
    "source_dirty": false
  },
  "map": {
    "status": "complete",
    "rendering": {
      "clipped_declarations": [],
      "declaration_character_limit": 8000,
      "declaration_line_limit": 80,
      "format": "grouped"
    },
    "coverage": {
      "candidates_seen": 1,
      "definitions_found": 2,
      "definitions_in_map": 2,
      "definitions_omitted": 0,
      "files_with_definitions": 1,
      "parsed_files": 1,
      "selected_files": 1
    },
    "raw_sha256_matches": true,
    "complete_multiline_signature": true,
    "body_excluded": true,
    "path": "C:\\Users\\BiuroEdukey\\AppData\\Local\\Temp\\legacy-skill-review-20261007-05bd\\native-consumer-windows\\run-37704966686\\grouped-smoke-output\\repo-map.md"
  },
  "warning": "This artifact predates pending renderer fixes; repeat with final reviewed CI source. Successful unsigned execution applies to this permitted host and download path, not consumer SmartScreen/Gatekeeper validation."
}
```
