# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic.services package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .auth import FlextOracleOicAuthMixin
    from .base import FlextOracleOicServiceBase
    from .integration_crud import FlextOracleOicIntegrationCrudMixin
    from .integration_lifecycle import FlextOracleOicIntegrationLifecycleMixin
    from .monitoring import FlextOracleOicMonitoringMixin
    from .orchestration import FlextOracleOicOrchestrationMixin
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
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
