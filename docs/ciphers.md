<p align="center">
  <img src="brand/GallusLogo.png" alt="Gallus" width="72">
</p>

# Cipher catalog

This is the letter book for Gallus Decoder Tools. It lists all 32 ciphers, the rule that separates each one, and the value of every letter. The operating guide is [guide.md](guide.md).

Copyright 2026 Gallus Labs.

A plain decode uses four ciphers: English Ordinal (`EO`), Full Reduction (`FR`), Reverse Ordinal (`RO`), and Reverse Full Reduction (`RFR`). `gallus-decoder-tools decode "PHRASE" --all` calculates every cipher below. `gallus-decoder-tools ciphers` prints the codes and names in this same order.

## How a total is produced

The total is a sum.

1. Walk the phrase from left to right.
2. If the character is a letter in that cipher's map, add the map value.
3. If the characters form a run of digits, add that run as one integer. `A10` is the value of A plus 10. `A01` is the value of A plus 1.
4. Skip spaces, punctuation, and any letter the map does not contain.

Most ciphers fold case. `N` and `n` are the same letter. Five ciphers do not. Hebrew keeps case, and it only adds lowercase `k` among the lowercase letters. Capitals Mixed, Capitals Added, Reverse Capitals Mixed, and Reverse Capitals Added have a separate value for each case.

`New York` in English Ordinal is the walk below. Spaces are skipped.

| Letter | Value |
| --- | --- |
| N | 14 |
| E | 5 |
| W | 23 |
| Y | 25 |
| O | 15 |
| R | 18 |
| K | 11 |
| Total | 111 |

The same phrase is 39 in Full Reduction, 78 in Reverse Ordinal, and 33 in Reverse Full Reduction.

One letter is enough to see why the reductions differ. `S` is 19 in English Ordinal, 1 in Full Reduction, and 10 in Single Reduction.

## Codes

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

## Letter values

These are the maps the program adds. A cipher code is accepted in any letter case. `eo` and `EO` select the same map. The phrase itself keeps its case only for the five case-sensitive ciphers.

### Everyday

```text
EO  A1 B2 C3 D4 E5 F6 G7 H8 I9 J10 K11 L12 M13 N14 O15 P16 Q17 R18 S19 T20 U21 V22 W23 X24 Y25 Z26
FR  A1 B2 C3 D4 E5 F6 G7 H8 I9 J1 K2 L3 M4 N5 O6 P7 Q8 R9 S1 T2 U3 V4 W5 X6 Y7 Z8
RO  A26 B25 C24 D23 E22 F21 G20 H19 I18 J17 K16 L15 M14 N13 O12 P11 Q10 R9 S8 T7 U6 V5 W4 X3 Y2 Z1
RFR A8 B7 C6 D5 E4 F3 G2 H1 I9 J8 K7 L6 M5 N4 O3 P2 Q1 R9 S8 T7 U6 V5 W4 X3 Y2 Z1
```

Full Reduction is the digital root of the English Ordinal value. `S` is 19, and 1 + 9 = 10, and 1 + 0 = 1. Reverse Full Reduction is that same reduction applied to Reverse Ordinal.

### Reductions and their reverses

```text
SR  A1 B2 C3 D4 E5 F6 G7 H8 I9 J1 K2 L3 M4 N5 O6 P7 Q8 R9 S10 T2 U3 V4 W5 X6 Y7 Z8
RSR A8 B7 C6 D5 E4 F3 G2 H10 I9 J8 K7 L6 M5 N4 O3 P2 Q1 R9 S8 T7 U6 V5 W4 X3 Y2 Z1
```

Single Reduction matches Full Reduction except `S`, which stays 10. Reverse Single Reduction places that 10 on `H`, the letter opposite `S`.

### Jewish, Chaldean, Sumerian, Satanic, Hebrew

```text
JO   A1 B2 C3 D4 E5 F6 G7 H8 I9 J10 K20 L30 M40 N50 O60 P70 Q80 R90 S100 T200 U300 V400 W500 X600 Y700 Z800
JR   A1 B2 C3 D4 E5 F6 G7 H8 I9 J1 K2 L3 M4 N5 O6 P7 Q8 R9 S1 T2 U3 V4 W5 X6 Y7 Z8
CH   A1 B2 C3 D4 E5 F8 G3 H5 I1 J1 K2 L3 M4 N5 O7 P8 Q1 R2 S3 T4 U6 V6 W6 X5 Y1 Z7
SUM  A6 B12 C18 D24 E30 F36 G42 H48 I54 J60 K66 L72 M78 N84 O90 P96 Q102 R108 S114 T120 U126 V132 W138 X144 Y150 Z156
SAT  A36 B37 C38 D39 E40 F41 G42 H43 I44 J45 K46 L47 M48 N49 O50 P51 Q52 R53 S54 T55 U56 V57 W58 X59 Y60 Z61
RSUM A156 B150 C144 D138 E132 F126 G120 H114 I108 J102 K96 L90 M84 N78 O72 P66 Q60 R54 S48 T42 U36 V30 W24 X18 Y12 Z6
RSAT A61 B60 C59 D58 E57 F56 G55 H54 I53 J52 K51 L50 M49 N48 O47 P46 Q45 R44 S43 T42 U41 V40 W39 X38 Y37 Z36
HEB  A1 B2 C3 D4 E5 F6 G7 H8 I9 J600 K20 L20 M30 N40 O50 P60 Q70 R80 S90 T100 U200 V700 W800 X300 Y400 Z500
```

Sumerian is the English Ordinal value multiplied by 6. Reverse Sumerian is the Reverse Ordinal value multiplied by 6. Jewish Reduction is the digital root of Jewish Ordinal. On this alphabet that root matches Full Reduction, so `JR` and `FR` return the same total for a phrase that ignores case.

Hebrew is case-sensitive. The line above is the uppercase map. Lowercase `k` is 10. Uppercase `K` is 20. Every other lowercase letter is absent, so it adds nothing. `Hello` in Hebrew is 8, from `H` alone.

### Primes, squares, and the other letter sequences

```text
PRIM A2 B3 C5 D7 E11 F13 G17 H19 I23 J29 K31 L37 M41 N43 O47 P53 Q59 R61 S67 T71 U73 V79 W83 X89 Y97 Z101
SQ   A1 B4 C9 D16 E25 F36 G49 H64 I81 J100 K121 L144 M169 N196 O225 P256 Q289 R324 S361 T400 U441 V484 W529 X576 Y625 Z676
TRI  A1 B3 C6 D10 E15 F21 G28 H36 I45 J55 K66 L78 M91 N105 O120 P136 Q153 R171 S190 T210 U231 V253 W276 X300 Y325 Z351
FIB  A0 B1 C1 D2 E3 F5 G8 H13 I21 J34 K55 L89 M144 N233 O377 P610 Q987 R1597 S2584 T4181 U6765 V10946 W17711 X28657 Y46368 Z75025
SEP  A1 B2 C3 D4 E5 F6 G7 H1 I2 J3 K4 L5 M6 N7 O1 P2 Q3 R4 S5 T6 U7 V1 W2 X3 Y4 Z5
KP   A2 B2 C2 D3 E3 F3 G4 H4 I4 J5 K5 L5 M6 N6 O6 P7 Q7 R7 S7 T8 U8 V8 W9 X9 Y9 Z9
```

Primes uses the first 26 prime numbers. Squares uses 1 squared through 26 squared. Trigonal uses the first 26 triangular numbers. Fibonacci starts at 0 for `A`. Septenary repeats 1 through 7. Keypad uses the telephone groups: ABC is 2, DEF is 3, GHI is 4, JKL is 5, MNO is 6, PQRS is 7, TUV is 8, and WXYZ is 9.

The reverse maps read those same rows from Z back to A.

```text
RPRIM A101 B97 C89 D83 E79 F73 G71 H67 I61 J59 K53 L47 M43 N41 O37 P31 Q29 R23 S19 T17 U13 V11 W7 X5 Y3 Z2
RSQ   A676 B625 C576 D529 E484 F441 G400 H361 I324 J289 K256 L225 M196 N169 O144 P121 Q100 R81 S64 T49 U36 V25 W16 X9 Y4 Z1
RTRI  A351 B325 C300 D276 E253 F231 G210 H190 I171 J153 K136 L120 M105 N91 O78 P66 Q55 R45 S36 T28 U21 V15 W10 X6 Y3 Z1
RFIB  A75025 B46368 C28657 D17711 E10946 F6765 G4181 H2584 I1597 J987 K610 L377 M233 N144 O89 P55 Q34 R21 S13 T8 U5 V3 W2 X1 Y1 Z0
```

### Capitals

These four ciphers keep case. Capitals Mixed and Capitals Added currently use one map. Reverse Capitals Mixed and Reverse Capitals Added currently use one map. The codes remain separate so a request can name either one.

Uppercase in the mixed and added maps is the English Ordinal value plus 26. Lowercase is the English Ordinal value.

```text
CM and CA, uppercase
A27 B28 C29 D30 E31 F32 G33 H34 I35 J36 K37 L38 M39 N40 O41 P42 Q43 R44 S45 T46 U47 V48 W49 X50 Y51 Z52

CM and CA, lowercase
a1 b2 c3 d4 e5 f6 g7 h8 i9 j10 k11 l12 m13 n14 o15 p16 q17 r18 s19 t20 u21 v22 w23 x24 y25 z26
```

`Ab` is 27 + 2 = 29.

```text
RCM and RCA, uppercase
A52 B51 C50 D49 E48 F47 G46 H45 I44 J43 K42 L41 M40 N39 O38 P37 Q36 R35 S34 T33 U32 V31 W30 X29 Y28 Z27

RCM and RCA, lowercase
a26 b25 c24 d23 e22 f21 g20 h19 i18 j17 k16 l15 m14 n13 o12 p11 q10 r9 s8 t7 u6 v5 w4 x3 y2 z1
```

### Exceptions

```text
KV  A1 B2 C3 D4 E5 F6 G7 H8 I9 J1 K11 L3 M4 N5 O6 P7 Q8 R9 S1 T2 U3 V22 W5 X6 Y7 Z8
SKV A1 B2 C3 D4 E5 F6 G7 H8 I9 J1 K11 L3 M4 N5 O6 P7 Q8 R9 S10 T2 U3 V22 W5 X6 Y7 Z8
EP  A1 B2 C3 D4 E5 F6 G7 H8 I9 J1 K2 L3 M4 N5 O6 P7 Q8 R9 S1 T2 U3 V4 W5 X6 Y7 Z8
EHP A1 B2 C3 D4 E5 F6 G7 H8 I9 J1 K2 L3 M4 N5 O6 P7 Q8 R9 S1 T2 U3 V4 W5 X6 Y7 Z8
```

KV Exception is Full Reduction with `K` kept at 11 and `V` kept at 22. SKV Exception also keeps `S` at 10. EP Exception and EHP Exception use the Full Reduction map. A phrase sent to `EP` or `EHP` returns the same total as `FR`.
