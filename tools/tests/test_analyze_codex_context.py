"""Behavioral checks for the offline session auditor; no real profiles required."""
import importlib.util
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).parents[1] / "analyze_codex_context.py"
spec = importlib.util.spec_from_file_location("audit", SCRIPT)
audit = importlib.util.module_from_spec(spec)


class SessionAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec.loader.exec_module(audit)

    def write(self, directory, name, records):
        path = Path(directory) / f"rollout-{name}.jsonl"
        path.write_text("".join(json.dumps(r) + "\n" for r in records), encoding="utf-8")
        return path

    def test_fork_reads_only_inherited_prefix(self):
        with tempfile.TemporaryDirectory() as directory:
            self.write(directory, "parent", [
                {"type": "session_meta", "payload": {"id": "parent"}},
                {"type": "response_item", "payload": {"type": "message", "role": "user", "content": [{"type": "input_text", "text": "inherited"}]}},
                {"type": "response_item", "payload": {"type": "message", "role": "user", "content": [{"type": "input_text", "text": "later unrelated"}]}},
            ])
            child = self.write(directory, "child", [
                {"type": "session_meta", "payload": {"id": "child", "history_base": {"thread_id": "parent", "end_ordinal_exclusive": 2}}},
                {"type": "response_item", "payload": {"type": "message", "role": "user", "content": [{"type": "input_text", "text": "new"}]}},
            ])
            records, sources = audit.load_lineage(child, Path(directory))
            self.assertEqual([r["payload"].get("content", []) for r in records if r["type"] == "response_item"], [
                [{"type": "input_text", "text": "inherited"}], [{"type": "input_text", "text": "new"}],
            ])
            self.assertEqual(len(sources), 2)

    def test_usage_records_and_ui_events_are_not_double_counted(self):
        usage = {"input_tokens": 100, "cached_input_tokens": 60, "output_tokens": 5, "reasoning_output_tokens": 2, "total_tokens": 105}
        records = [
            {"type": "token_usage_record", "timestamp": "t", "payload": {"response_id": "r", "thread_id": "root", "usage": usage}},
            {"type": "event_msg", "timestamp": "t", "payload": {"type": "token_count", "info": {"last_token_usage": usage, "model_context_window": 1000}}},
            {"type": "event_msg", "payload": {"type": "item_completed", "item": {"type": "message", "role": "user", "content": [{"text": "duplicate"}]}}},
            {"type": "response_item", "payload": {"type": "message", "role": "user", "content": [{"type": "input_text", "text": "real"}]}},
        ]
        report = audit.analyze(records, audit.TokenMeter("chars"))
        self.assertEqual(report["usage"]["calls"], 1)
        self.assertEqual(report["usage"]["cumulative_input_tokens"], 100)
        self.assertEqual(report["categories"]["user_messages"]["characters"], 4)
        self.assertEqual(report["usage"]["context_window_tokens"], 1000)

    def test_encrypted_reasoning_and_metadata_are_not_prompt_text(self):
        records = [
            {"type": "session_meta", "payload": {"id": "root", "base_instructions": {"text": "base"}}},
            {"type": "response_item", "payload": {"type": "reasoning", "summary": [], "encrypted_content": "X" * 10000}},
            {"type": "world_state", "payload": {"full": True, "state": {"host_skills": {"body": "catalog"}}}},
        ]
        report = audit.analyze(records, audit.TokenMeter("chars"))
        self.assertEqual(report["visible_text_estimated_tokens"], 1)
        self.assertEqual(report["encrypted_reasoning_characters_not_tokenized"], 10000)
        self.assertEqual(report["world_state_diagnostics"]["host_skills"]["characters"], 7)

    def test_skill_catalog_and_user_invoked_skill_are_separate(self):
        text = "## Memory\nremember\n<skills_instructions>catalog</skills_instructions>\npermissions"
        records = [
            {"type": "response_item", "payload": {"type": "message", "role": "developer", "content": [{"type": "input_text", "text": text}]}},
            {"type": "response_item", "payload": {"type": "message", "role": "user", "content": [{"type": "input_text", "text": "<skill><name>demo</name>body</skill>"}]}},
        ]
        report = audit.analyze(records, audit.TokenMeter("chars"))
        self.assertIn("skill_catalog", report["categories"])
        self.assertIn("invoked_skill_instructions", report["categories"])
        self.assertIn("memory_instructions", report["categories"])

    def test_growing_trailing_record_is_ignored_but_internal_corruption_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "log.jsonl"
            path.write_text('{"type":"session_meta","payload":{"id":"root"}}\n{"type":', encoding="utf-8")
            self.assertEqual(len(audit.read_records(path)), 1)
            path.write_text('{"type":\n{"type":"session_meta","payload":{"id":"root"}}\n', encoding="utf-8")
            with self.assertRaises(ValueError):
                audit.read_records(path)

    def test_schema_inventory_does_not_claim_catalog_is_injected(self):
        report = audit.analyze([], audit.TokenMeter("chars"), tool_catalog=[{"name": "mcp__demo__lookup", "description": "long description"}])
        self.assertEqual(report["visible_text_estimated_tokens"], 0)
        self.assertFalse(report["available_tools"]["proves_prompt_inclusion"])

    def test_repeated_ui_token_count_is_not_a_new_model_call(self):
        usage = {"input_tokens": 20, "output_tokens": 2, "total_tokens": 22}
        event = {"type": "event_msg", "payload": {"type": "token_count", "info": {"last_token_usage": usage, "total_token_usage": usage}}}
        report = audit.analyze([event, event], audit.TokenMeter("chars"))
        self.assertEqual(report["usage"]["calls"], 1)
        self.assertEqual(report["usage"]["cumulative_input_tokens"], 20)

    def test_older_ancestor_usage_survives_newer_fork_record_format(self):
        records = [
            {"type": "session_meta", "payload": {"id": "old"}},
            {"type": "event_msg", "timestamp": "a", "payload": {"type": "token_count", "info": {"last_token_usage": {"input_tokens": 20}}}},
            {"type": "session_meta", "payload": {"id": "new"}},
            {"type": "token_usage_record", "timestamp": "b", "payload": {"response_id": "r", "thread_id": "new", "usage": {"input_tokens": 30}}},
        ]
        report = audit.analyze(records, audit.TokenMeter("chars"))
        self.assertEqual(report["usage"]["calls"], 2)
        self.assertEqual(report["usage"]["cumulative_input_tokens"], 50)

    def test_media_only_tool_result_cannot_attach_text_attribution_to_previous_item(self):
        report = audit.analyze([
            {"type": "response_item", "payload": {"type": "custom_tool_call_output", "output": [{"type": "image", "data": "opaque"}]}}
        ], audit.TokenMeter("chars"), attribute_reads=True)
        self.assertEqual(report["entries"], [])

    def test_export_does_not_leak_message_text_or_config_credentials(self):
        with tempfile.TemporaryDirectory() as directory:
            session = self.write(directory, "root", [
                {"type": "session_meta", "payload": {"id": "root"}},
                {"type": "response_item", "payload": {"type": "message", "role": "user", "content": [{"type": "input_text", "text": "UNIQUE_PRIVATE_VALUE"}]}},
            ])
            config = Path(directory) / "config.toml"
            config.write_text('[mcp_servers.demo]\nenabled = false\nbearer_token = "UNIQUE_PRIVATE_VALUE"\n', encoding="utf-8")
            output = Path(directory) / "output"
            with contextlib.redirect_stdout(io.StringIO()):
                result = audit.main([str(session), "--output-dir", str(output), "--config", str(config)])
            self.assertEqual(result, 0)
            self.assertNotIn("UNIQUE_PRIVATE_VALUE", (output / "context-audit.json").read_text(encoding="utf-8"))
            self.assertNotIn("UNIQUE_PRIVATE_VALUE", (output / "context-audit.md").read_text(encoding="utf-8"))
            self.assertFalse(json.loads((output / "context-audit.json").read_text(encoding="utf-8"))["current_configuration_metadata"]["mcp_servers"]["demo"]["enabled"])

    def test_skill_read_is_attributed_only_to_a_matching_visible_file_prefix(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "skills" / "demo" / "SKILL.md"
            path.parent.mkdir(parents=True)
            path.write_text("---\nname: demo\n---\nRead only relevant source.\n", encoding="utf-8")
            command = f"Get-Content -LiteralPath '{path}'"
            code = "tools.exec_command({cmd:" + json.dumps(command) + "})"
            result = [{"type": "input_text", "text": json.dumps({"output": path.read_text(encoding='utf-8')})}]
            reads = audit.skill_reads(code, result, audit.TokenMeter("chars"))
            self.assertEqual(len(reads), 1)
            self.assertEqual(reads[0]["document"], "demo/SKILL.md")
            self.assertTrue(reads[0]["complete_excerpt"])
            self.assertEqual(audit.skill_reads(code, [{"text": "not the file"}], audit.TokenMeter("chars")), [])

    def test_cli_cutoff_excludes_later_appended_activity(self):
        with tempfile.TemporaryDirectory() as directory:
            session = self.write(directory, "root", [
                {"type": "session_meta", "payload": {"id": "root"}},
                {"type": "response_item", "payload": {"type": "message", "role": "user", "content": [{"type": "input_text", "text": "old"}]}},
                {"type": "response_item", "payload": {"type": "message", "role": "user", "content": [{"type": "input_text", "text": "later"}]}},
            ])
            output = Path(directory) / "output"
            with contextlib.redirect_stdout(io.StringIO()):
                result = audit.main([str(session), "--end-ordinal", "2", "--output-dir", str(output)])
            self.assertEqual(result, 0)
            report = json.loads((output / "context-audit.json").read_text(encoding="utf-8"))
            self.assertEqual(report["analysis"]["categories"]["user_messages"]["characters"], 3)
            self.assertEqual(report["sources"][0]["records_included"], 2)


if __name__ == "__main__":
    unittest.main()
