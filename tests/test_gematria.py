# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Gallus Labs
import unittest

from gallus_decoder_tools.ciphers import ciphers
from gallus_decoder_tools.errors import HarnessError
from gallus_decoder_tools.gematria import CIPHER_NAMES, DEFAULT_CIPHERS, decode


class DecodeTests(unittest.TestCase):
    def test_cipher_catalog_matches_maps(self) -> None:
        self.assertEqual(set(CIPHER_NAMES), set(ciphers))

    def test_default_four(self) -> None:
        result = decode("ABC")
        codes = [item["code"] for item in result["phrases"][0]["values"]]
        self.assertEqual(tuple(codes), DEFAULT_CIPHERS)
        values = {item["code"]: item["value"] for item in result["phrases"][0]["values"]}
        self.assertEqual(values, {"EO": 6, "FR": 6, "RO": 75, "RFR": 21})

    def test_digits_are_added_and_punctuation_is_skipped(self) -> None:
        values = {item["code"]: item["value"] for item in decode("A10!")["phrases"][0]["values"]}
        self.assertEqual(values["EO"], 11)

    def test_hebrew_keeps_case(self) -> None:
        lower = decode("k", ciphers_spec="heb")["phrases"][0]["values"][0]["value"]
        upper = decode("K", ciphers_spec="HEB")["phrases"][0]["values"][0]["value"]
        self.assertEqual(lower, 10)
        self.assertEqual(upper, 20)

    def test_capitals_mixed_keeps_case(self) -> None:
        value = decode("Ab", ciphers_spec="cm")["phrases"][0]["values"][0]["value"]
        self.assertEqual(value, 29)

    def test_comma_separates_phrases(self) -> None:
        phrases = [item["text"] for item in decode("Alpha, Beta")["phrases"]]
        self.assertEqual(phrases, ["Alpha", "Beta"])

    def test_explicit_phrase_list(self) -> None:
        phrases = [item["text"] for item in decode(phrases=["Alpha, Beta"])["phrases"]]
        self.assertEqual(phrases, ["Alpha, Beta"])

    def test_unknown_cipher_is_an_error(self) -> None:
        with self.assertRaises(HarnessError):
            decode("A", ciphers_spec="nope")

    def test_empty_text_is_an_error(self) -> None:
        with self.assertRaises(HarnessError):
            decode(" , ")

    def test_all_and_ciphers_conflict(self) -> None:
        with self.assertRaises(HarnessError):
            decode("A", ciphers_spec="eo", all_ciphers=True)


if __name__ == "__main__":
    unittest.main()
