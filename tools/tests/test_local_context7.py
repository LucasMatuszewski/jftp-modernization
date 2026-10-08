"""Behavior checks using synthetic source and the installed local retrieval runtime."""
import hashlib
import importlib.util
import json
from pathlib import Path
import queue
import subprocess
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import Request, urlopen

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import local_context7 as local


class LocalContext7Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runtime = local.runtime_path()
        cls.backend = local.load_backend(cls.runtime)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source = self.base / "source"
        self.source.mkdir()
        self.docs = self.source / "docs"
        self.docs.mkdir()
        self.java = self.source / "Demo.java"
        self.java.write_text("public class Demo {\n  public void retryTransfer() {}\n}\n", encoding="utf-8")
        (self.docs / "api.md").write_text("# Transfer lifecycle\nDemo.retryTransfer retries a transfer.\n", encoding="utf-8")
        self.database = self.base / "index.sqlite"
        self.reindex()

    def reindex(self):
        return self.backend.index(self.source, self.database, local.LIBRARY_ID, self.docs, None, None)

    def test_source_ranges_and_hashes_match_originals(self):
        with self.backend.connect(self.database) as con:
            result = self.backend.query(con, "retryTransfer")
        self.assertEqual({r["source"]["kind"] for r in result["results"]}, {"code", "docs"})
        for item in result["results"]:
            src = item["source"]
            path = (self.docs if src["kind"] == "docs" else self.source) / src["path"]
            original = path.read_text(encoding="utf-8")
            self.assertEqual(item["text"], "\n".join(original.splitlines()[src["startLine"] - 1:src["endLine"]]))
            self.assertEqual(src["fileSha256"], hashlib.sha256(path.read_bytes()).hexdigest())

    def test_http_rejects_stale_source_then_recovers_after_reindex(self):
        with local.local_server(self.backend, self.database) as url:
            endpoint = url + "/api/v2/context?libraryId=%2Flocal%2Fjftp&query=retryTransfer"
            with urlopen(endpoint, timeout=10) as response:
                self.assertTrue(json.load(response)["codeSnippets"])
            self.java.write_text("public class Demo { public void cancelTransfer() {} }\n", encoding="utf-8")
            with self.assertRaises(HTTPError) as caught:
                urlopen(endpoint, timeout=10)
            self.assertEqual(caught.exception.code, 409)
            caught.exception.close()
            self.reindex()
            with urlopen(endpoint, timeout=10) as response:
                payload = json.load(response)
            self.assertFalse(payload["codeSnippets"])
            self.assertTrue(payload["infoSnippets"])
            self.java.unlink()
            with self.assertRaises(HTTPError) as caught:
                urlopen(endpoint, timeout=10)
            self.assertEqual(caught.exception.code, 409)
            caught.exception.close()
        with self.assertRaises(OSError):
            urlopen(endpoint, timeout=2)

    def test_loopback_host_boundary(self):
        with local.local_server(self.backend, self.database) as url:
            request = Request(url + "/api/v2/libs/search?libraryName=jftp", headers={"Host": "outside.example"})
            with self.assertRaises(HTTPError) as caught:
                urlopen(request, timeout=10)
            self.assertEqual(caught.exception.code, 403)
            caught.exception.close()

    def test_credentials_and_proxy_environment_are_not_forwarded(self):
        with patch.dict(local.os.environ, {"CONTEXT7_API_KEY": "synthetic", "OPENAI_API_KEY": "synthetic", "HTTP_PROXY": "http://outside.example", "NODE_OPTIONS": "--inspect", "HOME": "unchanged-home"}):
            env = local.client_environment(self.runtime, "http://127.0.0.1:1234")
        self.assertEqual(env["HOME"], "unchanged-home")
        self.assertEqual(env["CONTEXT7_API_URL"], "http://127.0.0.1:1234/api")
        for name in ("CONTEXT7_API_KEY", "OPENAI_API_KEY", "HTTP_PROXY", "NODE_OPTIONS"):
            self.assertNotIn(name, env)

    def test_git_revision_change_requires_explicit_reindex(self):
        def git(*args):
            subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "-C", str(self.source), *args], stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, timeout=10)
        git("init")
        git("add", "Demo.java", "docs/api.md")
        git("commit", "-m", "Initial fixture")
        self.reindex()
        git("commit", "--allow-empty", "-m", "Revision changed")
        with self.backend.connect(self.database) as con:
            with self.assertRaises(self.backend.RetrievalError):
                self.backend.query(con, "retryTransfer")
        self.reindex()
        with self.backend.connect(self.database) as con:
            self.assertTrue(self.backend.query(con, "retryTransfer")["results"])

    def test_runtime_cannot_overlap_source(self):
        for path in (local.ROOT, local.ROOT / "cache", local.ROOT.parent):
            with self.assertRaises(ValueError):
                local.runtime_path(path)

    def test_pinned_cli_resolves_library_and_returns_source(self):
        entry = local.client_entry(self.runtime, "ctx7")
        with local.local_server(self.backend, self.database) as url:
            for command, name in (("library", "jftp"), ("docs", local.LIBRARY_ID)):
                result = subprocess.run(["node", str(entry), "--base-url", url, command, name, "retryTransfer", "--json"], env=local.client_environment(self.runtime, url), capture_output=True, text=True, encoding="utf-8", timeout=20, check=True)
                payload = json.loads(result.stdout)
                if command == "library":
                    self.assertEqual(payload[0]["id"], local.LIBRARY_ID)
                else:
                    self.assertIn("Demo.java", payload["codeSnippets"][0]["codeTitle"])

    def test_official_mcp_against_local_source_and_stale_index(self):
        entry = local.client_entry(self.runtime, "@upstash/context7-mcp")
        with local.local_server(self.backend, self.database) as url:
            with MCP(["node", str(entry)], local.client_environment(self.runtime, url)) as mcp:
                tools = mcp.request("tools/list")["tools"]
                self.assertEqual({tool["name"] for tool in tools}, {"resolve-library-id", "query-docs"})
                resolved = mcp.request("tools/call", {"name": "resolve-library-id", "arguments": {"libraryName": "jftp", "query": "retryTransfer"}})
                self.assertIn(local.LIBRARY_ID, resolved["content"][0]["text"])
                args = {"name": "query-docs", "arguments": {"libraryId": local.LIBRARY_ID, "query": "retryTransfer"}}
                result = mcp.request("tools/call", args)
                self.assertIn("Demo.java", result["content"][0]["text"])
                self.java.unlink()
                result = mcp.request("tools/call", args)
                self.assertIn("409", result["content"][0]["text"])

    def test_configured_wrapper_returns_current_jftp_source(self):
        # This read-only smoke test catches Windows Git/MCP stdin contention
        # that the small non-Git synthetic corpus cannot reproduce.
        with MCP([sys.executable, str(TOOLS / "local_context7.py"), "mcp"]) as mcp:
            result = mcp.request("tools/call", {"name": "query-docs", "arguments": {"libraryId": local.LIBRARY_ID, "query": "FavoritesManager"}})
            payload = json.loads(result["content"][0]["text"])
            self.assertTrue(any("FavoritesManager.java" in snippet["codeTitle"] for snippet in payload["codeSnippets"]))


class MCP:
    """Minimal real JSON-RPC client with bounded reads and owned process cleanup."""
    def __init__(self, command, env=None, stderr=subprocess.DEVNULL):
        self.command, self.env, self.stderr = command, env, stderr

    def __enter__(self):
        self.process = subprocess.Popen(self.command, env=self.env, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=self.stderr, text=True, encoding="utf-8")
        self.messages = queue.Queue()
        self.reader = threading.Thread(target=self.read, daemon=True)
        self.reader.start()
        self.serial = 0
        try:
            self.request("initialize", {"protocolVersion": "2025-03-26", "capabilities": {}, "clientInfo": {"name": "jftp-local-verification", "version": "1.0"}})
            self.write({"jsonrpc": "2.0", "method": "notifications/initialized"})
            return self
        except Exception:
            self.__exit__(None, None, None)
            raise

    def read(self):
        for line in self.process.stdout:
            try:
                self.messages.put(json.loads(line))
            except ValueError:
                self.messages.put({"error": {"message": "Non-JSON output on MCP stdout"}})
        self.messages.put({"error": {"message": "MCP closed stdout"}})

    def write(self, message):
        self.process.stdin.write(json.dumps(message) + "\n")
        self.process.stdin.flush()

    def request(self, method, params=None):
        self.serial += 1
        self.write({"jsonrpc": "2.0", "id": self.serial, "method": method, "params": params or {}})
        while True:
            message = self.messages.get(timeout=20)
            if "error" in message:
                raise AssertionError(message["error"])
            if message.get("id") == self.serial:
                return message["result"]

    def __exit__(self, *_args):
        self.process.stdin.close()
        try:
            self.process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self.process.terminate()
            self.process.wait(timeout=5)
        self.reader.join(timeout=2)
        self.process.stdout.close()


if __name__ == "__main__":
    unittest.main()
