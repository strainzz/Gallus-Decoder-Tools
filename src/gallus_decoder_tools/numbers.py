# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Gallus Labs
"""Mathematical properties of one integer.

Positions follow the decoder's sequence indexes. The first time a value
appears is the position that is kept when a sequence repeats a value.
"""

from __future__ import annotations

import math

from gallus_decoder_tools.errors import HarnessError

MIN_NUMBER = 1
MAX_NUMBER = 1_000_000

SACRED_NUMBERS = frozenset({3, 7, 12, 40, 144})
JESUIT_NUMBERS = frozenset({201, 56, 72, 47, 26})
ANGELIC_NUMBERS = frozenset(
    {
        11,
        22,
        33,
        44,
        55,
        66,
        77,
        88,
        99,
        111,
        222,
        333,
        444,
        555,
        666,
        777,
        888,
        999,
        1111,
        2222,
        3333,
        4444,
        5555,
        6666,
        7777,
        8888,
        9999,
    }
)
MASTER_NUMBERS = frozenset({11, 22, 33, 44})
PERFECT_NUMBERS = (6, 28, 496, 8128)

_TABLES: dict | None = None


def _fibonacci(index: int) -> int:
    """1-based Fibonacci. F(1)=1, F(2)=1, F(3)=2."""
    if index <= 0:
        return 0
    previous, current = 0, 1
    for _ in range(1, index):
        previous, current = current, previous + current
    return current


def _lucas(index: int) -> int:
    """Lucas with L(0)=2 and L(1)=1. Index 1 returns L(1)."""
    if index < 0:
        return 0
    if index == 0:
        return 2
    previous, current = 2, 1
    for _ in range(1, index):
        previous, current = current, previous + current
    return current


def _catalan(index: int) -> int:
    """0-based Catalan number."""
    if index < 0:
        return 0
    return math.factorial(2 * index) // (math.factorial(index + 1) * math.factorial(index))


def _first_position_map(values) -> dict[int, int]:
    positions: dict[int, int] = {}
    for position, value in enumerate(values, start=1):
        if value > MAX_NUMBER:
            break
        if value not in positions:
            positions[value] = position
    return positions


def _sequence_until(term) -> list[int]:
    values: list[int] = []
    index = 1
    while True:
        value = term(index)
        if value > MAX_NUMBER:
            break
        values.append(value)
        index += 1
        if index > MAX_NUMBER:
            break
    return values


def _build_tables() -> dict:
    limit = MAX_NUMBER
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    root = int(limit**0.5)
    for number in range(2, root + 1):
        if not is_prime[number]:
            continue
        start = number * number
        is_prime[start : limit + 1 : number] = b"\x00" * (((limit - start) // number) + 1)

    prime_count = [0] * (limit + 1)
    count = 0
    for number in range(limit + 1):
        if is_prime[number]:
            count += 1
        prime_count[number] = count

    def polygonal(formula):
        return _first_position_map(_sequence_until(formula))

    fibonacci_values = []
    index = 1
    while True:
        value = _fibonacci(index)
        if value > limit:
            break
        fibonacci_values.append(value)
        index += 1

    lucas_values = []
    index = 1
    while True:
        value = _lucas(index)
        if value > limit:
            break
        lucas_values.append(value)
        index += 1

    catalan_values = []
    index = 0
    while True:
        value = _catalan(index)
        if value > limit:
            break
        catalan_values.append(value)
        index += 1

    perfect = {
        value: position
        for position, value in enumerate(PERFECT_NUMBERS, start=1)
        if value <= limit
    }

    return {
        "is_prime": is_prime,
        "prime_count": prime_count,
        "fibonacci": _first_position_map(fibonacci_values),
        "lucas": _first_position_map(lucas_values),
        "catalan": _first_position_map(catalan_values),
        "triangular": polygonal(lambda n: n * (n + 1) // 2),
        "square": polygonal(lambda n: n * n),
        "hexagonal": polygonal(lambda n: n * (2 * n - 1)),
        "pentagonal": polygonal(lambda n: n * (3 * n - 1) // 2),
        "cubic": polygonal(lambda n: n * n * n),
        "octagonal": polygonal(lambda n: n * (3 * n - 2)),
        "tetrahedral": polygonal(lambda n: n * (n + 1) * (n + 2) // 6),
        "perfect": perfect,
    }


def _tables() -> dict:
    global _TABLES
    if _TABLES is None:
        _TABLES = _build_tables()
    return _TABLES


def parse_number(value: object) -> int:
    """Accept an integer from 1 through 1,000,000."""
    if isinstance(value, bool) or value is None:
        raise HarnessError("Number must be an integer from 1 to 1000000.")
    if isinstance(value, int):
        number = value
    elif isinstance(value, float):
        if not value.is_integer():
            raise HarnessError("Number must be an integer from 1 to 1000000.")
        number = int(value)
    else:
        text = str(value).strip().replace("_", "")
        if text.startswith("+"):
            text = text[1:]
        if not text.isdigit():
            raise HarnessError("Number must be an integer from 1 to 1000000.")
        number = int(text)
    if number < MIN_NUMBER or number > MAX_NUMBER:
        raise HarnessError("Number must be an integer from 1 to 1000000.")
    return number


def _flag(position: int | None) -> dict[str, int | bool | None]:
    return {"is": position is not None, "position": position}


def number_properties(number: object) -> dict:
    """Return sequence membership and the small special-number flags."""
    value = parse_number(number)
    tables = _tables()
    prime_position = tables["prime_count"][value] if tables["is_prime"][value] else None
    if value > 1 and prime_position is None:
        composite_position = value - 1 - tables["prime_count"][value]
    else:
        composite_position = None

    sequences = {
        "prime": _flag(prime_position),
        "composite": _flag(composite_position),
        "triangular": _flag(tables["triangular"].get(value)),
        "square": _flag(tables["square"].get(value)),
        "fibonacci": _flag(tables["fibonacci"].get(value)),
        "hexagonal": _flag(tables["hexagonal"].get(value)),
        "perfect": _flag(tables["perfect"].get(value)),
        "pentagonal": _flag(tables["pentagonal"].get(value)),
        "cubic": _flag(tables["cubic"].get(value)),
        "octagonal": _flag(tables["octagonal"].get(value)),
        "tetrahedral": _flag(tables["tetrahedral"].get(value)),
        "lucas": _flag(tables["lucas"].get(value)),
        "catalan": _flag(tables["catalan"].get(value)),
    }
    text = str(value)
    sequences["palindromic"] = {
        "is": len(text) >= 2 and text == text[::-1],
        "position": None,
    }
    return {
        "number": value,
        "sequences": sequences,
        "special": {
            "master": value in MASTER_NUMBERS,
            "sacred": value in SACRED_NUMBERS,
            "jesuit": value in JESUIT_NUMBERS,
            "angelic": value in ANGELIC_NUMBERS,
        },
    }
