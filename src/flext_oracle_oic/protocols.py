# AUTO-GENERATED FILE — Regenerate with: make gen
"""Oracle OIC protocols for FLEXT ecosystem.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_auth import p

from flext_oracle_oic._protocols import (
    FlextOracleOicProtocolsBase,
    FlextOracleOicProtocolsConfig,
    FlextOracleOicProtocolsDomain,
)


class FlextOracleOicProtocols(p):
    """Oracle OIC Extension protocols extending ``p`` with OIC-specific interfaces."""

    class OracleOic(
        FlextOracleOicProtocolsBase,
        FlextOracleOicProtocolsConfig,
        FlextOracleOicProtocolsDomain,
    ):
        """OracleOic domain namespace."""


p = FlextOracleOicProtocols
__all__: list[str] = ["FlextOracleOicProtocols", "p"]
