"""Tests for ext_config.py.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_oracle_oic import (
    FlextOracleOicAuthSettings,
    FlextOracleOicConnectionSettings,
    OracleOicExtensionSettings,
)


class TestFlextOracleOicConnectionSettings:
    """Test FlextOracleOicConnectionSettings."""

    def test_default_connection_config(self) -> None:
        """Test default connection config."""
        config = FlextOracleOicConnectionSettings()

        assert config.base_url == "https://localhost.integration.ocp.oraclecloud.com"
        assert config.api_version == "v1"
        assert config.request_timeout == 30
        assert config.max_retries == 3
        assert config.use_ssl is True
        assert config.verify_ssl is True

    def test_custom_connection_config(self) -> None:
        """Test custom connection config."""
        config = FlextOracleOicConnectionSettings(
            base_url="https://custom.integration.ocp.oraclecloud.com",
            api_version="v2",
            request_timeout=60,
            max_retries=5,
            use_ssl=False,
            verify_ssl=False,
        )

        assert config.base_url == "https://custom.integration.ocp.oraclecloud.com"
        assert config.api_version == "v2"
        assert config.request_timeout == 60
        assert config.max_retries == 5
        assert config.use_ssl is False
        assert config.verify_ssl is False


class TestFlextOracleOicAuthSettings:
    """Test FlextOracleOicAuthSettings."""

    def test_default_auth_config(self) -> None:
        """Test default auth config."""
        config = FlextOracleOicAuthSettings()

        assert config.oauth_client_id == "default_client_id"
        assert config.oauth_client_secret == "default_client_secret_value"
        assert (
            config.oauth_token_url
            == "https://idcs-tenant.identity.oraclecloud.com/oauth2/v1/token"
        )
        assert config.oauth_client_aud is None
        assert config.oauth_scope is not None

    def test_custom_auth_config(self) -> None:
        """Test custom auth config."""
        config = FlextOracleOicAuthSettings(
            oauth_client_id="custom_client_id",
            oauth_client_secret="custom_client_secret",
            oauth_token_url="https://custom.identity.oraclecloud.com/oauth2/v1/token",
            oauth_client_aud="custom_audience",
            oauth_scope="custom_scope",
        )

        assert config.oauth_client_id == "custom_client_id"
        assert config.oauth_client_secret == "custom_client_secret"
        assert (
            config.oauth_token_url
            == "https://custom.identity.oraclecloud.com/oauth2/v1/token"
        )
        assert config.oauth_client_aud == "custom_audience"
        assert config.oauth_scope == "custom_scope"


class TestOracleOicExtensionSettings:
    """Test OracleOicExtensionSettings."""

    def test_default_settings(self) -> None:
        """Test default settings."""
        settings = OracleOicExtensionSettings()

        # Test inherited from FlextSettings
        assert settings.environment == "development"
        assert settings.log_level == "INFO"
        assert settings.debug is False

        # Test extension-specific settings
        assert settings.enable_monitoring is True
        assert settings.enable_enterprise_patterns is True
        assert settings.enable_orchestration is True

        # Test sub-configurations
        assert settings.connection is not None
        assert settings.auth is not None

    def test_custom_settings(self) -> None:
        """Test custom settings."""
        settings = OracleOicExtensionSettings(
            environment="production",
            log_level="ERROR",
            debug=True,
            enable_monitoring=False,
            enable_enterprise_patterns=False,
            enable_orchestration=False,
        )

        assert settings.environment == "production"
        assert settings.log_level == "ERROR"
        assert settings.debug is True
        assert settings.enable_monitoring is False
        assert settings.enable_enterprise_patterns is False
        assert settings.enable_orchestration is False

    def test_settings_with_custom_configs(self) -> None:
        """Test settings with custom sub-configurations."""
        custom_connection = FlextOracleOicConnectionSettings(
            base_url="https://custom.integration.ocp.oraclecloud.com",
            request_timeout=60,
        )
        custom_auth = FlextOracleOicAuthSettings(
            oauth_client_id="custom_client_id",
            oauth_client_secret="custom_client_secret",
        )

        settings = OracleOicExtensionSettings(
            connection=custom_connection,
            auth=custom_auth,
        )

        assert (
            settings.connection.base_url
            == "https://custom.integration.ocp.oraclecloud.com"
        )
        assert settings.connection.request_timeout == 60
        assert settings.auth.oauth_client_id == "custom_client_id"
        assert settings.auth.oauth_client_secret == "custom_client_secret"
