"""Test models for flext-oracle-oic tests.

Provides TestsFlextOracleOicModels, extending FlextTestsModels with
flext-oracle-oic-specific models using COMPOSITION INHERITANCE.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_oracle_oic.models import FlextOracleOicModels
from flext_tests import FlextTestsModels


class TestsFlextOracleOicModels(FlextTestsModels, FlextOracleOicModels):
    """Models for flext-oracle-oic tests using COMPOSITION INHERITANCE.

    MANDATORY: Inherits from BOTH:
    1. FlextTestsModels - for test infrastructure (.Tests.*)
    2. FlextOracleOicModels - for domain models

    Access patterns:
    - tm.Tests.* (generic test models from FlextTestsModels)
    - tm.* (Oracle OIC domain models)
    - m.* (production models via alternative alias)
    """


# Short aliases per FLEXT convention
tm = TestsFlextOracleOicModels
m = TestsFlextOracleOicModels

__all__ = [
    "TestsFlextOracleOicModels",
    "m",
    "tm",
]
