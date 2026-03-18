"""Test protocol definitions for flext-oracle-oic.

Provides TestsFlextOracleOicProtocols, combining FlextTestsProtocols with
FlextOracleOicProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from flext_oracle_oic.protocols import FlextOracleOicProtocols


class TestsFlextOracleOicProtocols(FlextTestsProtocols, FlextOracleOicProtocols):
    """Test protocols combining FlextTestsProtocols and FlextOracleOicProtocols.

    Provides access to:
    - p.Tests.Docker.* (from FlextTestsProtocols)
    - p.Tests.Factory.* (from FlextTestsProtocols)
    - p.OracleOic.* (from FlextOracleOicProtocols)
    """


__all__ = ["TestsFlextOracleOicProtocols", "p"]

p = TestsFlextOracleOicProtocols
