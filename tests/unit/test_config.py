"""Behavioral tests for FlextOracleOicSettings public contract (ADR-005).

The settings layer carries flat scalars namespaced under
``settings.OracleOic.*``; range/enum validation lives at the domain-model
boundary (``m.OracleOic.OICConnectionConfig`` / ``OICAuthConfig``).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest
from flext_tests import tm
from pydantic import ValidationError

from flext_oracle_oic import FlextOracleOicSettings, c
from tests import m

__all__: list[str] = ["TestsFlextOracleOicConfig"]


class TestsFlextOracleOicConfig:
    """Public-contract behavior of FlextOracleOicSettings."""

    def test_defaults_match_declared_constants(self) -> None:
        """model_validate({}) yields the declared default contract."""
        ns = FlextOracleOicSettings.model_validate({}).OracleOic

        tm.that(ns.base_url, eq=c.OracleOic.DEFAULT_BASE_URL)
        tm.that(ns.api_version, eq=c.OICApiVersion.V1)
        tm.that(ns.request_timeout, eq=c.DEFAULT_TIMEOUT_SECONDS)
        tm.that(ns.max_retries, eq=c.MAX_RETRY_ATTEMPTS)
        tm.that(ns.use_ssl, eq=True)
        tm.that(ns.verify_ssl, eq=True)
        tm.that(ns.enable_monitoring, eq=True)
        tm.that(ns.enable_enterprise_patterns, eq=True)
        tm.that(ns.enable_orchestration, eq=True)
        tm.that(ns.oauth_client_id, eq="")
        tm.that(ns.oauth_client_secret, eq="")
        tm.that(ns.oauth_token_url, eq=(f"{c.OracleOic.DEFAULT_BASE_URL}/oauth/token"))
        tm.that(ns.oauth_client_aud, eq="")
        tm.that(ns.oauth_scope, eq="")

    def test_custom_connection_settings_are_preserved(self) -> None:
        """Connection overrides round-trip through the namespaced fields."""
        ns = FlextOracleOicSettings.model_validate({
            "OracleOic": {
                "base_url": "https://custom.integration.ocp.oraclecloud.com",
                "api_version": "v2",
                "request_timeout": 60,
                "max_retries": 5,
                "use_ssl": False,
                "verify_ssl": False,
            },
        }).OracleOic

        tm.that(ns.base_url, eq="https://custom.integration.ocp.oraclecloud.com")
        tm.that(ns.api_version, eq=c.OICApiVersion.V2)
        tm.that(ns.request_timeout, eq=60)
        tm.that(ns.max_retries, eq=5)
        tm.that(ns.use_ssl, eq=False)
        tm.that(ns.verify_ssl, eq=False)

    def test_custom_auth_settings_are_preserved(self) -> None:
        """OAuth overrides round-trip as plain scalars at the settings layer."""
        ns = FlextOracleOicSettings.model_validate({
            "OracleOic": {
                "oauth_client_id": "custom_client_id",
                "oauth_client_secret": "custom_client_secret",
                "oauth_token_url": (
                    "https://custom.identity.oraclecloud.com/oauth2/v1/token"
                ),
                "oauth_client_aud": "custom_audience",
                "oauth_scope": "custom_scope",
            },
        }).OracleOic

        tm.that(ns.oauth_client_id, eq="custom_client_id")
        tm.that(ns.oauth_client_secret, eq="custom_client_secret")
        tm.that(
            ns.oauth_token_url,
            eq=("https://custom.identity.oraclecloud.com/oauth2/v1/token"),
        )
        tm.that(ns.oauth_client_aud, eq="custom_audience")
        tm.that(ns.oauth_scope, eq="custom_scope")

    @pytest.mark.parametrize("enabled", [True, False])
    def test_feature_flags_reflect_input(self, *, enabled: bool) -> None:
        """Extension feature flags reflect exactly the supplied booleans."""
        ns = FlextOracleOicSettings.model_validate({
            "OracleOic": {
                "enable_monitoring": enabled,
                "enable_enterprise_patterns": enabled,
                "enable_orchestration": enabled,
            },
        }).OracleOic

        assert ns.enable_monitoring is enabled
        assert ns.enable_enterprise_patterns is enabled
        assert ns.enable_orchestration is enabled

    def test_domain_auth_config_masks_secret_but_settings_do_not(self) -> None:
        """SecretStr masking lives at the domain boundary, not in settings."""
        ns = FlextOracleOicSettings.model_validate({
            "OracleOic": {"oauth_client_secret": "topsecret"},
        }).OracleOic
        auth = m.OracleOic.OICAuthConfig.model_validate({
            "oauth_client_id": "id",
            "oauth_client_secret": "topsecret",
            "oauth_token_url": "https://token.example/oauth",
        })

        tm.that(ns.oauth_client_secret, eq="topsecret")
        tm.that(auth.oauth_client_secret.get_secret_value(), eq="topsecret")
        tm.that(str(auth.model_dump()["oauth_client_secret"]), lacks="topsecret")

    def test_unknown_keys_are_ignored(self) -> None:
        """extra='ignore' drops unknown keys without raising."""
        settings = FlextOracleOicSettings.model_validate({
            "OracleOic": {"base_url": "https://custom.integration.ocp.oraclecloud.com"},
            "nonexistent_field": "whatever",
        })

        assert (
            settings.OracleOic.base_url
            == "https://custom.integration.ocp.oraclecloud.com"
        )
        assert not hasattr(settings, "nonexistent_field")

    @pytest.mark.parametrize(
        ("field", "value"),
        [
            ("request_timeout", 0),
            ("request_timeout", -1),
            ("max_retries", -1),
            ("max_retries", 100),
        ],
    )
    def test_domain_boundary_rejects_out_of_range_values(
        self, *, field: str, value: int
    ) -> None:
        """Range constraints are enforced by OICConnectionConfig, not settings."""
        payload: dict[str, str | int] = {
            "base_url": "https://custom.integration.ocp.oraclecloud.com",
            field: value,
        }

        with pytest.raises(ValidationError) as exc_info:
            m.OracleOic.OICConnectionConfig.model_validate(payload)

        tm.that(str(exc_info.value), has=field)

    def test_validation_is_idempotent(self) -> None:
        """Re-validating a dumped model reproduces the same public state."""
        original = FlextOracleOicSettings.model_validate({
            "OracleOic": {
                "base_url": "https://custom.integration.ocp.oraclecloud.com",
                "api_version": "v2",
                "request_timeout": 45,
            },
        })
        reparsed = FlextOracleOicSettings.model_validate(original.model_dump())

        tm.that(reparsed.OracleOic.base_url, eq=original.OracleOic.base_url)
        tm.that(reparsed.OracleOic.api_version, eq=original.OracleOic.api_version)
        tm.that(
            reparsed.OracleOic.request_timeout, eq=original.OracleOic.request_timeout
        )

    def test_default_construction_is_deterministic(self) -> None:
        """Default construction returns fixed, valid defaults."""
        first = FlextOracleOicSettings.model_validate({})
        second = FlextOracleOicSettings.model_validate({})

        tm.that(first.OracleOic.base_url, eq=c.OracleOic.DEFAULT_BASE_URL)
        tm.that(first.OracleOic.api_version, eq=c.OICApiVersion.V1)
        tm.that(first.model_dump(), eq=second.model_dump())
