# Cipher catalog

Gallus Decoder Tools includes 32 ciphers. A plain decode uses the four marked Everyday. `gallus-decoder-tools decode "PHRASE" --all` runs the full catalog. `gallus-decoder-tools ciphers` prints the same codes.

Copyright 2026 Gallus Labs.

## How a total is produced

Each letter is looked up in the map for that cipher and added. A run of digits is added as that whole number. Spaces and punctuation are skipped.

Most ciphers fold upper and lower case together. Hebrew and the four capital ciphers keep the case you type. In Hebrew, lowercase `k` is 10 and uppercase `K` is 20.

## The ciphers

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
