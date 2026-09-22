<p align="center">
  <img src="docs/brand/GallusLogo.png" alt="Gallus" width="128">
</p>

# Gallus Decoder Tools

You type a phrase, a number, or two dates. The tool returns the total, the number properties, or the day count.

Copyright 2026 Gallus Labs. Using the tools includes the credit **Gallus Decoder Tools by Gallus Labs**. Free for personal and non-commercial use. Not for sale.

## Install

Python 3.11 or newer.

```bash
git clone https://github.com/strainzz/Gallus-Decoder-Tools.git
cd Gallus-Decoder-Tools
python -m pip install .
```

If this folder is already open, `python -m pip install .` is enough.

```bash
gallus-decoder-tools decode "DOG"
gallus-decoder-tools properties 28
gallus-decoder-tools span 01/01/2020 09/22/2026
```

- [Decode](#decode) adds a phrase.
- [The four ciphers](#the-four-ciphers-to-learn-first) are the ones to learn first.
- [The other ciphers](#every-other-cipher) are the rest, each with its grid.
- [Properties](#properties) checks one number.
- [Span](#span) counts the days between two dates.

## Get the most out of it

This repo is the calculator. It does the addition. It does not tell you how to set up a sports decode.

That setup is in **The Schizo Mathematician Decoder Handbook**. The handbook is for members of the Gallus Labs community. It shows how to use these tools for sports decoding, and more. It is not included here.

## Decode

Decode adds up a phrase.

```bash
gallus-decoder-tools decode "DOG"
```

With no extra flags, you get the four everyday ciphers. `DOG` comes back as 26, 17, 55, and 10.

| Cipher | What it did | Total |
| --- | --- | --- |
| English Ordinal | D is 4, O is 15, G is 7 | 26 |
| Full Reduction | D is 4, O is 6, G is 7 | 17 |
| Reverse Ordinal | D is 23, O is 12, G is 20 | 55 |
| Reverse Full Reduction | D is 5, O is 3, G is 2 | 10 |

Pick one cipher, or several, by code.

```bash
gallus-decoder-tools decode "DOG" --ciphers eo
gallus-decoder-tools decode "DOG" --ciphers eo,fr
gallus-decoder-tools decode "DOG" --all
```

`--all` runs every cipher on this page. A comma in the phrase splits it into two phrases, so `decode "Lions, Bears"` scores each name. Spaces and punctuation add nothing. A run of digits is added as that whole number: the 49 in `49ers` adds 49.

For the four everyday ciphers, capitals and small letters are the same letter. Hebrew and the capital ciphers care about case. That is called out under each of those codes.

Reverse means you start at Z and count back toward A. It does not mean you flip the digits of the answer.

## The four ciphers to learn first

### EO: English Ordinal

Count the alphabet. A is 1. B is 2. Z is 26. Find each letter in the grid and add the numbers under them.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

### FR: Full Reduction

Same letters as English Ordinal, but every number is one digit. If a number has two digits, add those digits. 10 becomes 1. 19 becomes 1 + 9 = 10, then 1 + 0 = 1. S is 1. Add the letters and stop. `DOG` is 4 + 6 + 7 = 17. Do not add 1 + 7 unless you say you are doing that extra step.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 1 | 2 | 3 | 4 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 6 | 7 | 8 | 9 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |

### RO: Reverse Ordinal

Count the alphabet from the end. Z is 1. Y is 2. A is 26. `DOG` is 23 + 12 + 20 = 55.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 26 | 25 | 24 | 23 | 22 | 21 | 20 | 19 | 18 | 17 | 16 | 15 | 14 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |

### RFR: Reverse Full Reduction

Start with Reverse Ordinal. Then make each letter one digit. A is 26, and 2 + 6 = 8. `DOG` is 5 + 3 + 2 = 10. Add the letters and stop.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 9 | 8 | 7 | 6 | 5 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 3 | 2 | 1 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |

## Every other cipher

Ask for one with `--ciphers` and its code. Find the letter in the grid. Add the number under it.

### SR: Single Reduction

Same as Full Reduction, but S is 10. In Full Reduction, S is 1. Here you stop at 10. Look at S in the grid.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 1 | 2 | 3 | 4 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 6 | 7 | 8 | 9 | 10 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |

### RSR: Reverse Single Reduction

Single Reduction, written from Z back to A. H is 10. Look at H in the grid.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 10 | 9 | 8 | 7 | 6 | 5 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 3 | 2 | 1 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |

### JO: Jewish Ordinal

A through I are 1 through 9. Then the numbers jump. J is 10. K is 20. L is 30. S is 100. Z is 800. Use the number under the letter. No extra math.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 20 | 30 | 40 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 50 | 60 | 70 | 80 | 90 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 |

### JR: Jewish Reduction

Jewish Ordinal, with every number made into one digit. 10 becomes 1. 20 becomes 2. 100 becomes 1. The grid matches Full Reduction, so the total matches `FR`.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 1 | 2 | 3 | 4 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 6 | 7 | 8 | 9 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |

### CH: Chaldean

Look up the letter. Some letters share a number. F and P are both 8. No letter is 9. Use the number under the letter.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 8 | 3 | 5 | 1 | 1 | 2 | 3 | 4 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 7 | 8 | 1 | 2 | 3 | 4 | 6 | 6 | 6 | 5 | 1 | 7 |

### SUM: Sumerian

The normal A=1 number, times 6. A is 1 times 6, so A is 6. B is 2 times 6, so B is 12. Z is 26 times 6, so Z is 156. Or just use the grid.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | 12 | 18 | 24 | 30 | 36 | 42 | 48 | 54 | 60 | 66 | 72 | 78 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 | 90 | 96 | 102 | 108 | 114 | 120 | 126 | 132 | 138 | 144 | 150 | 156 |

### SAT: Satanic

A is 36. Each next letter is 1 more. B is 37. C is 38. Z is 61.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 49 | 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 | 61 |

### HEB: Hebrew

Capital letters use the big numbers in the grid. Capital K is 20. Small k is 10. Any other small letter is skipped and adds nothing. `Hello` is only 8, from the capital H. Type the capitals you mean.

Uppercase

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 600 | 20 | 20 | 30 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 40 | 50 | 60 | 70 | 80 | 90 | 100 | 200 | 700 | 800 | 300 | 400 | 500 |

Small k is the only small letter in this grid.

| k |
| --- |
| 10 |

### RSUM: Reverse Sumerian

Reverse Ordinal, times 6. A is 26 in Reverse Ordinal, so A is 26 times 6, which is 156. Z is 6. Or just use the grid.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 156 | 150 | 144 | 138 | 132 | 126 | 120 | 114 | 108 | 102 | 96 | 90 | 84 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | 72 | 66 | 60 | 54 | 48 | 42 | 36 | 30 | 24 | 18 | 12 | 6 |

### RSAT: Reverse Satanic

Satanic counted from the end. A is 61. B is 60. Z is 36.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 61 | 60 | 59 | 58 | 57 | 56 | 55 | 54 | 53 | 52 | 51 | 50 | 49 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 48 | 47 | 46 | 45 | 44 | 43 | 42 | 41 | 40 | 39 | 38 | 37 | 36 |

### PRIM: Primes

A is 2. B is 3. C is 5. D is 7. These are prime numbers, in order, one per letter. You do not need to know what a prime is. Use the number under the letter. This is not "the 14th prime." That is the properties command.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 | 31 | 37 | 41 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 43 | 47 | 53 | 59 | 61 | 67 | 71 | 73 | 79 | 83 | 89 | 97 | 101 |

### SQ: Squares

A is 1 times 1, so 1. B is 2 times 2, so 4. C is 3 times 3, so 9. Z is 26 times 26, so 676. Or just use the grid.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 9 | 16 | 25 | 36 | 49 | 64 | 81 | 100 | 121 | 144 | 169 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 196 | 225 | 256 | 289 | 324 | 361 | 400 | 441 | 484 | 529 | 576 | 625 | 676 |

### TRI: Trigonal

A is 1. B is 1 + 2, so 3. C is 1 + 2 + 3, so 6. Each letter adds the next counting number. Or just use the grid.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 6 | 10 | 15 | 21 | 28 | 36 | 45 | 55 | 66 | 78 | 91 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 105 | 120 | 136 | 153 | 171 | 190 | 210 | 231 | 253 | 276 | 300 | 325 | 351 |

### FIB: Fibonacci

A is 0. B is 1. C is 1. D is 2. E is 3. Each next number is the two before it added: 1 + 2 = 3, then 2 + 3 = 5. Or just use the grid. This is not "the 10th Fibonacci number." That is the properties command.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 233 | 377 | 610 | 987 | 1597 | 2584 | 4181 | 6765 | 10946 | 17711 | 28657 | 46368 | 75025 |

### SEP: Septenary

Count 1, 2, 3, 4, 5, 6, 7, then start at 1 again. A is 1. H is 1. O is 1.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 1 | 2 | 3 | 4 | 5 | 6 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 1 | 2 | 3 | 4 | 5 |

### KP: Keypad

Old phone buttons. Letters on the same button share a number. A, B, and C are 2. D, E, and F are 3. W, X, Y, and Z are 9.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 2 | 2 | 3 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 6 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | 6 | 7 | 7 | 7 | 7 | 8 | 8 | 8 | 9 | 9 | 9 | 9 |

### RPRIM: Reverse Primes

The prime list, flipped. Z is 2. Y is 3. A is 101. Use the number under the letter.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 97 | 89 | 83 | 79 | 73 | 71 | 67 | 61 | 59 | 53 | 47 | 43 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 41 | 37 | 31 | 29 | 23 | 19 | 17 | 13 | 11 | 7 | 5 | 3 | 2 |

### RSQ: Reverse Squares

The square list, flipped. Z is 1. Y is 4. A is 676. Use the number under the letter.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 676 | 625 | 576 | 529 | 484 | 441 | 400 | 361 | 324 | 289 | 256 | 225 | 196 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 169 | 144 | 121 | 100 | 81 | 64 | 49 | 36 | 25 | 16 | 9 | 4 | 1 |

### RTRI: Reverse Trigonal

The trigonal list, flipped. Z is 1. Y is 3. A is 351. Use the number under the letter.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 351 | 325 | 300 | 276 | 253 | 231 | 210 | 190 | 171 | 153 | 136 | 120 | 105 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 91 | 78 | 66 | 55 | 45 | 36 | 28 | 21 | 15 | 10 | 6 | 3 | 1 |

### RFIB: Reverse Fibonacci

The Fibonacci list, flipped. Z is 0. Y is 1. A is 75025. Use the number under the letter.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 75025 | 46368 | 28657 | 17711 | 10946 | 6765 | 4181 | 2584 | 1597 | 987 | 610 | 377 | 233 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 144 | 89 | 55 | 34 | 21 | 13 | 8 | 5 | 3 | 2 | 1 | 1 | 0 |

### CM: Capitals Mixed, and CA: Capitals Added

Big letters and small letters are different. Big A is 27. Small a is 1. Big letters are the normal 1 to 26, plus 26. Small letters are the normal 1 to 26. `Ab` is 27 + 2 = 29. `CM` and `CA` use this same grid. Pick either code.

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

The capital grid above, flipped. Big A is 52. Small a is 26. Big letters and small letters are still different. `RCM` and `RCA` use this same grid. Pick either code.

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

Same as Full Reduction, except two letters. K is 11, not 2. V is 22, not 4. Look at K and V in the grid.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 1 | 11 | 3 | 4 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 6 | 7 | 8 | 9 | 1 | 2 | 3 | 22 | 5 | 6 | 7 | 8 |

### SKV: SKV Exception

Same as Full Reduction, except three letters. S is 10, not 1. K is 11, not 2. V is 22, not 4. Look at S, K, and V in the grid.

| A | B | C | D | E | F | G | H | I | J | K | L | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 1 | 11 | 3 | 4 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 6 | 7 | 8 | 9 | 10 | 2 | 3 | 22 | 5 | 6 | 7 | 8 |

### EP: EP Exception, and EHP: EHP Exception

Same numbers as Full Reduction. `EP` and `EHP` both use this grid. The totals match `FR`.

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

Each date also gets four date numbers. September 11, 2026 is the check:

| Number | What you add | Total |
| --- | --- | --- |
| DN1 | Every digit: 9 + 1 + 1 + 2 + 0 + 2 + 6 | 21 |
| DN2 | Month, day, and each year digit: 9 + 11 + 2 + 0 + 2 + 6 | 30 |
| DN3 | Month, day, and the last two year digits: 9 + 11 + 26 | 46 |
| DN4 | Month, day, first two year digits, and last two: 9 + 11 + 20 + 26 | 66 |

September 11, 2026 is day 254 of the year. 111 days are left after that date. The span result gives this breakdown for the start date and the end date. The written addition is in `steps`.

Each of those four numbers also gets its own small breakdown: the prime at that count, the triangular number at that count, the Fibonacci number at that count, and the square. For DN1, 21, the 21st prime is 73, the 21st triangular number is 231, and 21 times 21 is 441.

The date is also written both ways. September 11, 2026 is `9/11/2026` and `11/9/2026`. Placing the digits side by side gives 9112026 and 1192026. That is not addition.

To score the month name or the weekday, pass that word to `decode`. This result does not do that for you.

Dates can be `01/01/2020`, `2020-01-01`, or `September 22, 2026`. A slash date is month, then day. If the first number is greater than 12, as in `31/01/2020`, it is read as day, then month. Put the later date first and the tool swaps them and tells you it did.

```bash
gallus-decoder-tools span 01/01/2020 09/22/2026 --include-end
```

`--include-end` counts the end date as a day. Leave it off and the end date is the fence, not a counted day.

## What comes back

Every command prints one JSON object. `ok` means it finished. `credit` is `Gallus Decoder Tools by Gallus Labs`. `use` repeats the non-commercial terms. `result` is the calculation. A bad input exits with code 2 and an `error` sentence.

`DOG` with no flags:

```json
{
  "ok": true,
  "credit": "Gallus Decoder Tools by Gallus Labs",
  "use": "Personal and non-commercial use only. Keep this credit. Do not sell the tools or copy the cipher maps into another product that drops Gallus Labs.",
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

Show `credit` with the result. Do not replace a total with an estimate. An agent that uses these tools follows [AGENT_PROMPT.md](AGENT_PROMPT.md). [SKILL.md](SKILL.md) is the file to drop into an agent skills folder. [AGENTS.md](AGENTS.md) is the contract inside this repository. [agent-tools.json](agent-tools.json) lists the request fields.

## Credit

| | |
| --- | --- |
| Source | https://github.com/strainzz/Gallus-Decoder-Tools |
| Copyright | Copyright 2026 Gallus Labs |
| Required credit | Gallus Decoder Tools by Gallus Labs |
| License | [Gallus Labs terms](LICENSE). Free to use. Not for sale. |
| Attribution | [NOTICE](NOTICE) |
| Changes | [CHANGELOG.md](CHANGELOG.md) |
| Mark | The Gallus logo is a trademark of Gallus Labs. The license covers the software and does not grant rights in the mark. |

The credit stays on copies, on changes, and on results. You may not sell the tools or copy the cipher maps into another product that drops Gallus Labs. The logo is in [docs/brand](docs/brand).

To work on the source: `python -m pip install -e .`, then the notes in [CONTRIBUTING.md](CONTRIBUTING.md). A vulnerability goes through a private GitHub security advisory, as described in [SECURITY.md](SECURITY.md).
