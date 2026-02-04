"""Tests for container.py module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_oracle_oic import (
    create_development_oic_service,
    create_oic_extension_service,
    setup_oic_extension,
)


class TestContainer:
    """Test factory/extension setup (replaces legacy container module)."""

    def test_get_container_available(self) -> None:
        """Test create_development_oic_service is callable."""
        assert callable(create_development_oic_service)

    def test_configure_dependencies_available(self) -> None:
        """Test setup_oic_extension is callable."""
        assert callable(setup_oic_extension)

    def test_get_service_available(self) -> None:
        """Test create_oic_extension_service is callable."""
        assert callable(create_oic_extension_service)

    def test_factory_functions_available(self) -> None:
        """Test factory exports are present and callable."""
        assert create_development_oic_service is not None
        assert setup_oic_extension is not None
        assert create_oic_extension_service is not None
        assert callable(setup_oic_extension)
