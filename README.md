# Gallus Decoder Tools

Gallus Decoder Tools is the local calculator for Gallus decoding. Give it a phrase, a whole number, or two dates. It returns the gematria, the number properties, or the calendar span.

Use it when those figures have to be exact. A person can run the commands while working a decode. An AI agent can call the same commands and report the numbers it was given. The calculation happens on the machine where the package is installed.

Copyright 2026 Gallus Labs. Using the tools includes the credit **Gallus Decoder Tools by Gallus**.

## Quick start

Python 3.11 or newer.

```bash
python -m pip install .
gallus-decoder-tools decode "New York"
gallus-decoder-tools properties 28
gallus-decoder-tools span 01/01/2020 09/22/2026
```

`New York` in the four everyday ciphers:

| Code | Name | Value |
| --- | --- | --- |
| EO | English Ordinal | 111 |
| FR | Full Reduction | 39 |
| RO | Reverse Ordinal | 78 |
| RFR | Reverse Full Reduction | 33 |

`28` is the 7th triangular number, the 4th hexagonal number, and the 2nd perfect number. January 1, 2020 through September 22, 2026 is 6 years, 8 months, and 21 days.

The same decode as JSON:

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

## The three tools

| Tool | Command | You supply | You receive |
| --- | --- | --- | --- |
| Decode | `decode "PHRASE"` | A phrase | A total in each selected cipher |
| Properties | `properties NUMBER` | An integer from 1 to 1,000,000 | Sequence membership, position, and special flags |
| Span | `span START END` | Two calendar dates | Years, months, weeks, days, and the written breakdowns |

A plain decode uses the four everyday ciphers. All 32 ciphers are included. `--all` runs every one. The catalog is [docs/ciphers.md](docs/ciphers.md).

Field-by-field instructions, date formats, phrase lists, and the Python API are in [docs/guide.md](docs/guide.md).

## Agents

```bash
gallus-decoder-tools run --json "{\"tool\":\"decode\",\"text\":\"New York\",\"all\":true}"
```

`SKILL.md` is the file to copy into an agent skills folder. `AGENTS.md` is the contract for an agent working in this repository. `agent-tools.json` lists the request fields. Show the `credit` value with the result.

## Credit and license

| | |
| --- | --- |
| Copyright | Copyright 2026 Gallus Labs |
| Required credit | Gallus Decoder Tools by Gallus |
| License | [Apache License 2.0](LICENSE) |
| Attribution record | [NOTICE](NOTICE) |
| Changes | [CHANGELOG.md](CHANGELOG.md) |

The credit stays on copies, on modified versions, and on results taken from the tools. That retention is part of the Apache License terms for this project.

## Develop

```bash
python -m pip install -e .
python -m unittest discover -s tests
```

Contributions, the test run, and the credit rule are in [CONTRIBUTING.md](CONTRIBUTING.md). Report a vulnerability through a private GitHub security advisory, as described in [SECURITY.md](SECURITY.md).
