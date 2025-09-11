"""FLEXT Oracle OIC Extension - EXTENSION Pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextTypes

"""
Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""


import importlib.metadata
import warnings

# ================================
# EXTENSION Pattern: Core Imports
# ================================
# Foundation da flext-core
from flext_core import FlextConfig, FlextLogger, FlextModels, FlextResult

from flext_oracle_oic_ext.ext_client import (
    OICExtensionAuthenticator,
    OracleOICExtensionClient,
)

# EXTENSION Pattern: Main components
from flext_oracle_oic_ext.ext_config import (
    OICExtensionAuthConfig,
    OICExtensionConnectionConfig,
    OracleOICExtensionSettings,
)
from flext_oracle_oic_ext.ext_exceptions import (
    OICAPIError,
    OICAuthenticationError,
    OICConnectionError,
    OICIntegrationError,
)
from flext_oracle_oic_ext.ext_models import (
    OICAuthConfig,
    OICConnectionConfig,
    OICConnectionInfo,
    OICIntegrationInfo,
)
from flext_oracle_oic_ext.ext_services import (
    OICIntegrationPatternService,
    OracleOICExtensionService,
)

# Legacy extension for backward compatibility
from flext_oracle_oic_ext.extension import OracleOICExtension

logger = FlextLogger(__name__)

try:
    __version__ = importlib.metadata.version("flext-oracle-oic-ext")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())


class FlextOracleOicExtDeprecationWarning(DeprecationWarning):
    """Custom deprecation warning for FLEXT ORACLE OIC EXT import changes."""


import importlib.metadata

# ================================
# EXTENSION Pattern: Core Imports
# ================================
# Foundation da flext-core
from flext_core import FlextLogger

# EXTENSION Pattern: Main components

# Legacy extension for backward compatibility

logger = FlextLogger(__name__)

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
# EXTENSION Pattern: Convenience Functions
# ================================


def create_oic_extension_service(
    settings: OracleOICExtensionSettings | None = None,
) -> FlextResult[OracleOICExtensionService]:
    """Create Oracle OIC Extension service with configuration.

    Padrão EXTENSION: Função de conveniência para criar serviço
    Oracle OIC Extension com configuração padrão ou customizada.

    Args:
      settings: Configuration settings (uses defaults if None)

    Returns:
      FlextResult containing service instance or error

    """
    try:
        if settings is None:
            settings = OracleOICExtensionSettings()

        service = OracleOICExtensionService(settings)
        logger.info("OIC Extension service created successfully")
        return FlextResult[OracleOICExtensionService].ok(service)

    except Exception as e:
        error_msg = f"Failed to create OIC Extension service: {e}"
        logger.exception(error_msg)
        return FlextResult[OracleOICExtensionService].fail(error_msg)


def create_development_oic_service() -> FlextResult[OracleOICExtensionService]:
    """Create OIC Extension service for development.

    Padrão EXTENSION: Função de conveniência para ambiente de desenvolvimento
    com configurações adequadas para testes e desenvolvimento local.

    Returns:
      FlextResult containing development service or error

    """
    try:
        settings = OracleOICExtensionSettings(
            environment="development",
            log_level="DEBUG",
            enable_monitoring=True,
        )

        service = OracleOICExtensionService(settings)
        logger.info("Development OIC Extension service created")
        return FlextResult[OracleOICExtensionService].ok(service)

    except Exception as e:
        error_msg = f"Failed to create development OIC service: {e}"
        logger.exception(error_msg)
        return FlextResult[OracleOICExtensionService].fail(error_msg)


# ================================
# EXTENSION Pattern: Public API Exports
# ================================

__all__: FlextTypes.Core.StringList = [
    "FlextConfig",
    "FlextLogger",
    "FlextModels",
    # ===== Foundation flext-core =====
    "FlextResult",
    "OICAPIError",  # API errors
    "OICAuthConfig",  # Auth model
    # ===== Exceptions =====
    "OICAuthenticationError",  # Auth errors
    "OICConnectionConfig",  # Connection model
    "OICConnectionError",  # Connection errors
    "OICConnectionInfo",  # Connection info
    "OICExtensionAuthConfig",  # Auth config
    # ===== Authentication =====
    "OICExtensionAuthenticator",  # Main authenticator
    # ===== Configuration Models =====
    "OICExtensionConnectionConfig",  # Connection config
    "OICIntegrationError",  # Integration errors
    # ===== Business Models =====
    "OICIntegrationInfo",  # Integration info
    "OICIntegrationPatternService",  # Integration patterns
    # ===== Legacy Support =====
    "OracleOICExtension",  # Backward compatibility
    "OracleOICExtensionClient",  # API client
    # ===== Main EXTENSION Components =====
    "OracleOICExtensionService",  # Main service (EXTENSION Pattern)
    "OracleOICExtensionSettings",  # Configuration
    # ===== Version Info =====
    "__version__",
    "__version_info__",
    "create_development_oic_service",  # Development service
    # ===== Convenience Functions =====
    "create_oic_extension_service",  # Create service
]

# Legacy re-exports removed: lifecycle module not present in this package structure
