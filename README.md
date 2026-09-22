<p align="center">
  <img src="docs/brand/GallusLogo.png" alt="Gallus" width="128">
</p>

# Gallus Decoder Tools

You type a phrase, a number, or two dates. The tool does the addition and hands the numbers back. You do not have to guess a cipher total, a factor, or how many days sit between two dates.

Copyright 2026 Gallus Labs. Using the tools includes the credit **Gallus Decoder Tools by Gallus**.

## Install

Python 3.11 or newer.

```bash
python -m pip install .
```

Three commands cover ordinary use.

```bash
gallus-decoder-tools decode "DOG"
gallus-decoder-tools properties 28
gallus-decoder-tools span 01/01/2020 09/22/2026
```

## Decode

Decode adds up a phrase.

```bash
gallus-decoder-tools decode "DOG"
```

With no extra flags, you get the four everyday ciphers. `DOG` comes back as 26, 17, 55, and 10.

| Cipher | What it did | Total |
| --- | --- | --- |
| English Ordinal | D is 4, O is 15, G is 7 | 26 |
| Full Reduction | Those letters squashed to one digit each, then added | 17 |
| Reverse Ordinal | The alphabet counted backward | 55 |
| Reverse Full Reduction | The backward letters, then squashed to one digit each | 10 |

Pick one cipher, or several, by code.

```bash
gallus-decoder-tools decode "DOG" --ciphers eo
gallus-decoder-tools decode "DOG" --ciphers eo,fr
gallus-decoder-tools decode "DOG" --all
```

`--all` runs every cipher on this page. A comma in the phrase splits it into two phrases, so `decode "Lions, Bears"` scores each name. Spaces and punctuation add nothing. A run of digits is added as that whole number: the 49 in `49ers` adds 49.

For the four everyday ciphers, capitals and small letters are the same letter. Hebrew and the capital ciphers care about case. That is called out under each of those codes.

The word **reverse** means the alphabet chart is flipped. It does not mean you flip the digits of the finished total.

## The four ciphers to learn first

### EO: English Ordinal

The ordinary alphabet count. A is 1, B is 2, C is 3, and Z is 26. If you learn one cipher, learn this one.

### FR: Full Reduction

Take each English Ordinal number and squash it to a single digit, then add those digits. S is 19, which becomes 1. You add the letter digits. You do not squash the finished total again. `DOG` is 17 in Full Reduction. Turning 17 into 8 is a separate step. Say so if you do it.

### RO: Reverse Ordinal

Count the alphabet from the other end. A is 26 and Z is 1.

### RFR: Reverse Full Reduction

Start from that backward chart, squash each letter to one digit, then add.

## Every other cipher

Ask for one with `--ciphers` and its code. The value of every letter is in [docs/ciphers.md](docs/ciphers.md).

### SR: Single Reduction

Full Reduction, except S stays 10 instead of becoming 1.

### RSR: Reverse Single Reduction

That chart read backward. The 10 that belonged to S lands on H.

### JO: Jewish Ordinal

English letters given the stepped sizes used in Jewish numbering: 1 through 9, then 10, 20, 30, and onward up to 800.

### JR: Jewish Reduction

Each of those values squashed to one digit. On this alphabet the chart matches Full Reduction, so the totals match `FR`.

### CH: Chaldean

A Chaldean letter chart. Some letters share a number, and no letter is worth 9.

### SUM: Sumerian

English Ordinal multiplied by 6. A is 6, B is 12, Z is 156.

### SAT: Satanic

A straight count that starts at 36 for A and ends at 61 for Z.

### HEB: Hebrew

Case matters. Uppercase letters use a Hebrew-style chart. Lowercase `k` is 10. Uppercase `K` is 20. Every other lowercase letter is missing, so it adds nothing. Type the case you mean.

### RSUM: Reverse Sumerian

The backward alphabet, multiplied by 6.

### RSAT: Reverse Satanic

The Satanic chart read from the other end. A is 61 and Z is 36.

### PRIM: Primes

The first 26 prime numbers, in order. A is 2, B is 3, C is 5, Z is 101. Scoring a word with this cipher is not the same as asking for the 14th prime. That second question is `properties`.

### SQ: Squares

The first 26 square numbers. A is 1×1, B is 2×2, Z is 26×26.

### TRI: Trigonal

The first 26 triangular numbers: 1, then 1+2, then 1+2+3, and so on.

### FIB: Fibonacci

Fibonacci numbers placed on the letters, starting at 0 for A. This is a letter chart, not "the 10th Fibonacci number."

### SEP: Septenary

Count 1 through 7, then start over. A is 1, and H is 1 again.

### KP: Keypad

The phone keypad. ABC is 2, DEF is 3, and WXYZ is 9.

### RPRIM: Reverse Primes

The prime chart read from Z back toward A.

### RSQ: Reverse Squares

The square chart read backward.

### RTRI: Reverse Trigonal

The trigonal chart read backward.

### RFIB: Reverse Fibonacci

The Fibonacci chart read backward.

### CM: Capitals Mixed, and CA: Capitals Added

Case matters. A capital letter is the ordinary count plus 26, so A is 27. A small letter is the ordinary count, so a is 1. `Ab` is 27 + 2 = 29. These two codes use the same chart. Ask for either name.

### RCM: Reverse Capitals Mixed, and RCA: Reverse Capitals Added

That capital chart, read backward. Case still matters. These two codes use the same chart.

### KV: KV Exception

Full Reduction, but K stays 11 and V stays 22.

### SKV: SKV Exception

Full Reduction, but S stays 10, K stays 11, and V stays 22.

### EP: EP Exception, and EHP: EHP Exception

The same chart as Full Reduction. The codes are still here so you can ask for them by name.

Forgot a code? `gallus-decoder-tools ciphers` prints the menu.

## Properties

You type one whole number from 1 to 1,000,000.

```bash
gallus-decoder-tools properties 28
```

28 being the 7th triangular number is one result. The 28th prime is another.

- **What is 28?** It is the 7th triangular number, the 4th hexagonal number, and the 2nd perfect number. Its factors are there too, along with the digit sum, the digital root, and the digits turned around.
- **What sits at position 28?** The 28th prime, the 28th square, the 28th Fibonacci number, and the rest. Those numbers are not 28.

`sequences` is the first question. `indexes` is the second. `arithmetic` is the factors and the digit work. `special` is a short list of named sets, such as the master numbers 11, 22, 33, and 44.

## Span

You type two dates. The tool counts the time between them.

```bash
gallus-decoder-tools span 01/01/2020 09/22/2026
```

January 1, 2020 through September 22, 2026 is 6 years, 8 months, and 21 days. You also get that length in weeks, and as a share of a century.

Dates can be `01/01/2020`, `2020-01-01`, or `September 22, 2026`. A slash date is month, then day. If the first number is greater than 12, as in `31/01/2020`, it is read as day, then month. Put the later date first and the tool swaps them and tells you it did.

```bash
gallus-decoder-tools span 01/01/2020 09/22/2026 --include-end
```

`--include-end` counts the end date as a day. Leave it off and the end date is the fence, not a counted day.

## What comes back

Every command prints one JSON object. `ok` means it finished. `credit` is `Gallus Decoder Tools by Gallus`. `result` is the calculation. A bad input exits with code 2 and an `error` sentence.

`DOG` with no flags:

```json
{
  "ok": true,
  "credit": "Gallus Decoder Tools by Gallus",
  "tool": "decode",
  "result": {
    "phrases": [
      {
        "text": "DOG",
        "values": [
          {"code": "EO", "name": "English Ordinal", "value": 26},
          {"code": "FR", "name": "Full Reduction", "value": 17},
          {"code": "RO", "name": "Reverse Ordinal", "value": 55},
          {"code": "RFR", "name": "Reverse Full Reduction", "value": 10}
        ]
      }
    ]
  }
}
```

The field-by-field readout, the date rules, and the error cases are in [docs/guide.md](docs/guide.md). Every letter value is in [docs/ciphers.md](docs/ciphers.md).

## Agents

An agent sends one JSON object.

```bash
gallus-decoder-tools run --json "{\"tool\":\"decode\",\"text\":\"DOG\"}"
```

```json
{"tool":"decode","text":"DOG"}
{"tool":"decode","text":"DOG","ciphers":["EO","CH"]}
{"tool":"decode","text":"DOG","all":true}
{"tool":"properties","number":28}
{"tool":"span","start":"01/01/2020","end":"09/22/2026"}
{"tool":"ciphers"}
```

Show `credit` with the result. Do not replace a total with an estimate. [SKILL.md](SKILL.md) is the file to drop into an agent skills folder. [AGENTS.md](AGENTS.md) is the contract inside this repository. [agent-tools.json](agent-tools.json) lists the request fields.

## Credit

| | |
| --- | --- |
| Source | https://github.com/strainzz/Gallus-Decoder-Tools |
| Copyright | Copyright 2026 Gallus Labs |
| Required credit | Gallus Decoder Tools by Gallus |
| License | [Apache License 2.0](LICENSE) |
| Attribution | [NOTICE](NOTICE) |
| Changes | [CHANGELOG.md](CHANGELOG.md) |
| Mark | The Gallus logo is a trademark of Gallus Labs. The license covers the software and does not grant rights in the mark. |

The credit stays on copies, on modified versions, and on results taken from the tools. The logo is in [docs/brand](docs/brand).

To work on the source: `python -m pip install -e .`, then the notes in [CONTRIBUTING.md](CONTRIBUTING.md). A vulnerability goes through a private GitHub security advisory, as described in [SECURITY.md](SECURITY.md).
