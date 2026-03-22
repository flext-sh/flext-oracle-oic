"""Test constants for flext-oracle-oic tests.

Provides FlextOracleOicTestConstants, extending FlextTestsConstants with
flext-oracle-oic-specific constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsConstants


class FlextOracleOicTestConstants(FlextTestsConstants):
    """Test constants for flext-oracle-oic."""


c = FlextOracleOicTestConstants
__all__ = ["FlextOracleOicTestConstants", "c"]
