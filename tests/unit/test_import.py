"""Basic test to verify flext-extensions.oracle.flext-oracle-oic imports work.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import flext_oracle_oic
from flext_oracle_oic import FlextOracleOicSettings


class TestsFlextOracleOicImport:
    """Behavior contract for test_import."""

    def test_basic_import(self) -> None:
        """Test that we can import the module."""
        assert flext_oracle_oic is not None

    def test_config_import(self) -> None:
        """Test that we can import settings."""
        assert FlextOracleOicSettings is not None
