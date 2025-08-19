"""FLEXT Oracle OIC Extension - EXTENSION Pattern.

Este módulo estabelece o padrão EXTENSION PEP8 para Oracle OIC Extension
com API simplificada e integração flext-core. Serve como modelo para futuras extensions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Version 0.9.0 - Oracle OIC Extension API seguindo padrão EXTENSION:
- Imports simplificados: from flext_oracle_oic_ext import OracleOICExtensionService
- Integração flext-core completa: FlextResult, FlextSettings, etc
- Padrão EXTENSION estabelecido para futuras extensions
"""

from __future__ import annotations

import importlib.metadata
import warnings

# ================================
# EXTENSION Pattern: Core Imports
# ================================

# Foundation da flext-core
from flext_core import FlextResult, FlextValueObject, FlextSettings, get_logger

# EXTENSION Pattern: Main components
from flext_oracle_oic_ext.ext_config import (
    OracleOICExtensionSettings,
    OICExtensionConnectionConfig,
    OICExtensionAuthConfig,
)
from flext_oracle_oic_ext.ext_client import (
    OracleOICExtensionClient,
    OICExtensionAuthenticator,
)
from flext_oracle_oic_ext.ext_services import (
    OracleOICExtensionService,
    OICIntegrationPatternService,
)
from flext_oracle_oic_ext.ext_models import (
    OICAuthConfig,
    OICConnectionConfig,
    OICIntegrationInfo,
    OICConnectionInfo,
)
from flext_oracle_oic_ext.ext_exceptions import (
    OICAuthenticationError,
    OICConnectionError,
    OICAPIError,
    OICIntegrationError,
)

# Legacy extension for backward compatibility
from flext_oracle_oic_ext.extension import OracleOICExtension

logger = get_logger(__name__)

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
        return FlextResult[None].ok(service)

    except Exception as e:
        error_msg = f"Failed to create OIC Extension service: {e}"
        logger.exception(error_msg)
        return FlextResult[None].fail(error_msg)


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
        return FlextResult[None].ok(service)

    except Exception as e:
        error_msg = f"Failed to create development OIC service: {e}"
        logger.exception(error_msg)
        return FlextResult[None].fail(error_msg)


# ================================
# EXTENSION Pattern: Public API Exports
# ================================

__all__: list[str] = [
    # ===== Foundation flext-core =====
    "FlextResult",
    "FlextValueObject",
    "FlextSettings",
    "get_logger",
    # ===== Main EXTENSION Components =====
    "OracleOICExtensionService",  # Main service (EXTENSION Pattern)
    "OracleOICExtensionClient",  # API client
    "OracleOICExtensionSettings",  # Configuration
    "OICIntegrationPatternService",  # Integration patterns
    # ===== Configuration Models =====
    "OICExtensionConnectionConfig",  # Connection config
    "OICExtensionAuthConfig",  # Auth config
    "OICAuthConfig",  # Auth model
    "OICConnectionConfig",  # Connection model
    # ===== Business Models =====
    "OICIntegrationInfo",  # Integration info
    "OICConnectionInfo",  # Connection info
    # ===== Authentication =====
    "OICExtensionAuthenticator",  # Main authenticator
    # ===== Exceptions =====
    "OICAuthenticationError",  # Auth errors
    "OICConnectionError",  # Connection errors
    "OICAPIError",  # API errors
    "OICIntegrationError",  # Integration errors
    # ===== Convenience Functions =====
    "create_oic_extension_service",  # Create service
    "create_development_oic_service",  # Development service
    # ===== Legacy Support =====
    "OracleOICExtension",  # Backward compatibility
    # ===== Version Info =====
    "__version__",
    "__version_info__",
]

# Legacy re-exports removed: lifecycle module not present in this package structure
