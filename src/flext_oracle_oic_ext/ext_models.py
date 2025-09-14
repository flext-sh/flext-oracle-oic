"""FLEXT Module.

Copyright (c) 2025 FLEXT Team. All rights reserved. SPDX-License-Identifier: MIT Copyright (c) 2025 FLEXT Team. All rights reserved. SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from dataclasses import dataclass

from flext_core import FlextLogger, FlextTypes
from pydantic import BaseModel, ConfigDict, Field, SecretStr

logger = FlextLogger(__name__)


# ================================
# EXTENSION Pattern: Domain Models
# ================================


class OICAuthConfig(BaseModel):
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


class OICConnectionConfig(BaseModel):
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


class OICIntegrationInfo(BaseModel):
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


class OICConnectionInfo(BaseModel):
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


class IntegrationStatus(BaseModel):
    """Oracle OIC Integration status information.

    Padrão EXTENSION: Value Object representando status
    de uma integração Oracle OIC.
    """

    model_config = ConfigDict(extra="forbid")

    integration_id: str = Field(..., description="Integration unique identifier")
    version: str = Field(..., description="Integration version")
    status: str = Field(..., description="Integration status")
    last_updated: str = Field("", description="Last update timestamp")
    activated_by: str = Field("", description="User who activated the integration")


@dataclass
class RequestParams:
    """Parameters for OIC API request.

    Padrão EXTENSION: Dataclass para parâmetros de requisição
    Oracle OIC API com tipagem forte.
    """

    method: str
    url: str
    params: dict[str, str | int | float] | None = None
    data: FlextTypes.Core.Dict | None = None
    json_data: FlextTypes.Core.Dict | None = None
    headers: FlextTypes.Core.Headers | None = None
    timeout: int = 30


# Exports seguindo padrão EXTENSION
__all__: FlextTypes.Core.StringList = [
    "IntegrationStatus",
    "OICAuthConfig",
    "OICConnectionConfig",
    "OICConnectionInfo",
    "OICIntegrationInfo",
    "RequestParams",
]
