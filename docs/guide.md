<p align="center">
  <img src="brand/GallusLogo.png" alt="Gallus" width="72">
</p>

# Guide

This is the operating guide for Gallus Decoder Tools. The project overview is the [README](../README.md). The cipher rules are in [ciphers.md](ciphers.md).

The package has four commands. Each one calculates from the input you give it.

| Command | Section |
| --- | --- |
| `decode` | [Decode](#decode) |
| `ciphers` | [Cipher list](#cipher-list) |
| `properties` | [Properties](#properties) |
| `span` | [Span](#span) |

Copyright 2026 Gallus Labs. Results include the credit `Gallus Decoder Tools by Gallus`.

## Install

Python 3.11 or newer.

```bash
python -m pip install .
```

That installs the `gallus-decoder-tools` command and the `gallus_decoder_tools` Python package. To work on a checkout instead:

```bash
python -m pip install -e .
```

`python -m gallus_decoder_tools` runs the same command.

## Decode

```bash
gallus-decoder-tools decode "New York"
gallus-decoder-tools decode "New York" --ciphers eo,ch,heb
gallus-decoder-tools decode "New York" --all
gallus-decoder-tools ciphers
```

A plain decode uses English Ordinal (`EO`), Full Reduction (`FR`), Reverse Ordinal (`RO`), and Reverse Full Reduction (`RFR`). `--ciphers` takes a comma-separated list of codes. Codes may be upper or lower case. `--all` calculates all 32 ciphers. `ciphers` prints the code and the name of each one. An unknown code stops the command.

A comma splits phrases: `decode "Lions, Bears"` decodes two phrases. When the comma is part of one phrase, pass a `phrases` list through `run`.

The total is produced in four steps:

1. Each letter is looked up in that cipher's map and added.
2. A run of digits is added as that whole number. `A10` is the value of A plus 10.
3. Spaces and punctuation are skipped.
4. Most ciphers treat upper and lower case as the same letter. Hebrew (`HEB`) and the capital ciphers (`CM`, `CA`, `RCM`, `RCA`) keep the case you typed. In Hebrew, `k` is 10 and `K` is 20.

`New York` in the everyday ciphers:

| Code | Name | Value |
| --- | --- | --- |
| EO | English Ordinal | 111 |
| FR | Full Reduction | 39 |
| RO | Reverse Ordinal | 78 |
| RFR | Reverse Full Reduction | 33 |

The JSON for that decode:

```json
{
  "ok": true,
  "credit": "Gallus Decoder Tools by Gallus",
  "tool": "decode",
  "result": {
    "phrases": [
      {
        "text": "New York",
        "values": [
          {"code": "EO", "name": "English Ordinal", "value": 111},
          {"code": "FR", "name": "Full Reduction", "value": 39},
          {"code": "RO", "name": "Reverse Ordinal", "value": 78},
          {"code": "RFR", "name": "Reverse Full Reduction", "value": 33}
        ]
      }
    ]
  }
}
```

| Field | Meaning |
| --- | --- |
| `ok` | `true` when the calculation finished |
| `credit` | The attribution required with the result |
| `tool` | `decode`, `properties`, `span`, or `ciphers` |
| `result.phrases[].text` | The phrase after trimming |
| `result.phrases[].values[]` | One object per cipher: `code`, `name`, and `value` |

## Cipher list

```bash
gallus-decoder-tools ciphers
```

This prints every cipher code and its name, in decoder order. The rules for those codes are the table in [ciphers.md](ciphers.md).

```json
{
  "ok": true,
  "credit": "Gallus Decoder Tools by Gallus",
  "tool": "ciphers",
  "result": {
    "ciphers": [
      {"code": "EO", "name": "English Ordinal"}
    ]
  }
}
```

The array contains all 32 ciphers. The object above shows the shape of one entry.

## Properties

```bash
gallus-decoder-tools properties 28
```

The input is an integer from 1 through 1,000,000. The result has four blocks: `arithmetic`, `sequences`, `indexes`, and `special`.

`28` is the 7th triangular number, the 4th hexagonal number, and the 2nd perfect number. Its aliquot sum is 28, so `abundance` is `perfect`. `110` factors as 2 × 5 × 11 and its digital root is 2.

### Arithmetic

| Field | Meaning |
| --- | --- |
| `even` | Whether the number is divisible by 2 |
| `digit_sum` | The sum of its decimal digits |
| `digital_root` | That sum reduced to one digit. A multiple of 9 has digital root 9 |
| `reversed_digits` | The digits in reverse order. `110` becomes `011` |
| `reversed` | Those reversed digits read as an integer. `011` becomes 11 |
| `prime_factors` | Prime and exponent pairs. `1` has an empty list |
| `divisors` | Every positive divisor, in ascending order |
| `divisor_count` | How many positive divisors |
| `divisor_sum` | The sum of those divisors |
| `aliquot_sum` | `divisor_sum` minus the number itself |
| `abundance` | `perfect` when the aliquot sum equals the number, `abundant` when it is greater, `deficient` when it is smaller |

A prime has exactly two positive divisors. `1` is neither prime nor composite.

### Sequences

`result.sequences` has one entry for each sequence, in this order: prime, composite, triangular, square, fibonacci, hexagonal, perfect, pentagonal, cubic, octagonal, tetrahedral, lucas, catalan, palindromic.

| Field | Meaning |
| --- | --- |
| `is` | Whether the number belongs to that sequence |
| `position` | Its place in the sequence, counting from 1. A palindrome has no position |

When a sequence repeats a value, the stored position is the first occurrence. `1` is the 1st Fibonacci number. `2` is the 3rd Catalan number. A perfect number is one whose aliquot sum equals the number. The position is its place among the even perfect numbers generated from the Mersenne exponents 2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, and 127.

### Indexes

`result.indexes` uses the number as a position and returns that term. The 10th prime is 29, the 10th triangular number is 55, and the 10th Fibonacci number is 55. Fibonacci, Lucas, and Catalan use the same indexing as the sequence positions: the 1st and 2nd Fibonacci numbers are both 1, and the 1st Lucas number is 1. `indexes.perfect` is present for positions 1 through 12 and is null after that list.

`result.special` has four flags: `master`, `sacred`, `jesuit`, and `angelic`.

`110` shows the arithmetic block in full:

```json
{
  "number": 110,
  "arithmetic": {
    "even": true,
    "digit_sum": 2,
    "digital_root": 2,
    "reversed_digits": "011",
    "reversed": 11,
    "prime_factors": [
      {"prime": 2, "exponent": 1},
      {"prime": 5, "exponent": 1},
      {"prime": 11, "exponent": 1}
    ],
    "divisors": [1, 2, 5, 10, 11, 22, 55, 110],
    "divisor_count": 8,
    "divisor_sum": 216,
    "aliquot_sum": 106,
    "abundance": "deficient"
  }
}
```

`sequences`, `indexes`, and `special` are present on the same object. For this number, `indexes.triangular` is 6,105, because the 110th triangular number is 110 × 111 / 2.

## Span

```bash
gallus-decoder-tools span 01/01/2020 09/22/2026
gallus-decoder-tools span 01/01/2020 09/22/2026 --include-end
```

From January 1, 2020 to September 22, 2026 is 6 years, 8 months, and 21 days, which is 2,456 days.

Accepted dates:

| Form | Example |
| --- | --- |
| Month/day/year | `01/01/2020` |
| Year-month-day | `2020-01-01` |
| Month name | `September 22, 2026` |

A slash date is month, day, year. When the first number is greater than 12, it is read as day, month, year, so `31/01/2020` is January 31, 2020. If the second date falls before the first, the tool places the earlier date first and sets `reordered` to true. `--include-end` counts the end date as one full day.

| Field | Meaning |
| --- | --- |
| `start`, `end` | The dates in `YYYY-MM-DD` order |
| `start_display`, `end_display` | The same dates written out |
| `include_end` | Whether the end date was counted |
| `reordered` | Whether the dates were swapped into chronological order |
| `total_days` | The length in days |
| `years`, `months`, `days` | The calendar breakdown |
| `weeks`, `extra_days` | The same length as whole weeks plus leftover days |
| `century_percent`, `millennium_percent` | The length as a share of 36,525 days and of 365,250 days |
| `breakdowns` | The same spans written as sentences. The keys are `years_days`, `years_months_days`, `years_weeks_days`, `months_days`, and `weeks_days` |

January 1, 2020 through September 22, 2026, with the end date excluded:

```json
{
  "start": "2020-01-01",
  "end": "2026-09-22",
  "start_display": "January 01, 2020",
  "end_display": "September 22, 2026",
  "include_end": false,
  "reordered": false,
  "total_days": 2456,
  "years": 6,
  "months": 8,
  "days": 21,
  "weeks": 350,
  "extra_days": 6,
  "century_percent": "6.72%",
  "millennium_percent": "0.67%",
  "breakdowns": {
    "years_days": "6 Years, 264 Days",
    "years_months_days": "6 Years, 8 Months, 21 Days",
    "years_weeks_days": "6 Years, 37 Weeks, 5 Days",
    "months_days": "80 Months, 21 Days",
    "weeks_days": "350 Weeks, 6 Days"
  }
}
```

## JSON requests

`run` reads one JSON object from `--json` or from stdin.

```json
{"tool":"decode","text":"New York"}
{"tool":"decode","phrases":["New York, New York"],"ciphers":["EO","FR"]}
{"tool":"decode","text":"New York","all":true}
{"tool":"properties","number":28}
{"tool":"span","start":"01/01/2020","end":"09/22/2026","include_end":false}
{"tool":"ciphers"}
```

| Tool | Required fields | Optional fields |
| --- | --- | --- |
| `decode` | `text` or `phrases` | `ciphers`, `all` |
| `properties` | `number` | |
| `span` | `start`, `end` | `include_end` |
| `ciphers` | | |

A rejected request exits with status 2. The body is still JSON, `ok` is false, `error` explains the input, and `credit` is present.

## Python

```python
from gallus_decoder_tools import COPYRIGHT, CREDIT, decode, number_properties, date_span

decode("New York")
decode("New York", ciphers_spec=["EO", "CH"])
decode("New York", all_ciphers=True)
number_properties(28)
date_span("01/01/2020", "09/22/2026")
```

`CREDIT` is `Gallus Decoder Tools by Gallus`. `COPYRIGHT` is `Copyright 2026 Gallus Labs`. Keep both with any result you present.
