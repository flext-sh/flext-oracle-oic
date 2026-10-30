"""FLEXT Oracle OIC Service - MRO Composition Facade.

Service facade composing all domain mixins via MRO inheritance. Each mixin
encapsulates a single concern (CRUD, lifecycle, patterns, orchestration,
monitoring, auth).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_oracle_oic import FlextOracleOicServiceBase
from flext_oracle_oic.services.auth import FlextOracleOicAuth
from flext_oracle_oic.services.integration_crud import FlextOracleOicIntegrationCrud
from flext_oracle_oic.services.integration_lifecycle import (
    FlextOracleOicIntegrationLifecycle,
)
from flext_oracle_oic.services.monitoring import FlextOracleOicMonitoring
from flext_oracle_oic.services.orchestration import FlextOracleOicOrchestration


class FlextOracleOicService(
    FlextOracleOicAuth,
    FlextOracleOicMonitoring,
    FlextOracleOicOrchestration,
    FlextOracleOicIntegrationLifecycle,
    FlextOracleOicIntegrationCrud,
    FlextOracleOicServiceBase,
):
    """Unified Oracle OIC Service - MRO Composition Facade.

    Composes all Oracle OIC functionality via mixin inheritance:
    - FlextOracleOicIntegrationCrud: create, get, update, delete, deploy, list
    - FlextOracleOicIntegrationLifecycle: activate, deactivate, test_connection
    - FlextOracleOicOrchestration: app-driven, scheduled, file transfer
    - FlextOracleOicMonitoring: health status, performance metrics
    - FlextOracleOicAuth: token refresh, token validation
    - FlextOracleOicServiceBase: client management, value normalization, settings
    """


__all__: list[str] = ["FlextOracleOicService"]
