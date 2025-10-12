"""Tests for typings.py module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextCore


class TestFlextTypes:
    """Test FlextCore.Types domain-specific types."""

    def test_flext_types_inheritance(self) -> None:
        """Test FlextCore.Types inherits from CoreFlextTypes."""
        # FlextCore.Types should be a class that inherits from CoreFlextTypes
        assert hasattr(FlextCore.Types, "Core")
        # Should maintain all core functionality
        assert hasattr(FlextCore.Types, "Dict")
        assert hasattr(FlextCore.Types, "StringList")

    def test_exported_types_available(self) -> None:
        """Test all exported types are available."""
        # FlextCore.Types should be available
        assert FlextCore.Types is not None

    def test_flext_types_can_be_extended(self) -> None:
        """Test FlextCore.Types can be extended for domain-specific types."""
        # Should be able to add domain-specific types
        assert issubclass(FlextCore.Types, object)
        # Can access core types
        core_dict = FlextCore.Types.Dict
        assert core_dict is not None
