"""Factory functions and deprecation utilities for FLEXT Oracle OIC Extension.

This module contains factory functions and utilities that were moved from __init__.py
to maintain clean namespace separation and follow SOLID principles.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import warnings

from flext_core import FlextLogger, FlextResult, FlextTypes
from flext_oracle_oic.config import FlextOracleOicExtConfig
from flext_oracle_oic.ext_services import OracleOICExtensionService

logger = FlextLogger(__name__)


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


def create_oic_extension_service(
    settings: FlextOracleOicExtConfig | None = None,
) -> FlextResult[OracleOICExtensionService]:
    """Create Oracle OIC Extension service with configuration.

    Args:
      settings: Configuration settings (uses defaults if None)

    Returns:
      FlextResult containing service instance or error

    """
    try:
        if settings is None:
            settings = FlextOracleOicExtConfig.get_global_instance()

        service = OracleOICExtensionService(settings)
        logger.info("OIC Extension service created successfully")
        return FlextResult[OracleOICExtensionService].ok(service)

    except Exception as e:
        error_msg = f"Failed to create OIC Extension service: {e}"
        logger.exception(error_msg)
        return FlextResult[OracleOICExtensionService].fail(error_msg)


def create_development_oic_service() -> FlextResult[OracleOICExtensionService]:
    """Create OIC Extension service for development.

    Returns:
      FlextResult containing development service or error

    """
    try:
        settings = FlextOracleOicExtConfig(
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


def setup_oic_extension(
    settings: FlextOracleOicExtConfig | None = None,
) -> FlextResult[OracleOICExtensionService]:
    """Setup Oracle OIC Extension with configuration.

    Args:
        settings: Configuration settings (uses defaults if None)

    Returns:
        FlextResult containing configured service or error

    """
    try:
        if settings is None:
            settings = FlextOracleOicExtConfig.get_global_instance()

        service = OracleOICExtensionService(settings)
        logger.info("OIC Extension setup completed successfully")
        return FlextResult[OracleOICExtensionService].ok(service)

    except Exception as e:
        error_msg = f"Failed to setup OIC Extension: {e}"
        logger.exception(error_msg)
        return FlextResult[OracleOICExtensionService].fail(error_msg)


__all__: FlextTypes.StringList = [
    "FlextOracleOicExtDeprecationWarning",
    "_show_deprecation_warning",
    "create_development_oic_service",
    "create_oic_extension_service",
    "setup_oic_extension",
]
