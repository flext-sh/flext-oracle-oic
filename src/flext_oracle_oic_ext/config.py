"""Modern Configuration System using flext-core patterns."""

from __future__ import annotations

from typing import Literal

from flext_core import FlextSettings

# Type definitions
EnvironmentLiteral = Literal["development", "staging", "production"]
LogLevelLiteral = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class OICExtensionConnectionConfig(FlextSettings):
    """OIC extension connection configuration."""

    host: str = "localhost"
    port: int = 8080
    use_ssl: bool = False


class OracleOICExtensionSettings(FlextSettings):
    """Oracle OIC extension settings."""

    environment: EnvironmentLiteral = "development"
    log_level: LogLevelLiteral = "INFO"
    connection: OICExtensionConnectionConfig = OICExtensionConnectionConfig()


# Re-export for backward compatibility
__all__: list[str] = [
    "EnvironmentLiteral",
    "LogLevelLiteral",
    "OICExtensionConnectionConfig",
    "OracleOICExtensionSettings",
]
