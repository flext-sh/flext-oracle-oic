"""Behavioral tests for FlextOracleOicSettings public contract.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest
from pydantic import SecretStr, ValidationError

from flext_oracle_oic import FlextOracleOicSettings, c

__all__: list[str] = ["TestsFlextOracleOicConfig"]


class TestsFlextOracleOicConfig:
    """Public-contract behavior of FlextOracleOicSettings."""

    def test_defaults_match_declared_constants(self) -> None:
        """model_validate({}) yields the declared default contract."""
        settings = FlextOracleOicSettings.model_validate({})

        assert settings.base_url == c.OracleOic.DEFAULT_BASE_URL
        assert settings.api_version is c.OICApiVersion.V1
        assert settings.request_timeout == c.DEFAULT_TIMEOUT_SECONDS
        assert settings.max_retries == c.MAX_RETRY_ATTEMPTS
        assert settings.use_ssl is True
        assert settings.verify_ssl is True
        assert settings.enable_monitoring is True
        assert settings.enable_enterprise_patterns is True
        assert settings.enable_orchestration is True
        assert settings.oauth_client_id == ""
        assert settings.oauth_client_secret.get_secret_value() == ""
        assert settings.oauth_token_url == (
            f"{c.OracleOic.DEFAULT_BASE_URL}/oauth/token"
        )
        assert settings.oauth_client_aud == ""
        assert settings.oauth_scope == ""

    def test_custom_connection_settings_are_preserved(self) -> None:
        """Connection overrides round-trip through the public fields."""
        settings = FlextOracleOicSettings.model_validate({
            "base_url": "https://custom.integration.ocp.oraclecloud.com",
            "api_version": "v2",
            "request_timeout": 60,
            "max_retries": 5,
            "use_ssl": False,
            "verify_ssl": False,
        })

        assert settings.base_url == "https://custom.integration.ocp.oraclecloud.com"
        assert settings.api_version is c.OICApiVersion.V2
        assert settings.request_timeout == 60
        assert settings.max_retries == 5
        assert settings.use_ssl is False
        assert settings.verify_ssl is False

    def test_custom_auth_settings_are_preserved(self) -> None:
        """OAuth overrides round-trip; secret is wrapped in SecretStr."""
        settings = FlextOracleOicSettings.model_validate({
            "oauth_client_id": "custom_client_id",
            "oauth_client_secret": "custom_client_secret",
            "oauth_token_url": (
                "https://custom.identity.oraclecloud.com/oauth2/v1/token"
            ),
            "oauth_client_aud": "custom_audience",
            "oauth_scope": "custom_scope",
        })

        assert settings.oauth_client_id == "custom_client_id"
        assert isinstance(settings.oauth_client_secret, SecretStr)
        assert settings.oauth_client_secret.get_secret_value() == "custom_client_secret"
        assert settings.oauth_token_url == (
            "https://custom.identity.oraclecloud.com/oauth2/v1/token"
        )
        assert settings.oauth_client_aud == "custom_audience"
        assert settings.oauth_scope == "custom_scope"

    @pytest.mark.parametrize("enabled", [True, False])
    def test_feature_flags_reflect_input(self, *, enabled: bool) -> None:
        """Extension feature flags reflect exactly the supplied booleans."""
        settings = FlextOracleOicSettings.model_validate({
            "enable_monitoring": enabled,
            "enable_enterprise_patterns": enabled,
            "enable_orchestration": enabled,
        })

        assert settings.enable_monitoring is enabled
        assert settings.enable_enterprise_patterns is enabled
        assert settings.enable_orchestration is enabled

    def test_secret_is_masked_in_dump_but_readable_via_api(self) -> None:
        """SecretStr hides the value in model_dump/str but exposes it explicitly."""
        settings = FlextOracleOicSettings.model_validate({
            "oauth_client_secret": "topsecret",
        })

        assert settings.oauth_client_secret.get_secret_value() == "topsecret"
        assert "topsecret" not in str(settings.oauth_client_secret)
        assert settings.model_dump()["oauth_client_secret"] != "topsecret"

    def test_unknown_keys_are_ignored(self) -> None:
        """extra='ignore' drops unknown keys without raising."""
        settings = FlextOracleOicSettings.model_validate({
            "base_url": "https://custom.integration.ocp.oraclecloud.com",
            "nonexistent_field": "whatever",
        })

        assert settings.base_url == "https://custom.integration.ocp.oraclecloud.com"
        assert not hasattr(settings, "nonexistent_field")

    @pytest.mark.parametrize(
        ("field", "value"),
        [
            ("api_version", "v9"),
            ("base_url", ""),
            ("request_timeout", 0),
            ("request_timeout", -1),
            ("max_retries", -1),
            ("max_retries", 100),
        ],
    )
    def test_invalid_values_raise_validation_error(
        self, *, field: str, value: object
    ) -> None:
        """Out-of-contract values are rejected at construction time."""
        with pytest.raises(ValidationError) as exc_info:
            FlextOracleOicSettings.model_validate({field: value})

        assert field in str(exc_info.value)

    def test_validation_is_idempotent(self) -> None:
        """Re-validating a dumped model reproduces the same public state."""
        original = FlextOracleOicSettings.model_validate({
            "base_url": "https://custom.integration.ocp.oraclecloud.com",
            "api_version": "v2",
            "request_timeout": 45,
        })
        reparsed = FlextOracleOicSettings.model_validate(original.model_dump())

        assert reparsed.base_url == original.base_url
        assert reparsed.api_version == original.api_version
        assert reparsed.request_timeout == original.request_timeout

    def test_create_for_development_is_deterministic(self) -> None:
        """The development factory returns fixed, valid defaults."""
        dev = FlextOracleOicSettings.create_for_development()

        assert dev.base_url == c.OracleOic.DEFAULT_BASE_URL
        assert dev.api_version is c.OICApiVersion.V1
