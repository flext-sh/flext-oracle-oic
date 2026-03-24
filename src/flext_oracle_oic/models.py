"""Models for Oracle OIC External operations.

This module provides data models for Oracle OIC External operations.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Annotated, ClassVar

from flext_core import FlextModels
from pydantic import ConfigDict, Field, SecretStr

from flext_oracle_oic.constants import c
from flext_oracle_oic.typings import t


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

            model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")

            oauth_client_id: Annotated[str, Field(description="IDCS OAuth2 client ID")]
            oauth_client_secret: Annotated[
                SecretStr,
                Field(description="IDCS OAuth2 client secret"),
            ]
            oauth_token_url: Annotated[
                str,
                Field(description="IDCS OAuth2 token endpoint"),
            ]
            oauth_client_aud: Annotated[
                str | None,
                Field(
                    default=None,
                    description="OAuth2 audience",
                ),
            ]
            oauth_scope: Annotated[str, Field(default="", description="OAuth2 scope")]

        class OICConnectionConfig(FlextModels.Value):
            """Oracle Integration Cloud connection configuration.

            EXTENSION Pattern: Value Object for connection configuration
            Oracle OIC with enterprise validation.
            """

            model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")

            base_url: Annotated[str, Field(description="Oracle OIC instance base URL")]
            api_version: Annotated[
                str,
                Field(
                    default=c.OracleOic.DEFAULT_API_VERSION,
                    description="OIC API version",
                ),
            ]
            request_timeout: Annotated[
                int,
                Field(
                    default=c.DEFAULT_TIMEOUT_SECONDS,
                    ge=c.OracleOic.MIN_REQUEST_TIMEOUT,
                    description="Request timeout in seconds",
                ),
            ]
            max_retries: Annotated[
                int,
                Field(
                    default=c.DEFAULT_MAX_RETRY_ATTEMPTS,
                    ge=c.OracleOic.MIN_MAX_RETRIES,
                    description="Maximum retry attempts",
                ),
            ]
            verify_ssl: Annotated[
                bool,
                Field(
                    default=c.OracleOic.DEFAULT_VERIFY_SSL,
                    description="Verify SSL certificates",
                ),
            ]

        class OICIntegrationInfo(FlextModels.Entity):
            """Oracle OIC Integration information.

            EXTENSION Pattern: Value Object representing information
            for an Oracle OIC integration.
            """

            model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")

            integration_id: Annotated[
                str,
                Field(description="Integration unique identifier"),
            ]
            name: Annotated[str, Field(description="Integration name")]
            status: Annotated[str, Field(description="Integration status")]
            integration_version: Annotated[
                str,
                Field(description="Integration version"),
            ]
            description: Annotated[
                str,
                Field(default="", description="Integration description"),
            ]
            created_by: Annotated[
                str,
                Field(default="", description="Creator username"),
            ]
            last_updated: Annotated[
                str,
                Field(default="", description="Last update timestamp"),
            ]

        class OICConnectionInfo(FlextModels.Entity):
            """Oracle OIC Connection information.

            EXTENSION Pattern: Value Object representing information
            for an Oracle OIC connection.
            """

            model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")

            connection_id: Annotated[
                str,
                Field(description="Connection unique identifier"),
            ]
            name: Annotated[str, Field(description="Connection name")]
            adapter_type: Annotated[str, Field(description="Adapter type")]
            status: Annotated[str, Field(description="Connection status")]
            connection_type: Annotated[str, Field(description="Connection type")]
            description: Annotated[
                str,
                Field(default="", description="Connection description"),
            ]

        class IntegrationStatus(FlextModels.Entity):
            """Oracle OIC Integration status information.

            EXTENSION Pattern: Value Object representing status
            for an Oracle OIC integration.
            """

            model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")

            integration_id: Annotated[
                str,
                Field(description="Integration unique identifier"),
            ]
            integration_version: Annotated[
                str,
                Field(description="Integration version"),
            ]
            status: Annotated[str, Field(description="Integration status")]
            last_updated: Annotated[
                str,
                Field(default="", description="Last update timestamp"),
            ]
            activated_by: Annotated[
                str,
                Field(
                    default="",
                    description="User who activated the integration",
                ),
            ]

        class MessageRouterPatternConfig(FlextModels.Value):
            """Message router pattern configuration model."""

            model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")

            message_data: Annotated[
                t.ContainerMapping,
                Field(description="Message payload used for routing"),
            ]
            routing_rules: Annotated[
                Sequence[t.ContainerMapping],
                Field(description="Ordered routing rules"),
            ]

        class ScatterGatherPatternConfig(FlextModels.Value):
            """Scatter-gather pattern configuration model."""

            model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")

            request_data: Annotated[
                t.ContainerMapping,
                Field(description="Request payload to scatter"),
            ]
            target_services: Annotated[
                Sequence[str],
                Field(description="Target service endpoints"),
            ]
            aggregation_strategy: Annotated[
                str,
                Field(description="Aggregation behavior for gathered responses"),
            ] = "collect_all"

        class RequestParams(FlextModels.Value):
            """Parameters for OIC API request.

            EXTENSION Pattern: Value Object for request parameters
            Oracle OIC API com tipagem forte.
            """

            model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")

            method: Annotated[str, Field(description="HTTP method")]
            url: Annotated[str, Field(description="Request URL")]
            params: Annotated[
                Mapping[str, str | int | float] | None,
                Field(
                    default=None,
                    description="Query parameters",
                ),
            ]
            data: Annotated[
                t.ContainerMapping | None,
                Field(
                    default=None,
                    description="Form data",
                ),
            ]
            json_data: Annotated[
                t.ContainerMapping | None,
                Field(
                    default=None,
                    description="JSON data",
                ),
            ]
            headers: Annotated[
                Mapping[str, str] | None,
                Field(
                    default=None,
                    description="HTTP headers",
                ),
            ]


m = FlextOracleOicModels

__all__ = ["FlextOracleOicModels", "m"]
