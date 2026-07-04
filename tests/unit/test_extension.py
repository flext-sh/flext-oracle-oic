"""Tests for Oracle OIC Extension basic functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_oracle_oic import FlextOracleOicApi


class TestsFlextOracleOicExtension:
    """Test cases for Oracle OIC API (extension facade) functionality."""

    def test_api_class_exists(self) -> None:
        """Test FlextOracleOicApi class is available."""
        assert FlextOracleOicApi is not None

    def test_api_has_required_methods(self) -> None:
        """Test API class exposes expected methods."""
