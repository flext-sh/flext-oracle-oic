"""Simple API for FLEXT Oracle OIC Extension setup and configuration.

Copyright (c) 2025 Flext. All rights reserved.
SPDX-License-Identifier: MIT

This module provides a simple API for setting up Oracle Integration Cloud extensions.
It uses flext-core patterns for configuration and error handling.
"""

from __future__ import annotations

import os
from typing import cast

from flext_core import FlextResult, get_logger

from flext_oracle_oic_ext.config import (
    EnvironmentLiteral,
    LogLevelLiteral,
    OICExtensionConnectionConfig,
    OracleOICExtensionSettings,
)

logger = get_logger(__name__)


def setup_oic_extension(
    settings: OracleOICExtensionSettings | None = None,
) -> FlextResult[OracleOICExtensionSettings]:
    """Setup Oracle OIC extension with basic configuration validation."""
    try:
        if settings is None:
            connection = OICExtensionConnectionConfig(
                host=os.getenv("OIC_HOST", "localhost"),
                port=int(os.getenv("OIC_PORT", "8080")),
                use_ssl=os.getenv("OIC_USE_SSL", "false").lower() == "true",
            )
            settings = OracleOICExtensionSettings(
                environment="development",
                log_level="INFO",
                connection=connection,
            )

        logger.info(
            "OIC extension setup completed",
            extra={"settings": type(settings).__name__},
        )
        return FlextResult.ok(settings)

    except (RuntimeError, ValueError, TypeError) as e:
        return FlextResult.fail(f"Failed to setup OIC extension: {e}")


def create_development_oic_config(
    host: str | None = None,
    port: int | None = None,
    use_ssl: bool | None = None,
    **overrides: object,
) -> OracleOICExtensionSettings:
    """Create development configuration with conservative settings."""
    final_host = host or os.getenv("OIC_DEV_HOST") or "localhost"
    final_port = port or int(os.getenv("OIC_DEV_PORT", "8080"))
    final_use_ssl = (
        use_ssl
        if use_ssl is not None
        else os.getenv("OIC_DEV_USE_SSL", "false").lower() == "true"
    )

    connection = OICExtensionConnectionConfig(
        host=final_host,
        port=final_port,
        use_ssl=final_use_ssl,
    )

    return OracleOICExtensionSettings(
        environment="development",
        log_level="DEBUG",
        connection=connection,
    )


def create_production_oic_config(
    host: str,
    port: int = 443,
    use_ssl: bool = True,
    **overrides: object,
) -> OracleOICExtensionSettings:
    """Create production configuration with performance optimizations."""
    connection = OICExtensionConnectionConfig(
        host=host,
        port=port,
        use_ssl=use_ssl,
    )

    return OracleOICExtensionSettings(
        environment="production",
        log_level="INFO",
        connection=connection,
    )


def create_test_oic_config(**overrides: object) -> OracleOICExtensionSettings:
    """Create test configuration with minimal resource usage."""
    connection = OICExtensionConnectionConfig(
        host="test-host",
        port=8080,
        use_ssl=False,
    )

    return OracleOICExtensionSettings(
        environment="development",  # Test uses dev environment
        log_level="WARNING",
        connection=connection,
    )


def create_sandbox_oic_config(**overrides: object) -> OracleOICExtensionSettings:
    """Create sandbox configuration for experimentation and learning."""
    connection = OICExtensionConnectionConfig(
        host="sandbox-host",
        port=8080,
        use_ssl=False,
    )

    return OracleOICExtensionSettings(
        environment="development",  # Sandbox uses dev environment
        log_level="DEBUG",
        connection=connection,
    )


def configure_for_meltano(
    config_dict: dict[str, object],
) -> FlextResult[OracleOICExtensionSettings]:
    """Configure Oracle OIC extension from Meltano configuration dictionary."""
    try:
        # Extract basic configuration and create simple settings
        host = str(config_dict.get("host", "localhost"))
        port_value = config_dict.get("port", 8080)
        port = int(port_value) if isinstance(port_value, (int, str)) else 8080
        use_ssl_value = config_dict.get("use_ssl", False)
        use_ssl = (
            bool(use_ssl_value)
            if isinstance(use_ssl_value, (bool, str, int))
            else False
        )
        # Validate and cast to Literal types
        env_value = str(config_dict.get("environment", "development"))
        if env_value not in {"development", "staging", "production"}:
            env_value = "development"  # Default fallback
        environment = cast("EnvironmentLiteral", env_value)

        level_value = str(config_dict.get("log_level", "INFO"))
        if level_value not in {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}:
            level_value = "INFO"  # Default fallback
        log_level = cast("LogLevelLiteral", level_value)

        connection = OICExtensionConnectionConfig(
            host=host,
            port=port,
            use_ssl=use_ssl,
        )

        settings = OracleOICExtensionSettings(
            environment=environment,
            log_level=log_level,
            connection=connection,
        )

        return FlextResult.ok(settings)
    except (RuntimeError, ValueError, TypeError) as e:
        return FlextResult.fail(f"Failed to configure from Meltano: {e}")


# Export convenience functions
__all__: list[str] = [
    "configure_for_meltano",
    "create_development_oic_config",
    "create_production_oic_config",
    "create_sandbox_oic_config",
    "create_test_oic_config",
    "setup_oic_extension",
]
