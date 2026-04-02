# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT Oracle OIC Services - Service Facade Mixins.

Service decomposition following AGENTS.md Service Facade Pattern.
Each mixin encapsulates a single domain concern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_oracle_oic.services import (
        auth,
        base,
        integration_crud,
        integration_lifecycle,
        integration_patterns,
        monitoring,
        orchestration,
    )
    from flext_oracle_oic.services.auth import FlextOracleOicAuthMixin
    from flext_oracle_oic.services.base import FlextOracleOicServiceBase
    from flext_oracle_oic.services.integration_crud import (
        FlextOracleOicIntegrationCrudMixin,
    )
    from flext_oracle_oic.services.integration_lifecycle import (
        FlextOracleOicIntegrationLifecycleMixin,
    )
    from flext_oracle_oic.services.integration_patterns import (
        FlextOracleOicIntegrationPatternsMixin,
    )
    from flext_oracle_oic.services.monitoring import FlextOracleOicMonitoringMixin
    from flext_oracle_oic.services.orchestration import FlextOracleOicOrchestrationMixin

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "FlextOracleOicAuthMixin": "flext_oracle_oic.services.auth",
    "FlextOracleOicIntegrationCrudMixin": "flext_oracle_oic.services.integration_crud",
    "FlextOracleOicIntegrationLifecycleMixin": "flext_oracle_oic.services.integration_lifecycle",
    "FlextOracleOicIntegrationPatternsMixin": "flext_oracle_oic.services.integration_patterns",
    "FlextOracleOicMonitoringMixin": "flext_oracle_oic.services.monitoring",
    "FlextOracleOicOrchestrationMixin": "flext_oracle_oic.services.orchestration",
    "FlextOracleOicServiceBase": "flext_oracle_oic.services.base",
    "auth": "flext_oracle_oic.services.auth",
    "base": "flext_oracle_oic.services.base",
    "integration_crud": "flext_oracle_oic.services.integration_crud",
    "integration_lifecycle": "flext_oracle_oic.services.integration_lifecycle",
    "integration_patterns": "flext_oracle_oic.services.integration_patterns",
    "monitoring": "flext_oracle_oic.services.monitoring",
    "orchestration": "flext_oracle_oic.services.orchestration",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
