"""Models for Oracle OIC External operations.

This module provides data models for Oracle OIC External operations.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Annotated

from pydantic import SecretStr

from flext_core import FlextModels
from flext_oracle_oic import c, t


class FlextOracleOicModels(FlextModels):
    """Unified models for Oracle OIC Extension operations.

    Extends FlextModels to avoid duplication and ensure consistency.
    This class consolidates all Oracle OIC Extension domain models following
    the [Project]Models pattern for centralized Pydantic validation.
    """

    class OracleOic:
        """OracleOic domain namespace."""

        class OICAuthConfig(FlextModels.Value):
            """Oracle Integration Cloud authentication configuration.

            EXTENSION Pattern: Value Object for authentication configuration
            Oracle OIC with validation and security.
            """

            oauth_client_id: Annotated[
                str, m.Field(description="IDCS OAuth2 client ID")
            ]
            oauth_client_secret: Annotated[
                SecretStr,
                m.Field(description="IDCS OAuth2 client secret"),
            ]
            oauth_token_url: Annotated[
                str,
                m.Field(description="IDCS OAuth2 token endpoint"),
            ]
            oauth_client_aud: Annotated[
                str | None,
                m.Field(
                    description="OAuth2 audience",
                ),
            ] = None
            oauth_scope: Annotated[str, m.Field(description="OAuth2 scope")] = ""

        class OICConnectionConfig(FlextModels.Value):
            """Oracle Integration Cloud connection configuration.

            EXTENSION Pattern: Value Object for connection configuration
            Oracle OIC with enterprise validation.
            """

            base_url: Annotated[
                str, m.Field(description="Oracle OIC instance base URL")
            ]
            api_version: Annotated[
                str,
                m.Field(
                    description="OIC API version",
                ),
            ] = c.OracleOic.DEFAULT_API_VERSION
            request_timeout: Annotated[
                t.PositiveInt,
                m.Field(
                    description="Request timeout in seconds",
                ),
            ] = c.DEFAULT_TIMEOUT_SECONDS
            max_retries: Annotated[
                t.RetryCount,
                m.Field(
                    description="Maximum retry attempts",
                ),
            ] = c.MAX_RETRY_ATTEMPTS
            verify_ssl: Annotated[
                bool,
                m.Field(
                    description="Verify SSL certificates",
                ),
            ] = c.OracleOic.DEFAULT_VERIFY_SSL

        class OICIntegrationInfo(FlextModels.Entity):
            """Oracle OIC Integration information.

            EXTENSION Pattern: Value Object representing information
            for an Oracle OIC integration.
            """

            integration_id: Annotated[
                str,
                m.Field(description="Integration unique identifier"),
            ]
            name: Annotated[str, m.Field(description="Integration name")]
            status: Annotated[str, m.Field(description="Integration status")]
            integration_version: Annotated[
                str,
                m.Field(description="Integration version"),
            ]
            description: Annotated[
                str, m.Field(description="Integration description")
            ] = ""
            created_by: Annotated[str, m.Field(description="Creator username")] = ""
            last_updated: Annotated[
                str, m.Field(description="Last update timestamp")
            ] = ""

        class OICConnectionInfo(FlextModels.Entity):
            """Oracle OIC Connection information.

            EXTENSION Pattern: Value Object representing information
            for an Oracle OIC connection.
            """

            connection_id: Annotated[
                str,
                m.Field(description="Connection unique identifier"),
            ]
            name: Annotated[str, m.Field(description="Connection name")]
            adapter_type: Annotated[str, m.Field(description="Adapter type")]
            status: Annotated[str, m.Field(description="Connection status")]
            connection_type: Annotated[str, m.Field(description="Connection type")]
            description: Annotated[
                str, m.Field(description="Connection description")
            ] = ""

        class IntegrationStatus(FlextModels.Entity):
            """Oracle OIC Integration status information.

            EXTENSION Pattern: Value Object representing status
            for an Oracle OIC integration.
            """

            integration_id: Annotated[
                str,
                m.Field(description="Integration unique identifier"),
            ]
            integration_version: Annotated[
                str,
                m.Field(description="Integration version"),
            ]
            status: Annotated[str, m.Field(description="Integration status")]
            last_updated: Annotated[
                str, m.Field(description="Last update timestamp")
            ] = ""
            activated_by: Annotated[
                str,
                m.Field(
                    description="User who activated the integration",
                ),
            ] = ""

        class MessageRouterPatternConfig(FlextModels.Value):
            """Message router pattern configuration model."""

            message_data: Annotated[
                t.RecursiveContainerMapping,
                m.Field(description="Message payload used for routing"),
            ]
            routing_rules: Annotated[
                Sequence[t.RecursiveContainerMapping],
                m.Field(description="Ordered routing rules"),
            ]

        class ScatterGatherPatternConfig(FlextModels.Value):
            """Scatter-gather pattern configuration model."""

            request_data: Annotated[
                t.RecursiveContainerMapping,
                m.Field(description="Request payload to scatter"),
            ]
            target_services: Annotated[
                t.StrSequence,
                m.Field(description="Target service endpoints"),
            ]
            aggregation_strategy: Annotated[
                str,
                m.Field(description="Aggregation behavior for gathered responses"),
            ] = "collect_all"

        class RequestParams(FlextModels.Value):
            """Parameters for OIC API request.

            EXTENSION Pattern: Value Object for request parameters
            Oracle OIC API com tipagem forte.
            """

            method: Annotated[str, m.Field(description="HTTP method")]
            url: Annotated[str, m.Field(description="Request URL")]
            params: Annotated[
                t.ConfigValueMapping | None,
                m.Field(
                    description="Query parameters",
                ),
            ] = None
            data: Annotated[
                t.RecursiveContainerMapping | None,
                m.Field(
                    description="Form data",
                ),
            ] = None
            json_data: Annotated[
                t.RecursiveContainerMapping | None,
                m.Field(
                    description="JSON data",
                ),
            ] = None
            headers: Annotated[
                t.StrMapping | None,
                m.Field(
                    description="HTTP headers",
                ),
            ] = None


m = FlextOracleOicModels

__all__: list[str] = ["FlextOracleOicModels", "m"]
