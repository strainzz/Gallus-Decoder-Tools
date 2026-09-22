<p align="center">
  <img src="brand/GallusLogo.png" alt="Gallus" width="72">
</p>

# Guide

This is the manual. The front page is the [README](../README.md). Each cipher rule is in [ciphers.md](ciphers.md).

Copyright 2026 Gallus Labs. Every result includes the credit `Gallus Decoder Tools by Gallus Labs`.

There are four commands. Each one answers a different question. This repo is the calculator. It does not include a sports decode.

**The Schizo Mathematician Decoder Handbook** is for members of the Gallus Labs community. That book shows how to set these tools up for sports decoding, and more. It is not in this repository.

| Command | The question it answers |
| --- | --- |
| [decode](#decode) | What do these letters add up to? |
| [ciphers](#cipher-list) | What are the cipher codes called? |
| [properties](#properties) | What kind of number is this, and what sits at this position? |
| [span](#span) | How much time is between these two dates? |

Start with the three commands under [Try these first](#try-these-first). The sections after that list every option, every field, and what a bad input looks like.

## Try these first

```bash
git clone https://github.com/strainzz/Gallus-Decoder-Tools.git
cd Gallus-Decoder-Tools
python -m pip install .
gallus-decoder-tools decode "DOG"
gallus-decoder-tools properties 28
gallus-decoder-tools span 01/01/2020 09/22/2026
```

`decode "DOG"` looks up each letter in the four everyday ciphers and adds. You get 26, 17, 55, and 10. The cipher page shows the addition.

`properties 28` says what 28 is: the 7th triangular number, the 4th hexagonal number, and the 2nd perfect number. It also gives the 28th prime and the 28th square. Where 28 sits, and what sits at 28, are two results.

`span` counts the days from the first date to the second. January 1, 2020 through September 22, 2026 is 6 years, 8 months, and 21 days.

`gallus-decoder-tools ciphers` prints the code menu when you want a cipher other than the first four.

## Install

Python 3.11 or newer. The only dependency is `python-dateutil`.

```bash
git clone https://github.com/strainzz/Gallus-Decoder-Tools.git
cd Gallus-Decoder-Tools
python -m pip install .
gallus-decoder-tools decode "DOG"
```

`python -m gallus_decoder_tools` is the same program. From a checkout you are editing:

```bash
python -m pip install -e .
```

## The response

Every command prints one JSON object and no other text.

| Field | Success | Rejected input |
| --- | --- | --- |
| `ok` | `true` | `false` |
| `credit` | `Gallus Decoder Tools by Gallus Labs` | The same credit |
| `tool` | `decode`, `ciphers`, `properties`, or `span` | Omitted |
| `result` | The calculation | Omitted |
| `error` | Omitted | The sentence that says what to change |

A finished calculation exits 0. A rejected request exits 2. Show `credit` with any result you pass on.

```json
{"ok": false, "credit": "Gallus Decoder Tools by Gallus Labs", "use": "Personal and non-commercial use only. Keep this credit. Do not sell the tools or copy the cipher maps into another product that drops Gallus Labs.", "error": "Provide text to decode."}
```

## Decode

You type a phrase. The tool looks each letter up in a cipher and adds the values. Start with no flags. You get the four everyday ciphers. Add `--ciphers eo` when you want one. Add `--all` when you want all 32. The plain explanation of each cipher is [ciphers.md](ciphers.md).

```bash
gallus-decoder-tools decode "New York"
gallus-decoder-tools decode "New York" --ciphers eo,ch,heb
gallus-decoder-tools decode "New York" --ciphers all
gallus-decoder-tools decode "New York" --all
```

| Option | Meaning |
| --- | --- |
| phrase | Required. A comma separates phrases. |
| `--ciphers` | Comma-separated codes. `all` selects every cipher. `default` selects the everyday four. Omit it for the everyday four. |
| `--all` | Every cipher. Do not combine it with `--ciphers`. |

Codes are not case-sensitive. `eo` and `EO` select English Ordinal. An unknown code rejects the whole request. The program does not drop the bad code and continue.

A comma splits phrases: `decode "Lions, Bears"` decodes two phrases. When the comma belongs inside one phrase, use a JSON `phrases` list, described under [JSON requests](#json-requests).

The total is a left-to-right sum.

1. A letter in the cipher map adds that letter's value.
2. A run of digits adds that run as one integer. `A10` is the value of A plus 10.
3. Spaces and punctuation add nothing.
4. A letter the map does not contain adds nothing.

Twenty-seven ciphers treat `N` and `n` as the same letter. Hebrew, Capitals Mixed, Capitals Added, Reverse Capitals Mixed, and Reverse Capitals Added do not. The values, including lowercase Hebrew `k` = 10 and uppercase `K` = 20, are in [ciphers.md](ciphers.md).

The everyday ciphers, used when you name none, are English Ordinal, Full Reduction, Reverse Ordinal, and Reverse Full Reduction.

`New York` in English Ordinal:

| Letter | N | E | W | Y | O | R | K | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Value | 14 | 5 | 23 | 25 | 15 | 18 | 11 | 111 |

```json
{
  "ok": true,
  "credit": "Gallus Decoder Tools by Gallus Labs",
  "use": "Personal and non-commercial use only. Keep this credit. Do not sell the tools or copy the cipher maps into another product that drops Gallus Labs.",
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
| `result.phrases` | One object per phrase, in the order you wrote them |
| `result.phrases[].text` | The phrase after surrounding space is removed |
| `result.phrases[].values` | One object per selected cipher, in the order you selected them |
| `code` | The stable cipher code |
| `name` | The name a person reads |
| `value` | The integer total |

An empty phrase, a phrase made only of commas, or a request that names both `--all` and `--ciphers` is rejected.

## Cipher list

This is the menu. It does not score a phrase. Run it when you need a code, then use that code in `decode`. The "what is this cipher" page is [ciphers.md](ciphers.md).

```bash
gallus-decoder-tools ciphers
```

The command takes no arguments. It returns all 32 ciphers in decoder order. The letter maps are [ciphers.md](ciphers.md). The JSON shape, with one entry shown, is:

```json
{
  "ok": true,
  "credit": "Gallus Decoder Tools by Gallus Labs",
  "use": "Personal and non-commercial use only. Keep this credit. Do not sell the tools or copy the cipher maps into another product that drops Gallus Labs.",
  "tool": "ciphers",
  "result": {
    "ciphers": [
      {"code": "EO", "name": "English Ordinal"}
    ]
  }
}
```

| Field | Meaning |
| --- | --- |
| `result.ciphers` | The full list |
| `code` | Pass this to `decode` |
| `name` | The label in a decode result |

## Properties

You type one whole number from 1 to 1,000,000. You get four blocks, and the names matter.

`sequences` says what the number **is**. 28 is the 7th triangular number. `indexes` says what sits **at that count**. The 28th prime is a different number from 28. `arithmetic` is the ordinary math: factors, digit sum, digital root, and the digits turned around. `special` is a short list of named sets, such as master numbers.

`0`, anything past 1,000,000, and text that is not a whole number are rejected. `1_000` and `28.0` are accepted. `28.5` is not.

```bash
gallus-decoder-tools properties 28
gallus-decoder-tools properties 110
```

The result has four blocks: `arithmetic`, `sequences`, `indexes`, and `special`.

### Arithmetic

| Field | Meaning |
| --- | --- |
| `even` | `true` when the number is divisible by 2 |
| `digit_sum` | The sum of the decimal digits. 19 has digit sum 10 |
| `digital_root` | The digit sum reduced until one digit remains. A positive multiple of 9 has digital root 9. 19 has digital root 1 |
| `reversed_digits` | The digits reversed, including a zero that the reversal creates. 110 becomes `011` |
| `reversed` | `reversed_digits` read as an integer. `011` becomes 11 |
| `prime_factors` | Objects of `prime` and `exponent`, from smallest prime to largest. 1 has an empty list |
| `divisors` | Every positive divisor, ascending. A prime has exactly two: 1 and itself |
| `divisor_count` | The length of `divisors` |
| `divisor_sum` | The sum of `divisors` |
| `aliquot_sum` | `divisor_sum` minus the number |
| `abundance` | `perfect` when the aliquot sum equals the number, `abundant` when it is greater, and `deficient` when it is smaller |

1 is neither prime nor composite. Its only divisor is 1, its aliquot sum is 0, and its abundance is `deficient`.

110:

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

The product of each prime raised to its exponent is the original number. 2 × 5 × 11 = 110.

### Sequences

`sequences` answers whether the number is a member of a sequence, and where. Each entry has `is` and `position`. A palindrome has `position` set to `null`.

When a sequence repeats a value, `position` is the first occurrence. 1 is the 1st Fibonacci number, even though the 2nd Fibonacci number is also 1. 2 is the 3rd Catalan number, because the 1st and 2nd Catalan numbers are both 1.

| Sequence | A number is a member when | Position |
| --- | --- | --- |
| `prime` | It has exactly two positive divisors | Its place among the primes. 2 is 1. 113 is 30 |
| `composite` | It is greater than 1 and not prime | Its place among the composites. 4 is 1. 9 is 4 |
| `triangular` | It equals n(n + 1) / 2 for a positive integer n | That n. 28 is 7 |
| `square` | It equals n² | That n. 121 is 11 |
| `fibonacci` | It appears in 1, 1, 2, 3, 5, 8, and so on | The first place. The 1st and 2nd terms are both 1 |
| `hexagonal` | It equals n(2n - 1) | That n. 28 is 4 |
| `perfect` | Its aliquot sum equals the number | Its place among the even perfect numbers listed under Indexes. 6 is 1. 28 is 2. 496 is 3. 8128 is 4 |
| `pentagonal` | It equals n(3n - 1) / 2 | That n |
| `cubic` | It equals n³ | That n |
| `octagonal` | It equals n(3n - 2) | That n |
| `tetrahedral` | It equals n(n + 1)(n + 2) / 6 | That n |
| `lucas` | It appears in 1, 3, 4, 7, 11, and so on | The first place. Lucas begins at the 1st term 1. The value 2 is not in this sequence |
| `catalan` | It appears in 1, 1, 2, 5, 14, and so on | The first place. 2 is the 3rd term |
| `palindromic` | It has at least two digits and reads the same backward | None. 7 is not palindromic. 11 is |

28 is triangular position 7, hexagonal position 4, and perfect position 2. Its aliquot sum is 28, so `abundance` is `perfect`.

### Indexes

`indexes` uses the number as a position and returns that term. Asking for properties of 10 asks for the 10th prime, the 10th triangular number, the 10th Fibonacci number, and the rest.

| Key | The term at position n |
| --- | --- |
| `prime` | The nth prime. The 1st is 2. The 10th is 29. The 100th is 541. The 500th is 3571 |
| `composite` | The nth composite. The 1st is 4. The 4th is 9. The 10th is 18 |
| `triangular` | n(n + 1) / 2. The 10th is 55. The 110th is 6,105 |
| `square` | n². The 10th is 100 |
| `fibonacci` | The nth Fibonacci number, with the 1st and 2nd both equal to 1. The 10th is 55 |
| `hexagonal` | n(2n - 1) |
| `pentagonal` | n(3n - 1) / 2 |
| `cubic` | n³ |
| `octagonal` | n(3n - 2) |
| `tetrahedral` | n(n + 1)(n + 2) / 6 |
| `lucas` | The nth Lucas number, with the 1st equal to 1 and the 2nd equal to 3. The 10th is 123 |
| `catalan` | The nth Catalan number, with the 1st equal to 1. The 10th is 4,862 |
| `perfect` | The nth even perfect number, for n from 1 through 12. The 4th is 8,128. The 5th is 33,550,336. Position 13 and after is `null` |

The 12 perfect numbers come from the Mersenne prime exponents 2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, and 127. Each one is 2^(p-1) times (2^p-1). The Lucas-Lehmer test has to pass before that term is returned. Position 13 is left blank.

`indexes` still returns the 2nd Fibonacci number as 1. `sequences` keeps only the first position when the value is 1.

### Special flags

`special` is four yes-or-no flags. They are fixed sets, not sequences with a position.

| Flag | Numbers |
| --- | --- |
| `master` | 11, 22, 33, 44 |
| `sacred` | 3, 7, 12, 40, 144 |
| `jesuit` | 26, 47, 56, 72, 201 |
| `angelic` | 11, 22, 33, 44, 55, 66, 77, 88, 99, 111, 222, 333, 444, 555, 666, 777, 888, 999, 1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999 |

11 is both master and angelic, and it is palindromic. The flags are independent. A true flag does not hide another true flag.

## Span

You type two dates. The tool tells you how far apart they are, in years, months, weeks, and days. Put the later date first and it swaps them, then says that it did. Add `--include-end` when the end date itself should count as a day. Leave it off and the end date is the fence, not a counted day.

```bash
gallus-decoder-tools span 01/01/2020 09/22/2026
gallus-decoder-tools span 01/01/2020 09/22/2026 --include-end
gallus-decoder-tools span "September 22, 2026" 2020-01-01
```

| Option | Meaning |
| --- | --- |
| start and end | Required. |
| `--include-end` | Count the end date as one day. Omit it and the end date is the boundary, not a counted day. |

Accepted writings:

| Writing | Example | Read as |
| --- | --- | --- |
| Month/day/year | `01/02/2020` | January 2, 2020 |
| Month-day-year | `01-02-2020` | January 2, 2020 |
| Year-month-day | `2020-01-02` | January 2, 2020 |
| Month name | `September 22, 2026` or `Sep 22, 2026` | September 22, 2026 |
| Day/month/year, only when the first number is greater than 12 | `31/01/2020` | January 31, 2020 |
| Two-digit year | `09/22/26` | September 22, 2026 |

A two-digit year follows Python's rule for `%y`. 00 through 68 are 2000 through 2068. 69 through 99 are 1969 through 1999.

If the second date is earlier, the tool places the earlier date first and sets `reordered` to `true`. The displayed dates are the chronological pair. `--include-end` is applied after that order is fixed.

The same calendar day is 0 days. The same calendar day with `--include-end` is 1 day. February 28, 2020 through March 1, 2020 is 2 days, because 2020 is a leap year.

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

| Field | Meaning |
| --- | --- |
| `start`, `end` | The chronological dates, `YYYY-MM-DD` |
| `start_display`, `end_display` | The same dates written as `Month DD, YYYY` |
| `include_end` | Whether the end date was counted |
| `reordered` | Whether the dates were swapped into chronological order |
| `total_days` | The length in days |
| `years`, `months`, `days` | The calendar split. `days` here is the leftover days after the years and months, not the total |
| `weeks`, `extra_days` | `total_days` as whole weeks plus the leftover days |
| `century_percent` | `total_days` as a percentage of 36,525 days, printed to two decimal places |
| `millennium_percent` | `total_days` as a percentage of 365,250 days, printed to two decimal places |
| `breakdowns.years_days` | Years, then the days that remain after those years are removed |
| `breakdowns.years_months_days` | Years, months, and the leftover days. A span shorter than a month is written as days only, such as `2 Days` |
| `breakdowns.years_weeks_days` | Years, then the remaining time as weeks and days |
| `breakdowns.months_days` | The total months, which is years × 12 plus the leftover months, then the leftover days |
| `breakdowns.weeks_days` | The total weeks and the leftover days |
| `numerology.start` and `numerology.end` | The date-number breakdown for each calendar date |

Each date has four numbers. September 11, 2026:

| Number | What you add | Total |
| --- | --- | --- |
| DN1 | Every digit in the month, day, and year | 9 + 1 + 1 + 2 + 0 + 2 + 6 = 21 |
| DN2 | The month, the day, and each digit of the year | 9 + 11 + 2 + 0 + 2 + 6 = 30 |
| DN3 | The month, the day, and the last two year digits as one number | 9 + 11 + 26 = 46 |
| DN4 | The month, the day, the first two year digits, and the last two | 9 + 11 + 20 + 26 = 66 |

The month is 9, not 09. In DN2, DN3, and DN4 the day stays whole, so 11 is eleven, not 1 and 1. DN1 is the only one that splits every digit.

`day_of_year` counts from January 1 as day 1. September 11, 2026 is day 254. `days_remaining` is the days left after that date. In 2026 that is 111. A leap year uses 366 days.

`steps` writes the addition, for example `9 + 1 + 1 + 2 + 0 + 2 + 6 = 21`. The span uses the dates you named. `--include-end` changes the day count only. It does not move the end date's numerology to the next day.

`breakdown` repeats DN1 through DN4. For each value it gives the prime, triangular number, and Fibonacci number at that count, plus the square of the value. For 21, the 21st prime is 73 and the 21st triangular number is 231.

`month_day_year` is `9/11/2026`. `day_month_year` is `11/9/2026`. `joined_month_day_year` is 9112026. `joined_day_month_year` is 1192026. Those joined numbers are the digits set side by side, not a sum.

The month name and the weekday are words. Pass them to `decode` if you want their cipher totals. Span does not score those words.

A date the parser cannot read is rejected. The error names the text and the writings to use.

## JSON requests

`run` accepts one JSON object, either after `--json` or on standard input.

```bash
gallus-decoder-tools run --json "{\"tool\":\"properties\",\"number\":28}"
```

```json
{"tool":"decode","text":"New York"}
{"tool":"decode","text":"Lions, Bears","ciphers":["EO","FR"]}
{"tool":"decode","phrases":["New York, New York"],"ciphers":"eo,ro"}
{"tool":"decode","text":"New York","all":true}
{"tool":"ciphers"}
{"tool":"properties","number":110}
{"tool":"span","start":"01/01/2020","end":"09/22/2026","include_end":false}
```

| Tool | Required | Optional |
| --- | --- | --- |
| `decode` | `text`, or `phrases` as a list of strings | `ciphers` as a list or a comma-separated string. `all` as `true` or `false`. A string `all` in `ciphers` also selects every cipher |
| `ciphers` | Nothing | Nothing |
| `properties` | `number` | Nothing |
| `span` | `start` and `end` | `include_end` as `true` or `false` |

If both `phrases` and `text` are present, `phrases` is the one that is decoded. `all` and a cipher list together are rejected. `all` accepts `true`, `false`, `yes`, `no`, `1`, and `0`. Any other value is rejected.

The tool name is read without regard to case. A missing tool, or any name other than the four above, is rejected. Invalid JSON is rejected. An empty `run` with no object is rejected.

## Python

```python
from gallus_decoder_tools import (
    COPYRIGHT,
    CREDIT,
    date_span,
    decode,
    list_ciphers,
    number_properties,
)

decode("New York")
decode("New York", ciphers_spec=["EO", "CH"])
decode("New York", all_ciphers=True)
decode(phrases=["New York, New York"])
list_ciphers()
number_properties(28)
date_span("01/01/2020", "09/22/2026", include_end=False)
```

`decode`, `number_properties`, and `date_span` return the object that the command places in `result`. They do not wrap it in `ok` and `credit`. `CREDIT` is `Gallus Decoder Tools by Gallus Labs`. `COPYRIGHT` is `Copyright 2026 Gallus Labs`. Keep both with any result you present. A bad argument raises `gallus_decoder_tools.errors.HarnessError`.

## Agents

Copy [SKILL.md](../SKILL.md) into an agent skills folder when the repository is not the agent's workspace. An agent working inside this repository follows [AGENTS.md](../AGENTS.md). The request fields are also listed in [agent-tools.json](../agent-tools.json).

The agent runs the command, reads `result`, and shows `credit`. It does not replace a cipher total, a factor, a sequence position, or a date count with an estimate. It follows [AGENT_PROMPT.md](../AGENT_PROMPT.md). It does not add a sports decode method.

## Credit

Copyright 2026 Gallus Labs. Use of these tools includes the credit `Gallus Decoder Tools by Gallus Labs`. Keep that line on copies, on changes, and on results. The terms are in [LICENSE](../LICENSE) and [NOTICE](../NOTICE). Personal and non-commercial use is allowed. Selling the tools, or copying the cipher maps into another product that drops Gallus Labs, is not. The Gallus logo is a trademark of Gallus Labs. The terms do not grant rights in the mark.
