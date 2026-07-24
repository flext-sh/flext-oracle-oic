"""Test type definitions for flext-oracle-oic.

Provides TestsFlextOracleOicTypes, combining TestsFlextTypes with
FlextOracleOicTypes for test-specific type definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_oracle_oic import FlextOracleOicTypes
from flext_tests import FlextTestsTypes


class TestsFlextOracleOicTypes(FlextTestsTypes, FlextOracleOicTypes):
    """Test types combining TestsFlextTypes with flext-oracle-oic types."""


t = TestsFlextOracleOicTypes
__all__: list[str] = ["TestsFlextOracleOicTypes", "t"]
