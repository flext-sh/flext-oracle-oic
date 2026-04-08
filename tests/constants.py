"""Test constants for flext-oracle-oic tests.

Provides TestsFlextOracleOicConstants, extending FlextTestsConstants with
flext-oracle-oic-specific constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsConstants

from flext_oracle_oic import FlextOracleOicConstants


class TestsFlextOracleOicConstants(FlextTestsConstants, FlextOracleOicConstants):
    """Test constants for flext-oracle-oic."""


c = TestsFlextOracleOicConstants
__all__ = ["TestsFlextOracleOicConstants", "c"]
