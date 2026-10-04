# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic.services package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import build_lazy_import_map, install_lazy_exports

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

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".auth": ("FlextOracleOicAuthMixin",),
            ".base": ("FlextOracleOicServiceBase",),
            ".integration_crud": ("FlextOracleOicIntegrationCrudMixin",),
            ".integration_lifecycle": ("FlextOracleOicIntegrationLifecycleMixin",),
            ".monitoring": ("FlextOracleOicMonitoringMixin",),
            ".orchestration": ("FlextOracleOicOrchestrationMixin",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    ),
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
