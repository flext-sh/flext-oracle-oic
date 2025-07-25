"""Modern Configuration System using flext-core patterns.

CONSOLIDATED: Uses centralized config from flext-meltano.
Zero tolerance for code duplication.
"""

from __future__ import annotations

# CONSOLIDATED: Import from centralized flext-meltano
from flext_meltano.extensions.oracle_oic.config import (
    EnvironmentLiteral,
    LogLevelLiteral,
    OICExtensionConnectionConfig,
    OracleOICExtensionSettings,
)

# Re-export for backward compatibility
__all__ = [
    "EnvironmentLiteral",
    "LogLevelLiteral",
    "OICExtensionConnectionConfig",
    "OracleOICExtensionSettings",
]
