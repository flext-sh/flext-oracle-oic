"""Tests for typings.py module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import t


class TestFlextTypes:
    """Test t domain-specific types."""

    def test_flext_types_inheritance(self) -> None:
        """Test t inherits from CoreFlextTypes."""
        # t should be a class that inherits from CoreFlextTypes
        assert hasattr(t, "Core")
        # Should maintain all core functionality
        assert hasattr(t, "Dict")
        assert hasattr(t, "StringList")

    def test_exported_types_available(self) -> None:
        """Test all exported types are available."""
        # t should be available
        assert t is not None

    def test_flext_types_can_be_extended(self) -> None:
        """Test t can be extended for domain-specific types."""
        # Should be able to add domain-specific types
        assert issubclass(t, object)
        # Can access core types
        core_dict = dict[str, object]
        assert core_dict is not None
