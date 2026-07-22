# AUTO-GENERATED FILE — Regenerate with: make gen
"""Services package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_oracle_oic.services.auth import (
        FlextOracleOicAuthMixin as FlextOracleOicAuthMixin,
    )
    from flext_oracle_oic.services.base import (
        FlextOracleOicServiceBase as FlextOracleOicServiceBase,
    )
    from flext_oracle_oic.services.integration_crud import (
        FlextOracleOicIntegrationCrudMixin as FlextOracleOicIntegrationCrudMixin,
    )
    from flext_oracle_oic.services.integration_lifecycle import (
        FlextOracleOicIntegrationLifecycleMixin as FlextOracleOicIntegrationLifecycleMixin,
    )
    from flext_oracle_oic.services.monitoring import (
        FlextOracleOicMonitoringMixin as FlextOracleOicMonitoringMixin,
    )
    from flext_oracle_oic.services.orchestration import (
        FlextOracleOicOrchestrationMixin as FlextOracleOicOrchestrationMixin,
    )
_LAZY_IMPORTS = build_lazy_import_map({
    ".auth": ("FlextOracleOicAuthMixin",),
    ".base": ("FlextOracleOicServiceBase",),
    ".integration_crud": ("FlextOracleOicIntegrationCrudMixin",),
    ".integration_lifecycle": ("FlextOracleOicIntegrationLifecycleMixin",),
    ".monitoring": ("FlextOracleOicMonitoringMixin",),
    ".orchestration": ("FlextOracleOicOrchestrationMixin",),
})


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
