# SPDX-License-Identifier: LicenseRef-Gallus-Labs-Noncommercial
# Copyright 2026 Gallus Labs
"""Letter maps and the gematria sum for Gallus Decoder Tools."""

from typing import Literal

CipherType = Literal[
    "EO",
    "FR",
    "SR",
    "RO",
    "RFR",
    "JO",
    "JR",
    "CH",
    "SUM",
    "SAT",
    "HEB",
    "RSUM",
    "RSAT",
    "PRIM",
    "SQ",
    "TRI",
    "FIB",
    "SEP",
    "KP",
    "RSR",
    "RPRIM",
    "RSQ",
    "RTRI",
    "RFIB",
    "CM",
    "CA",
    "RCM",
    "RCA",
    "KV",
    "SKV",
    "EP",
    "EHP",
]

# Define all ciphers with fixed dictionaries
english_ordinal = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}

full_reduction = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 1,
    "K": 2,
    "L": 3,
    "M": 4,
    "N": 5,
    "O": 6,
    "P": 7,
    "Q": 8,
    "R": 9,
    "S": 1,
    "T": 2,
    "U": 3,
    "V": 4,
    "W": 5,
    "X": 6,
    "Y": 7,
    "Z": 8,
}

single_reduction = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 1,
    "K": 2,
    "L": 3,
    "M": 4,
    "N": 5,
    "O": 6,
    "P": 7,
    "Q": 8,
    "R": 9,
    "S": 10,
    "T": 2,
    "U": 3,
    "V": 4,
    "W": 5,
    "X": 6,
    "Y": 7,
    "Z": 8,
}

reverse_ordinal = {
    "A": 26,
    "B": 25,
    "C": 24,
    "D": 23,
    "E": 22,
    "F": 21,
    "G": 20,
    "H": 19,
    "I": 18,
    "J": 17,
    "K": 16,
    "L": 15,
    "M": 14,
    "N": 13,
    "O": 12,
    "P": 11,
    "Q": 10,
    "R": 9,
    "S": 8,
    "T": 7,
    "U": 6,
    "V": 5,
    "W": 4,
    "X": 3,
    "Y": 2,
    "Z": 1,
}

reverse_full_reduction = {
    "A": 8,
    "B": 7,
    "C": 6,
    "D": 5,
    "E": 4,
    "F": 3,
    "G": 2,
    "H": 1,
    "I": 9,
    "J": 8,
    "K": 7,
    "L": 6,
    "M": 5,
    "N": 4,
    "O": 3,
    "P": 2,
    "Q": 1,
    "R": 9,
    "S": 8,
    "T": 7,
    "U": 6,
    "V": 5,
    "W": 4,
    "X": 3,
    "Y": 2,
    "Z": 1,
}

# Jewish/Hebrew ciphers

# Hebrew cipher with case sensitivity: lowercase 'k' = 10, uppercase 'K' = 20
hebrew = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "k": 10,  # lowercase k = 10
    "K": 20,  # uppercase K = 20
    "L": 20,
    "M": 30,
    "N": 40,
    "O": 50,
    "P": 60,
    "Q": 70,
    "R": 80,
    "S": 90,
    "T": 100,
    "U": 200,
    "X": 300,
    "Y": 400,
    "Z": 500,
    "J": 600,
    "V": 700,
    "W": 800,
}

jewish_ordinal = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 20,
    "L": 30,
    "M": 40,
    "N": 50,
    "O": 60,
    "P": 70,
    "Q": 80,
    "R": 90,
    "S": 100,
    "T": 200,
    "U": 300,
    "V": 400,
    "W": 500,
    "X": 600,
    "Y": 700,
    "Z": 800,
}

jewish_reduction = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 1,
    "K": 2,
    "L": 3,
    "M": 4,
    "N": 5,
    "O": 6,
    "P": 7,
    "Q": 8,
    "R": 9,
    "S": 1,
    "T": 2,
    "U": 3,
    "V": 4,
    "W": 5,
    "X": 6,
    "Y": 7,
    "Z": 8,
}

# Chaldean cipher (ancient Babylonian)
chaldean = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 8,
    "G": 3,
    "H": 5,
    "I": 1,
    "J": 1,
    "K": 2,
    "L": 3,
    "M": 4,
    "N": 5,
    "O": 7,
    "P": 8,
    "Q": 1,
    "R": 2,
    "S": 3,
    "T": 4,
    "U": 6,
    "V": 6,
    "W": 6,
    "X": 5,
    "Y": 1,
    "Z": 7,
}

# Additional ciphers (not currently used but available)
sumerian = {
    "A": 6,
    "B": 12,
    "C": 18,
    "D": 24,
    "E": 30,
    "F": 36,
    "G": 42,
    "H": 48,
    "I": 54,
    "J": 60,
    "K": 66,
    "L": 72,
    "M": 78,
    "N": 84,
    "O": 90,
    "P": 96,
    "Q": 102,
    "R": 108,
    "S": 114,
    "T": 120,
    "U": 126,
    "V": 132,
    "W": 138,
    "X": 144,
    "Y": 150,
    "Z": 156,
}

satanic = {
    "A": 36,
    "B": 37,
    "C": 38,
    "D": 39,
    "E": 40,
    "F": 41,
    "G": 42,
    "H": 43,
    "I": 44,
    "J": 45,
    "K": 46,
    "L": 47,
    "M": 48,
    "N": 49,
    "O": 50,
    "P": 51,
    "Q": 52,
    "R": 53,
    "S": 54,
    "T": 55,
    "U": 56,
    "V": 57,
    "W": 58,
    "X": 59,
    "Y": 60,
    "Z": 61,
}

# ============================================================================
# TIER 1: Essential Ciphers - Reverse Variants and Mathematical Sequences
# ============================================================================

# Reverse Sumerian: Reverse Ordinal values multiplied by 6
reverse_sumerian = {
    "A": 156,  # 26 * 6
    "B": 150,  # 25 * 6
    "C": 144,  # 24 * 6
    "D": 138,  # 23 * 6
    "E": 132,  # 22 * 6
    "F": 126,  # 21 * 6
    "G": 120,  # 20 * 6
    "H": 114,  # 19 * 6
    "I": 108,  # 18 * 6
    "J": 102,  # 17 * 6
    "K": 96,  # 16 * 6
    "L": 90,  # 15 * 6
    "M": 84,  # 14 * 6
    "N": 78,  # 13 * 6
    "O": 72,  # 12 * 6
    "P": 66,  # 11 * 6
    "Q": 60,  # 10 * 6
    "R": 54,  # 9 * 6
    "S": 48,  # 8 * 6
    "T": 42,  # 7 * 6
    "U": 36,  # 6 * 6
    "V": 30,  # 5 * 6
    "W": 24,  # 4 * 6
    "X": 18,  # 3 * 6
    "Y": 12,  # 2 * 6
    "Z": 6,  # 1 * 6
}

# Reverse Satanic: Reverse Ordinal + 35 (reverse of Satanic)
reverse_satanic = {
    "A": 61,  # 26 + 35
    "B": 60,  # 25 + 35
    "C": 59,  # 24 + 35
    "D": 58,  # 23 + 35
    "E": 57,  # 22 + 35
    "F": 56,  # 21 + 35
    "G": 55,  # 20 + 35
    "H": 54,  # 19 + 35
    "I": 53,  # 18 + 35
    "J": 52,  # 17 + 35
    "K": 51,  # 16 + 35
    "L": 50,  # 15 + 35
    "M": 49,  # 14 + 35
    "N": 48,  # 13 + 35
    "O": 47,  # 12 + 35
    "P": 46,  # 11 + 35
    "Q": 45,  # 10 + 35
    "R": 44,  # 9 + 35
    "S": 43,  # 8 + 35
    "T": 42,  # 7 + 35
    "U": 41,  # 6 + 35
    "V": 40,  # 5 + 35
    "W": 39,  # 4 + 35
    "X": 38,  # 3 + 35
    "Y": 37,  # 2 + 35
    "Z": 36,  # 1 + 35
}

# Primes: Prime numbers in sequence
primes = {
    "A": 2,
    "B": 3,
    "C": 5,
    "D": 7,
    "E": 11,
    "F": 13,
    "G": 17,
    "H": 19,
    "I": 23,
    "J": 29,
    "K": 31,
    "L": 37,
    "M": 41,
    "N": 43,
    "O": 47,
    "P": 53,
    "Q": 59,
    "R": 61,
    "S": 67,
    "T": 71,
    "U": 73,
    "V": 79,
    "W": 83,
    "X": 89,
    "Y": 97,
    "Z": 101,
}

# Squares: Perfect squares (n^2)
squares = {
    "A": 1,  # 1^2
    "B": 4,  # 2^2
    "C": 9,  # 3^2
    "D": 16,  # 4^2
    "E": 25,  # 5^2
    "F": 36,  # 6^2
    "G": 49,  # 7^2
    "H": 64,  # 8^2
    "I": 81,  # 9^2
    "J": 100,  # 10^2
    "K": 121,  # 11^2
    "L": 144,  # 12^2
    "M": 169,  # 13^2
    "N": 196,  # 14^2
    "O": 225,  # 15^2
    "P": 256,  # 16^2
    "Q": 289,  # 17^2
    "R": 324,  # 18^2
    "S": 361,  # 19^2
    "T": 400,  # 20^2
    "U": 441,  # 21^2
    "V": 484,  # 22^2
    "W": 529,  # 23^2
    "X": 576,  # 24^2
    "Y": 625,  # 25^2
    "Z": 676,  # 26^2
}

# Trigonal/Triangular: Triangular numbers (n(n+1)/2)
trigonal = {
    "A": 1,  # 1(1+1)/2
    "B": 3,  # 2(2+1)/2
    "C": 6,  # 3(3+1)/2
    "D": 10,  # 4(4+1)/2
    "E": 15,  # 5(5+1)/2
    "F": 21,  # 6(6+1)/2
    "G": 28,  # 7(7+1)/2
    "H": 36,  # 8(8+1)/2
    "I": 45,  # 9(9+1)/2
    "J": 55,  # 10(10+1)/2
    "K": 66,  # 11(11+1)/2
    "L": 78,  # 12(12+1)/2
    "M": 91,  # 13(13+1)/2
    "N": 105,  # 14(14+1)/2
    "O": 120,  # 15(15+1)/2
    "P": 136,  # 16(16+1)/2
    "Q": 153,  # 17(17+1)/2
    "R": 171,  # 18(18+1)/2
    "S": 190,  # 19(19+1)/2
    "T": 210,  # 20(20+1)/2
    "U": 231,  # 21(21+1)/2
    "V": 253,  # 22(22+1)/2
    "W": 276,  # 23(23+1)/2
    "X": 300,  # 24(24+1)/2
    "Y": 325,  # 25(25+1)/2
    "Z": 351,  # 26(26+1)/2
}

# Fibonacci: Fibonacci sequence (starting from 0, 1)
fibonacci = {
    "A": 0,
    "B": 1,
    "C": 1,
    "D": 2,
    "E": 3,
    "F": 5,
    "G": 8,
    "H": 13,
    "I": 21,
    "J": 34,
    "K": 55,
    "L": 89,
    "M": 144,
    "N": 233,
    "O": 377,
    "P": 610,
    "Q": 987,
    "R": 1597,
    "S": 2584,
    "T": 4181,
    "U": 6765,
    "V": 10946,
    "W": 17711,
    "X": 28657,
    "Y": 46368,
    "Z": 75025,
}

# Septenary: Base-7 system (A=1, B=2, ..., G=7, then repeats)
septenary = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 1,
    "I": 2,
    "J": 3,
    "K": 4,
    "L": 5,
    "M": 6,
    "N": 7,
    "O": 1,
    "P": 2,
    "Q": 3,
    "R": 4,
    "S": 5,
    "T": 6,
    "U": 7,
    "V": 1,
    "W": 2,
    "X": 3,
    "Y": 4,
    "Z": 5,
}

# Keypad: Telephone keypad layout
keypad = {
    "A": 2,
    "B": 2,
    "C": 2,
    "D": 3,
    "E": 3,
    "F": 3,
    "G": 4,
    "H": 4,
    "I": 4,
    "J": 5,
    "K": 5,
    "L": 5,
    "M": 6,
    "N": 6,
    "O": 6,
    "P": 7,
    "Q": 7,
    "R": 7,
    "S": 7,
    "T": 8,
    "U": 8,
    "V": 8,
    "W": 9,
    "X": 9,
    "Y": 9,
    "Z": 9,
}

# ============================================================================
# TIER 2: Reverse Variants of Mathematical Sequences
# ============================================================================

# Reverse Single Reduction: Reverse of Single Reduction
reverse_single_reduction = {
    "A": 8,  # Reverse of Z=8
    "B": 7,  # Reverse of Y=7
    "C": 6,  # Reverse of X=6
    "D": 5,  # Reverse of W=5
    "E": 4,  # Reverse of V=4
    "F": 3,  # Reverse of U=3
    "G": 2,  # Reverse of T=2
    "H": 10,  # Reverse of S=10
    "I": 9,  # Reverse of R=9
    "J": 8,  # Reverse of Q=8
    "K": 7,  # Reverse of P=7
    "L": 6,  # Reverse of O=6
    "M": 5,  # Reverse of N=5
    "N": 4,  # Reverse of M=4
    "O": 3,  # Reverse of L=3
    "P": 2,  # Reverse of K=2
    "Q": 1,  # Reverse of J=1
    "R": 9,  # Reverse of I=9
    "S": 8,  # Reverse of H=8
    "T": 7,  # Reverse of G=7
    "U": 6,  # Reverse of F=6
    "V": 5,  # Reverse of E=5
    "W": 4,  # Reverse of D=4
    "X": 3,  # Reverse of C=3
    "Y": 2,  # Reverse of B=2
    "Z": 1,  # Reverse of A=1
}

# Reverse Primes: Reverse order of primes
reverse_primes = {
    "A": 101,  # Reverse of Z=101
    "B": 97,  # Reverse of Y=97
    "C": 89,  # Reverse of X=89
    "D": 83,  # Reverse of W=83
    "E": 79,  # Reverse of V=79
    "F": 73,  # Reverse of U=73
    "G": 71,  # Reverse of T=71
    "H": 67,  # Reverse of S=67
    "I": 61,  # Reverse of R=61
    "J": 59,  # Reverse of Q=59
    "K": 53,  # Reverse of P=53
    "L": 47,  # Reverse of O=47
    "M": 43,  # Reverse of N=43
    "N": 41,  # Reverse of M=41
    "O": 37,  # Reverse of L=37
    "P": 31,  # Reverse of K=31
    "Q": 29,  # Reverse of J=29
    "R": 23,  # Reverse of I=23
    "S": 19,  # Reverse of H=19
    "T": 17,  # Reverse of G=17
    "U": 13,  # Reverse of F=13
    "V": 11,  # Reverse of E=11
    "W": 7,  # Reverse of D=7
    "X": 5,  # Reverse of C=5
    "Y": 3,  # Reverse of B=3
    "Z": 2,  # Reverse of A=2
}

# Reverse Squares: Reverse order of squares
reverse_squares = {
    "A": 676,  # Reverse of Z=676
    "B": 625,  # Reverse of Y=625
    "C": 576,  # Reverse of X=576
    "D": 529,  # Reverse of W=529
    "E": 484,  # Reverse of V=484
    "F": 441,  # Reverse of U=441
    "G": 400,  # Reverse of T=400
    "H": 361,  # Reverse of S=361
    "I": 324,  # Reverse of R=324
    "J": 289,  # Reverse of Q=289
    "K": 256,  # Reverse of P=256
    "L": 225,  # Reverse of O=225
    "M": 196,  # Reverse of N=196
    "N": 169,  # Reverse of M=169
    "O": 144,  # Reverse of L=144
    "P": 121,  # Reverse of K=121
    "Q": 100,  # Reverse of J=100
    "R": 81,  # Reverse of I=81
    "S": 64,  # Reverse of H=64
    "T": 49,  # Reverse of G=49
    "U": 36,  # Reverse of F=36
    "V": 25,  # Reverse of E=25
    "W": 16,  # Reverse of D=16
    "X": 9,  # Reverse of C=9
    "Y": 4,  # Reverse of B=4
    "Z": 1,  # Reverse of A=1
}

# Reverse Trigonal: Reverse order of triangular numbers
reverse_trigonal = {
    "A": 351,  # Reverse of Z=351
    "B": 325,  # Reverse of Y=325
    "C": 300,  # Reverse of X=300
    "D": 276,  # Reverse of W=276
    "E": 253,  # Reverse of V=253
    "F": 231,  # Reverse of U=231
    "G": 210,  # Reverse of T=210
    "H": 190,  # Reverse of S=190
    "I": 171,  # Reverse of R=171
    "J": 153,  # Reverse of Q=153
    "K": 136,  # Reverse of P=136
    "L": 120,  # Reverse of O=120
    "M": 105,  # Reverse of N=105
    "N": 91,  # Reverse of M=91
    "O": 78,  # Reverse of L=78
    "P": 66,  # Reverse of K=66
    "Q": 55,  # Reverse of J=55
    "R": 45,  # Reverse of I=45
    "S": 36,  # Reverse of H=36
    "T": 28,  # Reverse of G=28
    "U": 21,  # Reverse of F=21
    "V": 15,  # Reverse of E=15
    "W": 10,  # Reverse of D=10
    "X": 6,  # Reverse of C=6
    "Y": 3,  # Reverse of B=3
    "Z": 1,  # Reverse of A=1
}

# Reverse Fibonacci: Reverse order of Fibonacci sequence
reverse_fibonacci = {
    "A": 75025,  # Reverse of Z=75025
    "B": 46368,  # Reverse of Y=46368
    "C": 28657,  # Reverse of X=28657
    "D": 17711,  # Reverse of W=17711
    "E": 10946,  # Reverse of V=10946
    "F": 6765,  # Reverse of U=6765
    "G": 4181,  # Reverse of T=4181
    "H": 2584,  # Reverse of S=2584
    "I": 1597,  # Reverse of R=1597
    "J": 987,  # Reverse of Q=987
    "K": 610,  # Reverse of P=610
    "L": 377,  # Reverse of O=377
    "M": 233,  # Reverse of N=233
    "N": 144,  # Reverse of M=144
    "O": 89,  # Reverse of L=89
    "P": 55,  # Reverse of K=55
    "Q": 34,  # Reverse of J=34
    "R": 21,  # Reverse of I=21
    "S": 13,  # Reverse of H=13
    "T": 8,  # Reverse of G=8
    "U": 5,  # Reverse of F=5
    "V": 3,  # Reverse of E=3
    "W": 2,  # Reverse of D=2
    "X": 1,  # Reverse of C=1
    "Y": 1,  # Reverse of B=1
    "Z": 0,  # Reverse of A=0
}

# ============================================================================
# TIER 3: Capital Variants
# ============================================================================

# Capitals Mixed: Lowercase = ordinal, Uppercase = ordinal + 26
capitals_mixed = {
    "A": 27,  # Uppercase A = 1 + 26
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
    "a": 1,  # Lowercase = ordinal
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

# Capitals Added: Uppercase adds 26 to ordinal value
capitals_added = {
    "A": 27,  # 1 + 26
    "B": 28,  # 2 + 26
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
    "a": 1,  # Lowercase = ordinal
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

# Reverse Capitals Mixed: Reverse of Capitals Mixed
reverse_capitals_mixed = {
    "A": 52,  # Reverse of Z=52
    "B": 51,
    "C": 50,
    "D": 49,
    "E": 48,
    "F": 47,
    "G": 46,
    "H": 45,
    "I": 44,
    "J": 43,
    "K": 42,
    "L": 41,
    "M": 40,
    "N": 39,
    "O": 38,
    "P": 37,
    "Q": 36,
    "R": 35,
    "S": 34,
    "T": 33,
    "U": 32,
    "V": 31,
    "W": 30,
    "X": 29,
    "Y": 28,
    "Z": 27,
    "a": 26,  # Reverse lowercase
    "b": 25,
    "c": 24,
    "d": 23,
    "e": 22,
    "f": 21,
    "g": 20,
    "h": 19,
    "i": 18,
    "j": 17,
    "k": 16,
    "l": 15,
    "m": 14,
    "n": 13,
    "o": 12,
    "p": 11,
    "q": 10,
    "r": 9,
    "s": 8,
    "t": 7,
    "u": 6,
    "v": 5,
    "w": 4,
    "x": 3,
    "y": 2,
    "z": 1,
}

# Reverse Capitals Added: Reverse of Capitals Added
reverse_capitals_added = {
    "A": 52,  # Same as reverse capitals mixed
    "B": 51,
    "C": 50,
    "D": 49,
    "E": 48,
    "F": 47,
    "G": 46,
    "H": 45,
    "I": 44,
    "J": 43,
    "K": 42,
    "L": 41,
    "M": 40,
    "N": 39,
    "O": 38,
    "P": 37,
    "Q": 36,
    "R": 35,
    "S": 34,
    "T": 33,
    "U": 32,
    "V": 31,
    "W": 30,
    "X": 29,
    "Y": 28,
    "Z": 27,
    "a": 26,
    "b": 25,
    "c": 24,
    "d": 23,
    "e": 22,
    "f": 21,
    "g": 20,
    "h": 19,
    "i": 18,
    "j": 17,
    "k": 16,
    "l": 15,
    "m": 14,
    "n": 13,
    "o": 12,
    "p": 11,
    "q": 10,
    "r": 9,
    "s": 8,
    "t": 7,
    "u": 6,
    "v": 5,
    "w": 4,
    "x": 3,
    "y": 2,
    "z": 1,
}

# ============================================================================
# TIER 4: Exception Variants and Standard
# ============================================================================

# KV Exception: Full Reduction with K=11, V=22 (master numbers preserved)
# K is the 11th letter and V is the 22nd - these are master numbers in
# numerology and are NOT reduced in this cipher variant.
kv_exception = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 1,
    "K": 11,  # Master number - not reduced
    "L": 3,
    "M": 4,
    "N": 5,
    "O": 6,
    "P": 7,
    "Q": 8,
    "R": 9,
    "S": 1,
    "T": 2,
    "U": 3,
    "V": 22,  # Master number - not reduced
    "W": 5,
    "X": 6,
    "Y": 7,
    "Z": 8,
}

# SKV Exception: Full Reduction with S=10, K=11, V=22 (all exceptions preserved)
# S is the 19th letter (1+9=10), K is the 11th, V is the 22nd. These three
# letters skip reduction in this cipher variant - the strictest exception
# set stacking on top of KV Exception.
skv_exception = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 1,
    "K": 11,  # Master number - not reduced
    "L": 3,
    "M": 4,
    "N": 5,
    "O": 6,
    "P": 7,
    "Q": 8,
    "R": 9,
    "S": 10,  # Exception - not reduced
    "T": 2,
    "U": 3,
    "V": 22,  # Master number - not reduced
    "W": 5,
    "X": 6,
    "Y": 7,
    "Z": 8,
}

# EP Exception: Exception variant
ep_exception = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 1,
    "K": 2,
    "L": 3,
    "M": 4,
    "N": 5,
    "O": 6,
    "P": 7,
    "Q": 8,
    "R": 9,
    "S": 1,
    "T": 2,
    "U": 3,
    "V": 4,
    "W": 5,
    "X": 6,
    "Y": 7,
    "Z": 8,
}

# EHP Exception: Exception variant
ehp_exception = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 1,
    "K": 2,
    "L": 3,
    "M": 4,
    "N": 5,
    "O": 6,
    "P": 7,
    "Q": 8,
    "R": 9,
    "S": 1,
    "T": 2,
    "U": 3,
    "V": 4,
    "W": 5,
    "X": 6,
    "Y": 7,
    "Z": 8,
}


# Export the ciphers dictionary
ciphers: dict[CipherType, dict[str, int]] = {
    # Original ciphers
    "EO": english_ordinal,
    "FR": full_reduction,
    "SR": single_reduction,
    "RO": reverse_ordinal,
    "RFR": reverse_full_reduction,
    "JO": jewish_ordinal,
    "JR": jewish_reduction,
    "CH": chaldean,
    "SUM": sumerian,
    "SAT": satanic,
    # Hebrew cipher (case-sensitive)
    "HEB": hebrew,
    # Tier 1: Essential ciphers
    "RSUM": reverse_sumerian,
    "RSAT": reverse_satanic,
    "PRIM": primes,
    "SQ": squares,
    "TRI": trigonal,
    "FIB": fibonacci,
    "SEP": septenary,
    "KP": keypad,
    # Tier 2: Reverse variants
    "RSR": reverse_single_reduction,
    "RPRIM": reverse_primes,
    "RSQ": reverse_squares,
    "RTRI": reverse_trigonal,
    "RFIB": reverse_fibonacci,
    # Tier 3: Capital variants
    "CM": capitals_mixed,
    "CA": capitals_added,
    "RCM": reverse_capitals_mixed,
    "RCA": reverse_capitals_added,
    # Tier 4: Exception variants
    "KV": kv_exception,
    "SKV": skv_exception,
    "EP": ep_exception,
    "EHP": ehp_exception,
}


def calculate_gematria(text: str, cipher: dict[str, int], cipher_code: str = None) -> int:
    """Calculate the gematria value of a text using the specified cipher.

    Args:
        text: The text to calculate the gematria value for
        cipher: The cipher dictionary to use for calculation
        cipher_code: Optional cipher code (e.g., "HEB") for special handling

    Returns:
        The calculated gematria value

    """
    total = 0
    i = 0

    # Hebrew cipher requires case sensitivity - don't convert to uppercase
    # Capital variants also need case sensitivity
    case_sensitive_ciphers = {"HEB", "CM", "CA", "RCM", "RCA"}
    if cipher_code in case_sensitive_ciphers:
        # Keep original case for case-sensitive ciphers
        processed_text = text
    else:
        # Convert to uppercase for standard ciphers
        processed_text = text.upper()

    while i < len(processed_text):
        char = processed_text[i]
        if char.isalpha():
            if char in cipher:
                total += cipher[char]
            i += 1
        elif char.isdigit():
            num_start = i
            while i < len(processed_text) and processed_text[i].isdigit():
                i += 1
            number = int(processed_text[num_start:i])
            total += number
        else:
            i += 1
    return total


__all__ = ["ciphers", "CipherType", "calculate_gematria"]
