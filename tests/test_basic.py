"""Basic tests for flext-oracle-oic-ext.

Tests the actual functionality that exists in the current implementation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_oracle_oic_ext import (
    OICExtensionAuthConfig,
    OICExtensionConnectionConfig,
    OracleOICExtension,
    OracleOICExtensionSettings,
)


class TestBasicFunctionality:
    """Test basic functionality that actually exists."""

    def test_oracle_oic_extension_basic(self) -> None:
        """Test basic OracleOICExtension functionality."""
        ext = OracleOICExtension()

        # Test basic initialization
        assert ext.name == "Oracle OIC Extension"

        # Test info method
        info = ext.get_info()
        assert "Oracle OIC Extension" in info
        assert "Implementation pending" in info

    def test_oracle_oic_extension_settings(self) -> None:
        """Test OracleOICExtensionSettings creation."""
        settings = OracleOICExtensionSettings(
            connection=OICExtensionConnectionConfig(
                base_url="https://test.integration.ocp.oraclecloud.com"
            ),
            auth=OICExtensionAuthConfig(
                oauth_client_id="test_client_id",
                oauth_client_secret="test_client_secret",
                oauth_token_url="https://test.identity.oraclecloud.com/oauth2/v1/token",
            ),
        )

        # Test that settings were created correctly
        assert (
            settings.connection.base_url
            == "https://test.integration.ocp.oraclecloud.com"
        )
        assert settings.auth.oauth_client_id == "test_client_id"
        assert settings.enable_monitoring is True
        assert settings.enable_enterprise_patterns is True

    def test_config_classes(self) -> None:
        """Test configuration classes."""
        # Test connection config
        conn_config = OICExtensionConnectionConfig(
            base_url="https://test.integration.ocp.oraclecloud.com",
            api_version="v1",
            request_timeout=30,
        )
        assert conn_config.base_url == "https://test.integration.ocp.oraclecloud.com"
        assert conn_config.api_version == "v1"
        assert conn_config.request_timeout == 30

        # Test auth config
        auth_config = OICExtensionAuthConfig(
            oauth_client_id="test_client_id",
            oauth_client_secret="test_client_secret",
            oauth_token_url="https://test.identity.oraclecloud.com/oauth2/v1/token",
        )
        assert auth_config.oauth_client_id == "test_client_id"
        assert auth_config.oauth_client_secret == "test_client_secret"
        assert (
            auth_config.oauth_token_url
            == "https://test.identity.oraclecloud.com/oauth2/v1/token"
        )
