"""Test models for flext-oracle-oic.

Provides FlextOracleOicTestModels, combining FlextTestsModels with
FlextOracleOicModels for test-specific model definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from flext_oracle_oic import FlextOracleOicModels


class FlextOracleOicTestModels(FlextTestsModels, FlextOracleOicModels):
    """Test models combining FlextTestsModels with flext-oracle-oic models."""


m = FlextOracleOicTestModels

__all__ = [
    "FlextOracleOicTestModels",
    "m",
]
