# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic.services package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
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


__all__: tuple[str, ...] = (
    "FlextOracleOicAuthMixin",
    "FlextOracleOicIntegrationCrudMixin",
    "FlextOracleOicIntegrationLifecycleMixin",
    "FlextOracleOicMonitoringMixin",
    "FlextOracleOicOrchestrationMixin",
    "FlextOracleOicServiceBase",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextOracleOicAuthMixin": ".auth",
        "FlextOracleOicIntegrationCrudMixin": ".integration_crud",
        "FlextOracleOicIntegrationLifecycleMixin": ".integration_lifecycle",
        "FlextOracleOicMonitoringMixin": ".monitoring",
        "FlextOracleOicOrchestrationMixin": ".orchestration",
        "FlextOracleOicServiceBase": ".base",
    }),
    public_exports=__all__,
)
