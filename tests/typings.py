"""Test type definitions for flext-oracle-oic.

Provides FlextOracleOicTestTypes, combining FlextTestsTypes with
FlextOracleOicTypes for test-specific type definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsTypes

from flext_oracle_oic import FlextOracleOicTypes


class FlextOracleOicTestTypes(FlextTestsTypes, FlextOracleOicTypes):
    """Test types combining FlextTestsTypes with flext-oracle-oic types."""


t = FlextOracleOicTestTypes
__all__ = ["FlextOracleOicTestTypes", "t"]
