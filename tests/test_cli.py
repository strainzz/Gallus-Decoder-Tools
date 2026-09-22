# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Gallus Labs
import json
import unittest
from contextlib import redirect_stdout
from io import StringIO

from gallus_decoder_tools.cli import execute, main
from gallus_decoder_tools.errors import HarnessError


class CliTests(unittest.TestCase):
    def run_cli(self, argv: list[str]) -> tuple[int, dict]:
        buffer = StringIO()
        with redirect_stdout(buffer):
            code = main(argv)
        return code, json.loads(buffer.getvalue())

    def test_properties_command(self) -> None:
        code, payload = self.run_cli(["properties", "28"])
        self.assertEqual(code, 0)
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["credit"], "Gallus Decoder Tools by Gallus")
        self.assertEqual(payload["tool"], "properties")
        self.assertEqual(payload["result"]["sequences"]["perfect"]["position"], 2)

    def test_run_json(self) -> None:
        code, payload = self.run_cli(["run", "--json", '{"tool":"decode","text":"A","ciphers":["EO"]}'])
        self.assertEqual(code, 0)
        self.assertEqual(payload["result"]["phrases"][0]["values"][0]["value"], 1)

    def test_all_false_string_does_not_enable_every_cipher(self) -> None:
        result = execute({"tool": "decode", "text": "A", "all": "false"})
        self.assertEqual(
            [item["code"] for item in result["phrases"][0]["values"]],
            ["EO", "FR", "RO", "RFR"],
        )

    def test_bad_tool(self) -> None:
        code, payload = self.run_cli(["run", "--json", '{"tool":"matches"}'])
        self.assertEqual(code, 2)
        self.assertFalse(payload["ok"])
        self.assertEqual(payload["credit"], "Gallus Decoder Tools by Gallus")

    def test_phrases_must_be_a_list(self) -> None:
        with self.assertRaises(HarnessError):
            execute({"tool": "decode", "phrases": "A"})


if __name__ == "__main__":
    unittest.main()
