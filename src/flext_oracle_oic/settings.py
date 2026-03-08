"""Oracle OIC Extension Configuration - Unified Class Pattern.

FLEXT Unified Class Pattern: Single OracleOicExtensionConfig class
with nested configuration classes following FLEXT architectural standards.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

# Type definitions outside class to avoid Pydantic field errors
EnvironmentLiteral = Literal["development", "staging", "production"]
LogLevelLiteral = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
OICApiVersionLiteral = Literal["v1", "v2"]


# Note: FlextOracleOicSettings follows direct instantiation pattern
# No global instance methods needed - use FlextOracleOicSettings() directly


__all__ = [
    "FlextOracleOicSettings",
]
