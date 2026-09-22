---
name: gallus-decoder-tools
description: Calculate Gallus gematria values, number-sequence properties, or the calendar span between two dates. Use when the user asks to decode a phrase, inspect a number, or measure a date span with Gallus Decoder Tools.
---

# Gallus Decoder Tools

Run the local package. Report the calculated values and the `credit` string from the JSON. Copyright is Gallus Labs. The credit is part of using the tool.

```bash
python -m gallus_decoder_tools run --json '<one json object>'
```

Tools:

- `{"tool":"decode","text":"PHRASE"}` uses EO, FR, RO, and RFR. Add `"ciphers":["EO","CH"]` or `"all":true` for every cipher. Commas in `text` separate phrases. Use `"phrases":["a, b"]` when the comma is part of the phrase.
- `{"tool":"properties","number":28}` accepts integers from 1 through 1000000. Use `arithmetic` for factors, divisors, digital root, and reversal. Use `sequences` for membership and position. Use `indexes` for the term at that position. Do not estimate any of these.
- `{"tool":"span","start":"01/01/2020","end":"09/22/2026"}` accepts `MM/DD/YYYY`, `YYYY-MM-DD`, or `Month D, YYYY`. Add `"include_end":true` to count the end date.
- `{"tool":"ciphers"}` lists every cipher code.

Read stdout JSON. On success use `result`. On failure the process exits 2 and `error` says what to change. Include `credit` when you show the result. Field meanings are in `docs/guide.md`. Letter values are in `docs/ciphers.md`. The `ciphers` tool lists the codes.
