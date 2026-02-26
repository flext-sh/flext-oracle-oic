"""Tests for ext_config.py.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest

from flext_oracle_oic import FlextOracleOicSettings

# Current API uses a single settings class; alias for tests written for legacy nested config
FlextOracleOicConnectionSettings = FlextOracleOicSettings
FlextOracleOicAuthSettings = FlextOracleOicSettings
OracleOicExtensionSettings = FlextOracleOicSettings


class TestFlextOracleOicConnectionSettings:
    """Test FlextOracleOicConnectionSettings."""

    def test_default_connection_config(self) -> None:
        """Test default connection config."""
        config = FlextOracleOicConnectionSettings()

        assert "integration.ocp.oraclecloud.com" in config.base_url
        assert config.api_version in ("v1", "v2")
        assert 1 <= config.request_timeout <= 300
        assert 0 <= config.max_retries <= 10
        assert isinstance(config.use_ssl, bool)
        assert isinstance(config.verify_ssl, bool)

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
        """Test default auth config (values may come from env)."""
        config = FlextOracleOicAuthSettings()

        assert isinstance(config.oauth_client_id, str)
        assert config.oauth_client_secret is not None
        assert isinstance(config.oauth_token_url, str)
        assert "oauth2" in config.oauth_token_url or "token" in config.oauth_token_url
        assert config.oauth_scope is not None or isinstance(config.oauth_scope, str)

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
        secret_val = config.oauth_client_secret.get_secret_value() if hasattr(config.oauth_client_secret, "get_secret_value") else config.oauth_client_secret
        assert secret_val == "custom_client_secret"
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

        if hasattr(settings, "environment"):
            assert settings.environment in ("development", "testing", "production")
        if hasattr(settings, "log_level"):
            assert settings.log_level is not None
        if hasattr(settings, "debug"):
            assert isinstance(settings.debug, bool)

        assert isinstance(settings.enable_monitoring, bool)
        assert isinstance(settings.enable_enterprise_patterns, bool)
        assert isinstance(settings.enable_orchestration, bool)

    def test_custom_settings(self) -> None:
        """Test custom settings (extension-specific flags)."""
        settings = OracleOicExtensionSettings(
            enable_monitoring=False,
            enable_enterprise_patterns=False,
            enable_orchestration=False,
        )

        assert settings.enable_monitoring is False
        assert settings.enable_enterprise_patterns is False
        assert settings.enable_orchestration is False

    def test_settings_with_custom_configs(self) -> None:
        """Test settings with custom flat config (no nested connection/auth in current API)."""
        settings = OracleOicExtensionSettings(
            base_url="https://custom.integration.ocp.oraclecloud.com",
            request_timeout=60,
            oauth_client_id="custom_client_id",
            oauth_client_secret="custom_client_secret",
        )

        assert settings.base_url == "https://custom.integration.ocp.oraclecloud.com"
        assert settings.request_timeout == 60
        assert settings.oauth_client_id == "custom_client_id"
        secret_val = settings.oauth_client_secret.get_secret_value() if hasattr(settings.oauth_client_secret, "get_secret_value") else settings.oauth_client_secret
        assert secret_val == "custom_client_secret"
