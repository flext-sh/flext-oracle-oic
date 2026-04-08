"""Test protocol definitions for flext-oracle-oic.

Provides TestsFlextOracleOicProtocols, combining TestsFlextProtocols with
FlextOracleOicProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from flext_oracle_oic import FlextOracleOicProtocols


class TestsFlextOracleOicProtocols(FlextTestsProtocols, FlextOracleOicProtocols):
    """Test protocols combining TestsFlextProtocols and FlextOracleOicProtocols."""

    class OracleOic(FlextOracleOicProtocols.OracleOic):
        """OracleOic test protocols namespace."""

        class Tests:
            """OracleOic-specific test protocols."""


p = TestsFlextOracleOicProtocols
__all__ = ["TestsFlextOracleOicProtocols", "p"]
