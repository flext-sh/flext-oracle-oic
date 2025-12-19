"""FLEXT Oracle OIC Factory - Unified Factory Pattern.

FLEXT Unified Module Pattern: Single unified factory class consolidating
all Oracle OIC factory functionality. Implements complete dependency injection
with railway-oriented error handling.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import warnings

from flext_core import FlextContainer, FlextLogger, FlextResult

from flext_oracle_oic.service import FlextOracleOicService
from flext_oracle_oic.settings import FlextOracleOicSettings

logger = FlextLogger(__name__)


class FlextOracleOicFactory:
    """Unified Oracle OIC Factory consolidating all factory functionality.

    FLEXT Unified Module Pattern: Single unified factory class consolidating
    all Oracle OIC factory functionality including service creation, configuration
    management, and dependency injection.
    """

    class FlextDeprecationWarning(DeprecationWarning):
        """Custom deprecation warning for FLEXT ORACLE OIC EXT import changes."""

    def __init__(self) -> None:
        """Initialize the factory."""
        self._container = FlextContainer.get_global()
        self.logger = FlextLogger(f"{__name__}.{self.__class__.__name__}")

    def _show_deprecation_warning(self, old_import: str, new_import: str) -> None:
        """Show deprecation warning for import paths."""
        message_parts = [
            f"⚠️  DEPRECATED IMPORT: {old_import}",
            f"USE INSTEAD: {new_import}",
            "🔗 This will be removed in version 1.0.0",
            "📖 See FLEXT ORACLE OIC EXT docs for migration guide",
        ]
        warnings.warn(
            "\n".join(message_parts),
            self.FlextDeprecationWarning,
            stacklevel=3,
        )

    def create_oic_extension_service(
        self,
    ) -> FlextResult[FlextOracleOicService]:
        """Create Oracle OIC Extension service with configuration.

        Uses singleton config pattern - no config parameter needed.

        Returns:
        FlextResult containing service instance or error

        """
        # Railway-oriented service creation - uses singleton config
        config = FlextOracleOicSettings.get_global_instance()
        return self._create_service_instance(
            config,
            "OIC Extension service created successfully",
        )

    def _create_service_instance(
        self,
        _config: FlextOracleOicSettings,
        success_message: str,
    ) -> FlextResult[FlextOracleOicService]:
        """Create service instance with proper error handling."""
        try:
            # Note: config parameter reserved for future use with custom configurations
            service = FlextOracleOicService()
            self.logger.info(success_message)
            return FlextResult[FlextOracleOicService].ok(service)
        except Exception as e:
            error_msg = f"Failed to create OIC Extension service: {e}"
            self.logger.exception(error_msg)
            return FlextResult[FlextOracleOicService].fail(error_msg)

    def create_development_oic_service(self) -> FlextResult[FlextOracleOicService]:
        """Create OIC Extension service for development.

        Returns:
        FlextResult containing development service or error

        """
        # Railway-oriented development service creation
        return (
            FlextResult[object]
            .ok(None)
            .flat_map(lambda _: self._create_development_config())
            .flat_map(
                lambda config: self._create_service_instance(
                    config,
                    "Development OIC Extension service created",
                ),
            )
        )

    def _create_development_config(self) -> FlextResult[FlextOracleOicSettings]:
        """Create development configuration."""
        try:
            settings = FlextOracleOicSettings(
                environment="development",
                log_level="DEBUG",
                enable_monitoring=True,
            )
            return FlextResult[FlextOracleOicSettings].ok(settings)
        except Exception as e:
            error_msg = f"Failed to create development config: {e}"
            self.logger.exception(error_msg)
            return FlextResult[FlextOracleOicSettings].fail(error_msg)

    def setup_oic_extension(
        self,
    ) -> FlextResult[FlextOracleOicService]:
        """Setup Oracle OIC Extension with configuration.

        Uses singleton config pattern - no config parameter needed.

        Returns:
        FlextResult containing configured service or error

        """
        # Railway-oriented extension setup - uses singleton config
        config = FlextOracleOicSettings.get_global_instance()
        return self._create_service_instance(
            config,
            "OIC Extension setup completed successfully",
        )


# Backward compatibility functions using the factory
_factory_instance = FlextOracleOicFactory()


def create_oic_extension_service() -> FlextResult[FlextOracleOicService]:
    """Create Oracle OIC Extension service with configuration (backward compatibility)."""
    return _factory_instance.create_oic_extension_service()


def create_development_oic_service() -> FlextResult[FlextOracleOicService]:
    """Create OIC Extension service for development (backward compatibility)."""
    return _factory_instance.create_development_oic_service()


def setup_oic_extension() -> FlextResult[FlextOracleOicService]:
    """Setup Oracle OIC Extension with configuration (backward compatibility)."""
    return _factory_instance.setup_oic_extension()


# Backward compatibility warning class with real inheritance
class FlextOracleOicDeprecationWarning(FlextOracleOicFactory.FlextDeprecationWarning):
    """FlextOracleOicDeprecationWarning - real inheritance from FlextDeprecationWarning."""


__all__: list[str] = [
    "FlextOracleOicDeprecationWarning",
    "FlextOracleOicFactory",
    "create_development_oic_service",
    "create_oic_extension_service",
    "setup_oic_extension",
]
