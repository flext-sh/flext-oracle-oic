"""Oracle OIC HTTP client and service-rules protocol contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime
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
    class OICAuthConfig(FlextAuthProtocols.BaseModel, Protocol):
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
    class OICConnectionConfig(FlextAuthProtocols.BaseModel, Protocol):
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
    class OICIntegrationInfo(FlextAuthProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        version: t.NonNegativeInt
        unique_id: t.NonEmptyStr

        @property
        def created_at(self) -> datetime:
            """Creation timestamp (configured timezone)."""
            ...

        updated_at: datetime | None

        @property
        def domain_events(self) -> Sequence[p.DomainEvent]:
            """List of uncommitted domain events for event sourcing."""
            ...

        integration_id: str
        name: str
        status: str
        integration_version: str
        description: str
        created_by: str
        last_updated: str

    @runtime_checkable
    class OICConnectionInfo(FlextAuthProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        version: t.NonNegativeInt
        unique_id: t.NonEmptyStr

        @property
        def created_at(self) -> datetime:
            """Creation timestamp (configured timezone)."""
            ...

        updated_at: datetime | None

        @property
        def domain_events(self) -> Sequence[p.DomainEvent]:
            """List of uncommitted domain events for event sourcing."""
            ...

        connection_id: str
        name: str
        adapter_type: str
        status: str
        connection_type: str
        description: str

    @runtime_checkable
    class IntegrationStatus(FlextAuthProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        version: t.NonNegativeInt
        unique_id: t.NonEmptyStr

        @property
        def created_at(self) -> datetime:
            """Creation timestamp (configured timezone)."""
            ...

        updated_at: datetime | None

        @property
        def domain_events(self) -> Sequence[p.DomainEvent]:
            """List of uncommitted domain events for event sourcing."""
            ...

        integration_id: str
        integration_version: str
        status: str
        last_updated: str
        activated_by: str


__all__: list[str] = ["FlextOracleOicProtocolsDomain"]
