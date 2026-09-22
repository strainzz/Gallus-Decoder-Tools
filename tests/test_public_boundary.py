# SPDX-License-Identifier: LicenseRef-Gallus-Labs-Noncommercial
# Copyright 2026 Gallus Labs
import re
import unittest
from pathlib import Path

from gallus_decoder_tools.credit import COPYRIGHT, CREDIT
from gallus_decoder_tools.gematria import list_ciphers

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
NOTICE = (ROOT / "NOTICE").read_text(encoding="utf-8")
LICENSE = (ROOT / "LICENSE").read_text(encoding="utf-8")
CIPHERS = (ROOT / "docs" / "ciphers.md").read_text(encoding="utf-8")
SKIP = {".git", "__pycache__", ".venv", "build", "dist"}


def published_text_files():
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in SKIP for part in path.parts):
            continue
        if path.suffix.lower() in {".py", ".md", ".toml", ".json", ".yml", ".yaml"} or path.name in {"LICENSE", "NOTICE"}:
            yield path


class PresentationTests(unittest.TestCase):
    def test_copyright_is_gallus_labs(self) -> None:
        self.assertEqual(COPYRIGHT, "Copyright 2026 Gallus Labs")
        for text in (NOTICE, LICENSE, README):
            self.assertIn(COPYRIGHT, text)
            self.assertIn(CREDIT, text)
        pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
        self.assertIn('name = "Gallus Labs"', pyproject)
        self.assertNotIn("email", pyproject)

    def test_catalog_lists_every_cipher(self) -> None:
        ciphers = list_ciphers()
        self.assertEqual(len(ciphers), 32)
        self.assertIn("docs/ciphers.md", README)
        self.assertIn("English Ordinal", README)
        self.assertIn("DOG", README)
        workflow = (ROOT / ".github" / "workflows" / "tests.yml").read_text(encoding="utf-8")
        self.assertIn("python -m unittest discover -s tests", workflow)
        self.assertIn("32 ciphers", CIPHERS)
        for cipher in ciphers:
            self.assertIn(f"| {cipher['code']} | {cipher['name']} |", CIPHERS)

    def test_published_tree_has_no_personal_material(self) -> None:
        banned = (
            "stra" + "inz",
            "big roo" + "ster",
            "ge" + "mz",
            "disc" + "ord",
            "sc" + "ry",
        )
        repository = re.compile(
            "https://github.com/" + "stra" + "inzz" + "/gallus-decoder-tools",
            re.IGNORECASE,
        )
        email = re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}")
        offenders = []
        for path in published_text_files():
            text = repository.sub("", path.read_text(encoding="utf-8"))
            lowered = text.lower()
            for word in banned:
                if word in lowered:
                    offenders.append(f"{path.relative_to(ROOT)}: private name")
            for match in email.findall(text):
                offenders.append(f"{path.relative_to(ROOT)}: email {match}")
        self.assertEqual(offenders, [])


if __name__ == "__main__":
    unittest.main()
