"""Test utilities for flext-oracle-oic.

Provides TestsFlextOracleOicUtilities, combining TestsFlextUtilities with
FlextOracleOicUtilities for test-specific utility definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsUtilities

from flext_oracle_oic import FlextOracleOicUtilities


class TestsFlextOracleOicUtilities(FlextTestsUtilities, FlextOracleOicUtilities):
    """Test utilities combining TestsFlextUtilities with flext-oracle-oic utilities."""

    class OracleOic(FlextOracleOicUtilities.OracleOic):
        """OracleOic test utilities namespace."""

        class Tests:
            """Internal tests declarations."""


u = TestsFlextOracleOicUtilities
__all__: list[str] = ["TestsFlextOracleOicUtilities", "u"]
