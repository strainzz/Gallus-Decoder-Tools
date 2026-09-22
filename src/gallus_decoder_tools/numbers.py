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
# Prime exponents of the Mersenne primes used to build the even perfect numbers.
_MERSENNE_EXPONENTS = (2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127)
_PERFECT_NUMBERS: tuple[int, ...] | None = None

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


def _lucas_lehmer(exponent: int) -> bool:
    """Return whether 2**exponent - 1 is a Mersenne prime."""
    if exponent == 2:
        return True
    mersenne = (1 << exponent) - 1
    residue = 4
    for _ in range(exponent - 2):
        residue = (residue * residue - 2) % mersenne
    return residue == 0


def perfect_numbers() -> tuple[int, ...]:
    """Even perfect numbers generated from the enumerated Mersenne exponents."""
    global _PERFECT_NUMBERS
    if _PERFECT_NUMBERS is None:
        values = []
        for exponent in _MERSENNE_EXPONENTS:
            if _lucas_lehmer(exponent):
                values.append((1 << (exponent - 1)) * ((1 << exponent) - 1))
        _PERFECT_NUMBERS = tuple(values)
    return _PERFECT_NUMBERS


def _sieve(limit: int) -> bytearray:
    is_prime = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        is_prime[0] = 0
    if limit >= 1:
        is_prime[1] = 0
    root = int(limit**0.5)
    for number in range(2, root + 1):
        if not is_prime[number]:
            continue
        start = number * number
        is_prime[start : limit + 1 : number] = b"\x00" * (((limit - start) // number) + 1)
    return is_prime


def _prime_prefix(flags: bytearray) -> list[int]:
    prefix = [0] * len(flags)
    count = 0
    for number, flag in enumerate(flags):
        if flag:
            count += 1
        prefix[number] = count
    return prefix


def _nth_prime(index: int) -> int:
    if index < 6:
        return (2, 3, 5, 7, 11)[index - 1]
    if index < 20:
        limit = 100
    else:
        log_n = math.log(index)
        limit = math.ceil(index * (log_n + math.log(log_n))) + 10
    while True:
        flags = _sieve(limit)
        primes = [number for number, flag in enumerate(flags) if flag]
        if len(primes) >= index:
            return primes[index - 1]
        limit = limit * 2 + 10


def _nth_composite(index: int) -> int:
    high = index * 2 + 4
    while True:
        flags = _sieve(high)
        prefix = _prime_prefix(flags)
        if high - 1 - prefix[high] >= index:
            break
        high = high * 2 + 4
    low = 4
    while low < high:
        mid = (low + high) // 2
        if mid - 1 - prefix[mid] < index:
            low = mid + 1
        else:
            high = mid
    return low


def _fib_pair(index: int) -> tuple[int, int]:
    """Return standard (F(index), F(index + 1)) with F(0)=0 and F(1)=1."""
    if index == 0:
        return (0, 1)
    first, second = _fib_pair(index // 2)
    twice = first * (2 * second - first)
    squared = first * first + second * second
    if index % 2 == 0:
        return (twice, squared)
    return (squared, twice + squared)


def _fibonacci_fast(index: int) -> int:
    return _fib_pair(index)[0]


def _lucas_fast(index: int) -> int:
    previous, current = _fib_pair(index - 1)
    return current + 2 * previous


def _catalan_zero_based(index: int) -> int:
    value = 1
    for step in range(index):
        value = value * (4 * step + 2) // (step + 2)
    return value


def _factor(number: int, primes: list[int]) -> list[dict[str, int]]:
    if number == 1:
        return []
    factors = []
    remaining = number
    for prime in primes:
        if prime * prime > remaining:
            break
        if remaining % prime != 0:
            continue
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        factors.append({"prime": prime, "exponent": exponent})
    if remaining > 1:
        factors.append({"prime": remaining, "exponent": 1})
    return factors


def _divisors(factors: list[dict[str, int]]) -> list[int]:
    divisors = [1]
    for factor in factors:
        prime = factor["prime"]
        power = 1
        grown = []
        for _ in range(factor["exponent"]):
            power *= prime
            grown.extend(divisor * power for divisor in divisors)
        divisors.extend(grown)
    divisors.sort()
    return divisors


def _arithmetic(number: int, primes: list[int]) -> dict:
    factors = _factor(number, primes)
    divisors = _divisors(factors)
    divisor_sum = sum(divisors)
    aliquot_sum = divisor_sum - number
    if number > 1 and aliquot_sum == number:
        abundance = "perfect"
    elif aliquot_sum > number:
        abundance = "abundant"
    else:
        abundance = "deficient"
    digits = str(number)
    reversed_digits = digits[::-1]
    return {
        "even": number % 2 == 0,
        "digit_sum": sum(int(digit) for digit in digits),
        "digital_root": 1 + (number - 1) % 9,
        "reversed_digits": reversed_digits,
        "reversed": int(reversed_digits),
        "prime_factors": factors,
        "divisors": divisors,
        "divisor_count": len(divisors),
        "divisor_sum": divisor_sum,
        "aliquot_sum": aliquot_sum,
        "abundance": abundance,
    }


def _indexes(number: int) -> dict[str, int | None]:
    perfects = perfect_numbers()
    return {
        "prime": _nth_prime(number),
        "composite": _nth_composite(number),
        "triangular": number * (number + 1) // 2,
        "square": number * number,
        "fibonacci": _fibonacci_fast(number),
        "hexagonal": number * (2 * number - 1),
        "perfect": perfects[number - 1] if number <= len(perfects) else None,
        "pentagonal": number * (3 * number - 1) // 2,
        "cubic": number * number * number,
        "octagonal": number * (3 * number - 2),
        "tetrahedral": number * (number + 1) * (number + 2) // 6,
        "lucas": _lucas_fast(number),
        "catalan": _catalan_zero_based(number - 1),
    }


def _build_tables() -> dict:
    limit = MAX_NUMBER
    is_prime = _sieve(limit)
    prime_count = _prime_prefix(is_prime)
    primes = [number for number, flag in enumerate(is_prime) if flag]

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
        for position, value in enumerate(perfect_numbers(), start=1)
        if value <= limit
    }

    return {
        "is_prime": is_prime,
        "primes": primes,
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
    """Return the arithmetic, sequence membership, index terms, and special flags."""
    value = parse_number(number)
    tables = _tables()
    arithmetic = _arithmetic(value, tables["primes"])
    prime_position = tables["prime_count"][value] if tables["is_prime"][value] else None
    if value > 1 and prime_position is None:
        composite_position = value - 1 - tables["prime_count"][value]
    else:
        composite_position = None
    perfect_position = tables["perfect"].get(value)

    sequences = {
        "prime": _flag(prime_position),
        "composite": _flag(composite_position),
        "triangular": _flag(tables["triangular"].get(value)),
        "square": _flag(tables["square"].get(value)),
        "fibonacci": _flag(tables["fibonacci"].get(value)),
        "hexagonal": _flag(tables["hexagonal"].get(value)),
        "perfect": _flag(perfect_position if arithmetic["abundance"] == "perfect" else None),
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
        "arithmetic": arithmetic,
        "sequences": sequences,
        "indexes": _indexes(value),
        "special": {
            "master": value in MASTER_NUMBERS,
            "sacred": value in SACRED_NUMBERS,
            "jesuit": value in JESUIT_NUMBERS,
            "angelic": value in ANGELIC_NUMBERS,
        },
    }
