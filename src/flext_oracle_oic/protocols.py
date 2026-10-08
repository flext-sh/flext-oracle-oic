"""Oracle OIC protocols for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_auth import FlextAuthProtocols

from flext_oracle_oic import t
from flext_oracle_oic._protocols.config import FlextOracleOicProtocolsConfig


class FlextOracleOicProtocols(FlextAuthProtocols):
    """Oracle OIC Extension protocols extending ``p`` with OIC-specific interfaces."""

    class OracleOic(FlextOracleOicProtocolsConfig):
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
                """Execute HTTP DELETE request."""
                ...

            def get(
                self,
                url: str,
                *,
                headers: t.StrMapping | None = None,
            ) -> p.Result[t.JsonValue]:
                """Execute HTTP GET request."""
                ...

            def post(
                self,
                url: str,
                data: t.JsonMapping | None = None,
                *,
                headers: t.StrMapping | None = None,
            ) -> p.Result[t.JsonValue]:
                """Execute HTTP POST request."""
                ...

            def put(
                self,
                url: str,
                data: t.JsonMapping | None = None,
                *,
                headers: t.StrMapping | None = None,
            ) -> p.Result[t.JsonValue]:
                """Execute HTTP PUT request."""
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
                """Validate the service's own business rules."""
                ...


p = FlextOracleOicProtocols
__all__: list[str] = ["FlextOracleOicProtocols", "p"]
