"""Behavioral tests for flext-oracle-oic public settings and config models.

Exercises the observable public contract of FlextOracleOicSettings (ADR-005:
flat scalars namespaced under ``settings.OracleOic.*``) and the
OICAuthConfig / OICConnectionConfig domain models (range/enum validation lives
at this boundary, not in settings): default values, explicit overrides, secret
handling, validation error paths, and idempotence.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest
from flext_tests import tm

from flext_oracle_oic import FlextOracleOicSettings, c
from tests import m, t

__all__: list[str] = ["TestsFlextOracleOicBasic"]


class TestsFlextOracleOicBasic:
    """Behavioral contract of settings and config models."""

    def test_settings_apply_defaults_when_empty(self) -> None:
        """Empty input yields fully-defaulted, usable settings."""
        settings = FlextOracleOicSettings.model_validate({})
        ns = settings.OracleOic

        tm.that(ns.base_url, eq=c.OracleOic.DEFAULT_BASE_URL)
        tm.that(ns.api_version, eq=c.OracleOic.DEFAULT_API_VERSION)
        tm.that(ns.request_timeout, eq=c.DEFAULT_TIMEOUT_SECONDS)
        tm.that(ns.max_retries, eq=c.MAX_RETRY_ATTEMPTS)
        tm.that(ns.verify_ssl, eq=True)

    def test_settings_preserve_explicit_overrides(self) -> None:
        """Explicit values override defaults on the namespaced fields."""
        settings = FlextOracleOicSettings.model_validate({
            "OracleOic": {
                "base_url": "https://test.integration.ocp.oraclecloud.com",
                "oauth_client_id": "test_client_id",
                "oauth_client_secret": "test_client_secret",
                "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            }
        })
        ns = settings.OracleOic

        tm.that(ns.base_url, eq="https://test.integration.ocp.oraclecloud.com")
        tm.that(ns.oauth_client_id, eq="test_client_id")
        assert ns.oauth_token_url.endswith("/oauth2/v1/token")

    def test_settings_ignore_unknown_keys(self) -> None:
        """Unknown keys are ignored per the extra=ignore contract."""
        settings = FlextOracleOicSettings.model_validate({
            "not_a_real_setting": "value"
        })

        tm.that(settings.model_dump(), lacks="not_a_real_setting")
        tm.that(settings.OracleOic.base_url, eq=c.OracleOic.DEFAULT_BASE_URL)

    @pytest.mark.parametrize(
        ("raw", "expected"), [("v1", c.OICApiVersion.V1), ("v2", c.OICApiVersion.V2)]
    )
    def test_settings_preserve_api_version_scalar(
        self, raw: str, expected: c.OICApiVersion
    ) -> None:
        """api_version is a plain scalar; the enum contract lives in c."""
        settings = FlextOracleOicSettings.model_validate({
            "OracleOic": {"api_version": raw}
        })

        tm.that(settings.OracleOic.api_version, eq=raw)
        tm.that(settings.OracleOic.api_version, eq=expected)

    def test_settings_accept_unvalidated_scalars(self) -> None:
        """Settings carry raw scalars; range checks live at the domain boundary."""
        settings = FlextOracleOicSettings.model_validate({
            "OracleOic": {"request_timeout": -1}
        })

        tm.that(settings.OracleOic.request_timeout, eq=-1)

    def test_settings_secret_is_plain_scalar(self) -> None:
        """At the settings layer the OAuth secret is an env-provided plain str."""
        settings = FlextOracleOicSettings.model_validate({
            "OracleOic": {"oauth_client_secret": "s3cr3t"}
        })

        tm.that(settings.OracleOic.oauth_client_secret, eq="s3cr3t")

    def test_default_construction_is_deterministic(self) -> None:
        """Default construction yields stable, equal settings."""
        first = FlextOracleOicSettings.model_validate({})
        second = FlextOracleOicSettings.model_validate({})

        tm.that(first.OracleOic.base_url, eq=c.OracleOic.DEFAULT_BASE_URL)
        tm.that(first.OracleOic.api_version, eq=c.OICApiVersion.V1)
        tm.that(first.model_dump(), eq=second.model_dump())

    def test_auth_config_exposes_provided_credentials(self) -> None:
        """OICAuthConfig surfaces credentials via its public fields."""
        auth = m.OracleOic.OICAuthConfig.model_validate({
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": t.SecretStr("test_secret"),
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        })

        tm.that(auth.oauth_client_id, eq="test_client_id")
        tm.that(auth.oauth_client_secret.get_secret_value(), eq="test_secret")
        tm.that(auth.oauth_client_aud, none=True)

    @pytest.mark.parametrize(
        "missing", ["oauth_client_id", "oauth_client_secret", "oauth_token_url"]
    )
    def test_auth_config_requires_mandatory_fields(self, missing: str) -> None:
        """Each required auth field is enforced at validation time."""
        payload: t.MutableMappingKV[str, t.SecretStr | str] = {
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

        tm.that(conn.base_url, eq="https://test.integration.ocp.oraclecloud.com")
        tm.that(conn.request_timeout, eq=30)
        tm.that(conn.max_retries, eq=3)
        tm.that(conn.verify_ssl, eq=True)

    def test_connection_config_rejects_non_positive_timeout(self) -> None:
        """request_timeout on the connection model enforces its constraint."""
        with pytest.raises(c.ValidationError):
            m.OracleOic.OICConnectionConfig.model_validate({
                "base_url": "https://test.integration.ocp.oraclecloud.com",
                "request_timeout": 0,
            })
