"""Test protocol definitions for flext-oracle-oic.

Provides TestsFlextOracleOicProtocols, combining p with
FlextOracleOicProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import p

from flext_oracle_oic.protocols import FlextOracleOicProtocols


class TestsFlextOracleOicProtocols(p, FlextOracleOicProtocols):
    """Test protocols combining p and FlextOracleOicProtocols.

    Provides access to:
    - p.Tests.Docker.* (from p)
    - p.Tests.Factory.* (from p)
    - p.OracleOic.* (from FlextOracleOicProtocols)
    """


__all__ = ["TestsFlextOracleOicProtocols", "p"]

p = TestsFlextOracleOicProtocols
