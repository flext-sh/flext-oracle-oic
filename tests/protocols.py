"""Test protocol definitions for flext-oracle-oic.

Provides TestsFlextOracleOicProtocols, combining FlextTestsProtocols with
FlextOracleOicProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests.protocols import FlextTestsProtocols

from flext_oracle_oic.protocols import FlextOracleOicProtocols


class TestsFlextOracleOicProtocols(FlextTestsProtocols, FlextOracleOicProtocols):
    """Test protocols combining FlextTestsProtocols and FlextOracleOicProtocols.

    Provides access to:
    - tp.Tests.Docker.* (from FlextTestsProtocols)
    - tp.Tests.Factory.* (from FlextTestsProtocols)
    - tp.OracleOic.* (from FlextOracleOicProtocols)
    """

    class Tests:
        """Project-specific test protocols.

        Extends FlextTestsProtocols.Tests with OracleOic-specific protocols.
        """

        class OracleOic:
            """OracleOic-specific test protocols."""


# Runtime aliases
p = TestsFlextOracleOicProtocols
tp = TestsFlextOracleOicProtocols

__all__ = ["TestsFlextOracleOicProtocols", "p", "tp"]
