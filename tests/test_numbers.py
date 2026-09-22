# SPDX-License-Identifier: LicenseRef-Gallus-Labs-Noncommercial
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

    def test_arithmetic_of_one_hundred_ten(self) -> None:
        arithmetic = number_properties(110)["arithmetic"]
        self.assertEqual(
            arithmetic["prime_factors"],
            [
                {"prime": 2, "exponent": 1},
                {"prime": 5, "exponent": 1},
                {"prime": 11, "exponent": 1},
            ],
        )
        self.assertEqual(arithmetic["divisors"], [1, 2, 5, 10, 11, 22, 55, 110])
        self.assertEqual(arithmetic["divisor_count"], 8)
        self.assertEqual(arithmetic["divisor_sum"], 216)
        self.assertEqual(arithmetic["aliquot_sum"], 106)
        self.assertEqual(arithmetic["abundance"], "deficient")
        self.assertEqual(arithmetic["digit_sum"], 2)
        self.assertEqual(arithmetic["digital_root"], 2)
        self.assertTrue(arithmetic["even"])
        self.assertEqual(arithmetic["reversed_digits"], "011")
        self.assertEqual(arithmetic["reversed"], 11)

    def test_perfect_abundant_and_deficient(self) -> None:
        perfect = number_properties(28)
        self.assertEqual(perfect["arithmetic"]["aliquot_sum"], 28)
        self.assertEqual(perfect["arithmetic"]["abundance"], "perfect")
        self.assertEqual(number_properties(12)["arithmetic"]["abundance"], "abundant")
        self.assertEqual(number_properties(8)["arithmetic"]["abundance"], "deficient")
        self.assertEqual(number_properties(9)["arithmetic"]["digital_root"], 9)
        self.assertEqual(number_properties(19)["arithmetic"]["digit_sum"], 10)
        self.assertEqual(number_properties(19)["arithmetic"]["digital_root"], 1)

    def test_factorization_multiplies_back(self) -> None:
        for number in (1, 2, 28, 97, 360, 8128):
            factors = number_properties(number)["arithmetic"]["prime_factors"]
            product = 1
            for factor in factors:
                product *= factor["prime"] ** factor["exponent"]
            self.assertEqual(product, number)

    def test_index_terms(self) -> None:
        ten = number_properties(10)["indexes"]
        self.assertEqual(ten["prime"], 29)
        self.assertEqual(ten["composite"], 18)
        self.assertEqual(ten["triangular"], 55)
        self.assertEqual(ten["square"], 100)
        self.assertEqual(ten["fibonacci"], 55)
        self.assertEqual(ten["lucas"], 123)
        self.assertEqual(ten["catalan"], 4862)
        self.assertEqual(number_properties(1)["indexes"]["prime"], 2)
        self.assertEqual(number_properties(1)["indexes"]["composite"], 4)
        self.assertEqual(number_properties(4)["indexes"]["composite"], 9)
        self.assertEqual(number_properties(100)["indexes"]["prime"], 541)
        self.assertEqual(number_properties(500)["indexes"]["prime"], 3571)
        self.assertEqual(number_properties(5)["indexes"]["perfect"], 33550336)
        self.assertEqual(number_properties(4)["indexes"]["perfect"], 8128)
        self.assertIsNone(number_properties(13)["indexes"]["perfect"])

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
