"""Oracle OIC integration, connection and authentication models.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated

from flext_auth import FlextAuthModels

from flext_oracle_oic import c, t


class FlextOracleOicModelsDomain:
    """Oracle OIC domain models composed into ``m.OracleOic``."""

    class OICAuthConfig(FlextAuthModels.Value):
        """Oracle Integration Cloud authentication configuration.

        EXTENSION Pattern: Value Object for authentication configuration
        Oracle OIC with validation and security.
        """

        oauth_client_id: Annotated[
            str,
            m.Field(description="IDCS OAuth2 client ID"),
        ]
        oauth_client_secret: Annotated[
            t.SecretStr,
            m.Field(description="IDCS OAuth2 client secret"),
        ]
        oauth_token_url: Annotated[
            str,
            m.Field(description="IDCS OAuth2 token endpoint"),
        ]
        oauth_client_aud: Annotated[
            str | None,
            m.Field(description="OAuth2 audience"),
        ] = None
        oauth_scope: Annotated[str, m.Field(description="OAuth2 scope")] = ""

    class OICConnectionConfig(FlextAuthModels.Value):
        """Oracle Integration Cloud connection configuration.

        EXTENSION Pattern: Value Object for connection configuration
        Oracle OIC with enterprise validation.
        """

        base_url: Annotated[
            str,
            m.Field(description="Oracle OIC instance base URL"),
        ]
        api_version: Annotated[str, m.Field(description="OIC API version")] = (
            c.OracleOic.DEFAULT_API_VERSION
        )
        request_timeout: Annotated[
            t.PositiveInt,
            m.Field(description="Request timeout in seconds"),
        ] = c.DEFAULT_TIMEOUT_SECONDS
        max_retries: Annotated[
            t.RetryCount,
            m.Field(description="Maximum retry attempts"),
        ] = c.MAX_RETRY_ATTEMPTS
        verify_ssl: Annotated[
            bool,
            m.Field(description="Verify SSL certificates"),
        ] = c.OracleOic.DEFAULT_VERIFY_SSL

    class OICIntegrationInfo(FlextAuthModels.Entity):
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
            str,
            m.Field(description="Integration description"),
        ] = ""
        created_by: Annotated[str, m.Field(description="Creator username")] = ""
        last_updated: Annotated[
            str,
            m.Field(description="Last update timestamp"),
        ] = ""

    class OICConnectionInfo(FlextAuthModels.Entity):
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
            str,
            m.Field(description="Connection description"),
        ] = ""

    class IntegrationStatus(FlextAuthModels.Entity):
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
            str,
            m.Field(description="Last update timestamp"),
        ] = ""
        activated_by: Annotated[
            str,
            m.Field(description="User who activated the integration"),
        ] = ""


__all__: list[str] = ["FlextOracleOicModelsDomain"]
