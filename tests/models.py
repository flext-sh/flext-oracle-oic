"""Test models for flext-oracle-oic.

Provides TestsFlextOracleOicModels, combining TestsFlextModels with
FlextOracleOicModels for test-specific model definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_oracle_oic import FlextOracleOicModels
from flext_tests import FlextTestsModels


class TestsFlextOracleOicModels(FlextTestsModels, FlextOracleOicModels):
    """Test models combining TestsFlextModels with flext-oracle-oic models."""


m = TestsFlextOracleOicModels

__all__: list[str] = ["TestsFlextOracleOicModels", "m"]
