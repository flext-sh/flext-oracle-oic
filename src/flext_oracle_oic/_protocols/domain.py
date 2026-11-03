"""Oracle OIC HTTP client and service-rules protocol contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_auth import FlextAuthProtocols

from flext_oracle_oic import t

if TYPE_CHECKING:
    from collections.abc import Sequence

    from flext_auth import p


class FlextOracleOicProtocolsDomain:
    """Oracle OIC domain protocol contracts composed into ``p.OracleOic``."""

    @runtime_checkable
    class HTTPClient(FlextAuthProtocols.Service[t.JsonValue], Protocol):
        """Protocol for HTTP client operations used by Oracle OIC services."""

        def delete(
            self,
            url: str,
            *,
            headers: Mapping[str, str] | None = None,
        ) -> p.Result[bool]:
            """Execute an HTTP DELETE request.

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
            headers: Mapping[str, str] | None = None,
        ) -> p.Result[t.JsonValue]:
            """Execute an HTTP GET request.

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
            headers: Mapping[str, str] | None = None,
        ) -> p.Result[t.JsonValue]:
            """Execute an HTTP POST request.

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
            headers: Mapping[str, str] | None = None,
        ) -> p.Result[t.JsonValue]:
            """Execute an HTTP PUT request.

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

    @runtime_checkable
    class OICAuthConfig(FlextAuthProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def oauth_client_id(self) -> str:
            """IDCS OAuth2 client ID."""
            ...

        @property
        def oauth_client_secret(self) -> t.SecretStr:
            """IDCS OAuth2 client secret."""
            ...

        @property
        def oauth_token_url(self) -> str:
            """IDCS OAuth2 token endpoint."""
            ...

        @property
        def oauth_client_aud(self) -> str | None:
            """OAuth2 audience."""
            ...

        @property
        def oauth_scope(self) -> str:
            """OAuth2 scope."""
            ...

    @runtime_checkable
    class OICConnectionConfig(FlextAuthProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def base_url(self) -> str:
            """Oracle OIC instance base URL."""
            ...

        @property
        def api_version(self) -> str:
            """OIC API version."""
            ...

        @property
        def request_timeout(self) -> t.PositiveInt:
            """Request timeout in seconds."""
            ...

        @property
        def max_retries(self) -> t.RetryCount:
            """Maximum retry attempts."""
            ...

        @property
        def verify_ssl(self) -> bool:
            """Verify SSL certificates."""
            ...

    @runtime_checkable
    class OICIntegrationInfo(FlextAuthProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def domain_events(self) -> Sequence[p.DomainEvent]:
            """List of uncommitted domain events for event sourcing."""
            ...

        @property
        def integration_id(self) -> str:
            """Integration unique identifier."""
            ...

        @property
        def name(self) -> str:
            """Integration name."""
            ...

        @property
        def status(self) -> str:
            """Integration status."""
            ...

        @property
        def integration_version(self) -> str:
            """Integration version."""
            ...

        @property
        def description(self) -> str:
            """Integration description."""
            ...

        @property
        def created_by(self) -> str:
            """Creator username."""
            ...

        @property
        def last_updated(self) -> str:
            """Last update timestamp."""
            ...

    @runtime_checkable
    class OICConnectionInfo(FlextAuthProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def domain_events(self) -> Sequence[p.DomainEvent]:
            """List of uncommitted domain events for event sourcing."""
            ...

        @property
        def connection_id(self) -> str:
            """Connection unique identifier."""
            ...

        @property
        def name(self) -> str:
            """Connection name."""
            ...

        @property
        def adapter_type(self) -> str:
            """Adapter type."""
            ...

        @property
        def status(self) -> str:
            """Connection status."""
            ...

        @property
        def connection_type(self) -> str:
            """Connection type."""
            ...

        @property
        def description(self) -> str:
            """Connection description."""
            ...

    @runtime_checkable
    class IntegrationStatus(FlextAuthProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def domain_events(self) -> Sequence[p.DomainEvent]:
            """List of uncommitted domain events for event sourcing."""
            ...

        @property
        def integration_id(self) -> str:
            """Integration unique identifier."""
            ...

        @property
        def integration_version(self) -> str:
            """Integration version."""
            ...

        @property
        def status(self) -> str:
            """Integration status."""
            ...

        @property
        def last_updated(self) -> str:
            """Last update timestamp."""
            ...

        @property
        def activated_by(self) -> str:
            """User who activated the integration."""
            ...


__all__: list[str] = ["FlextOracleOicProtocolsDomain"]
