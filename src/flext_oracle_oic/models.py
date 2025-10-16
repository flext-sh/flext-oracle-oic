"""Models for Oracle OIC External operations.

This module provides data models for Oracle OIC External operations.
"""

from __future__ import annotations

from flext_core import FlextModels, FlextTypes
from pydantic import ConfigDict, Field, SecretStr

from flext_oracle_oic.constants import FlextOracleOicConstants


class FlextOracleOicModels(FlextModels):
    """Unified models for Oracle OIC Extension operations.

    Extends FlextModels to avoid duplication and ensure consistency.
    This class consolidates all Oracle OIC Extension domain models following
    the [Project]Models pattern for centralized Pydantic validation.
    """

    # Legacy type aliases for backward compatibility
    OicRecord = FlextTypes.Dict
    OicRecords = list[OicRecord]

    class OICAuthConfig(FlextModels.Value):
        """Oracle Integration Cloud authentication configuration.

        Padrão EXTENSION: Value Object para configuração de autenticação
        Oracle OIC com validação e segurança.
        """

        model_config = ConfigDict(extra="forbid")

        oauth_client_id: str = Field(description="IDCS OAuth2 client ID")
        oauth_client_secret: SecretStr = Field(description="IDCS OAuth2 client secret")
        oauth_token_url: str = Field(description="IDCS OAuth2 token endpoint")
        oauth_client_aud: str | None = Field(
            default=None, description="OAuth2 audience"
        )
        oauth_scope: str = Field(default="", description="OAuth2 scope")

    class OICConnectionConfig(FlextModels.Value):
        """Oracle Integration Cloud connection configuration.

        Padrão EXTENSION: Value Object para configuração de conexão
        Oracle OIC com validação enterprise.
        """

        model_config = ConfigDict(extra="forbid")

        base_url: str = Field(description="Oracle OIC instance base URL")
        api_version: str = Field(
            default=FlextOracleOicConstants.OIC.DEFAULT_API_VERSION,
            description="OIC API version",
        )
        request_timeout: int = Field(
            default=FlextOracleOicConstants.OIC.DEFAULT_REQUEST_TIMEOUT,
            ge=FlextOracleOicConstants.OIC.MIN_REQUEST_TIMEOUT,
            description="Request timeout in seconds",
        )
        max_retries: int = Field(
            default=FlextOracleOicConstants.OIC.DEFAULT_MAX_RETRIES,
            ge=FlextOracleOicConstants.OIC.MIN_MAX_RETRIES,
            description="Maximum retry attempts",
        )
        verify_ssl: bool = Field(
            default=FlextOracleOicConstants.OIC.DEFAULT_VERIFY_SSL,
            description="Verify SSL certificates",
        )

    class OICIntegrationInfo(FlextModels.Entity):
        """Oracle OIC Integration information.

        Padrão EXTENSION: Value Object representando informações
        de uma integração Oracle OIC.
        """

        model_config = ConfigDict(extra="forbid")

        integration_id: str = Field(description="Integration unique identifier")
        name: str = Field(description="Integration name")
        status: str = Field(description="Integration status")
        integration_version: str = Field(description="Integration version")
        description: str = Field(default="", description="Integration description")
        created_by: str = Field(default="", description="Creator username")
        last_updated: str = Field(default="", description="Last update timestamp")

    class OICConnectionInfo(FlextModels.Entity):
        """Oracle OIC Connection information.

        Padrão EXTENSION: Value Object representando informações
        de uma conexão Oracle OIC.
        """

        model_config = ConfigDict(extra="forbid")

        connection_id: str = Field(description="Connection unique identifier")
        name: str = Field(description="Connection name")
        adapter_type: str = Field(description="Adapter type")
        status: str = Field(description="Connection status")
        connection_type: str = Field(description="Connection type")
        description: str = Field(default="", description="Connection description")

    class IntegrationStatus(FlextModels.Entity):
        """Oracle OIC Integration status information.

        Padrão EXTENSION: Value Object representando status
        de uma integração Oracle OIC.
        """

        model_config = ConfigDict(extra="forbid")

        integration_id: str = Field(description="Integration unique identifier")
        integration_version: str = Field(description="Integration version")
        status: str = Field(description="Integration status")
        last_updated: str = Field(default="", description="Last update timestamp")
        activated_by: str = Field(
            default="", description="User who activated the integration"
        )

    class RequestParams(FlextModels.Value):
        """Parameters for OIC API request.

        Padrão EXTENSION: Value Object para parâmetros de requisição
        Oracle OIC API com tipagem forte.
        """

        model_config = ConfigDict(extra="forbid")

        method: str = Field(description="HTTP method")
        url: str = Field(description="Request URL")
        params: dict[str, str | int | float] | None = Field(
            default=None, description="Query parameters"
        )
        data: FlextTypes.Dict | None = Field(default=None, description="Form data")
        json_data: FlextTypes.Dict | None = Field(default=None, description="JSON data")
        headers: FlextTypes.StringDict | None = Field(
            default=None, description="HTTP headers"
        )
        timeout: int = Field(
            default=FlextOracleOicConstants.OIC.DEFAULT_REQUEST_TIMEOUT,
            description="Request timeout in seconds",
        )
