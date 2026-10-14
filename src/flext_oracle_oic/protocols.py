"""Oracle OIC protocols for FLEXT ecosystem.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_auth import FlextAuthProtocols

from flext_oracle_oic import t
from flext_oracle_oic._protocols import (
    FlextOracleOicProtocolsBase,
    FlextOracleOicProtocolsConfig,
)


class FlextOracleOicProtocols(FlextAuthProtocols):
    """Oracle OIC Extension protocols extending ``p`` with OIC-specific interfaces."""

    class OracleOic(FlextOracleOicProtocolsBase, FlextOracleOicProtocolsConfig):
        """OracleOic domain namespace."""

        @runtime_checkable
        class HTTPClient(FlextAuthProtocols.Service[t.JsonValue], Protocol):
            """Protocol for HTTP client operations used by Oracle OIC services."""

            def delete(
                self,
                url: str,
                *,
                headers: t.StrMapping | None = None,
            ) -> p.Result[bool]:
                """                    Execute an HTTP DELETE request.

                Args:
                    url: Target URL.
                    headers: Optional request headers.

                Returns:
                    The resulting ``p.Result[bool]``.

"""
                ...

            def get(
                self,
                url: str,
                *,
                headers: t.StrMapping | None = None,
            ) -> p.Result[t.JsonValue]:
                """                    Execute an HTTP GET request.

                Args:
                    url: Target URL.
                    headers: Optional request headers.

                Returns:
                    The resulting ``p.Result[t.JsonValue]``.

"""
                ...

            def post(
                self,
                url: str,
                data: t.JsonMapping | None = None,
                *,
                headers: t.StrMapping | None = None,
            ) -> p.Result[t.JsonValue]:
                """                    Execute an HTTP POST request.

                Args:
                    url: Target URL.
                    data: Optional JSON payload mapping.
                    headers: Optional request headers.

                Returns:
                    The resulting ``p.Result[t.JsonValue]``.

"""
                ...

            def put(
                self,
                url: str,
                data: t.JsonMapping | None = None,
                *,
                headers: t.StrMapping | None = None,
            ) -> p.Result[t.JsonValue]:
                """                    Execute an HTTP PUT request.

                Args:
                    url: Target URL.
                    data: Optional JSON payload mapping.
                    headers: Optional request headers.

                Returns:
                    The resulting ``p.Result[t.JsonValue]``.

"""
                ...

        @runtime_checkable
        class ServiceRules(FlextAuthProtocols.Base, Protocol):
            """Protocol for an Oracle OIC service that validates its own rules.

            Declares only the ``validate_business_rules`` capability this member
            actually consumes, deliberately not extending ``p.Service`` while that
            base still carries unimplemented members (``service_info``, ``ok``,
            ``fail_op``) which would make this protocol structurally
            unsatisfiable by real services.
            """

            def validate_business_rules(self) -> p.Result[bool]:
                """Validate the service's own business rules.

                Returns:
                The resulting ``p.Result[bool]``.

                """
                ...


p = FlextOracleOicProtocols
__all__: list[str] = ["FlextOracleOicProtocols", "p"]
