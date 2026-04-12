"""Oracle OIC protocols for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_core import FlextProtocols
from flext_oracle_oic import t


class FlextOracleOicProtocols(FlextProtocols):
    """Oracle OIC Extension protocols extending p with Oracle OIC-specific interfaces."""

    @runtime_checkable
    class OracleOic(Protocol):
        """OracleOic domain namespace."""

        @runtime_checkable
        class HTTPClient(FlextProtocols.Service[t.RecursiveContainer], Protocol):
            """Protocol for HTTP client operations used by Oracle OIC services."""

            def delete(
                self,
                url: str,
                *,
                headers: t.StrMapping | None = None,
            ) -> FlextProtocols.Result[bool]:
                """Execute HTTP DELETE request."""
                ...

            def get(
                self,
                url: str,
                *,
                headers: t.StrMapping | None = None,
            ) -> FlextProtocols.Result[t.RecursiveContainer]:
                """Execute HTTP GET request."""
                ...

            def post(
                self,
                url: str,
                data: t.RecursiveContainerMapping | None = None,
                *,
                headers: t.StrMapping | None = None,
            ) -> FlextProtocols.Result[t.RecursiveContainer]:
                """Execute HTTP POST request."""
                ...

            def put(
                self,
                url: str,
                data: t.RecursiveContainerMapping | None = None,
                *,
                headers: t.StrMapping | None = None,
            ) -> FlextProtocols.Result[t.RecursiveContainer]:
                """Execute HTTP PUT request."""
                ...


p = FlextOracleOicProtocols
__all__: list[str] = ["FlextOracleOicProtocols", "p"]
