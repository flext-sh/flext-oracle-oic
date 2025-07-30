"""FLEXT ORACLE OIC EXT - Oracle Integration Cloud Extensions with simplified imports.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Version 0.9.0 - Oracle OIC Extensions with simplified public API:
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
from flext_core import (
    FlextBaseSettings as BaseConfig,  # Alias for backward compatibility
    FlextFields as Field,  # Alias for backward compatibility
    FlextResult,
    FlextValueObject,
)
from pydantic import BaseModel as DomainEntity

__all__ = [
    "BaseConfig",
    "DomainEntity",
    "Field",
    "FlextResult",
    "FlextValueObject",
]

# Add BaseModel alias for exports
BaseModel = DomainEntity

try:
    __version__ = importlib.metadata.version("flext-oracle-oic-ext")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

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

# CONSOLIDATED: Import from centralized flext-meltano
with contextlib.suppress(ImportError):
    from flext_meltano.extensions.oracle_oic import OracleOICExtension

# Note: Other complex classes may not be directly available,
# keeping simplified interface focused on core extension functionality

# ================================

__all__ = [
    # Core foundation patterns from flext-core
    "BaseConfig",
    "BaseModel",
    "DomainEntity",
    "Field",
    "FlextResult",
    "FlextValueObject",
    # Main OIC Extension (consolidated from flext-meltano)
    "OracleOICExtension",
    # Version info
    "__version__",
    "__version_info__",
]
