"""Oracle OIC Extension Models - EXTENSION Pattern.

Este módulo estabelece o padrão EXTENSION PEP8 para modelos
de dados Oracle OIC. Serve como modelo para futuras extensions.
"""

from __future__ import annotations

from dataclasses import dataclass

from flext_core import FlextLogger, FlextModels
from pydantic import ConfigDict, Field, SecretStr

logger = FlextLogger(__name__)


# ================================
# EXTENSION Pattern: Domain Models
# ================================


class OICAuthConfig(FlextModels):
    """Oracle Integration Cloud authentication configuration.

    Padrão EXTENSION: Value Object para configuração de autenticação
    Oracle OIC com validação e segurança.
    """

    model_config = ConfigDict(extra="forbid")

    oauth_client_id: str = Field(..., description="IDCS OAuth2 client ID")
    oauth_client_secret: SecretStr = Field(..., description="IDCS OAuth2 client secret")
    oauth_token_url: str = Field(..., description="IDCS OAuth2 token endpoint")
    oauth_client_aud: str | None = Field(None, description="OAuth2 audience")
    oauth_scope: str = Field("", description="OAuth2 scope")


class OICConnectionConfig(FlextModels):
    """Oracle Integration Cloud connection configuration.

    Padrão EXTENSION: Value Object para configuração de conexão
    Oracle OIC com validação enterprise.
    """

    model_config = ConfigDict(extra="forbid")

    base_url: str = Field(..., description="Oracle OIC instance base URL")
    api_version: str = Field("v1", description="OIC API version")
    request_timeout: int = Field(30, ge=1, description="Request timeout in seconds")
    max_retries: int = Field(3, ge=0, description="Maximum retry attempts")
    verify_ssl: bool = Field(default=True, description="Verify SSL certificates")


class OICIntegrationInfo(FlextModels):
    """Oracle OIC Integration information.

    Padrão EXTENSION: Value Object representando informações
    de uma integração Oracle OIC.
    """

    model_config = ConfigDict(extra="forbid")

    integration_id: str = Field(..., description="Integration unique identifier")
    name: str = Field(..., description="Integration name")
    status: str = Field(..., description="Integration status")
    version: str = Field(..., description="Integration version")
    description: str = Field("", description="Integration description")
    created_by: str = Field("", description="Creator username")
    last_updated: str = Field("", description="Last update timestamp")


class OICConnectionInfo(FlextModels):
    """Oracle OIC Connection information.

    Padrão EXTENSION: Value Object representando informações
    de uma conexão Oracle OIC.
    """

    model_config = ConfigDict(extra="forbid")

    connection_id: str = Field(..., description="Connection unique identifier")
    name: str = Field(..., description="Connection name")
    adapter_type: str = Field(..., description="Adapter type")
    status: str = Field(..., description="Connection status")
    connection_type: str = Field(..., description="Connection type")
    description: str = Field("", description="Connection description")


@dataclass
class RequestParams:
    """Parameters for OIC API request.

    Padrão EXTENSION: Dataclass para parâmetros de requisição
    Oracle OIC API com tipagem forte.
    """

    method: str
    url: str
    params: dict[str, str | int | float] | None = None
    data: dict[str, object] | None = None
    json_data: dict[str, object] | None = None
    headers: dict[str, str] | None = None
    timeout: int = 30


# Exports seguindo padrão EXTENSION
__all__: list[str] = [
    # Configuration models
    "OICAuthConfig",
    "OICConnectionConfig",
    "OICConnectionInfo",
    # Business models
    "OICIntegrationInfo",
    # Request models
    "RequestParams",
]
