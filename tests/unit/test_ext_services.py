"""Behavioral tests for the Oracle OIC service facade public contract.

Exercises the observable behavior of ``FlextOracleOicService`` (the MRO
composition facade for all Oracle OIC extension services) through its public
API only: the ``r[T]`` outcomes of its fallible operations, the graceful
failure channel when the service is unconfigured, and the business-rule
validation contract.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Iterator

import pytest

from flext_oracle_oic import (
    FlextOracleOicAuthMixin,
    FlextOracleOicIntegrationCrudMixin,
    FlextOracleOicIntegrationLifecycleMixin,
    FlextOracleOicMonitoringMixin,
    FlextOracleOicOrchestrationMixin,
    FlextOracleOicService,
    FlextOracleOicServiceBase,
    FlextOracleOicSettings,
    s,
)
from flext_tests import tm

__all__: list[str] = ["TestsFlextOracleOicExtServices"]

_VALID_CLIENT_ID = "client-id-123"
_VALID_CLIENT_SECRET = "supersecret-value"


class TestsFlextOracleOicExtServices:
    """Public-contract behavior of the Oracle OIC service facade."""

    @pytest.fixture
    def unconfigured_service(self) -> Iterator[FlextOracleOicService]:
        """Service backed by default (credential-less) global settings."""
        FlextOracleOicSettings.reset_for_testing()
        yield FlextOracleOicService()
        FlextOracleOicSettings.reset_for_testing()

    @pytest.fixture
    def configured_service(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> Iterator[FlextOracleOicService]:
        """Service backed by global settings with valid OAuth credentials."""
        # NOTE (ADR-005): project fields are namespaced under settings.OracleOic,
        # so env vars use the nested delimiter form ORACLEOIC__<FIELD>.
        monkeypatch.setenv(
            "FLEXT_ORACLE_OIC_ORACLEOIC__OAUTH_CLIENT_ID", _VALID_CLIENT_ID
        )
        monkeypatch.setenv(
            "FLEXT_ORACLE_OIC_ORACLEOIC__OAUTH_CLIENT_SECRET", _VALID_CLIENT_SECRET
        )
        FlextOracleOicSettings.reset_for_testing()
        yield FlextOracleOicService()
        FlextOracleOicSettings.reset_for_testing()

    # -- composition contract -------------------------------------------------

    @pytest.mark.parametrize(
        "mixin",
        [
            FlextOracleOicServiceBase,
            FlextOracleOicAuthMixin,
            FlextOracleOicMonitoringMixin,
            FlextOracleOicOrchestrationMixin,
            FlextOracleOicIntegrationLifecycleMixin,
            FlextOracleOicIntegrationCrudMixin,
        ],
    )
    def test_service_composes_every_documented_domain_mixin(
        self,
        unconfigured_service: FlextOracleOicService,
        mixin: type[FlextOracleOicServiceBase],
    ) -> None:
        """The facade is-a every domain mixin it advertises composing."""
        tm.that(unconfigured_service, is_=mixin)

    def test_module_alias_s_is_the_service_class(self) -> None:
        """The short ``s`` alias resolves to the service facade class."""
        assert s is FlextOracleOicService

    def test_context_manager_yields_the_same_service(
        self, unconfigured_service: FlextOracleOicService
    ) -> None:
        """Entering the service context returns the service instance itself."""
        with unconfigured_service as entered:
            assert entered is unconfigured_service

    # -- fallible operations: graceful failure when unconfigured --------------

    @pytest.mark.parametrize(
        "operation",
        [
            "execute",
            "list_integrations",
            "create_integration",
            "fetch_integration",
            "update_integration",
            "delete_integration",
            "deploy_integration",
            "list_connections",
            "activate_integration",
            "deactivate_integration",
            "test_connection",
        ],
    )
    def test_operations_fail_gracefully_without_credentials(
        self, unconfigured_service: FlextOracleOicService, operation: str
    ) -> None:
        """Every fallible op returns a failed ``r`` (never raises) when unconfigured."""
        svc = unconfigured_service
        match operation:
            case "execute":
                result = svc.execute()
            case "list_integrations":
                result = svc.list_integrations()
            case "create_integration":
                result = svc.create_integration({})
            case "fetch_integration":
                result = svc.fetch_integration("int-1")
            case "update_integration":
                result = svc.update_integration("int-1", {})
            case "delete_integration":
                result = svc.delete_integration("int-1")
            case "deploy_integration":
                result = svc.deploy_integration({})
            case "list_connections":
                result = svc.list_connections()
            case "activate_integration":
                result = svc.activate_integration("int-1")
            case "deactivate_integration":
                result = svc.deactivate_integration("int-1")
            case _:
                result = svc.test_connection()

        assert result.failure
        assert result.error

    def test_execute_delegates_to_integration_listing(
        self, unconfigured_service: FlextOracleOicService
    ) -> None:
        """``execute`` mirrors ``list_integrations`` (same failure error)."""
        assert (
            unconfigured_service.execute().error
            == unconfigured_service.list_integrations().error
        )

    # -- authentication contract (independent of settings/network) ------------

    def test_refresh_auth_token_reports_missing_authenticator(
        self, unconfigured_service: FlextOracleOicService
    ) -> None:
        """Token refresh fails with an explicit missing-authenticator error."""
        result = unconfigured_service.refresh_auth_token()

        tm.fail(result)
        tm.that(result.error, eq="Authenticator not initialized")

    @pytest.mark.parametrize("token", ["", "some-token", "expired.jwt.value"])
    def test_validate_auth_token_reports_missing_authenticator(
        self, unconfigured_service: FlextOracleOicService, token: str
    ) -> None:
        """Token validation fails identically regardless of the token value."""
        result = unconfigured_service.validate_auth_token(token)

        tm.fail(result)
        tm.that(result.error, eq="Authenticator not initialized")

    # -- business-rule validation contract ------------------------------------

    def test_business_rules_fail_without_oauth_credentials(
        self, unconfigured_service: FlextOracleOicService
    ) -> None:
        """Default (credential-less) settings fail business-rule validation."""
        result = unconfigured_service.validate_business_rules()
        error = result.error

        tm.fail(result)
        assert error is not None
        tm.that(error.lower(), has="validation")

    def test_business_rules_pass_with_valid_credentials(
        self, configured_service: FlextOracleOicService
    ) -> None:
        """Valid OAuth credentials satisfy business-rule validation."""
        result = configured_service.validate_business_rules()

        tm.ok(result)
        tm.that(result.value, eq=True)

    def test_business_rules_validation_is_idempotent(
        self, configured_service: FlextOracleOicService
    ) -> None:
        """Repeated validation of the same settings yields the same success."""
        first = configured_service.validate_business_rules()
        second = configured_service.validate_business_rules()

        assert first.success is second.success is True
        tm.that(first.value, eq=second.value)
