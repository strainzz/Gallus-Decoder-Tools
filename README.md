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

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 1 | N | 14 |
| B | 2 | O | 15 |
| C | 3 | P | 16 |
| D | 4 | Q | 17 |
| E | 5 | R | 18 |
| F | 6 | S | 19 |
| G | 7 | T | 20 |
| H | 8 | U | 21 |
| I | 9 | V | 22 |
| J | 10 | W | 23 |
| K | 11 | X | 24 |
| L | 12 | Y | 25 |
| M | 13 | Z | 26 |

### FR: Full Reduction

Take each English Ordinal number and squash it to a single digit, then add those digits. S is 19, which becomes 1. You add the letter digits. You do not squash the finished total again. `DOG` is 17 in Full Reduction. Turning 17 into 8 is a separate step. Say so if you do it.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 1 | N | 5 |
| B | 2 | O | 6 |
| C | 3 | P | 7 |
| D | 4 | Q | 8 |
| E | 5 | R | 9 |
| F | 6 | S | 1 |
| G | 7 | T | 2 |
| H | 8 | U | 3 |
| I | 9 | V | 4 |
| J | 1 | W | 5 |
| K | 2 | X | 6 |
| L | 3 | Y | 7 |
| M | 4 | Z | 8 |

### RO: Reverse Ordinal

Count the alphabet from the other end. A is 26 and Z is 1.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 26 | N | 13 |
| B | 25 | O | 12 |
| C | 24 | P | 11 |
| D | 23 | Q | 10 |
| E | 22 | R | 9 |
| F | 21 | S | 8 |
| G | 20 | T | 7 |
| H | 19 | U | 6 |
| I | 18 | V | 5 |
| J | 17 | W | 4 |
| K | 16 | X | 3 |
| L | 15 | Y | 2 |
| M | 14 | Z | 1 |

### RFR: Reverse Full Reduction

Start from that backward chart, squash each letter to one digit, then add.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 8 | N | 4 |
| B | 7 | O | 3 |
| C | 6 | P | 2 |
| D | 5 | Q | 1 |
| E | 4 | R | 9 |
| F | 3 | S | 8 |
| G | 2 | T | 7 |
| H | 1 | U | 6 |
| I | 9 | V | 5 |
| J | 8 | W | 4 |
| K | 7 | X | 3 |
| L | 6 | Y | 2 |
| M | 5 | Z | 1 |

## Every other cipher

Ask for one with `--ciphers` and its code. The grid under each name is the chart the program adds.

### SR: Single Reduction

Full Reduction, except S stays 10 instead of becoming 1.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 1 | N | 5 |
| B | 2 | O | 6 |
| C | 3 | P | 7 |
| D | 4 | Q | 8 |
| E | 5 | R | 9 |
| F | 6 | S | 10 |
| G | 7 | T | 2 |
| H | 8 | U | 3 |
| I | 9 | V | 4 |
| J | 1 | W | 5 |
| K | 2 | X | 6 |
| L | 3 | Y | 7 |
| M | 4 | Z | 8 |

### RSR: Reverse Single Reduction

That chart read backward. The 10 that belonged to S lands on H.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 8 | N | 4 |
| B | 7 | O | 3 |
| C | 6 | P | 2 |
| D | 5 | Q | 1 |
| E | 4 | R | 9 |
| F | 3 | S | 8 |
| G | 2 | T | 7 |
| H | 10 | U | 6 |
| I | 9 | V | 5 |
| J | 8 | W | 4 |
| K | 7 | X | 3 |
| L | 6 | Y | 2 |
| M | 5 | Z | 1 |

### JO: Jewish Ordinal

English letters given the stepped sizes used in Jewish numbering: 1 through 9, then 10, 20, 30, and onward up to 800.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 1 | N | 50 |
| B | 2 | O | 60 |
| C | 3 | P | 70 |
| D | 4 | Q | 80 |
| E | 5 | R | 90 |
| F | 6 | S | 100 |
| G | 7 | T | 200 |
| H | 8 | U | 300 |
| I | 9 | V | 400 |
| J | 10 | W | 500 |
| K | 20 | X | 600 |
| L | 30 | Y | 700 |
| M | 40 | Z | 800 |

### JR: Jewish Reduction

Each of those values squashed to one digit. On this alphabet the chart matches Full Reduction, so the totals match `FR`.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 1 | N | 5 |
| B | 2 | O | 6 |
| C | 3 | P | 7 |
| D | 4 | Q | 8 |
| E | 5 | R | 9 |
| F | 6 | S | 1 |
| G | 7 | T | 2 |
| H | 8 | U | 3 |
| I | 9 | V | 4 |
| J | 1 | W | 5 |
| K | 2 | X | 6 |
| L | 3 | Y | 7 |
| M | 4 | Z | 8 |

### CH: Chaldean

A Chaldean letter chart. Some letters share a number, and no letter is worth 9.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 1 | N | 5 |
| B | 2 | O | 7 |
| C | 3 | P | 8 |
| D | 4 | Q | 1 |
| E | 5 | R | 2 |
| F | 8 | S | 3 |
| G | 3 | T | 4 |
| H | 5 | U | 6 |
| I | 1 | V | 6 |
| J | 1 | W | 6 |
| K | 2 | X | 5 |
| L | 3 | Y | 1 |
| M | 4 | Z | 7 |

### SUM: Sumerian

English Ordinal multiplied by 6. A is 6, B is 12, Z is 156.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 6 | N | 84 |
| B | 12 | O | 90 |
| C | 18 | P | 96 |
| D | 24 | Q | 102 |
| E | 30 | R | 108 |
| F | 36 | S | 114 |
| G | 42 | T | 120 |
| H | 48 | U | 126 |
| I | 54 | V | 132 |
| J | 60 | W | 138 |
| K | 66 | X | 144 |
| L | 72 | Y | 150 |
| M | 78 | Z | 156 |

### SAT: Satanic

A straight count that starts at 36 for A and ends at 61 for Z.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 36 | N | 49 |
| B | 37 | O | 50 |
| C | 38 | P | 51 |
| D | 39 | Q | 52 |
| E | 40 | R | 53 |
| F | 41 | S | 54 |
| G | 42 | T | 55 |
| H | 43 | U | 56 |
| I | 44 | V | 57 |
| J | 45 | W | 58 |
| K | 46 | X | 59 |
| L | 47 | Y | 60 |
| M | 48 | Z | 61 |

### HEB: Hebrew

Case matters. Uppercase letters use a Hebrew-style chart. Lowercase `k` is 10. Uppercase `K` is 20. Every other lowercase letter is missing, so it adds nothing. Type the case you mean.

Uppercase

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 1 | N | 40 |
| B | 2 | O | 50 |
| C | 3 | P | 60 |
| D | 4 | Q | 70 |
| E | 5 | R | 80 |
| F | 6 | S | 90 |
| G | 7 | T | 100 |
| H | 8 | U | 200 |
| I | 9 | V | 700 |
| J | 600 | W | 800 |
| K | 20 | X | 300 |
| L | 20 | Y | 400 |
| M | 30 | Z | 500 |

Lowercase `k` is the only lowercase letter on this chart.

| Letter | Value |
| --- | --- |
| k | 10 |

### RSUM: Reverse Sumerian

The backward alphabet, multiplied by 6.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 156 | N | 78 |
| B | 150 | O | 72 |
| C | 144 | P | 66 |
| D | 138 | Q | 60 |
| E | 132 | R | 54 |
| F | 126 | S | 48 |
| G | 120 | T | 42 |
| H | 114 | U | 36 |
| I | 108 | V | 30 |
| J | 102 | W | 24 |
| K | 96 | X | 18 |
| L | 90 | Y | 12 |
| M | 84 | Z | 6 |

### RSAT: Reverse Satanic

The Satanic chart read from the other end. A is 61 and Z is 36.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 61 | N | 48 |
| B | 60 | O | 47 |
| C | 59 | P | 46 |
| D | 58 | Q | 45 |
| E | 57 | R | 44 |
| F | 56 | S | 43 |
| G | 55 | T | 42 |
| H | 54 | U | 41 |
| I | 53 | V | 40 |
| J | 52 | W | 39 |
| K | 51 | X | 38 |
| L | 50 | Y | 37 |
| M | 49 | Z | 36 |

### PRIM: Primes

The first 26 prime numbers, in order. A is 2, B is 3, C is 5, Z is 101. Scoring a word with this cipher is not the same as asking for the 14th prime. That second question is `properties`.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 2 | N | 43 |
| B | 3 | O | 47 |
| C | 5 | P | 53 |
| D | 7 | Q | 59 |
| E | 11 | R | 61 |
| F | 13 | S | 67 |
| G | 17 | T | 71 |
| H | 19 | U | 73 |
| I | 23 | V | 79 |
| J | 29 | W | 83 |
| K | 31 | X | 89 |
| L | 37 | Y | 97 |
| M | 41 | Z | 101 |

### SQ: Squares

The first 26 square numbers. A is 1×1, B is 2×2, Z is 26×26.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 1 | N | 196 |
| B | 4 | O | 225 |
| C | 9 | P | 256 |
| D | 16 | Q | 289 |
| E | 25 | R | 324 |
| F | 36 | S | 361 |
| G | 49 | T | 400 |
| H | 64 | U | 441 |
| I | 81 | V | 484 |
| J | 100 | W | 529 |
| K | 121 | X | 576 |
| L | 144 | Y | 625 |
| M | 169 | Z | 676 |

### TRI: Trigonal

The first 26 triangular numbers: 1, then 1+2, then 1+2+3, and so on.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 1 | N | 105 |
| B | 3 | O | 120 |
| C | 6 | P | 136 |
| D | 10 | Q | 153 |
| E | 15 | R | 171 |
| F | 21 | S | 190 |
| G | 28 | T | 210 |
| H | 36 | U | 231 |
| I | 45 | V | 253 |
| J | 55 | W | 276 |
| K | 66 | X | 300 |
| L | 78 | Y | 325 |
| M | 91 | Z | 351 |

### FIB: Fibonacci

Fibonacci numbers placed on the letters, starting at 0 for A. This is a letter chart, not "the 10th Fibonacci number."

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 0 | N | 233 |
| B | 1 | O | 377 |
| C | 1 | P | 610 |
| D | 2 | Q | 987 |
| E | 3 | R | 1597 |
| F | 5 | S | 2584 |
| G | 8 | T | 4181 |
| H | 13 | U | 6765 |
| I | 21 | V | 10946 |
| J | 34 | W | 17711 |
| K | 55 | X | 28657 |
| L | 89 | Y | 46368 |
| M | 144 | Z | 75025 |

### SEP: Septenary

Count 1 through 7, then start over. A is 1, and H is 1 again.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 1 | N | 7 |
| B | 2 | O | 1 |
| C | 3 | P | 2 |
| D | 4 | Q | 3 |
| E | 5 | R | 4 |
| F | 6 | S | 5 |
| G | 7 | T | 6 |
| H | 1 | U | 7 |
| I | 2 | V | 1 |
| J | 3 | W | 2 |
| K | 4 | X | 3 |
| L | 5 | Y | 4 |
| M | 6 | Z | 5 |

### KP: Keypad

The phone keypad. ABC is 2, DEF is 3, and WXYZ is 9.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 2 | N | 6 |
| B | 2 | O | 6 |
| C | 2 | P | 7 |
| D | 3 | Q | 7 |
| E | 3 | R | 7 |
| F | 3 | S | 7 |
| G | 4 | T | 8 |
| H | 4 | U | 8 |
| I | 4 | V | 8 |
| J | 5 | W | 9 |
| K | 5 | X | 9 |
| L | 5 | Y | 9 |
| M | 6 | Z | 9 |

### RPRIM: Reverse Primes

The prime chart read from Z back toward A.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 101 | N | 41 |
| B | 97 | O | 37 |
| C | 89 | P | 31 |
| D | 83 | Q | 29 |
| E | 79 | R | 23 |
| F | 73 | S | 19 |
| G | 71 | T | 17 |
| H | 67 | U | 13 |
| I | 61 | V | 11 |
| J | 59 | W | 7 |
| K | 53 | X | 5 |
| L | 47 | Y | 3 |
| M | 43 | Z | 2 |

### RSQ: Reverse Squares

The square chart read backward.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 676 | N | 169 |
| B | 625 | O | 144 |
| C | 576 | P | 121 |
| D | 529 | Q | 100 |
| E | 484 | R | 81 |
| F | 441 | S | 64 |
| G | 400 | T | 49 |
| H | 361 | U | 36 |
| I | 324 | V | 25 |
| J | 289 | W | 16 |
| K | 256 | X | 9 |
| L | 225 | Y | 4 |
| M | 196 | Z | 1 |

### RTRI: Reverse Trigonal

The trigonal chart read backward.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 351 | N | 91 |
| B | 325 | O | 78 |
| C | 300 | P | 66 |
| D | 276 | Q | 55 |
| E | 253 | R | 45 |
| F | 231 | S | 36 |
| G | 210 | T | 28 |
| H | 190 | U | 21 |
| I | 171 | V | 15 |
| J | 153 | W | 10 |
| K | 136 | X | 6 |
| L | 120 | Y | 3 |
| M | 105 | Z | 1 |

### RFIB: Reverse Fibonacci

The Fibonacci chart read backward.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 75025 | N | 144 |
| B | 46368 | O | 89 |
| C | 28657 | P | 55 |
| D | 17711 | Q | 34 |
| E | 10946 | R | 21 |
| F | 6765 | S | 13 |
| G | 4181 | T | 8 |
| H | 2584 | U | 5 |
| I | 1597 | V | 3 |
| J | 987 | W | 2 |
| K | 610 | X | 1 |
| L | 377 | Y | 1 |
| M | 233 | Z | 0 |

### CM: Capitals Mixed, and CA: Capitals Added

Case matters. A capital letter is the ordinary count plus 26, so A is 27. A small letter is the ordinary count, so a is 1. `Ab` is 27 + 2 = 29. These two codes use the same chart. Ask for either name.

Uppercase

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 27 | N | 40 |
| B | 28 | O | 41 |
| C | 29 | P | 42 |
| D | 30 | Q | 43 |
| E | 31 | R | 44 |
| F | 32 | S | 45 |
| G | 33 | T | 46 |
| H | 34 | U | 47 |
| I | 35 | V | 48 |
| J | 36 | W | 49 |
| K | 37 | X | 50 |
| L | 38 | Y | 51 |
| M | 39 | Z | 52 |

Lowercase

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| a | 1 | n | 14 |
| b | 2 | o | 15 |
| c | 3 | p | 16 |
| d | 4 | q | 17 |
| e | 5 | r | 18 |
| f | 6 | s | 19 |
| g | 7 | t | 20 |
| h | 8 | u | 21 |
| i | 9 | v | 22 |
| j | 10 | w | 23 |
| k | 11 | x | 24 |
| l | 12 | y | 25 |
| m | 13 | z | 26 |

### RCM: Reverse Capitals Mixed, and RCA: Reverse Capitals Added

That capital chart, read backward. Case still matters. These two codes use the same chart.

Uppercase

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 52 | N | 39 |
| B | 51 | O | 38 |
| C | 50 | P | 37 |
| D | 49 | Q | 36 |
| E | 48 | R | 35 |
| F | 47 | S | 34 |
| G | 46 | T | 33 |
| H | 45 | U | 32 |
| I | 44 | V | 31 |
| J | 43 | W | 30 |
| K | 42 | X | 29 |
| L | 41 | Y | 28 |
| M | 40 | Z | 27 |

Lowercase

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| a | 26 | n | 13 |
| b | 25 | o | 12 |
| c | 24 | p | 11 |
| d | 23 | q | 10 |
| e | 22 | r | 9 |
| f | 21 | s | 8 |
| g | 20 | t | 7 |
| h | 19 | u | 6 |
| i | 18 | v | 5 |
| j | 17 | w | 4 |
| k | 16 | x | 3 |
| l | 15 | y | 2 |
| m | 14 | z | 1 |

### KV: KV Exception

Full Reduction, but K stays 11 and V stays 22.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 1 | N | 5 |
| B | 2 | O | 6 |
| C | 3 | P | 7 |
| D | 4 | Q | 8 |
| E | 5 | R | 9 |
| F | 6 | S | 1 |
| G | 7 | T | 2 |
| H | 8 | U | 3 |
| I | 9 | V | 22 |
| J | 1 | W | 5 |
| K | 11 | X | 6 |
| L | 3 | Y | 7 |
| M | 4 | Z | 8 |

### SKV: SKV Exception

Full Reduction, but S stays 10, K stays 11, and V stays 22.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 1 | N | 5 |
| B | 2 | O | 6 |
| C | 3 | P | 7 |
| D | 4 | Q | 8 |
| E | 5 | R | 9 |
| F | 6 | S | 10 |
| G | 7 | T | 2 |
| H | 8 | U | 3 |
| I | 9 | V | 22 |
| J | 1 | W | 5 |
| K | 11 | X | 6 |
| L | 3 | Y | 7 |
| M | 4 | Z | 8 |

### EP: EP Exception, and EHP: EHP Exception

The same chart as Full Reduction. The codes are still here so you can ask for them by name.

Forgot a code? `gallus-decoder-tools ciphers` prints the menu.

| Letter | Value | Letter | Value |
| --- | --- | --- | --- |
| A | 1 | N | 5 |
| B | 2 | O | 6 |
| C | 3 | P | 7 |
| D | 4 | Q | 8 |
| E | 5 | R | 9 |
| F | 6 | S | 1 |
| G | 7 | T | 2 |
| H | 8 | U | 3 |
| I | 9 | V | 4 |
| J | 1 | W | 5 |
| K | 2 | X | 6 |
| L | 3 | Y | 7 |
| M | 4 | Z | 8 |

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
