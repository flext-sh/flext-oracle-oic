"""FLEXT Oracle OIC Service - MRO Composition Facade.

Service facade composing all domain mixins via MRO inheritance.
Each mixin encapsulates a single concern (CRUD, lifecycle, patterns,
orchestration, monitoring, auth).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_oracle_oic.services.auth import FlextOracleOicAuthMixin
from flext_oracle_oic.services.base import FlextOracleOicServiceBase
from flext_oracle_oic.services.integration_crud import (
    FlextOracleOicIntegrationCrudMixin,
)
from flext_oracle_oic.services.integration_lifecycle import (
    FlextOracleOicIntegrationLifecycleMixin,
)
from flext_oracle_oic.services.monitoring import FlextOracleOicMonitoringMixin
from flext_oracle_oic.services.orchestration import FlextOracleOicOrchestrationMixin


class FlextOracleOicService(
    FlextOracleOicAuthMixin,
    FlextOracleOicMonitoringMixin,
    FlextOracleOicOrchestrationMixin,
    FlextOracleOicIntegrationLifecycleMixin,
    FlextOracleOicIntegrationCrudMixin,
    FlextOracleOicServiceBase,
):
    """Unified Oracle OIC Service - MRO Composition Facade.

    Composes all Oracle OIC functionality via mixin inheritance:
    - FlextOracleOicIntegrationCrudMixin: create, get, update, delete, deploy, list
    - FlextOracleOicIntegrationLifecycleMixin: activate, deactivate, test_connection
    - FlextOracleOicOrchestrationMixin: app-driven, scheduled, file transfer
    - FlextOracleOicMonitoringMixin: health status, performance metrics
    - FlextOracleOicAuthMixin: token refresh, token validation
    - FlextOracleOicServiceBase: client management, value normalization, settings
    """


s = FlextOracleOicService

__all__: list[str] = ["FlextOracleOicService", "s"]
