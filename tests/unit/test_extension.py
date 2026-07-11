"""Behavioral tests for the Oracle OIC public facade (FlextOracleOicApi).

Asserts observable public contract only: the facade alias, context payloads
derived from settings, and the r[T] outcome of fallible operations. No private
attribute access, no internal-collaborator spying, no network.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Callable

import pytest

from flext_oracle_oic import FlextOracleOicApi, FlextOracleOicSettings, c, p, t
from flext_oracle_oic.api import oracle_oic


class TestsFlextOracleOicExtension:
    """Public-contract tests for the Oracle OIC API facade."""

    @pytest.fixture
    def settings(self) -> FlextOracleOicSettings:
        """Deterministic in-memory settings with distinctive values."""
        return FlextOracleOicSettings.model_validate({
            "OracleOic": {
                "base_url": "https://custom.example.com",
                "oauth_client_id": "client-abc",
                "oauth_scope": "urn:opc:idm:__myscopes__",
            },
        })

    @pytest.fixture
    def api(self, settings: FlextOracleOicSettings) -> FlextOracleOicApi:
        """Facade built from the deterministic settings fixture."""
        return FlextOracleOicApi(settings)

    def test_facade_alias_refers_to_the_api_class(self) -> None:
        """The public `oracle_oic` alias is the FlextOracleOicApi class itself."""
        assert oracle_oic is FlextOracleOicApi

    def test_facade_constructs_without_settings(self) -> None:
        """Constructing with no settings yields a usable facade instance."""
        api = FlextOracleOicApi()

        assert isinstance(api, FlextOracleOicApi)

    def test_facade_constructs_with_explicit_settings(
        self,
        api: FlextOracleOicApi,
    ) -> None:
        """Constructing with explicit settings yields a facade instance."""
        assert isinstance(api, FlextOracleOicApi)

    def test_connection_context_reports_success(
        self,
        api: FlextOracleOicApi,
    ) -> None:
        """fetch_connection_context is a total operation that succeeds."""
        result: p.Result[t.JsonMapping] = api.fetch_connection_context()

        assert result.success

    def test_connection_context_reflects_provided_settings(
        self,
        api: FlextOracleOicApi,
    ) -> None:
        """The connection context echoes the configured base URL and timeout."""
        payload = api.fetch_connection_context().unwrap()

        assert payload["base_url"] == "https://custom.example.com"
        assert payload["request_timeout"] == 30

    def test_auth_context_reflects_provided_settings(
        self,
        api: FlextOracleOicApi,
    ) -> None:
        """The auth context echoes the configured OAuth client id and scope."""
        payload = api.fetch_auth_context().unwrap()

        assert payload["oauth_client_id"] == "client-abc"
        assert payload["oauth_scope"] == "urn:opc:idm:__myscopes__"

    def test_features_context_exposes_boolean_feature_flags(
        self,
        api: FlextOracleOicApi,
    ) -> None:
        """The features context exposes the default-enabled boolean flags."""
        payload = api.fetch_features_context().unwrap()

        assert payload["enable_monitoring"] is True
        assert payload["use_ssl"] is True
        assert payload["verify_ssl"] is True

    @pytest.mark.parametrize(
        ("key", "expected"),
        [
            ("base_url", "https://custom.example.com"),
            ("api_version", c.OICApiVersion.V1),
        ],
    )
    def test_connection_context_keys(
        self,
        api: FlextOracleOicApi,
        key: str,
        expected: object,
    ) -> None:
        """Connection context surfaces each expected key with the config value."""
        payload = api.fetch_connection_context().unwrap()

        assert payload[key] == expected

    def test_monitoring_health_status_returns_status_payload(
        self,
        api: FlextOracleOicApi,
    ) -> None:
        """Health status is a total operation returning a status mapping."""
        result = api.fetch_health_status()

        assert result.success
        assert "status" in result.unwrap()

    def test_performance_metrics_returns_metrics_payload(
        self,
        api: FlextOracleOicApi,
    ) -> None:
        """Performance metrics is a total operation returning a metrics mapping."""
        result = api.fetch_performance_metrics()

        assert result.success
        assert "success_rate" in result.unwrap()

    @pytest.mark.parametrize(
        "operation",
        [
            lambda api: api.test_connection(),
            lambda api: api.list_integrations(),
            lambda api: api.execute(),
            lambda api: api.refresh_auth_token(),
            lambda api: api.validate_auth_token("some-token"),
            lambda api: api.activate_integration("int-1"),
            lambda api: api.deactivate_integration("int-1"),
        ],
    )
    def test_client_operations_fail_when_credentials_incomplete(
        self,
        api: FlextOracleOicApi,
        operation: Callable[[FlextOracleOicApi], p.Result[object]],
    ) -> None:
        """Client-backed operations return a failure result (never raise).

        With the OAuth client secret unset, business-rule validation rejects
        client creation, so every client-dependent operation surfaces the
        failure through r[T] rather than raising or inventing a success.
        """
        result = operation(api)

        assert not result.success
        assert result.error

    def test_failed_operation_preserves_validation_error_message(
        self,
        api: FlextOracleOicApi,
    ) -> None:
        """The failure error identifies the offending credential validation."""
        result = api.test_connection()

        assert not result.success
        assert "secret" in (result.error or "").lower()


__all__: list[str] = ["TestsFlextOracleOicExtension"]
