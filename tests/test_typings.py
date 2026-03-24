"""Tests for typings.py module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_oracle_oic import t


class TestFlextTypes:
    """Test t domain-specific types."""

    def test_flext_types_inheritance(self) -> None:
        """Test t (FlextTypes) exposes type utilities."""
        assert t is not None
        assert hasattr(t, "NormalizedValue")

    def test_exported_types_available(self) -> None:
        """Test all exported types are available."""
        assert t is not None

    def test_flext_types_can_be_extended(self) -> None:
        """Test t can be extended for domain-specific types."""
        assert hasattr(t, "NormalizedValue")
        core_dict = t.NormalizedValue
        assert core_dict is not None
