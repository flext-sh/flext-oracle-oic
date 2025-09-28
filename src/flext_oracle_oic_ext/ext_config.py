"""Oracle OIC Extension Configuration Classes.

Legacy configuration classes for backward compatibility.
These classes provide the expected API for existing tests and integrations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import ConfigDict, Field

from flext_core import FlextConfig
from flext_oracle_oic_ext.models import FlextOracleOicExtModels


class OICExtensionAuthConfig(FlextOracleOicExtModels.OICAuthConfig):
    """Legacy alias for OICAuthConfig for backward compatibility."""


class OICExtensionConnectionConfig(FlextOracleOicExtModels.OICConnectionConfig):
    """Legacy alias for OICConnectionConfig for backward compatibility."""


class OracleOICExtensionSettings(FlextConfig):
    """Oracle OIC Extension settings with nested connection and auth configs.

    This class provides the expected API for existing tests and integrations.
    """

    model_config = ConfigDict(extra="forbid")

    # Nested configurations
    connection: OICExtensionConnectionConfig = Field(
        default_factory=OICExtensionConnectionConfig,
        description="Oracle OIC connection configuration"
    )

    auth: OICExtensionAuthConfig = Field(
        default_factory=OICExtensionAuthConfig,
        description="Oracle OIC authentication configuration"
    )

    # Feature flags
    enable_monitoring: bool = Field(
        default=True,
        description="Enable monitoring features"
    )

    enable_enterprise_patterns: bool = Field(
        default=True,
        description="Enable enterprise patterns"
    )

    enable_orchestration: bool = Field(
        default=True,
        description="Enable orchestration features"
    )
