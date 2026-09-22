# SPDX-License-Identifier: LicenseRef-Gallus-Labs-Noncommercial
# Copyright 2026 Gallus Labs
"""Errors an agent can correct by changing the request."""


class HarnessError(ValueError):
    """The request is outside what these calculators accept."""
