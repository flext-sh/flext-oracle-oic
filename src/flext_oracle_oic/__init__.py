# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

from .__version__ import (
    __author__ as __author__,
    __author_email__ as __author_email__,
    __description__ as __description__,
    __license__ as __license__,
    __title__ as __title__,
    __url__ as __url__,
    __version__ as __version__,
    __version_info__ as __version_info__,
)

if TYPE_CHECKING:
    from enum import StrEnum, unique
    from typing import TYPE_CHECKING, Final

    from flext_auth import d, e, h, r, x

    from . import services as services
    from ._config import FlextOracleOicConfig, config
    from ._settings import FlextOracleOicSettings, settings
    from .api import FlextOracleOicApi, oracle_oic
    from .constants import FlextOracleOicConstants, FlextOracleOicConstants as c
    from .ext_client import FlextOracleOicClient
    from .main import FlextOracleOicCli, main
    from .models import FlextOracleOicModels, FlextOracleOicModels as m
    from .protocols import FlextOracleOicProtocols, FlextOracleOicProtocols as p
    from .service import FlextOracleOicService, s
    from .services.auth import FlextOracleOicAuthMixin
    from .services.base import FlextOracleOicServiceBase
    from .services.integration_crud import FlextOracleOicIntegrationCrudMixin
    from .services.integration_lifecycle import FlextOracleOicIntegrationLifecycleMixin
    from .services.monitoring import FlextOracleOicMonitoringMixin
    from .services.orchestration import FlextOracleOicOrchestrationMixin
    from .typings import FlextOracleOicTypes, FlextOracleOicTypes as t
    from .utilities import FlextOracleOicUtilities, FlextOracleOicUtilities as u
__all__: tuple[str, ...] = (
    "TYPE_CHECKING",
    "Final",
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
    "MappingProxyType",
    "StrEnum",
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
    "unique",
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
            "enum": ("StrEnum", "unique"),
            "flext_auth": ("d", "e", "h", "r", "x"),
            "types": ("MappingProxyType",),
            "typing": ("Final", "TYPE_CHECKING"),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
