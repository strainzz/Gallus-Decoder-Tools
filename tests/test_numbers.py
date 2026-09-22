# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Gallus Labs
import unittest

from gallus_decoder_tools.errors import HarnessError
from gallus_decoder_tools.numbers import number_properties


def position(result: dict, name: str) -> int | None:
    entry = result["sequences"][name]
    if not entry["is"]:
        return None
    return entry["position"]


class NumberPropertyTests(unittest.TestCase):
    def test_one_is_the_first_term_of_the_figurate_sequences(self) -> None:
        result = number_properties(1)
        for name in (
            "triangular",
            "square",
            "fibonacci",
            "hexagonal",
            "pentagonal",
            "cubic",
            "octagonal",
            "tetrahedral",
            "lucas",
            "catalan",
        ):
            self.assertEqual(position(result, name), 1, name)
        self.assertIsNone(position(result, "prime"))
        self.assertIsNone(position(result, "composite"))
        self.assertFalse(result["sequences"]["palindromic"]["is"])

    def test_small_primes_and_composites(self) -> None:
        self.assertEqual(position(number_properties(2), "prime"), 1)
        self.assertEqual(position(number_properties(4), "composite"), 1)
        self.assertEqual(position(number_properties(9), "composite"), 4)
        self.assertEqual(position(number_properties(113), "prime"), 30)

    def test_twenty_eight(self) -> None:
        result = number_properties(28)
        self.assertEqual(position(result, "triangular"), 7)
        self.assertEqual(position(result, "hexagonal"), 4)
        self.assertEqual(position(result, "perfect"), 2)
        self.assertIsNotNone(position(result, "composite"))
        self.assertFalse(result["special"]["master"])

    def test_repeated_sequence_values_keep_the_first_position(self) -> None:
        self.assertEqual(position(number_properties(1), "fibonacci"), 1)
        self.assertIsNone(position(number_properties(2), "lucas"))
        self.assertEqual(position(number_properties(3), "lucas"), 2)
        self.assertEqual(position(number_properties(2), "catalan"), 3)

    def test_special_flags(self) -> None:
        eleven = number_properties(11)
        self.assertTrue(eleven["special"]["master"])
        self.assertTrue(eleven["special"]["angelic"])
        self.assertTrue(eleven["sequences"]["palindromic"]["is"])
        self.assertTrue(number_properties(40)["special"]["sacred"])
        self.assertTrue(number_properties(47)["special"]["jesuit"])
        self.assertTrue(number_properties(121)["sequences"]["palindromic"]["is"])
        self.assertEqual(position(number_properties(121), "square"), 11)

    def test_range(self) -> None:
        with self.assertRaises(HarnessError):
            number_properties(0)
        with self.assertRaises(HarnessError):
            number_properties(1_000_001)
        with self.assertRaises(HarnessError):
            number_properties("nope")
        self.assertEqual(number_properties("1_000")["number"], 1000)
        self.assertEqual(number_properties(28.0)["number"], 28)


if __name__ == "__main__":
    unittest.main()
