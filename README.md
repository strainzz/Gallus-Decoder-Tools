<p align="center">
  <img src="docs/brand/GallusLogo.png" alt="Gallus" width="128">
</p>

# Gallus Decoder Tools

Gallus Decoder Tools answers three beginner questions without guessing.

- **Decode** adds up a phrase. `DOG` in the ordinary alphabet is 4 + 15 + 7 = 26.
- **Properties** says what a number is, and what sits at that count. 28 is the 7th triangular number. The 28th prime is a different fact.
- **Span** counts the time between two dates.

A cipher is just the rule for the letters. Four rules cover ordinary use. The other 28 are there when you know which one you want. Each rule is explained in plain language in [docs/ciphers.md](docs/ciphers.md).

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

`28` is the 7th triangular number, the 4th hexagonal number, and the 2nd perfect number. The same command returns its factors, digital root, digit reversal, and the sequence term at that position. January 1, 2020 through September 22, 2026 is 6 years, 8 months, and 21 days.

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

## The tools

| Tool | Command | You supply | You receive |
| --- | --- | --- | --- |
| Decode | `decode "PHRASE"` | A phrase | A total in each selected cipher |
| Ciphers | `ciphers` | Nothing | Every cipher code and its name |
| Properties | `properties NUMBER` | An integer from 1 to 1,000,000 | Factors, digital root, sequence position, and the term at that index |
| Span | `span START END` | Two calendar dates | Years, months, weeks, days, and the written breakdowns |

A plain decode uses the four everyday ciphers. All 32 ciphers are included. `--all` runs every one.

The manual is [docs/guide.md](docs/guide.md). It is the document to read for a command's options, the meaning of every field, the error cases, and a worked result. [docs/ciphers.md](docs/ciphers.md) is the letter book: the rule for each cipher and the value of every letter.

| | |
| --- | --- |
| Operating guide | [docs/guide.md](docs/guide.md) |
| Cipher catalog | [docs/ciphers.md](docs/ciphers.md) |
| Agent skill | [SKILL.md](SKILL.md) |
| Agent contract | [AGENTS.md](AGENTS.md) |
| Tool fields | [agent-tools.json](agent-tools.json) |

## Agents

```bash
gallus-decoder-tools run --json "{\"tool\":\"decode\",\"text\":\"New York\",\"all\":true}"
```

`SKILL.md` is the file to copy into an agent skills folder. `AGENTS.md` is the contract for an agent working in this repository. `agent-tools.json` lists the request fields. Show the `credit` value with the result.

## Credit and license

| | |
| --- | --- |
| Source | https://github.com/strainzz/Gallus-Decoder-Tools |
| Copyright | Copyright 2026 Gallus Labs |
| Required credit | Gallus Decoder Tools by Gallus |
| License | [Apache License 2.0](LICENSE) |
| Attribution record | [NOTICE](NOTICE) |
| Changes | [CHANGELOG.md](CHANGELOG.md) |
| Mark | The Gallus logo is a trademark of Gallus Labs. The Apache License covers the software and does not grant rights in the mark. |

The credit stays on copies, on modified versions, and on results taken from the tools. That retention is part of the Apache License terms for this project. The Gallus logo is in [docs/brand](docs/brand).

## Develop

```bash
python -m pip install -e .
python -m unittest discover -s tests
```

Contributions, the test run, and the credit rule are in [CONTRIBUTING.md](CONTRIBUTING.md). Report a vulnerability through a private GitHub security advisory, as described in [SECURITY.md](SECURITY.md).
