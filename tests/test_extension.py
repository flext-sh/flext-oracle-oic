"""Tests for Oracle OIC Extension basic functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_oracle_oic_ext import OracleOICExtension


class TestOracleOICExtension:
    """Test cases for OracleOICExtension basic functionality."""

    def test_extension_initialization(self) -> None:
        """Test extension initialization."""
        ext = OracleOICExtension()
        assert ext.name == "Oracle OIC Extension"

    def test_get_info(self) -> None:
        """Test get_info method."""
        ext = OracleOICExtension()
        info = ext.get_info()
        assert "Oracle OIC Extension" in info
        assert "Implementation pending" in info
        assert isinstance(info, str)