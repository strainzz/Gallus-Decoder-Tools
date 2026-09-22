# SPDX-License-Identifier: LicenseRef-Gallus-Labs-Noncommercial
# Copyright 2026 Gallus Labs
"""Decode a phrase with the gematria cipher maps."""

from __future__ import annotations

from gallus_decoder_tools.ciphers import calculate_gematria, ciphers
from gallus_decoder_tools.errors import HarnessError

# Codes are the stable agent interface. Names are the labels a person reads.
CIPHER_NAMES: dict[str, str] = {
    "EO": "English Ordinal",
    "FR": "Full Reduction",
    "SR": "Single Reduction",
    "RO": "Reverse Ordinal",
    "RFR": "Reverse Full Reduction",
    "JO": "Jewish Ordinal",
    "JR": "Jewish Reduction",
    "CH": "Chaldean",
    "SUM": "Sumerian",
    "SAT": "Satanic",
    "HEB": "Hebrew",
    "RSUM": "Reverse Sumerian",
    "RSAT": "Reverse Satanic",
    "PRIM": "Primes",
    "SQ": "Squares",
    "TRI": "Trigonal",
    "FIB": "Fibonacci",
    "SEP": "Septenary",
    "KP": "Keypad",
    "RSR": "Reverse Single Reduction",
    "RPRIM": "Reverse Primes",
    "RSQ": "Reverse Squares",
    "RTRI": "Reverse Trigonal",
    "RFIB": "Reverse Fibonacci",
    "CM": "Capitals Mixed",
    "CA": "Capitals Added",
    "RCM": "Reverse Capitals Mixed",
    "RCA": "Reverse Capitals Added",
    "KV": "KV Exception",
    "SKV": "SKV Exception",
    "EP": "EP Exception",
    "EHP": "EHP Exception",
}

DEFAULT_CIPHERS: tuple[str, ...] = ("EO", "FR", "RO", "RFR")


def list_ciphers() -> list[dict[str, str]]:
    """Return every cipher in decoder order."""
    return [
        {"code": code, "name": CIPHER_NAMES[code]}
        for code in ciphers
        if code in CIPHER_NAMES
    ]


def _all_codes() -> list[str]:
    return [code for code in ciphers if code in CIPHER_NAMES]


def resolve_ciphers(
    spec: str | list[str] | None = None,
    *,
    all_ciphers: bool = False,
) -> list[str]:
    """Turn a cipher request into ordered codes.

    Omitted input uses the four default ciphers. ``all`` uses every cipher.
    Unknown codes raise instead of being dropped.
    """
    if spec not in (None, "", []) and not isinstance(spec, (str, list)):
        raise HarnessError("ciphers must be a list of codes or a comma-separated string.")
    if all_ciphers and spec not in (None, "", []):
        raise HarnessError("Pass either ciphers or all, not both.")
    if all_ciphers:
        return _all_codes()

    if spec is None or spec == "" or spec == []:
        return list(DEFAULT_CIPHERS)

    if isinstance(spec, str):
        text = spec.strip()
        if text.lower() == "all":
            return _all_codes()
        if text.lower() == "default":
            return list(DEFAULT_CIPHERS)
        parts = [part.strip() for part in text.split(",") if part.strip()]
    else:
        parts = [str(part).strip() for part in spec if str(part).strip()]

    if not parts:
        return list(DEFAULT_CIPHERS)

    lookup = {code.lower(): code for code in ciphers}
    selected: list[str] = []
    unknown: list[str] = []
    for part in parts:
        code = lookup.get(part.lower())
        if code is None or code not in CIPHER_NAMES:
            unknown.append(part)
        elif code not in selected:
            selected.append(code)
    if unknown:
        known = ", ".join(ciphers)
        raise HarnessError(
            f"Unknown cipher code(s): {', '.join(unknown)}. Known codes: {known}."
        )
    return selected


def _phrases_from_text(text: str) -> list[str]:
    phrases = [part.strip() for part in text.split(",") if part.strip()]
    if not phrases:
        raise HarnessError("Provide text to decode.")
    return phrases


def decode(
    text: str | None = None,
    phrases: list[str] | None = None,
    ciphers_spec: str | list[str] | None = None,
    *,
    all_ciphers: bool = False,
) -> dict:
    """Decode one or more phrases.

    A comma in ``text`` separates phrases, matching the decoder command.
    ``phrases`` is the explicit list and is used as given.
    Letters use the cipher map. A run of digits is added as that integer.
    Other characters are skipped. Hebrew and capital ciphers keep case.
    """
    codes = resolve_ciphers(ciphers_spec, all_ciphers=all_ciphers)
    if phrases is not None and not isinstance(phrases, list):
        raise HarnessError("phrases must be a list of strings.")
    if phrases is not None:
        cleaned = [str(phrase).strip() for phrase in phrases if str(phrase).strip()]
        if not cleaned:
            raise HarnessError("Provide text to decode.")
    elif text is not None:
        cleaned = _phrases_from_text(str(text))
    else:
        raise HarnessError("Provide text to decode.")

    decoded = []
    for phrase in cleaned:
        values = [
            {
                "code": code,
                "name": CIPHER_NAMES[code],
                "value": calculate_gematria(phrase, ciphers[code], cipher_code=code),
            }
            for code in codes
        ]
        decoded.append({"text": phrase, "values": values})
    return {"phrases": decoded}
