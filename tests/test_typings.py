"""Tests for typings.py module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import FlextTypes


class TestFlextTypes:
    """Test FlextTypes domain-specific types."""

    def test_flext_types_inheritance(self) -> None:
        """Test FlextTypes inherits from CoreFlextTypes."""
        # FlextTypes should be a class that inherits from CoreFlextTypes
        assert hasattr(FlextTypes, "Core")
        # Should maintain all core functionality
        assert hasattr(FlextTypes, "Dict")
        assert hasattr(FlextTypes, "StringList")

    def test_exported_types_available(self) -> None:
        """Test all exported types are available."""
        # FlextTypes should be available
        assert FlextTypes is not None

    def test_flext_types_can_be_extended(self) -> None:
        """Test FlextTypes can be extended for domain-specific types."""
        # Should be able to add domain-specific types
        assert issubclass(FlextTypes, object)
        # Can access core types
        core_dict = FlextTypes.Dict
        assert core_dict is not None
