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

from collections.abc import Callable, Iterator, Sequence

import pytest

from flext_oracle_oic import (
    FlextOracleOicServiceBase,
    FlextOracleOicSettings,
    m,
    p,
    s,
    t,
)
from flext_oracle_oic.services import FlextOracleOicService
from flext_oracle_oic.services.auth import FlextOracleOicAuthMixin
from flext_oracle_oic.services.integration_crud import (
    FlextOracleOicIntegrationCrudMixin,
)
from flext_oracle_oic.services.integration_lifecycle import (
    FlextOracleOicIntegrationLifecycleMixin,
)
from flext_oracle_oic.services.monitoring import FlextOracleOicMonitoringMixin
from flext_oracle_oic.services.orchestration import FlextOracleOicOrchestrationMixin
from tests import c, tm

_VALID_CLIENT_ID = "client-id-123"
_VALID_OAUTH_CREDENTIAL = "test-credential-123"

type _OperationResult = (
    p.Result[Sequence[m.OracleOic.OICIntegrationInfo]]
    | p.Result[m.OracleOic.OICIntegrationInfo]
    | p.Result[Sequence[m.OracleOic.OICConnectionInfo]]
    | p.Result[bool]
    | p.Result[str]
)
"""Union of every fallible service-operation result the contract invokes."""


def _invoke_unconfigured_operation(
    svc: FlextOracleOicService,
    operation: str,
) -> _OperationResult:
    """Invoke one fallible service operation by name.

    Returns:
        The resulting operation ``r``.

    """
    operations: t.MappingKV[str, Callable[[], _OperationResult]] = {
        "execute": svc.execute,
        "list_integrations": svc.list_integrations,
        "create_integration": lambda: svc.create_integration({}),
        "fetch_integration": lambda: svc.fetch_integration("int-1"),
        "update_integration": lambda: svc.update_integration("int-1", {}),
        "delete_integration": lambda: svc.delete_integration("int-1"),
        "deploy_integration": lambda: svc.deploy_integration({}),
        "list_connections": svc.list_connections,
        "activate_integration": lambda: svc.activate_integration("int-1"),
        "deactivate_integration": lambda: svc.deactivate_integration("int-1"),
    }
    fallback = svc.test_connection
    invoke = operations.get(operation, fallback)
    return invoke()


class TestsFlextOracleOicExtServices:
    """Public-contract behavior of the Oracle OIC service facade."""

    @pytest.fixture
    def unconfigured_service() -> Iterator[FlextOracleOicService]:
        """Service backed by default (credential-less) global settings.

        Yields:
            Each ``FlextOracleOicService``.

        """
        FlextOracleOicSettings.reset_for_testing()
        yield FlextOracleOicService()
        FlextOracleOicSettings.reset_for_testing()

    @pytest.fixture
    def configured_service(
        self: pytest.MonkeyPatch,
    ) -> Iterator[FlextOracleOicService]:
        """Service backed by global settings with valid OAuth credentials.

        Yields:
            Each ``FlextOracleOicService``.

        """
        # NOTE (ADR-005): project fields are namespaced under settings.OracleOic,
        # so env vars use the nested delimiter form ORACLEOIC__<FIELD>.
        self.setenv(
            "FLEXT_ORACLE_OIC_ORACLEOIC__OAUTH_CLIENT_ID",
            _VALID_CLIENT_ID,
        )
        self.setenv(
            "FLEXT_ORACLE_OIC_ORACLEOIC__OAUTH_CLIENT_SECRET",
            _VALID_OAUTH_CREDENTIAL,
        )
        FlextOracleOicSettings.reset_for_testing()
        yield FlextOracleOicService()
        FlextOracleOicSettings.reset_for_testing()

    # -- composition contract -------------------------------------------------

    @staticmethod
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
        unconfigured_service: FlextOracleOicService,
        mixin: type[FlextOracleOicServiceBase],
    ) -> None:
        """The facade is-a every domain mixin it advertises composing."""
        tm.that(unconfigured_service, is_=mixin)

    @staticmethod
    def test_module_alias_s_is_the_service_base_class() -> None:
        """The short ``s`` alias resolves to the base service facade class."""
        tm.ok(s is FlextOracleOicServiceBase)

    @staticmethod
    def test_context_manager_yields_the_same_service(
        unconfigured_service: FlextOracleOicService,
    ) -> None:
        """Entering the service context returns the service instance itself."""
        with unconfigured_service as entered:
            tm.ok(entered is unconfigured_service)

    # -- fallible operations: graceful failure when unconfigured --------------

    @staticmethod
    @pytest.mark.parametrize(
        c.ContextScope.OPERATION,
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
        unconfigured_service: FlextOracleOicService,
        operation: str,
    ) -> None:
        """Every fallible op returns a failed ``r`` (never raises) when unconfigured."""
        result = _invoke_unconfigured_operation(unconfigured_service, operation)
        tm.fail(result)
        tm.that(tm.not_none(result.error), empty=False)

    @staticmethod
    def test_execute_delegates_to_integration_listing(
        unconfigured_service: FlextOracleOicService,
    ) -> None:
        """``execute`` mirrors ``list_integrations`` (same failure error)."""
        tm.that(
            unconfigured_service.execute().error,
            eq=unconfigured_service.list_integrations().error,
        )

    # -- authentication contract (independent of settings/network) ------------

    @staticmethod
    def test_refresh_auth_token_reports_missing_authenticator(
        unconfigured_service: FlextOracleOicService,
    ) -> None:
        """Token refresh fails with an explicit missing-authenticator error."""
        result = unconfigured_service.refresh_auth_token()

        tm.fail(result)
        tm.that(result.error, eq="Authenticator not initialized")

    @staticmethod
    @pytest.mark.parametrize("token", ["", "some-token", "expired.jwt.value"])
    def test_validate_auth_token_reports_missing_authenticator(
        unconfigured_service: FlextOracleOicService,
        token: str,
    ) -> None:
        """Token validation fails identically regardless of the token value."""
        result = unconfigured_service.validate_auth_token(token)

        tm.fail(result)
        tm.that(result.error, eq="Authenticator not initialized")

    # -- business-rule validation contract ------------------------------------

    @staticmethod
    def test_business_rules_fail_without_oauth_credentials(
        unconfigured_service: FlextOracleOicService,
    ) -> None:
        """Default (credential-less) settings fail business-rule validation."""
        result = unconfigured_service.validate_business_rules()
        error = result.error

        tm.fail(result)
        error = tm.not_none(error)
        tm.that(error.lower(), has="validation")

    @staticmethod
    def test_business_rules_pass_with_valid_credentials(
        configured_service: FlextOracleOicService,
    ) -> None:
        """Valid OAuth credentials satisfy business-rule validation."""
        result = configured_service.validate_business_rules()

        tm.ok(result)
        tm.ok(result.value)

    @staticmethod
    def test_business_rules_validation_is_idempotent(
        configured_service: FlextOracleOicService,
    ) -> None:
        """Repeated validation of the same settings yields the same success."""
        first = configured_service.validate_business_rules()
        second = configured_service.validate_business_rules()

        tm.ok(first)
        tm.ok(second)
        tm.that(first.value, eq=second.value)

    @staticmethod
    def _is_service_rules(candidate: p.Base) -> bool:
        """Report structural conformance without a type-narrowed argument.

        Returns:
            The resulting ``bool``.

        """
        return isinstance(candidate, p.OracleOic.ServiceRules)

    def test_configured_service_satisfies_its_own_rules_protocol(
        self,
        configured_service: FlextOracleOicService,
    ) -> None:
        """The real service structurally satisfies its own declared protocol."""
        tm.ok(self._is_service_rules(configured_service))
        result = configured_service.validate_business_rules()
        tm.ok(result)
        tm.ok(result.value)
