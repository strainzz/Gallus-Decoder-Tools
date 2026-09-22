# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Gallus Labs
"""Command line for Gallus Decoder Tools.

Every call prints one JSON object, including the Gallus credit.
"""

from __future__ import annotations

import argparse
import json
import sys

from gallus_decoder_tools.credit import CREDIT
from gallus_decoder_tools.errors import HarnessError
from gallus_decoder_tools.gematria import decode, list_ciphers
from gallus_decoder_tools.numbers import number_properties
from gallus_decoder_tools.span import date_span


def _emit(payload: dict, code: int = 0) -> int:
    json.dump(payload, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return code


def _ok(tool: str, result: dict) -> int:
    return _emit({"ok": True, "credit": CREDIT, "tool": tool, "result": result})


def _fail(message: str) -> int:
    return _emit({"ok": False, "credit": CREDIT, "error": message}, 2)


def _as_bool(value: object, field: str) -> bool:
    if value is None or value is False:
        return False
    if value is True:
        return True
    if isinstance(value, str):
        text = value.strip().lower()
        if text in {"1", "true", "yes"}:
            return True
        if text in {"0", "false", "no", ""}:
            return False
    if isinstance(value, (int, float)) and value in (0, 1):
        return bool(value)
    raise HarnessError(f"{field} must be true or false.")


def execute(request: dict) -> dict:
    """Run one request object and return the result payload."""
    if not isinstance(request, dict):
        raise HarnessError("Request must be a JSON object.")
    tool = str(request.get("tool", "")).strip().lower()
    if tool == "decode":
        return decode(
            text=request.get("text"),
            phrases=request.get("phrases"),
            ciphers_spec=request.get("ciphers"),
            all_ciphers=_as_bool(request.get("all"), "all"),
        )
    if tool == "properties":
        if "number" not in request:
            raise HarnessError("properties requires a number.")
        return number_properties(request["number"])
    if tool == "span":
        if "start" not in request or "end" not in request:
            raise HarnessError("span requires start and end.")
        return date_span(request["start"], request["end"], request.get("include_end", False))
    if tool == "ciphers":
        return {"ciphers": list_ciphers()}
    raise HarnessError("tool must be decode, properties, span, or ciphers.")


def _load_request(raw: str) -> dict:
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise HarnessError(f"Request is not valid JSON: {exc.msg}.") from exc
    if not isinstance(payload, dict):
        raise HarnessError("Request must be a JSON object.")
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="gallus-decoder-tools",
        description="Gallus Decoder Tools: gematria, number properties, and date span.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    decode_parser = sub.add_parser("decode", help="Decode one or more phrases.")
    decode_parser.add_argument("text", help="Phrase to decode. Commas separate phrases.")
    decode_parser.add_argument(
        "--ciphers",
        default="",
        help="Comma-separated cipher codes. Omit for EO, FR, RO, RFR. Use all for every cipher.",
    )
    decode_parser.add_argument("--all", action="store_true", help="Use every cipher.")

    properties_parser = sub.add_parser("properties", help="Properties of one integer.")
    properties_parser.add_argument("number", help="Integer from 1 to 1000000.")

    span_parser = sub.add_parser("span", help="Calendar span between two dates.")
    span_parser.add_argument("start", help="Start date.")
    span_parser.add_argument("end", help="End date.")
    span_parser.add_argument(
        "--include-end",
        action="store_true",
        help="Count the end date as one day.",
    )

    sub.add_parser("ciphers", help="List cipher codes.")

    run_parser = sub.add_parser("run", help="Run one JSON request from --json or stdin.")
    run_parser.add_argument("--json", help="JSON request object.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "decode":
            result = decode(text=args.text, ciphers_spec=args.ciphers, all_ciphers=args.all)
            return _ok("decode", result)
        if args.command == "properties":
            return _ok("properties", number_properties(args.number))
        if args.command == "span":
            return _ok("span", date_span(args.start, args.end, args.include_end))
        if args.command == "ciphers":
            return _ok("ciphers", {"ciphers": list_ciphers()})
        raw = args.json if args.json is not None else sys.stdin.read()
        if not raw.strip():
            return _fail("Provide a JSON request.")
        payload = _load_request(raw)
        tool = str(payload.get("tool", "")).strip().lower()
        return _ok(tool, execute(payload))
    except HarnessError as exc:
        return _fail(str(exc))


if __name__ == "__main__":
    raise SystemExit(main())
