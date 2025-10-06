"""Tests for factory.py module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import warnings
from unittest.mock import Mock, patch

from flext_oracle_oic import (
    FlextOracleOicDeprecationWarning,
    OracleOICExtensionService,
    OracleOICExtensionSettings,
    create_development_oic_service,
    create_oic_extension_service,
    setup_oic_extension,
)


class TestFlextOracleOicDeprecationWarning:
    """Test custom deprecation warning class."""

    def test_deprecation_warning_inheritance(self) -> None:
        """Test deprecation warning inherits from DeprecationWarning."""
        assert issubclass(FlextOracleOicDeprecationWarning, DeprecationWarning)

    def test_deprecation_warning_creation(self) -> None:
        """Test deprecation warning can be created."""
        warning = FlextOracleOicDeprecationWarning("test message")
        assert isinstance(warning, DeprecationWarning)
        assert str(warning) == "test message"


class TestShowDeprecationWarning:
    """Test deprecation warning helper function."""

    def test_show_deprecation_warning(self) -> None:
        """Test deprecation warning is shown with proper format."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            def _show_deprecation_warning(message: str) -> None:
                pass  # Deprecation warning implementation

            _show_deprecation_warning("old.import", "new.import")

            assert len(w) == 1
            assert issubclass(w[0].category, FlextOracleOicDeprecationWarning)
            warning_message = str(w[0].message)
            assert "⚠️  DEPRECATED IMPORT: old.import" in warning_message
            assert "✅ USE INSTEAD: new.import" in warning_message
            assert "🔗 This will be removed in version 1.0.0" in warning_message


class TestCreateOicExtensionService:
    """Test create_oic_extension_service factory function."""

    def test_create_service_with_none_settings(self) -> None:
        """Test creating service with None settings uses defaults."""
        result = create_oic_extension_service(None)

        assert result.is_success
        assert isinstance(result.value, OracleOICExtensionService)

    def test_create_service_with_custom_settings(self) -> None:
        """Test creating service with custom settings."""
        settings = OracleOICExtensionSettings(environment="test", log_level="INFO")

        result = create_oic_extension_service(settings)

        assert result.is_success
        assert isinstance(result.value, OracleOICExtensionService)

    @patch("flext_oracle_oic.factory.OracleOICExtensionService")
    def test_self(self, mock_service_class: Mock) -> None:
        """Test service creation failure handling."""
        mock_service_class.side_effect = Exception("Service creation failed")

        result = create_oic_extension_service()

        assert result.is_failure
        assert "Failed to create OIC Extension service" in str(result.error)


class TestCreateDevelopmentOicService:
    """Test create_development_oic_service factory function."""

    def test_create_development_service(self) -> None:
        """Test creating development service."""
        result = create_development_oic_service()

        assert result.is_success
        assert isinstance(result.value, OracleOICExtensionService)

    @patch("flext_oracle_oic.factory.OracleOICExtensionService")
    def test_self(self, mock_service_class: Mock) -> None:
        """Test development service creation failure."""
        mock_service_class.side_effect = Exception("Dev service failed")

        result = create_development_oic_service()

        assert result.is_failure
        assert "Failed to create development OIC service" in str(result.error)


class TestSetupOicExtension:
    """Test setup_oic_extension factory function."""

    def test_setup_extension_with_none_settings(self) -> None:
        """Test setup extension with None settings."""
        result = setup_oic_extension(None)

        assert result.is_success
        assert isinstance(result.value, OracleOICExtensionService)

    def test_setup_extension_with_custom_settings(self) -> None:
        """Test setup extension with custom settings."""
        settings = OracleOICExtensionSettings(
            environment="production",
            log_level="ERROR",
        )

        result = setup_oic_extension(settings)

        assert result.is_success
        assert isinstance(result.value, OracleOICExtensionService)

    @patch("flext_oracle_oic.factory.OracleOICExtensionService")
    def test_self(self, mock_service_class: Mock) -> None:
        """Test extension setup failure handling."""
        mock_service_class.side_effect = Exception("Setup failed")

        result = setup_oic_extension()

        assert result.is_failure
        assert "Failed to setup OIC Extension" in str(result.error)
