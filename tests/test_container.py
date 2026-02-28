"""Tests for container.py module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_oracle_oic import FlextOracleOicFactory


class TestContainer:
    """Test factory/extension setup (replaces legacy container module)."""

    def test_factory_available(self) -> None:
        """Test FlextOracleOicFactory is available."""
        assert FlextOracleOicFactory is not None

    def test_factory_instantiable(self) -> None:
        """Test FlextOracleOicFactory can be instantiated."""
        factory = FlextOracleOicFactory()
        assert factory is not None

    def test_factory_methods_available(self) -> None:
        """Test factory methods are present and callable."""
        factory = FlextOracleOicFactory()
        assert callable(factory.create_oic_extension_service)
        assert callable(factory.create_development_oic_service)
        assert callable(factory.setup_oic_extension)
