# AUTO-GENERATED FILE — Regenerate with: make gen
"""Models for Oracle OIC External operations.

This module provides data models for Oracle OIC External operations.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_auth import FlextAuthModels

from flext_oracle_oic._models import (
    FlextOracleOicModelsConfig,
    FlextOracleOicModelsDomain,
    domain as _domain,
)


class FlextOracleOicModels(FlextAuthModels):
    """Unified models for Oracle OIC Extension operations.

    Extends m to avoid duplication and ensure consistency.
    This class consolidates all Oracle OIC Extension domain models following
    the [Project]Models pattern for centralized Pydantic validation.
    """

    class OracleOic(FlextOracleOicModelsConfig, FlextOracleOicModelsDomain):
        """OracleOic domain namespace."""

        OICAuthConfig = _domain.OICAuthConfig
        OICConnectionConfig = _domain.OICConnectionConfig
        OICIntegrationInfo = _domain.OICIntegrationInfo
        OICConnectionInfo = _domain.OICConnectionInfo
        IntegrationStatus = _domain.IntegrationStatus


m = FlextOracleOicModels

__all__: list[str] = ["FlextOracleOicModels", "m"]
