"""Test utilities for flext-oracle-oic.

Provides FlextOracleOicTestUtilities, combining FlextTestsUtilities with
FlextOracleOicUtilities for test-specific utility definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsUtilities

from flext_oracle_oic import FlextOracleOicUtilities


class FlextOracleOicTestUtilities(FlextTestsUtilities, FlextOracleOicUtilities):
    """Test utilities combining FlextTestsUtilities with flext-oracle-oic utilities."""

    class OracleOic(FlextOracleOicUtilities.OracleOic):
        """OracleOic test utilities namespace."""

        class Tests:
            """Internal tests declarations."""


u = FlextOracleOicTestUtilities
__all__ = ["FlextOracleOicTestUtilities", "u"]
