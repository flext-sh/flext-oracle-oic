# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic. Protocols package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_oracle_oic._protocols.base import FlextOracleOicProtocolsBase
    from flext_oracle_oic._protocols.config import FlextOracleOicProtocolsConfig
    from flext_oracle_oic._protocols.domain import (
        FlextOracleOicProtocolsDomain,
        HTTPClient,
        ServiceRules,
    )


__all__: tuple[str, ...] = (
    "FlextOracleOicProtocolsBase",
    "FlextOracleOicProtocolsConfig",
    "FlextOracleOicProtocolsDomain",
    "HTTPClient",
    "ServiceRules",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextOracleOicProtocolsBase": ".base",
        "FlextOracleOicProtocolsConfig": ".config",
        "FlextOracleOicProtocolsDomain": ".domain",
        "HTTPClient": ".domain",
        "ServiceRules": ".domain",
    }),
    public_exports=__all__,
)
