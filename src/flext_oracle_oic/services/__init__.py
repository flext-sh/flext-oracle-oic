# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic.services package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_oracle_oic.services.auth import FlextOracleOicAuth
    from flext_oracle_oic.services.facade import FlextOracleOicService
    from flext_oracle_oic.services.integration_crud import FlextOracleOicIntegrationCrud
    from flext_oracle_oic.services.integration_lifecycle import (
        FlextOracleOicIntegrationLifecycle,
    )
    from flext_oracle_oic.services.monitoring import FlextOracleOicMonitoring
    from flext_oracle_oic.services.orchestration import FlextOracleOicOrchestration


__all__: tuple[str, ...] = (
    "FlextOracleOicAuth",
    "FlextOracleOicIntegrationCrud",
    "FlextOracleOicIntegrationLifecycle",
    "FlextOracleOicMonitoring",
    "FlextOracleOicOrchestration",
    "FlextOracleOicService",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextOracleOicAuth": ".auth",
        "FlextOracleOicIntegrationCrud": ".integration_crud",
        "FlextOracleOicIntegrationLifecycle": ".integration_lifecycle",
        "FlextOracleOicMonitoring": ".monitoring",
        "FlextOracleOicOrchestration": ".orchestration",
        "FlextOracleOicService": ".facade",
    }),
    public_exports=__all__,
)
