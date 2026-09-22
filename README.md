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

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

### FR: Full Reduction

Take each English Ordinal number and squash it to a single digit, then add those digits. S is 19, which becomes 1. You add the letter digits. You do not squash the finished total again. `DOG` is 17 in Full Reduction. Turning 17 into 8 is a separate step. Say so if you do it.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 1 | 2 | 3 | 4 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 6 | 7 | 8 | 9 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |

### RO: Reverse Ordinal

Count the alphabet from the other end. A is 26 and Z is 1.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 26 | 25 | 24 | 23 | 22 | 21 | 20 | 19 | 18 | 17 | 16 | 15 | 14 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |

### RFR: Reverse Full Reduction

Start from that backward chart, squash each letter to one digit, then add.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 9 | 8 | 7 | 6 | 5 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 3 | 2 | 1 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |

## Every other cipher

Ask for one with `--ciphers` and its code. The grid under each name is the chart the program adds.

### SR: Single Reduction

Full Reduction, except S stays 10 instead of becoming 1.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 1 | 2 | 3 | 4 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 6 | 7 | 8 | 9 | 10 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |

### RSR: Reverse Single Reduction

That chart read backward. The 10 that belonged to S lands on H.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 10 | 9 | 8 | 7 | 6 | 5 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 3 | 2 | 1 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |

### JO: Jewish Ordinal

English letters given the stepped sizes used in Jewish numbering: 1 through 9, then 10, 20, 30, and onward up to 800.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 20 | 30 | 40 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 50 | 60 | 70 | 80 | 90 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 |

### JR: Jewish Reduction

Each of those values squashed to one digit. On this alphabet the chart matches Full Reduction, so the totals match `FR`.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 1 | 2 | 3 | 4 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 6 | 7 | 8 | 9 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |

### CH: Chaldean

A Chaldean letter chart. Some letters share a number, and no letter is worth 9.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 8 | 3 | 5 | 1 | 1 | 2 | 3 | 4 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 7 | 8 | 1 | 2 | 3 | 4 | 6 | 6 | 6 | 5 | 1 | 7 |

### SUM: Sumerian

English Ordinal multiplied by 6. A is 6, B is 12, Z is 156.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | 12 | 18 | 24 | 30 | 36 | 42 | 48 | 54 | 60 | 66 | 72 | 78 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 | 90 | 96 | 102 | 108 | 114 | 120 | 126 | 132 | 138 | 144 | 150 | 156 |

### SAT: Satanic

A straight count that starts at 36 for A and ends at 61 for Z.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 49 | 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 | 61 |

### HEB: Hebrew

Case matters. Uppercase letters use a Hebrew-style chart. Lowercase `k` is 10. Uppercase `K` is 20. Every other lowercase letter is missing, so it adds nothing. Type the case you mean.

Uppercase

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 600 | 20 | 20 | 30 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 40 | 50 | 60 | 70 | 80 | 90 | 100 | 200 | 700 | 800 | 300 | 400 | 500 |

Lowercase k is the only lowercase letter on this chart.

| k |
| --- |
| 10 |

### RSUM: Reverse Sumerian

The backward alphabet, multiplied by 6.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 156 | 150 | 144 | 138 | 132 | 126 | 120 | 114 | 108 | 102 | 96 | 90 | 84 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | 72 | 66 | 60 | 54 | 48 | 42 | 36 | 30 | 24 | 18 | 12 | 6 |

### RSAT: Reverse Satanic

The Satanic chart read from the other end. A is 61 and Z is 36.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 61 | 60 | 59 | 58 | 57 | 56 | 55 | 54 | 53 | 52 | 51 | 50 | 49 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 48 | 47 | 46 | 45 | 44 | 43 | 42 | 41 | 40 | 39 | 38 | 37 | 36 |

### PRIM: Primes

The first 26 prime numbers, in order. A is 2, B is 3, C is 5, Z is 101. Scoring a word with this cipher is not the same as asking for the 14th prime. That second question is `properties`.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 | 31 | 37 | 41 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 43 | 47 | 53 | 59 | 61 | 67 | 71 | 73 | 79 | 83 | 89 | 97 | 101 |

### SQ: Squares

The first 26 square numbers. A is 1×1, B is 2×2, Z is 26×26.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 9 | 16 | 25 | 36 | 49 | 64 | 81 | 100 | 121 | 144 | 169 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 196 | 225 | 256 | 289 | 324 | 361 | 400 | 441 | 484 | 529 | 576 | 625 | 676 |

### TRI: Trigonal

The first 26 triangular numbers: 1, then 1+2, then 1+2+3, and so on.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 6 | 10 | 15 | 21 | 28 | 36 | 45 | 55 | 66 | 78 | 91 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 105 | 120 | 136 | 153 | 171 | 190 | 210 | 231 | 253 | 276 | 300 | 325 | 351 |

### FIB: Fibonacci

Fibonacci numbers placed on the letters, starting at 0 for A. This is a letter chart, not "the 10th Fibonacci number."

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 233 | 377 | 610 | 987 | 1597 | 2584 | 4181 | 6765 | 10946 | 17711 | 28657 | 46368 | 75025 |

### SEP: Septenary

Count 1 through 7, then start over. A is 1, and H is 1 again.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 1 | 2 | 3 | 4 | 5 | 6 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 1 | 2 | 3 | 4 | 5 |

### KP: Keypad

The phone keypad. ABC is 2, DEF is 3, and WXYZ is 9.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 2 | 2 | 3 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 6 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | 6 | 7 | 7 | 7 | 7 | 8 | 8 | 8 | 9 | 9 | 9 | 9 |

### RPRIM: Reverse Primes

The prime chart read from Z back toward A.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 97 | 89 | 83 | 79 | 73 | 71 | 67 | 61 | 59 | 53 | 47 | 43 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 41 | 37 | 31 | 29 | 23 | 19 | 17 | 13 | 11 | 7 | 5 | 3 | 2 |

### RSQ: Reverse Squares

The square chart read backward.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 676 | 625 | 576 | 529 | 484 | 441 | 400 | 361 | 324 | 289 | 256 | 225 | 196 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 169 | 144 | 121 | 100 | 81 | 64 | 49 | 36 | 25 | 16 | 9 | 4 | 1 |

### RTRI: Reverse Trigonal

The trigonal chart read backward.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 351 | 325 | 300 | 276 | 253 | 231 | 210 | 190 | 171 | 153 | 136 | 120 | 105 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 91 | 78 | 66 | 55 | 45 | 36 | 28 | 21 | 15 | 10 | 6 | 3 | 1 |

### RFIB: Reverse Fibonacci

The Fibonacci chart read backward.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 75025 | 46368 | 28657 | 17711 | 10946 | 6765 | 4181 | 2584 | 1597 | 987 | 610 | 377 | 233 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 144 | 89 | 55 | 34 | 21 | 13 | 8 | 5 | 3 | 2 | 1 | 1 | 0 |

### CM: Capitals Mixed, and CA: Capitals Added

Case matters. A capital letter is the ordinary count plus 26, so A is 27. A small letter is the ordinary count, so a is 1. `Ab` is 27 + 2 = 29. These two codes use the same chart. Ask for either name.

Uppercase

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 | 51 | 52 |

Lowercase

| a | b | c | d | e | f | g | h | i | j | k | l | m |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |

| n | o | p | q | r | s | t | u | v | w | x | y | z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

### RCM: Reverse Capitals Mixed, and RCA: Reverse Capitals Added

That capital chart, read backward. Case still matters. These two codes use the same chart.

Uppercase

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 52 | 51 | 50 | 49 | 48 | 47 | 46 | 45 | 44 | 43 | 42 | 41 | 40 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | 38 | 37 | 36 | 35 | 34 | 33 | 32 | 31 | 30 | 29 | 28 | 27 |

Lowercase

| a | b | c | d | e | f | g | h | i | j | k | l | m |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 26 | 25 | 24 | 23 | 22 | 21 | 20 | 19 | 18 | 17 | 16 | 15 | 14 |

| n | o | p | q | r | s | t | u | v | w | x | y | z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |

### KV: KV Exception

Full Reduction, but K stays 11 and V stays 22.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 1 | 11 | 3 | 4 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 6 | 7 | 8 | 9 | 1 | 2 | 3 | 22 | 5 | 6 | 7 | 8 |

### SKV: SKV Exception

Full Reduction, but S stays 10, K stays 11, and V stays 22.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 1 | 11 | 3 | 4 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 6 | 7 | 8 | 9 | 10 | 2 | 3 | 22 | 5 | 6 | 7 | 8 |

### EP: EP Exception, and EHP: EHP Exception

The same chart as Full Reduction. The codes are still here so you can ask for them by name.

Forgot a code? `gallus-decoder-tools ciphers` prints the menu.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 1 | 2 | 3 | 4 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 6 | 7 | 8 | 9 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |

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
