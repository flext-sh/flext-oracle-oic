"""Tests for ext_config.py.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_oracle_oic import FlextOracleOicSettings


class TestsFlextOracleOicConfig:
    """Test FlextOracleOicSettings."""

    def test_default_settings(self) -> None:
        """Test default settings."""
        settings = FlextOracleOicSettings.model_validate({})
        assert "integration.ocp.oraclecloud.com" in settings.base_url
        assert settings.api_version in {"v1", "v2"}
        assert 1 <= settings.request_timeout <= 300
        assert 0 <= settings.max_retries <= 10
        assert isinstance(settings.use_ssl, bool)
        assert isinstance(settings.verify_ssl, bool)

    def test_custom_settings(self) -> None:
        """Test custom settings."""
        settings = FlextOracleOicSettings.model_validate({
            "base_url": "https://custom.integration.ocp.oraclecloud.com",
            "api_version": "v2",
            "request_timeout": 60,
            "max_retries": 5,
            "use_ssl": False,
            "verify_ssl": False,
        })
        assert settings.base_url == "https://custom.integration.ocp.oraclecloud.com"
        assert settings.api_version == "v2"
        assert settings.request_timeout == 60
        assert settings.max_retries == 5
        assert settings.use_ssl is False
        assert settings.verify_ssl is False

    def test_default_auth_settings(self) -> None:
        """Test default auth settings (values may come from env)."""
        settings = FlextOracleOicSettings.model_validate({})
        assert isinstance(settings.oauth_client_id, str)
        assert settings.oauth_client_secret is not None
        assert isinstance(settings.oauth_token_url, str)
        assert (
            "oauth2" in settings.oauth_token_url or "token" in settings.oauth_token_url
        )
        assert settings.oauth_scope is not None or isinstance(settings.oauth_scope, str)

    def test_custom_auth_settings(self) -> None:
        """Test custom auth settings."""
        settings = FlextOracleOicSettings.model_validate({
            "oauth_client_id": "custom_client_id",
            "oauth_client_secret": "custom_client_secret",
            "oauth_token_url": "https://custom.identity.oraclecloud.com/oauth2/v1/token",
            "oauth_client_aud": "custom_audience",
            "oauth_scope": "custom_scope",
        })
        assert settings.oauth_client_id == "custom_client_id"
        secret_val = (
            settings.oauth_client_secret.get_secret_value()
            if hasattr(settings.oauth_client_secret, "get_secret_value")
            else settings.oauth_client_secret
        )
        assert secret_val == "custom_client_secret"
        assert (
            settings.oauth_token_url
            == "https://custom.identity.oraclecloud.com/oauth2/v1/token"
        )
        assert settings.oauth_client_aud == "custom_audience"
        assert settings.oauth_scope == "custom_scope"

    def test_default_extension_settings(self) -> None:
        """Test default extension settings."""
        settings = FlextOracleOicSettings.model_validate({})
        if hasattr(settings, "environment"):
            assert settings.environment in {"development", "testing", "production"}
        if hasattr(settings, "log_level"):
            assert settings.log_level is not None
        if hasattr(settings, "debug"):
            assert isinstance(settings.debug, bool)
        assert isinstance(settings.enable_monitoring, bool)
        assert isinstance(settings.enable_enterprise_patterns, bool)
        assert isinstance(settings.enable_orchestration, bool)

    def test_custom_extension_settings(self) -> None:
        """Test custom extension settings (extension-specific flags)."""
        settings = FlextOracleOicSettings.model_validate({
            "enable_monitoring": False,
            "enable_enterprise_patterns": False,
            "enable_orchestration": False,
        })
        assert settings.enable_monitoring is False
        assert settings.enable_enterprise_patterns is False
        assert settings.enable_orchestration is False

    def test_settings_with_custom_configs(self) -> None:
        """Test settings with custom flat settings (no nested connection/auth in current API)."""
        settings = FlextOracleOicSettings.model_validate({
            "base_url": "https://custom.integration.ocp.oraclecloud.com",
            "request_timeout": 60,
            "oauth_client_id": "custom_client_id",
            "oauth_client_secret": "custom_client_secret",
        })
        assert settings.base_url == "https://custom.integration.ocp.oraclecloud.com"
        assert settings.request_timeout == 60
        assert settings.oauth_client_id == "custom_client_id"
        secret_val = (
            settings.oauth_client_secret.get_secret_value()
            if hasattr(settings.oauth_client_secret, "get_secret_value")
            else settings.oauth_client_secret
        )
        assert secret_val == "custom_client_secret"
