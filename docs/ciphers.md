<p align="center">
  <img src="brand/GallusLogo.png" alt="Gallus" width="72">
</p>

# Cipher catalog

A cipher is a rule that turns each letter into a number. You look the letters up and add them. That sum is the gematria total.

Gallus Decoder Tools includes 32 ciphers. You do not need all of them on day one. Learn the first four. Use the rest when you know which rule you are asking for.

Copyright 2026 Gallus Labs. The letter charts below are the ones the program adds.

## How to use a cipher

```bash
gallus-decoder-tools decode "DOG"
gallus-decoder-tools decode "DOG" --ciphers eo
gallus-decoder-tools decode "DOG" --ciphers eo,fr,ro,rfr
gallus-decoder-tools decode "DOG" --all
```

With no extra flags, `decode` uses the four everyday ciphers. `--ciphers` is how you pick. `--all` runs every cipher on this page. `gallus-decoder-tools ciphers` prints the code list if you forget a name.

Spaces and punctuation add nothing. A run of digits is added as that whole number, so the 49 in `49ers` adds 49. For the four everyday ciphers, capital letters and small letters are the same letter.

`DOG` in the four everyday ciphers:

| Cipher | Addition | Total |
| --- | --- | --- |
| English Ordinal | 4 + 15 + 7 | 26 |
| Full Reduction | 4 + 6 + 7 | 17 |
| Reverse Ordinal | 23 + 12 + 20 | 55 |
| Reverse Full Reduction | 5 + 3 + 2 | 10 |

The word **reverse** means the alphabet chart is flipped. It does not mean you flip the digits of the finished total.

## The four to learn first

### EO — English Ordinal

This is the ordinary alphabet count. A is 1, B is 2, C is 3, and Z is 26. If you only learn one cipher, learn this one. Check it with `DOG`: D is 4, O is 15, G is 7, and 4 + 15 + 7 = 26.

```text
A1 B2 C3 D4 E5 F6 G7 H8 I9 J10 K11 L12 M13 N14 O15 P16 Q17 R18 S19 T20 U21 V22 W23 X24 Y25 Z26
```

### FR — Full Reduction

Take each English Ordinal number and squash it to a single digit, then add those digits. 10 becomes 1. 11 becomes 2. 19 becomes 1 + 9 = 10, then 1 + 0 = 1, so S is 1.

You add the letter digits. You do not squash the finished total again. `DOG` is 4 + 6 + 7 = 17. Turning 17 into 8 is a separate digital root. Say so if you do it. It is not the Full Reduction total.

```text
A1 B2 C3 D4 E5 F6 G7 H8 I9 J1 K2 L3 M4 N5 O6 P7 Q8 R9 S1 T2 U3 V4 W5 X6 Y7 Z8
```

### RO — Reverse Ordinal

Count the alphabet from the other end. A is 26 and Z is 1. `DOG` is 23 + 12 + 20 = 55.

```text
A26 B25 C24 D23 E22 F21 G20 H19 I18 J17 K16 L15 M14 N13 O12 P11 Q10 R9 S8 T7 U6 V5 W4 X3 Y2 Z1
```

### RFR — Reverse Full Reduction

Start from the backward chart, squash each letter to one digit, then add. `DOG` is 5 + 3 + 2 = 10. As with Full Reduction, leave that 10 as 10 unless you are openly doing a second digital root.

```text
A8 B7 C6 D5 E4 F3 G2 H1 I9 J8 K7 L6 M5 N4 O3 P2 Q1 R9 S8 T7 U6 V5 W4 X3 Y2 Z1
```

## The other ciphers

Each one is another letter chart. Ask for it with `--ciphers` and its code. The charts are case-insensitive except Hebrew and the four capital ciphers, which are marked.

### SR — Single Reduction

Almost Full Reduction. The one difference is S. In Full Reduction, S is squashed all the way to 1. Here S stops at 10.

```text
A1 B2 C3 D4 E5 F6 G7 H8 I9 J1 K2 L3 M4 N5 O6 P7 Q8 R9 S10 T2 U3 V4 W5 X6 Y7 Z8
```

### RSR — Reverse Single Reduction

The Single Reduction chart read backward. The 10 that belonged to S lands on H, the letter opposite S.

```text
A8 B7 C6 D5 E4 F3 G2 H10 I9 J8 K7 L6 M5 N4 O3 P2 Q1 R9 S8 T7 U6 V5 W4 X3 Y2 Z1
```

### JO — Jewish Ordinal

English letters are given the stepped sizes used in Jewish numbering. The first nine letters are 1 through 9. After that the steps get bigger: 10, 20, 30, and onward up to 800 for Z.

```text
A1 B2 C3 D4 E5 F6 G7 H8 I9 J10 K20 L30 M40 N50 O60 P70 Q80 R90 S100 T200 U300 V400 W500 X600 Y700 Z800
```

### JR — Jewish Reduction

Each Jewish Ordinal value, squashed to one digit. On this alphabet that chart matches Full Reduction, so a normal phrase gets the same total from `JR` and `FR`.

```text
A1 B2 C3 D4 E5 F6 G7 H8 I9 J1 K2 L3 M4 N5 O6 P7 Q8 R9 S1 T2 U3 V4 W5 X6 Y7 Z8
```

### CH — Chaldean

A Chaldean letter chart. Some letters share a number, and no letter is worth 9.

```text
A1 B2 C3 D4 E5 F8 G3 H5 I1 J1 K2 L3 M4 N5 O7 P8 Q1 R2 S3 T4 U6 V6 W6 X5 Y1 Z7
```

### SUM — Sumerian

English Ordinal multiplied by 6. A is 6, B is 12, and Z is 156.

```text
A6 B12 C18 D24 E30 F36 G42 H48 I54 J60 K66 L72 M78 N84 O90 P96 Q102 R108 S114 T120 U126 V132 W138 X144 Y150 Z156
```

### SAT — Satanic

A straight count that starts at 36 for A and ends at 61 for Z. Each letter is one more than the letter before it.

```text
A36 B37 C38 D39 E40 F41 G42 H43 I44 J45 K46 L47 M48 N49 O50 P51 Q52 R53 S54 T55 U56 V57 W58 X59 Y60 Z61
```

### HEB — Hebrew

Case matters. The uppercase letters use a Hebrew-style chart. Lowercase `k` is 10, and uppercase `K` is 20. Every other lowercase letter is missing from the chart, so it adds nothing. `Hello` totals 8, from H alone. Type the case you mean.

```text
A1 B2 C3 D4 E5 F6 G7 H8 I9 J600 K20 L20 M30 N40 O50 P60 Q70 R80 S90 T100 U200 V700 W800 X300 Y400 Z500
k10
```

### RSUM — Reverse Sumerian

The backward alphabet, multiplied by 6. A is 156 and Z is 6.

```text
A156 B150 C144 D138 E132 F126 G120 H114 I108 J102 K96 L90 M84 N78 O72 P66 Q60 R54 S48 T42 U36 V30 W24 X18 Y12 Z6
```

### RSAT — Reverse Satanic

The Satanic chart read from the other end. A is 61 and Z is 36.

```text
A61 B60 C59 D58 E57 F56 G55 H54 I53 J52 K51 L50 M49 N48 O47 P46 Q45 R44 S43 T42 U41 V40 W39 X38 Y37 Z36
```

### PRIM — Primes

The first 26 prime numbers, stuck to the letters in order. A is 2, B is 3, C is 5, and Z is 101. This is a letter chart. It is not the same question as "what is the 14th prime?"

```text
A2 B3 C5 D7 E11 F13 G17 H19 I23 J29 K31 L37 M41 N43 O47 P53 Q59 R61 S67 T71 U73 V79 W83 X89 Y97 Z101
```

### SQ — Squares

The first 26 square numbers. A is 1×1, B is 2×2, and Z is 26×26, which is 676.

```text
A1 B4 C9 D16 E25 F36 G49 H64 I81 J100 K121 L144 M169 N196 O225 P256 Q289 R324 S361 T400 U441 V484 W529 X576 Y625 Z676
```

### TRI — Trigonal

The first 26 triangular numbers. Those are the sums 1, then 1+2, then 1+2+3, and so on. A is 1 and Z is 351.

```text
A1 B3 C6 D10 E15 F21 G28 H36 I45 J55 K66 L78 M91 N105 O120 P136 Q153 R171 S190 T210 U231 V253 W276 X300 Y325 Z351
```

### FIB — Fibonacci

Fibonacci numbers placed on the letters, starting at 0 for A, then 1, 1, 2, 3, 5, and so on. Using this cipher on a word is not the same as asking for the 10th Fibonacci number. That second question is what `properties` answers in `indexes`.

```text
A0 B1 C1 D2 E3 F5 G8 H13 I21 J34 K55 L89 M144 N233 O377 P610 Q987 R1597 S2584 T4181 U6765 V10946 W17711 X28657 Y46368 Z75025
```

### SEP — Septenary

Count from 1 to 7, then start over. A is 1, H is 1 again, O is 1 again.

```text
A1 B2 C3 D4 E5 F6 G7 H1 I2 J3 K4 L5 M6 N7 O1 P2 Q3 R4 S5 T6 U7 V1 W2 X3 Y4 Z5
```

### KP — Keypad

The phone keypad. ABC is 2, DEF is 3, GHI is 4, JKL is 5, MNO is 6, PQRS is 7, TUV is 8, and WXYZ is 9.

```text
A2 B2 C2 D3 E3 F3 G4 H4 I4 J5 K5 L5 M6 N6 O6 P7 Q7 R7 S7 T8 U8 V8 W9 X9 Y9 Z9
```

### RPRIM — Reverse Primes

The prime chart read from Z back toward A. A is 101 and Z is 2.

```text
A101 B97 C89 D83 E79 F73 G71 H67 I61 J59 K53 L47 M43 N41 O37 P31 Q29 R23 S19 T17 U13 V11 W7 X5 Y3 Z2
```

### RSQ — Reverse Squares

The square chart read backward. A is 676 and Z is 1.

```text
A676 B625 C576 D529 E484 F441 G400 H361 I324 J289 K256 L225 M196 N169 O144 P121 Q100 R81 S64 T49 U36 V25 W16 X9 Y4 Z1
```

### RTRI — Reverse Trigonal

The trigonal chart read backward. A is 351 and Z is 1.

```text
A351 B325 C300 D276 E253 F231 G210 H190 I171 J153 K136 L120 M105 N91 O78 P66 Q55 R45 S36 T28 U21 V15 W10 X6 Y3 Z1
```

### RFIB — Reverse Fibonacci

The Fibonacci chart read backward. A is 75025 and Z is 0.

```text
A75025 B46368 C28657 D17711 E10946 F6765 G4181 H2584 I1597 J987 K610 L377 M233 N144 O89 P55 Q34 R21 S13 T8 U5 V3 W2 X1 Y1 Z0
```

### CM — Capitals Mixed, and CA — Capitals Added

Case matters. A capital letter is the ordinary alphabet count plus 26, so A is 27. A small letter is the ordinary count, so a is 1. `Ab` is 27 + 2 = 29.

These two codes use the same chart. You can ask for either name.

```text
Uppercase
A27 B28 C29 D30 E31 F32 G33 H34 I35 J36 K37 L38 M39 N40 O41 P42 Q43 R44 S45 T46 U47 V48 W49 X50 Y51 Z52

Lowercase
a1 b2 c3 d4 e5 f6 g7 h8 i9 j10 k11 l12 m13 n14 o15 p16 q17 r18 s19 t20 u21 v22 w23 x24 y25 z26
```

### RCM — Reverse Capitals Mixed, and RCA — Reverse Capitals Added

The capital chart above, read backward. Case still matters. These two codes use the same chart.

```text
Uppercase
A52 B51 C50 D49 E48 F47 G46 H45 I44 J43 K42 L41 M40 N39 O38 P37 Q36 R35 S34 T33 U32 V31 W30 X29 Y28 Z27

Lowercase
a26 b25 c24 d23 e22 f21 g20 h19 i18 j17 k16 l15 m14 n13 o12 p11 q10 r9 s8 t7 u6 v5 w4 x3 y2 z1
```

### KV — KV Exception

Full Reduction, with two letters left unsquashed. K stays 11. V stays 22.

```text
A1 B2 C3 D4 E5 F6 G7 H8 I9 J1 K11 L3 M4 N5 O6 P7 Q8 R9 S1 T2 U3 V22 W5 X6 Y7 Z8
```

### SKV — SKV Exception

Full Reduction, with three letters left unsquashed. S stays 10, K stays 11, and V stays 22.

```text
A1 B2 C3 D4 E5 F6 G7 H8 I9 J1 K11 L3 M4 N5 O6 P7 Q8 R9 S10 T2 U3 V22 W5 X6 Y7 Z8
```

### EP — EP Exception, and EHP — EHP Exception

These two use the Full Reduction chart. A phrase sent to `EP` or `EHP` totals the same as `FR`. The codes are still here so you can ask for them by name.

```text
A1 B2 C3 D4 E5 F6 G7 H8 I9 J1 K2 L3 M4 N5 O6 P7 Q8 R9 S1 T2 U3 V4 W5 X6 Y7 Z8
```

## Code list

| Code | Name | Rule |
| --- | --- | --- |
| EO | English Ordinal | Everyday. A=1 through Z=26. |
| FR | Full Reduction | Everyday. Each letter reduced to a single digit. |
| SR | Single Reduction | Full reduction, with S left as 10. |
| RO | Reverse Ordinal | Everyday. A=26 through Z=1. |
| RFR | Reverse Full Reduction | Everyday. Reverse ordinal, then reduced. |
| JO | Jewish Ordinal | Jewish letter values on the English alphabet, from 1 through 800. |
| JR | Jewish Reduction | Jewish ordinal reduced to a single digit. |
| CH | Chaldean | Chaldean letter values. |
| SUM | Sumerian | Ordinal value multiplied by 6. A=6 through Z=156. |
| SAT | Satanic | A=36 through Z=61. |
| HEB | Hebrew | Case-sensitive. Lowercase k is 10. Uppercase K is 20. |
| RSUM | Reverse Sumerian | Reverse ordinal multiplied by 6. |
| RSAT | Reverse Satanic | A=61 through Z=36. |
| PRIM | Primes | The first 26 prime numbers, A=2 through Z=101. |
| SQ | Squares | The first 26 squares, A=1 through Z=676. |
| TRI | Trigonal | The first 26 triangular numbers, A=1 through Z=351. |
| FIB | Fibonacci | Fibonacci values from A=0 through Z=75025. |
| SEP | Septenary | Repeating values 1 through 7. |
| KP | Keypad | Telephone keypad groups. ABC=2, DEF=3, and so on through WXYZ=9. |
| RSR | Reverse Single Reduction | The single-reduction map read in reverse. |
| RPRIM | Reverse Primes | The prime map read in reverse. |
| RSQ | Reverse Squares | The square map read in reverse. |
| RTRI | Reverse Trigonal | The trigonal map read in reverse. |
| RFIB | Reverse Fibonacci | The Fibonacci map read in reverse. |
| CM | Capitals Mixed | Case-sensitive. Lowercase is ordinal. Uppercase is ordinal plus 26. |
| CA | Capitals Added | Case-sensitive. Uppercase adds 26 to the ordinal value. |
| RCM | Reverse Capitals Mixed | Case-sensitive reverse of capitals mixed. |
| RCA | Reverse Capitals Added | Case-sensitive reverse of capitals added. |
| KV | KV Exception | Full reduction, with K kept at 11 and V kept at 22. |
| SKV | SKV Exception | Full reduction, with S kept at 10, K kept at 11, and V kept at 22. |
| EP | EP Exception | Same letter values as Full Reduction. |
| EHP | EHP Exception | Same letter values as Full Reduction. |
