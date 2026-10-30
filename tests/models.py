"""Test models for flext-oracle-oic.

Provides TestsFlextOracleOicModels, combining TestsFlextModels with
FlextModelsOracleOic for test-specific model definitions.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from flext_oracle_oic import FlextModelsOracleOic


class TestsFlextOracleOicModels(FlextTestsModels, FlextModelsOracleOic):
    """Test models combining TestsFlextModels with flext-oracle-oic models."""


m = TestsFlextOracleOicModels

__all__: list[str] = ["TestsFlextOracleOicModels", "m"]
