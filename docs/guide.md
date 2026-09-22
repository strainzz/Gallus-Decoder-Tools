# Guide

This is the operating guide for Gallus Decoder Tools. The project overview is the [README](../README.md). The cipher catalog is [ciphers.md](ciphers.md).

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

## Properties

```bash
gallus-decoder-tools properties 28
```

The input is an integer from 1 through 1,000,000. `28` belongs to three sequences a decoder commonly checks: it is the 7th triangular number, the 4th hexagonal number, and the 2nd perfect number.

`result.sequences` has one entry for each sequence, in this order: prime, composite, triangular, square, fibonacci, hexagonal, perfect, pentagonal, cubic, octagonal, tetrahedral, lucas, catalan, palindromic.

| Field | Meaning |
| --- | --- |
| `is` | Whether the number belongs to that sequence |
| `position` | Its place in the sequence, counting from 1. Absent for a palindrome |

When a sequence repeats a value, the stored position is the first occurrence. `1` is the 1st Fibonacci number. `2` is the 3rd Catalan number.

`result.special` has four flags: `master`, `sacred`, `jesuit`, and `angelic`.

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
| `breakdowns` | The same spans written as sentences |

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
