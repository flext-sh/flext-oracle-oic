# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic. Models package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_oracle_oic._models.config import FlextOracleOicModelsConfig
    from flext_oracle_oic._models.domain import (
        FlextOracleOicModelsDomain,
        IntegrationStatus,
        OICAuthConfig,
        OICConnectionConfig,
        OICConnectionInfo,
        OICIntegrationInfo,
    )


__all__: tuple[str, ...] = (
    "FlextOracleOicModelsConfig",
    "FlextOracleOicModelsDomain",
    "IntegrationStatus",
    "OICAuthConfig",
    "OICConnectionConfig",
    "OICConnectionInfo",
    "OICIntegrationInfo",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextOracleOicModelsConfig": ".config",
        "FlextOracleOicModelsDomain": ".domain",
        "IntegrationStatus": ".domain",
        "OICAuthConfig": ".domain",
        "OICConnectionConfig": ".domain",
        "OICConnectionInfo": ".domain",
        "OICIntegrationInfo": ".domain",
    }),
    public_exports=__all__,
)
