# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import build_lazy_import_map, install_lazy_exports
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

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            "._config": ("FlextOracleOicConfig", "config"),
            "._settings": ("FlextOracleOicSettings", "settings"),
            ".api": ("FlextOracleOicApi", "oracle_oic"),
            ".constants": ("FlextOracleOicConstants", "c"),
            ".ext_client": ("FlextOracleOicClient",),
            ".main": ("FlextOracleOicCli", "main"),
            ".models": ("FlextOracleOicModels", "m"),
            ".protocols": ("FlextOracleOicProtocols", "p"),
            ".service": ("FlextOracleOicService", "s"),
            ".services": ("services",),
            ".services.auth": ("FlextOracleOicAuthMixin",),
            ".services.base": ("FlextOracleOicServiceBase",),
            ".services.integration_crud": ("FlextOracleOicIntegrationCrudMixin",),
            ".services.integration_lifecycle": (
                "FlextOracleOicIntegrationLifecycleMixin",
            ),
            ".services.monitoring": ("FlextOracleOicMonitoringMixin",),
            ".services.orchestration": ("FlextOracleOicOrchestrationMixin",),
            ".typings": ("FlextOracleOicTypes", "t"),
            ".utilities": ("FlextOracleOicUtilities", "u"),
            "flext_auth": ("d", "e", "h", "r", "x"),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    ),
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
