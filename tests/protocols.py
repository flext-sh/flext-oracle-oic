"""Test protocol definitions for flext-oracle-oic.

Provides TestsFlextOracleOicProtocols, combining TestsFlextProtocols with
FlextOracleOicProtocols for test-specific protocol definitions.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from tests import FlextOracleOicProtocols


class TestsFlextOracleOicProtocols(FlextTestsProtocols, FlextOracleOicProtocols):
    """Test protocols combining TestsFlextProtocols and FlextOracleOicProtocols."""

    class Tests(FlextTestsProtocols.Tests):
        """OracleOic-specific test protocols."""


p = TestsFlextOracleOicProtocols
__all__: list[str] = ["TestsFlextOracleOicProtocols", "p"]
