# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from types import MappingProxyType

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

from .__version__ import __author__ as __author__
from .__version__ import __author_email__ as __author_email__
from .__version__ import __description__ as __description__
from .__version__ import __license__ as __license__
from .__version__ import __title__ as __title__
from .__version__ import __url__ as __url__
from .__version__ import __version__ as __version__
from .__version__ import __version_info__ as __version_info__

if TYPE_CHECKING:
    from flext_auth import d, e, h, r, x

    from ._config import FlextOracleOicConfig, config
    from ._settings import FlextOracleOicSettings, settings
    from .api import FlextOracleOicApi, oracle_oic
    from .constants import FlextOracleOicConstants, FlextOracleOicConstants as c
    from .main import FlextOracleOicCli, main
    from .models import FlextOracleOicModels, FlextOracleOicModels as m
    from .protocols import FlextOracleOicProtocols, FlextOracleOicProtocols as p
    from .service import FlextOracleOicService, s
    from .typings import FlextOracleOicTypes, FlextOracleOicTypes as t
    from .utilities import FlextOracleOicUtilities, FlextOracleOicUtilities as u
__all__: tuple[str, ...] = (
    "FlextOracleOicApi",
    "FlextOracleOicCli",
    "FlextOracleOicConfig",
    "FlextOracleOicConstants",
    "FlextOracleOicModels",
    "FlextOracleOicProtocols",
    "FlextOracleOicService",
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
    "settings",
    "t",
    "u",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType(
        build_lazy_import_map(
            MappingProxyType({
                "._config": ("FlextOracleOicConfig", "config"),
                "._settings": ("FlextOracleOicSettings", "settings"),
                ".api": ("FlextOracleOicApi", "oracle_oic"),
                ".constants": ("FlextOracleOicConstants", "c"),
                ".main": ("FlextOracleOicCli", "main"),
                ".models": ("FlextOracleOicModels", "m"),
                ".protocols": ("FlextOracleOicProtocols", "p"),
                ".service": ("FlextOracleOicService", "s"),
                ".typings": ("FlextOracleOicTypes", "t"),
                ".utilities": ("FlextOracleOicUtilities", "u"),
                "flext_auth": ("d", "e", "h", "r", "x"),
            }),
            alias_groups=MappingProxyType({}),
            sort_keys=False,
        )
    ),
    public_exports=__all__,
)
