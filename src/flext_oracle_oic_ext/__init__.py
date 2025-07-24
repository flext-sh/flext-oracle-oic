"""FLEXT ORACLE OIC EXT - Oracle Integration Cloud Extensions with simplified imports.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Version 0.7.0 - Oracle OIC Extensions with simplified public API:
- All common imports available from root: from flext_oracle_oic_ext import ExtendedOICClient
- Built on flext-core foundation for robust Oracle OIC integration
- Deprecation warnings for internal imports
"""

from __future__ import annotations

import contextlib
import importlib.metadata
import warnings

# Import from flext-core for foundational patterns
# 🚨 ARCHITECTURAL COMPLIANCE: Using módulo raiz imports
# 🚨 ARCHITECTURAL COMPLIANCE: Using DI container
from flext_oracle_oic_ext.infrastructure.di_container import (
    get_base_config,
    get_domain_entity,
    get_domain_value_object,
    get_field,
    get_service_result,
)

ServiceResult = get_service_result()
DomainEntity = get_domain_entity()
Field = get_field()
DomainValueObject = get_domain_value_object()
BaseConfig = get_base_config()

__all__ = [
    "BaseConfig",
    "DomainEntity",
    "DomainValueObject",
    "Field",
    "ServiceResult",
]

try:
    __version__ = importlib.metadata.version("flext-oracle-oic-ext")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.7.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())


class FlextOracleOicExtDeprecationWarning(DeprecationWarning):
    """Custom deprecation warning for FLEXT ORACLE OIC EXT import changes."""


def _show_deprecation_warning(old_import: str, new_import: str) -> None:
    """Show deprecation warning for import paths."""
    message_parts = [
        f"⚠️  DEPRECATED IMPORT: {old_import}",
        f"✅ USE INSTEAD: {new_import}",
        "🔗 This will be removed in version 1.0.0",
        "📖 See FLEXT ORACLE OIC EXT docs for migration guide",
    ]
    warnings.warn(
        "\n".join(message_parts),
        FlextOracleOicExtDeprecationWarning,
        stacklevel=3,
    )


# ================================
# SIMPLIFIED PUBLIC API EXPORTS
# ================================

# Foundation patterns - ALWAYS from flext-core (imported above)

with contextlib.suppress(ImportError):
    from flext_oracle_oic_ext.extension import OracleOICExtension

with contextlib.suppress(ImportError):
    from flext_oracle_oic_ext.client.extended_client import ExtendedOICClient

with contextlib.suppress(ImportError):
    from flext_oracle_oic_ext.orchestration.patterns import (
        IntegrationPattern,
        IntegrationPatternOrchestrator,
    )

with contextlib.suppress(ImportError):
    from flext_oracle_oic_ext.adapters import (
        CustomDatabaseAdapter,
        CustomRESTAdapter,
        OICAdapterManager,
    )

# ================================

__all__ = [
    "BaseModel",  # from flext_oracle_oic_ext import BaseModel
    # OIC Custom Adapters (simplified access)
    "CustomDatabaseAdapter",  # from flext_oracle_oic_ext import CustomDatabaseAdapter
    "CustomRESTAdapter",  # from flext_oracle_oic_ext import CustomRESTAdapter
    # OIC Extended Client (simplified access)
    "ExtendedOICClient",  # from flext_oracle_oic_ext import ExtendedOICClient
    # OIC Integration Patterns (simplified access)
    "IntegrationPattern",  # from flext_oracle_oic_ext import IntegrationPattern
    "IntegrationPatternOrchestrator",  # from flext_oracle_oic_ext import IntegrationPatternOrchestrator
    # OIC Adapters (simplified access)
    "OICAdapterManager",  # from flext_oracle_oic_ext import OICAdapterManager
    # Core Patterns (from flext-core)
    "OICBaseConfig",  # from flext_oracle_oic_ext import OICBaseConfig
    "OICError",  # from flext_oracle_oic_ext import OICError
    # Main OIC Extension (simplified access)
    "OracleOICExtension",  # from flext_oracle_oic_ext import OracleOICExtension
    "ServiceResult",  # from flext_oracle_oic_ext import ServiceResult
    "ValidationError",  # from flext_oracle_oic_ext import ValidationError
    # Version
    "__version__",
    "__version_info__",
]
