<p align="center">
  <img src="docs/brand/GallusLogo.png" alt="Gallus" width="72">
</p>

# Contributing

Gallus Decoder Tools is Gallus Labs software. Copyright 2026 Gallus Labs. Changes keep the credit `Gallus Decoder Tools by Gallus` in `NOTICE`, in the license appendix, and in the JSON every command prints.

## Set up

Python 3.11 or newer.

```bash
python -m pip install -e .
python -m unittest discover -s tests
```

The test run is the check that has to pass. GitHub Actions runs the same command on Python 3.11 and 3.14.

## What a change includes

- A calculation change needs a test that locks the new value.
- A new or renamed cipher needs a row in [docs/ciphers.md](docs/ciphers.md). The catalog test reads that table.
- The public pages stay free of personal contact details. Copyright remains Gallus Labs.
- The tools stay local. A change calculates from the phrase, number, or dates it was given.

## Reports

Open a GitHub issue for a wrong total, a broken command, or a gap in the guide. Use a private security advisory for a vulnerability, as described in [SECURITY.md](SECURITY.md).
