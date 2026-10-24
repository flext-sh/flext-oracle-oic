"""Behavioral tests for FlextOracleOicSettings public contract (ADR-005).

The settings layer carries flat scalars namespaced under
``settings.OracleOic.*``; range/enum validation lives at the domain-model
boundary (``m.OracleOic.OICConnectionConfig`` / ``OICAuthConfig``).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path

import pytest

from flext_oracle_oic import FlextOracleOicConfig, FlextOracleOicSettings, config
from tests import c, m, t, tm, u


class TestsFlextOracleOicConfig:
    """Public-contract behavior of FlextOracleOicSettings."""

    @staticmethod
    def test_defaults_match_declared_constants() -> None:
        """model_validate({}) yields the declared default contract."""
        ns = FlextOracleOicSettings.model_validate({}).OracleOic

        tm.that(ns.base_url, eq=c.OracleOic.DEFAULT_BASE_URL)
        tm.that(ns.api_version, eq=c.OracleOic.OICApiVersion.V1)
        tm.that(ns.request_timeout, eq=c.DEFAULT_TIMEOUT_SECONDS)
        tm.that(ns.max_retries, eq=c.MAX_RETRY_ATTEMPTS)
        tm.ok(ns.use_ssl)
        tm.ok(ns.verify_ssl)
        tm.ok(ns.enable_monitoring)
        tm.ok(ns.enable_enterprise_patterns)
        tm.ok(ns.enable_orchestration)
        tm.that(ns.oauth_client_id, eq="")
        tm.that(ns.oauth_client_secret, eq="")
        tm.that(ns.oauth_token_url, eq=(f"{c.OracleOic.DEFAULT_BASE_URL}/oauth/token"))
        tm.that(ns.oauth_client_aud, eq="")
        tm.that(ns.oauth_scope, eq="")

    @staticmethod
    def test_custom_connection_settings_are_preserved() -> None:
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
        tm.that(ns.api_version, eq=c.OracleOic.OICApiVersion.V2)
        tm.that(ns.request_timeout, eq=60)
        tm.that(ns.max_retries, eq=5)
        tm.fail(ns.use_ssl)
        tm.fail(ns.verify_ssl)

    @staticmethod
    def test_custom_auth_settings_are_preserved() -> None:
        """OAuth overrides round-trip as plain scalars at the settings layer."""
        client_secret = "s" + c.ParserBooleanToken.ONE * 16
        ns = FlextOracleOicSettings.model_validate({
            "OracleOic": {
                "oauth_client_id": "custom_client_id",
                "oauth_client_secret": client_secret,
                "oauth_token_url": (
                    "https://custom.identity.oraclecloud.com/oauth2/v1/token"
                ),
                "oauth_client_aud": "custom_audience",
                "oauth_scope": "custom_scope",
            },
        }).OracleOic

        tm.that(ns.oauth_client_id, eq="custom_client_id")
        tm.that(ns.oauth_client_secret, eq=client_secret)
        tm.that(
            ns.oauth_token_url,
            eq=("https://custom.identity.oraclecloud.com/oauth2/v1/token"),
        )
        tm.that(ns.oauth_client_aud, eq="custom_audience")
        tm.that(ns.oauth_scope, eq="custom_scope")

    @staticmethod
    @pytest.mark.parametrize("enabled", [True, False])
    def test_feature_flags_reflect_input(*, enabled: bool) -> None:
        """Extension feature flags reflect exactly the supplied booleans."""
        ns = FlextOracleOicSettings.model_validate({
            "OracleOic": {
                "enable_monitoring": enabled,
                "enable_enterprise_patterns": enabled,
                "enable_orchestration": enabled,
            },
        }).OracleOic

        tm.that(ns.enable_monitoring is enabled, truth=True)
        tm.that(ns.enable_enterprise_patterns is enabled, truth=True)
        tm.that(ns.enable_orchestration is enabled, truth=True)

    @staticmethod
    def test_domain_auth_config_masks_secret_but_settings_do_not() -> None:
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

    @staticmethod
    def test_unknown_keys_are_ignored() -> None:
        """extra='ignore' drops unknown keys without raising."""
        settings = FlextOracleOicSettings.model_validate({
            "OracleOic": {"base_url": "https://custom.integration.ocp.oraclecloud.com"},
            "nonexistent_field": "whatever",
        })

        tm.that(
            settings.OracleOic.base_url,
            eq="https://custom.integration.ocp.oraclecloud.com",
        )
        tm.that(hasattr(settings, "nonexistent_field"), truth=False)

    @staticmethod
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
        *,
        field: str,
        value: int,
    ) -> None:
        """Range constraints are enforced by OICConnectionConfig, not settings."""
        payload: t.JsonDict = {
            "base_url": "https://custom.integration.ocp.oraclecloud.com",
            field: value,
        }

        with pytest.raises(m.ValidationError) as exc_info:
            m.OracleOic.OICConnectionConfig.model_validate(payload)

        tm.that(str(exc_info.value), has=field)

    @staticmethod
    def test_validation_is_idempotent() -> None:
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
            reparsed.OracleOic.request_timeout,
            eq=original.OracleOic.request_timeout,
        )

    @staticmethod
    def test_default_construction_is_deterministic() -> None:
        """Default construction returns fixed, valid defaults."""
        first = FlextOracleOicSettings.model_validate({})
        second = FlextOracleOicSettings.model_validate({})

        tm.that(first.OracleOic.base_url, eq=c.OracleOic.DEFAULT_BASE_URL)
        tm.that(first.OracleOic.api_version, eq=c.OracleOic.OICApiVersion.V1)
        tm.that(first.model_dump(), eq=second.model_dump())

    @staticmethod
    def test_business_namespace_preserves_loaded_values() -> None:
        """The public namespace preserves the loader's complete validated payload."""
        loaded = FlextOracleOicConfig()
        expected = m.OracleOic.Config.model_validate(loaded.model_dump()["OracleOic"])

        tm.that(loaded.OracleOic.model_dump(), eq=expected.model_dump())
        tm.that(loaded.OracleOic is loaded.OracleOic, truth=True)

    @staticmethod
    def test_business_config_is_a_shared_frozen_root() -> None:
        """Publication keeps the same root without copying its loaded state."""
        tm.that(FlextOracleOicConfig.fetch_global() is config, truth=True)

    @staticmethod
    @pytest.mark.parametrize("page_size", [1, 17, 401])
    def test_business_namespace_loads_arbitrary_valid_yaml(
        tmp_path: Path,
        page_size: int,
    ) -> None:
        """The native YAML loader validates supplied values without defaults."""
        payload: t.JsonDict = {
            "OracleOic": {
                "api": {"page_size": page_size},
                "integration": {},
                "validation": {},
                "monitoring": {},
            },
        }
        tm.ok(
            u.Cli.atomic_write_text_file(
                tmp_path / "business.yaml", u.Cli.yaml_dump_str(payload)
            )
        )
        with u.Tests.env_vars_context({"FLEXT_ORACLE_OIC_CONFIG_DIR": str(tmp_path)}):
            loaded = FlextOracleOicConfig()

        tm.that(loaded.OracleOic.api["page_size"], eq=page_size)
        tm.that(loaded.OracleOic.model_dump(), eq=payload["OracleOic"])
        tm.that(FlextOracleOicConfig.fetch_global() is config, truth=True)
        with pytest.raises(m.ValidationError, match="frozen_instance"):
            loaded.OracleOic = loaded.OracleOic

    @staticmethod
    @pytest.mark.parametrize("yaml_text", ["{}", "OracleOic: {}"])
    def test_business_namespace_rejects_missing_data_at_load(
        tmp_path: Path,
        yaml_text: str,
    ) -> None:
        """Missing namespaces and required domains fail before publication."""
        tm.ok(u.Cli.atomic_write_text_file(tmp_path / "business.yaml", yaml_text))
        with (
            u.Tests.env_vars_context({"FLEXT_ORACLE_OIC_CONFIG_DIR": str(tmp_path)}),
            pytest.raises(m.ValidationError, match="OracleOic"),
        ):
            FlextOracleOicConfig()

        tm.that(FlextOracleOicConfig.fetch_global() is config, truth=True)
