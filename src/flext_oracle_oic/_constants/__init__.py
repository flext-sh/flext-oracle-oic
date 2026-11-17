# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic. Constants package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_oracle_oic._constants.base import FlextOracleOicConstantsBase
    from flext_oracle_oic._constants.values import FlextOracleOicConstantsValues


__all__: tuple[str, ...] = (
    "FlextOracleOicConstantsBase",
    "FlextOracleOicConstantsValues",
)

install_lazy_exports(
    __name__,
    globals(),
    {
        "FlextOracleOicConstantsBase": ".base",
        "FlextOracleOicConstantsValues": ".values",
    },
    public_exports=__all__,
    deferred_members={
        "FlextOracleOicConstantsBase": (
            "DEFAULT_BASE_URL",
            "DEFAULT_TOKEN_URL",
        ),
        "FlextOracleOicConstantsValues": (
            "DEFAULT_API_VERSION",
            "DEFAULT_PAGE_SIZE",
            "MIN_PAGE_SIZE",
            "MIN_REQUEST_TIMEOUT",
            "DEFAULT_VERIFY_SSL",
            "Auth",
            "OICApiVersion",
            "Integration",
            "Connection",
            "Monitoring",
            "API",
            "OracleOicValidation",
            "Cli",
        ),
    },
)
