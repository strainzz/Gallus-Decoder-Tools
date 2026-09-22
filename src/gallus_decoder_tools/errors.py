# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Gallus Labs
"""Errors an agent can correct by changing the request."""


class HarnessError(ValueError):
    """The request is outside what these calculators accept."""
