"""FLEXT Oracle OIC Factory - Unified Factory Pattern.

FLEXT Unified Module Pattern: Single unified factory class consolidating
all Oracle OIC factory functionality. Implements complete dependency injection
with railway-oriented error handling.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import warnings

from flext_core import FlextContainer, FlextLogger, FlextResult, FlextTypes

from flext_oracle_oic.config import FlextOracleOicConfig
from flext_oracle_oic.service import FlextOracleOicService

logger = FlextLogger(__name__)


class FlextOracleOicFactory:
    """Unified Oracle OIC Factory consolidating all factory functionality.

    FLEXT Unified Module Pattern: Single unified factory class consolidating
    all Oracle OIC factory functionality including service creation, configuration
    management, and dependency injection.
    """

    class DeprecationWarning(DeprecationWarning):
        """Custom deprecation warning for FLEXT ORACLE OIC EXT import changes."""

    def __init__(self) -> None:
        """Initialize the factory."""
        self._container = FlextContainer.get_global()
        self.logger = FlextLogger(f"{__name__}.{self.__class__.__name__}")

    def _show_deprecation_warning(self, old_import: str, new_import: str) -> None:
        """Show deprecation warning for import paths."""
        message_parts = [
            f"⚠️  DEPRECATED IMPORT: {old_import}",
            f"✅ USE INSTEAD: {new_import}",
            "🔗 This will be removed in version 1.0.0",
            "📖 See FLEXT ORACLE OIC EXT docs for migration guide",
        ]
        warnings.warn(
            "\n".join(message_parts),
            self.DeprecationWarning,
            stacklevel=3,
        )

    def create_oic_extension_service(
        self,
        settings: FlextOracleOicConfig | None = None,
    ) -> FlextResult[FlextOracleOicService]:
        """Create Oracle OIC Extension service with configuration.

        Args:
          settings: Configuration settings (uses defaults if None)

        Returns:
          FlextResult containing service instance or error

        """
        # Railway-oriented service creation
        config = settings or FlextOracleOicConfig.get_global_instance()
        return self._create_service_instance(
            config, "OIC Extension service created successfully"
        )

    def _create_service_instance(
        self, config: FlextOracleOicConfig, success_message: str
    ) -> FlextResult[FlextOracleOicService]:
        """Create service instance with proper error handling."""
        try:
            service = FlextOracleOicService(config)
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
                    config, "Development OIC Extension service created"
                )
            )
        )

    def _create_development_config(self) -> FlextResult[FlextOracleOicConfig]:
        """Create development configuration."""
        try:
            settings = FlextOracleOicConfig(
                environment="development",
                log_level="DEBUG",
                enable_monitoring=True,
            )
            return FlextResult[FlextOracleOicConfig].ok(settings)
        except Exception as e:
            error_msg = f"Failed to create development config: {e}"
            self.logger.exception(error_msg)
            return FlextResult[FlextOracleOicConfig].fail(error_msg)

    def setup_oic_extension(
        self,
        settings: FlextOracleOicConfig | None = None,
    ) -> FlextResult[FlextOracleOicService]:
        """Setup Oracle OIC Extension with configuration.

        Args:
            settings: Configuration settings (uses defaults if None)

        Returns:
            FlextResult containing configured service or error

        """
        # Railway-oriented extension setup
        config = settings or FlextOracleOicConfig.get_global_instance()
        return self._create_service_instance(
            config, "OIC Extension setup completed successfully"
        )


# Backward compatibility functions using the factory
_factory_instance = FlextOracleOicFactory()


def create_oic_extension_service(
    settings: FlextOracleOicConfig | None = None,
) -> FlextResult[FlextOracleOicService]:
    """Create Oracle OIC Extension service with configuration (backward compatibility)."""
    return _factory_instance.create_oic_extension_service(settings)


def create_development_oic_service() -> FlextResult[FlextOracleOicService]:
    """Create OIC Extension service for development (backward compatibility)."""
    return _factory_instance.create_development_oic_service()


def setup_oic_extension(
    settings: FlextOracleOicConfig | None = None,
) -> FlextResult[FlextOracleOicService]:
    """Setup Oracle OIC Extension with configuration (backward compatibility)."""
    return _factory_instance.setup_oic_extension(settings)


# Backward compatibility warning
FlextOracleOicDeprecationWarning = FlextOracleOicFactory.DeprecationWarning


__all__: FlextTypes.StringList = [
    "FlextOracleOicDeprecationWarning",
    "FlextOracleOicFactory",
    "create_development_oic_service",
    "create_oic_extension_service",
    "setup_oic_extension",
]
