"""Behavioral tests for flext-oracle-oic public settings and config models.

Exercises the observable public contract of FlextOracleOicSettings and the
OICAuthConfig / OICConnectionConfig models: default values, explicit overrides,
enum coercion, secret handling, validation error paths, and idempotence.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest

from flext_oracle_oic import FlextOracleOicSettings, c
from tests.models import m
from tests.typings import t

__all__: list[str] = ["TestsFlextOracleOicBasic"]


class TestsFlextOracleOicBasic:
    """Behavioral contract of settings and config models."""

    def test_settings_apply_defaults_when_empty(self) -> None:
        """Empty input yields fully-defaulted, usable settings."""
        settings = FlextOracleOicSettings.model_validate({})

        assert settings.base_url == c.OracleOic.DEFAULT_BASE_URL
        assert settings.api_version == c.OICApiVersion.V1
        assert settings.request_timeout == c.DEFAULT_TIMEOUT_SECONDS
        assert settings.max_retries == c.MAX_RETRY_ATTEMPTS
        assert settings.verify_ssl is True

    def test_settings_preserve_explicit_overrides(self) -> None:
        """Explicit values override defaults on the public fields."""
        settings = FlextOracleOicSettings.model_validate({
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        })

        assert settings.base_url == "https://test.integration.ocp.oraclecloud.com"
        assert settings.oauth_client_id == "test_client_id"
        assert settings.oauth_token_url.endswith("/oauth2/v1/token")

    def test_settings_ignore_unknown_keys(self) -> None:
        """Unknown keys are ignored per the extra=ignore contract."""
        settings = FlextOracleOicSettings.model_validate({
            "not_a_real_setting": "value",
        })

        assert "not_a_real_setting" not in settings.model_dump()
        assert settings.base_url == c.OracleOic.DEFAULT_BASE_URL

    @pytest.mark.parametrize(
        ("raw", "expected"),
        [
            ("v1", c.OICApiVersion.V1),
            ("v2", c.OICApiVersion.V2),
        ],
    )
    def test_settings_coerce_valid_api_version(
        self, raw: str, expected: c.OICApiVersion
    ) -> None:
        """Valid api_version strings coerce to the enum member."""
        settings = FlextOracleOicSettings.model_validate({"api_version": raw})

        assert settings.api_version == expected

    def test_settings_reject_invalid_api_version(self) -> None:
        """Unknown api_version fails validation, never a silent fallback."""
        with pytest.raises(c.ValidationError):
            FlextOracleOicSettings.model_validate({"api_version": "v99"})

    def test_settings_reject_non_positive_timeout(self) -> None:
        """request_timeout enforces its positive-int constraint."""
        with pytest.raises(c.ValidationError):
            FlextOracleOicSettings.model_validate({"request_timeout": -1})

    def test_settings_secret_is_masked_in_dump(self) -> None:
        """The client secret round-trips as a SecretStr, not plaintext."""
        settings = FlextOracleOicSettings.model_validate({
            "oauth_client_secret": "s3cr3t",
        })

        assert isinstance(settings.oauth_client_secret, t.SecretStr)
        assert settings.oauth_client_secret.get_secret_value() == "s3cr3t"
        assert "s3cr3t" not in str(settings.model_dump()["oauth_client_secret"])

    def test_create_for_development_is_deterministic(self) -> None:
        """The development factory yields stable, equal settings."""
        first = FlextOracleOicSettings.create_for_development()
        second = FlextOracleOicSettings.create_for_development()

        assert first.base_url == c.OracleOic.DEFAULT_BASE_URL
        assert first.api_version == c.OICApiVersion.V1
        assert first.model_dump() == second.model_dump()

    def test_auth_config_exposes_provided_credentials(self) -> None:
        """OICAuthConfig surfaces credentials via its public fields."""
        auth = m.OracleOic.OICAuthConfig.model_validate({
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": t.SecretStr("test_secret"),
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        })

        assert auth.oauth_client_id == "test_client_id"
        assert auth.oauth_client_secret.get_secret_value() == "test_secret"
        assert auth.oauth_client_aud is None

    @pytest.mark.parametrize(
        "missing",
        ["oauth_client_id", "oauth_client_secret", "oauth_token_url"],
    )
    def test_auth_config_requires_mandatory_fields(self, missing: str) -> None:
        """Each required auth field is enforced at validation time."""
        payload: dict[str, t.SecretStr | str] = {
            "oauth_client_id": "id",
            "oauth_client_secret": t.SecretStr("secret"),
            "oauth_token_url": "https://token.example/oauth",
        }
        del payload[missing]

        with pytest.raises(c.ValidationError):
            m.OracleOic.OICAuthConfig.model_validate(payload)

    def test_connection_config_applies_defaults(self) -> None:
        """OICConnectionConfig defaults optional fields, keeps overrides."""
        conn = m.OracleOic.OICConnectionConfig.model_validate({
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "api_version": "v1",
            "request_timeout": 30,
        })

        assert conn.base_url == "https://test.integration.ocp.oraclecloud.com"
        assert conn.request_timeout == 30
        assert conn.max_retries == 3
        assert conn.verify_ssl is True

    def test_connection_config_rejects_non_positive_timeout(self) -> None:
        """request_timeout on the connection model enforces its constraint."""
        with pytest.raises(c.ValidationError):
            m.OracleOic.OICConnectionConfig.model_validate({
                "base_url": "https://test.integration.ocp.oraclecloud.com",
                "request_timeout": 0,
            })
