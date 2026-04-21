"""Oracle OIC protocols for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import (
    Mapping,
)
from typing import Protocol, runtime_checkable

from flext_auth import p

from flext_oracle_oic import t


class FlextOracleOicProtocols(p):
    """Oracle OIC Extension protocols extending p with Oracle OIC-specific interfaces."""

    @runtime_checkable
    class OracleOic(Protocol):
        """OracleOic domain namespace."""

        @runtime_checkable
        class HTTPClient(p.Service[t.Container], Protocol):
            """Protocol for HTTP client operations used by Oracle OIC services."""

            def delete(
                self,
                url: str,
                *,
                headers: t.StrMapping | None = None,
            ) -> p.Result[bool]:
                """Execute HTTP DELETE request."""
                ...

            def get(
                self,
                url: str,
                *,
                headers: t.StrMapping | None = None,
            ) -> p.Result[t.Container]:
                """Execute HTTP GET request."""
                ...

            def post(
                self,
                url: str,
                data: Mapping[str, t.Container] | None = None,
                *,
                headers: t.StrMapping | None = None,
            ) -> p.Result[t.Container]:
                """Execute HTTP POST request."""
                ...

            def put(
                self,
                url: str,
                data: Mapping[str, t.Container] | None = None,
                *,
                headers: t.StrMapping | None = None,
            ) -> p.Result[t.Container]:
                """Execute HTTP PUT request."""
                ...


p = FlextOracleOicProtocols
__all__: list[str] = ["FlextOracleOicProtocols", "p"]
