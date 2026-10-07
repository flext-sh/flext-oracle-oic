# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports
from flext_oracle_oic.__version__ import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if TYPE_CHECKING:
    from flext_auth import d, e, h, r, x

    from flext_oracle_oic import services
    from flext_oracle_oic._config import FlextOracleOicConfig, config
    from flext_oracle_oic._settings import FlextOracleOicSettings, settings
    from flext_oracle_oic.api import FlextOracleOicApi, oracle_oic
    from flext_oracle_oic.constants import FlextOracleOicConstants, c
    from flext_oracle_oic.ext_client import FlextOracleOicClient
    from flext_oracle_oic.main import FlextOracleOicCli, main
    from flext_oracle_oic.models import FlextOracleOicModels, m
    from flext_oracle_oic.protocols import FlextOracleOicProtocols, p
    from flext_oracle_oic.service import FlextOracleOicService, s
    from flext_oracle_oic.services.auth import FlextOracleOicAuthMixin
    from flext_oracle_oic.services.base import FlextOracleOicServiceBase
    from flext_oracle_oic.services.integration_crud import (
        FlextOracleOicIntegrationCrudMixin,
    )
    from flext_oracle_oic.services.integration_lifecycle import (
        FlextOracleOicIntegrationLifecycleMixin,
    )
    from flext_oracle_oic.services.monitoring import FlextOracleOicMonitoringMixin
    from flext_oracle_oic.services.orchestration import FlextOracleOicOrchestrationMixin
    from flext_oracle_oic.typings import FlextOracleOicTypes, t
    from flext_oracle_oic.utilities import FlextOracleOicUtilities, u


__all__: tuple[str, ...] = (
    "FlextOracleOicApi",
    "FlextOracleOicAuthMixin",
    "FlextOracleOicCli",
    "FlextOracleOicClient",
    "FlextOracleOicConfig",
    "FlextOracleOicConstants",
    "FlextOracleOicIntegrationCrudMixin",
    "FlextOracleOicIntegrationLifecycleMixin",
    "FlextOracleOicModels",
    "FlextOracleOicMonitoringMixin",
    "FlextOracleOicOrchestrationMixin",
    "FlextOracleOicProtocols",
    "FlextOracleOicService",
    "FlextOracleOicServiceBase",
    "FlextOracleOicSettings",
    "FlextOracleOicTypes",
    "FlextOracleOicUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "config",
    "d",
    "e",
    "h",
    "m",
    "main",
    "oracle_oic",
    "p",
    "r",
    "s",
    "services",
    "settings",
    "t",
    "u",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextOracleOicApi": ".api",
        "FlextOracleOicAuthMixin": ".services.auth",
        "FlextOracleOicCli": ".main",
        "FlextOracleOicClient": ".ext_client",
        "FlextOracleOicConfig": "._config",
        "FlextOracleOicConstants": ".constants",
        "FlextOracleOicIntegrationCrudMixin": ".services.integration_crud",
        "FlextOracleOicIntegrationLifecycleMixin": ".services.integration_lifecycle",
        "FlextOracleOicModels": ".models",
        "FlextOracleOicMonitoringMixin": ".services.monitoring",
        "FlextOracleOicOrchestrationMixin": ".services.orchestration",
        "FlextOracleOicProtocols": ".protocols",
        "FlextOracleOicService": ".service",
        "FlextOracleOicServiceBase": ".services.base",
        "FlextOracleOicSettings": "._settings",
        "FlextOracleOicTypes": ".typings",
        "FlextOracleOicUtilities": ".utilities",
        "c": ".constants",
        "config": "._config",
        "d": "flext_auth",
        "e": "flext_auth",
        "h": "flext_auth",
        "m": ".models",
        "main": ".main",
        "oracle_oic": ".api",
        "p": ".protocols",
        "r": "flext_auth",
        "s": ".service",
        "services": ".services",
        "settings": "._settings",
        "t": ".typings",
        "u": ".utilities",
        "x": "flext_auth",
    }),
    public_exports=__all__,
)
