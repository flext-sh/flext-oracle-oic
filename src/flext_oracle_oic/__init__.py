# @generated AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic package."""

from __future__ import annotations

from typing import TYPE_CHECKING

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
    from flext_auth import d as d
    from flext_auth import e as e
    from flext_auth import h as h
    from flext_auth import r as r
    from flext_auth import x as x

    from ._config import FlextOracleOicConfig as FlextOracleOicConfig
    from ._config import config as config
    from ._settings import FlextOracleOicSettings as FlextOracleOicSettings
    from ._settings import settings as settings
    from .api import FlextOracleOicApi as FlextOracleOicApi
    from .api import oracle_oic as oracle_oic
    from .constants import FlextOracleOicConstants as FlextOracleOicConstants

    c: type[FlextOracleOicConstants]
    from .main import FlextOracleOicCli as FlextOracleOicCli
    from .main import main as main
    from .models import FlextOracleOicModels as FlextOracleOicModels

    m: type[FlextOracleOicModels]
    from .protocols import FlextOracleOicProtocols as FlextOracleOicProtocols

    p: type[FlextOracleOicProtocols]
    from .service import FlextOracleOicService as FlextOracleOicService
    from .service import s as s
    from .typings import FlextOracleOicTypes as FlextOracleOicTypes

    t: type[FlextOracleOicTypes]
    from .utilities import FlextOracleOicUtilities as FlextOracleOicUtilities

    u: type[FlextOracleOicUtilities]

_LAZY_MODULES: dict[str, tuple[str, ...]] = {
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
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES, alias_groups=_LAZY_ALIAS_GROUPS, sort_keys=False
)

_PUBLIC_EXPORTS: tuple[str, ...] = (
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

__all__: tuple[str, ...] = tuple(_PUBLIC_EXPORTS)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
