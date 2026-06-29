# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports
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
    from flext_auth import d as d, e as e, h as h, r as r, x as x

    from flext_oracle_oic.api import (
        FlextOracleOicApi as FlextOracleOicApi,
        oracle_oic as oracle_oic,
    )
    from flext_oracle_oic.constants import (
        FlextOracleOicConstants as FlextOracleOicConstants,
        c as c,
    )
    from flext_oracle_oic.main import (
        FlextOracleOicCli as FlextOracleOicCli,
        main as main,
    )
    from flext_oracle_oic.models import (
        FlextOracleOicModels as FlextOracleOicModels,
        m as m,
    )
    from flext_oracle_oic.protocols import (
        FlextOracleOicProtocols as FlextOracleOicProtocols,
        p as p,
    )
    from flext_oracle_oic.service import (
        FlextOracleOicService as FlextOracleOicService,
        s as s,
    )
    from flext_oracle_oic.settings import (
        FlextOracleOicSettings as FlextOracleOicSettings,
    )
    from flext_oracle_oic.typings import (
        FlextOracleOicTypes as FlextOracleOicTypes,
        t as t,
    )
    from flext_oracle_oic.utilities import (
        FlextOracleOicUtilities as FlextOracleOicUtilities,
        u as u,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".api": (
            "FlextOracleOicApi",
            "oracle_oic",
        ),
        ".constants": (
            "FlextOracleOicConstants",
            "c",
        ),
        ".main": (
            "FlextOracleOicCli",
            "main",
        ),
        ".models": (
            "FlextOracleOicModels",
            "m",
        ),
        ".protocols": (
            "FlextOracleOicProtocols",
            "p",
        ),
        ".service": (
            "FlextOracleOicService",
            "s",
        ),
        ".settings": ("FlextOracleOicSettings",),
        ".typings": (
            "FlextOracleOicTypes",
            "t",
        ),
        ".utilities": (
            "FlextOracleOicUtilities",
            "u",
        ),
        "flext_auth": (
            "d",
            "e",
            "h",
            "r",
            "x",
        ),
    },
)


__all__: tuple[str, ...] = (
    "FlextOracleOicApi",
    "FlextOracleOicCli",
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
    "d",
    "e",
    "h",
    "m",
    "main",
    "oracle_oic",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    public_exports=__all__,
)
