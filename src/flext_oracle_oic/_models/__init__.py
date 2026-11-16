# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic. Models package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import defer_lazy_bases, install_lazy_exports

if TYPE_CHECKING:
    from flext_oracle_oic._models.config import FlextOracleOicModelsConfig
    from flext_oracle_oic._models.domain import FlextOracleOicModelsDomain


__all__: tuple[str, ...] = ("FlextOracleOicModelsConfig", "FlextOracleOicModelsDomain")

install_lazy_exports(
    __name__,
    globals(),
    {"FlextOracleOicModelsConfig": ".config", "FlextOracleOicModelsDomain": ".domain"},
    public_exports=__all__,
    deferred_members={
        "FlextOracleOicModelsConfig": ("FieldValidationPlan",),
        "FlextOracleOicModelsDomain": (
            "OICAuthConfig",
            "OICConnectionConfig",
            "OICIntegrationInfo",
            "OICConnectionInfo",
            "IntegrationStatus",
        ),
    },
)

defer_lazy_bases(
    __name__,
    {
        "FlextOracleOicModelsConfig": (
            ("flext_oracle_oic", "FlextOracleOicModelsConfig"),
        ),
    },
)
