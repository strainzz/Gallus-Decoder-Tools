<p align="center">
  <img src="docs/brand/GallusLogo.png" alt="Gallus" width="72">
</p>

# Contributing

Gallus Decoder Tools is Gallus Labs software. Copyright 2026 Gallus Labs. Changes keep the credit `Gallus Decoder Tools by Gallus Labs` in `NOTICE`, in `LICENSE`, and in the JSON every command prints. Do not add moon phase, zodiac, weekday-name decodes, or a sports decode method. Those are Gallus Bot tools for paying members. Do not weaken the no-sale terms.

## Set up

Python 3.11 or newer.

```bash
python -m pip install -e .
python -m unittest discover -s tests
```

The test run is the check that has to pass. GitHub Actions runs the same command on Python 3.11 and 3.14.

## What a change includes

- A calculation change needs a test that locks the new value.
- A new or renamed cipher needs a row in the code table in [docs/ciphers.md](docs/ciphers.md) and its letter values in that same catalog. The manual in [docs/guide.md](docs/guide.md) has to stay accurate when a field or an error sentence changes.
- The public pages stay free of personal contact details. Copyright remains Gallus Labs.
- The tools stay local. A change calculates from the phrase, number, or dates it was given.

## Reports

Open a GitHub issue for a wrong total, a broken command, or a gap in the guide. Use a private security advisory for a vulnerability, as described in [SECURITY.md](SECURITY.md).
