"""FLEXT Oracle OIC Factory - Unified Factory Pattern.

FLEXT Unified Module Pattern: Single unified factory class consolidating
all Oracle OIC factory functionality. Implements complete dependency injection
with railway-oriented error handling.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import warnings

from flext_core import FlextCore

from flext_oracle_oic.config import FlextOracleOicConfig
from flext_oracle_oic.service import FlextOracleOicService

logger = FlextCore.Logger(__name__)


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
        self._container = FlextCore.Container.get_global()
        self.logger = FlextCore.Logger(f"{__name__}.{self.__class__.__name__}")

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
            self.FlextDeprecationWarning,
            stacklevel=3,
        )

    def create_oic_extension_service(
        self,
    ) -> FlextCore.Result[FlextOracleOicService]:
        """Create Oracle OIC Extension service with configuration.

        Uses singleton config pattern - no config parameter needed.

        Returns:
          FlextCore.Result containing service instance or error

        """
        # Railway-oriented service creation - uses singleton config
        config = FlextOracleOicConfig.get_global_instance()
        return self._create_service_instance(
            config, "OIC Extension service created successfully"
        )

    def _create_service_instance(
        self, _config: FlextOracleOicConfig, success_message: str
    ) -> FlextCore.Result[FlextOracleOicService]:
        """Create service instance with proper error handling."""
        try:
            # Note: config parameter reserved for future use with custom configurations
            service = FlextOracleOicService()
            self.logger.info(success_message)
            return FlextCore.Result[FlextOracleOicService].ok(service)
        except Exception as e:
            error_msg = f"Failed to create OIC Extension service: {e}"
            self.logger.exception(error_msg)
            return FlextCore.Result[FlextOracleOicService].fail(error_msg)

    def create_development_oic_service(self) -> FlextCore.Result[FlextOracleOicService]:
        """Create OIC Extension service for development.

        Returns:
          FlextCore.Result containing development service or error

        """
        # Railway-oriented development service creation
        return (
            FlextCore.Result[object]
            .ok(None)
            .flat_map(lambda _: self._create_development_config())
            .flat_map(
                lambda config: self._create_service_instance(
                    config, "Development OIC Extension service created"
                )
            )
        )

    def _create_development_config(self) -> FlextCore.Result[FlextOracleOicConfig]:
        """Create development configuration."""
        try:
            settings = FlextOracleOicConfig(
                environment="development",
                log_level="DEBUG",
                enable_monitoring=True,
            )
            return FlextCore.Result[FlextOracleOicConfig].ok(settings)
        except Exception as e:
            error_msg = f"Failed to create development config: {e}"
            self.logger.exception(error_msg)
            return FlextCore.Result[FlextOracleOicConfig].fail(error_msg)

    def setup_oic_extension(
        self,
    ) -> FlextCore.Result[FlextOracleOicService]:
        """Setup Oracle OIC Extension with configuration.

        Uses singleton config pattern - no config parameter needed.

        Returns:
            FlextCore.Result containing configured service or error

        """
        # Railway-oriented extension setup - uses singleton config
        config = FlextOracleOicConfig.get_global_instance()
        return self._create_service_instance(
            config, "OIC Extension setup completed successfully"
        )


# Backward compatibility functions using the factory
_factory_instance = FlextOracleOicFactory()


def create_oic_extension_service() -> FlextCore.Result[FlextOracleOicService]:
    """Create Oracle OIC Extension service with configuration (backward compatibility)."""
    return _factory_instance.create_oic_extension_service()


def create_development_oic_service() -> FlextCore.Result[FlextOracleOicService]:
    """Create OIC Extension service for development (backward compatibility)."""
    return _factory_instance.create_development_oic_service()


def setup_oic_extension() -> FlextCore.Result[FlextOracleOicService]:
    """Setup Oracle OIC Extension with configuration (backward compatibility)."""
    return _factory_instance.setup_oic_extension()


# Backward compatibility warning
FlextOracleOicDeprecationWarning = FlextOracleOicFactory.FlextDeprecationWarning


__all__: FlextCore.Types.StringList = [
    "FlextOracleOicDeprecationWarning",
    "FlextOracleOicFactory",
    "create_development_oic_service",
    "create_oic_extension_service",
    "setup_oic_extension",
]
