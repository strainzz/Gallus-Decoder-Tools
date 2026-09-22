# Gallus Decoder Tools

This repository is Gallus Decoder Tools: gematria decode, number properties, and date span. Calculate with the package and return its JSON, including the credit.

Copyright is Gallus Labs. The credit line is `Gallus Decoder Tools by Gallus`. It is required by `NOTICE` under the Apache License 2.0. Leave that line in the JSON, in `NOTICE`, and in the license appendix. The operating guide is `docs/guide.md`. All 32 ciphers are in `docs/ciphers.md`.

## Run

From a checkout with the package installed, or with `PYTHONPATH=src`:

```bash
python -m gallus_decoder_tools decode "TEXT"
python -m gallus_decoder_tools decode "TEXT" --ciphers eo,fr
python -m gallus_decoder_tools decode "TEXT" --all
python -m gallus_decoder_tools ciphers
python -m gallus_decoder_tools properties NUMBER
python -m gallus_decoder_tools span START END
python -m gallus_decoder_tools span START END --include-end
python -m gallus_decoder_tools run --json '{"tool":"properties","number":28}'
```

Stdout is one JSON object. `ok` is true on success. A rejected request exits 2 with `ok` false and an `error` string. Both shapes include `credit`.

## Request fields

- `decode`: `text` (commas separate phrases) or `phrases` (a list). Optional `ciphers` as a list or comma-separated codes. Optional `all`. Default ciphers are `EO`, `FR`, `RO`, `RFR`. `--all` uses every cipher in `docs/ciphers.md`.
- `properties`: `number`, an integer from 1 through 1000000.
- `span`: `start`, `end`, optional `include_end`. Dates are `MM/DD/YYYY`, `YYYY-MM-DD`, or `Month D, YYYY`.
- `ciphers`: no fields. Returns the code list.

Letters use the cipher map. A run of digits is added as that integer. Hebrew and capital ciphers keep the original case. Sequence positions keep the first index when a value repeats. `include_end` counts the end date as one day. The span tool puts the earlier date first.

Tool names and field names are in `agent-tools.json`.

## Working on this repo

Keep the tools pure functions of their inputs. A change to a cipher map, a sequence index, or a span breakdown needs a test that locks the new value. A new cipher also has to appear in the README table. Run `python -m unittest discover -s tests` with `PYTHONPATH=src`.
