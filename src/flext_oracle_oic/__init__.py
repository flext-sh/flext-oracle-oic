# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT Oracle OIC Extension - EXTENSION Pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

from flext_oracle_oic.__version__ import (
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
    from flext_oracle_oic import (
        api as api,
        constants as constants,
        ext_client as ext_client,
        ext_services as ext_services,
        models as models,
        protocols as protocols,
        service as service,
        settings as settings,
        typings as typings,
        utilities as utilities,
    )
    from flext_oracle_oic.api import FlextOracleOicApi as FlextOracleOicApi
    from flext_oracle_oic.constants import (
        FlextOracleOicConstants as FlextOracleOicConstants,
        FlextOracleOicConstants as c,
    )
    from flext_oracle_oic.ext_client import FlextOracleOicClient as FlextOracleOicClient
    from flext_oracle_oic.ext_services import (
        FlextOracleOicExtServices as FlextOracleOicExtServices,
        logger as logger,
    )
    from flext_oracle_oic.main import (
        FlextOracleOicCli as FlextOracleOicCli,
        main as main,
    )
    from flext_oracle_oic.models import (
        FlextOracleOicModels as FlextOracleOicModels,
        FlextOracleOicModels as m,
    )
    from flext_oracle_oic.protocols import (
        FlextOracleOicProtocols as FlextOracleOicProtocols,
        FlextOracleOicProtocols as p,
    )
    from flext_oracle_oic.service import (
        FlextOracleOicService as FlextOracleOicService,
        FlextOracleOicService as s,
    )
    from flext_oracle_oic.settings import (
        FlextOracleOicSettings as FlextOracleOicSettings,
    )
    from flext_oracle_oic.typings import (
        FlextOracleOicTypes as FlextOracleOicTypes,
        FlextOracleOicTypes as t,
    )
    from flext_oracle_oic.utilities import (
        FlextOracleOicUtilities as FlextOracleOicUtilities,
        FlextOracleOicUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextOracleOicApi": ["flext_oracle_oic.api", "FlextOracleOicApi"],
    "FlextOracleOicCli": ["flext_oracle_oic.main", "FlextOracleOicCli"],
    "FlextOracleOicClient": ["flext_oracle_oic.ext_client", "FlextOracleOicClient"],
    "FlextOracleOicConstants": [
        "flext_oracle_oic.constants",
        "FlextOracleOicConstants",
    ],
    "FlextOracleOicExtServices": [
        "flext_oracle_oic.ext_services",
        "FlextOracleOicExtServices",
    ],
    "FlextOracleOicModels": ["flext_oracle_oic.models", "FlextOracleOicModels"],
    "FlextOracleOicProtocols": [
        "flext_oracle_oic.protocols",
        "FlextOracleOicProtocols",
    ],
    "FlextOracleOicService": ["flext_oracle_oic.service", "FlextOracleOicService"],
    "FlextOracleOicSettings": ["flext_oracle_oic.settings", "FlextOracleOicSettings"],
    "FlextOracleOicTypes": ["flext_oracle_oic.typings", "FlextOracleOicTypes"],
    "FlextOracleOicUtilities": [
        "flext_oracle_oic.utilities",
        "FlextOracleOicUtilities",
    ],
    "api": ["flext_oracle_oic.api", ""],
    "c": ["flext_oracle_oic.constants", "FlextOracleOicConstants"],
    "constants": ["flext_oracle_oic.constants", ""],
    "d": ["flext_core", "d"],
    "e": ["flext_core", "e"],
    "ext_client": ["flext_oracle_oic.ext_client", ""],
    "ext_services": ["flext_oracle_oic.ext_services", ""],
    "h": ["flext_core", "h"],
    "logger": ["flext_oracle_oic.ext_services", "logger"],
    "m": ["flext_oracle_oic.models", "FlextOracleOicModels"],
    "main": ["flext_oracle_oic.main", "main"],
    "models": ["flext_oracle_oic.models", ""],
    "p": ["flext_oracle_oic.protocols", "FlextOracleOicProtocols"],
    "protocols": ["flext_oracle_oic.protocols", ""],
    "r": ["flext_core", "r"],
    "s": ["flext_oracle_oic.service", "FlextOracleOicService"],
    "service": ["flext_oracle_oic.service", ""],
    "settings": ["flext_oracle_oic.settings", ""],
    "t": ["flext_oracle_oic.typings", "FlextOracleOicTypes"],
    "typings": ["flext_oracle_oic.typings", ""],
    "u": ["flext_oracle_oic.utilities", "FlextOracleOicUtilities"],
    "utilities": ["flext_oracle_oic.utilities", ""],
    "x": ["flext_core", "x"],
}

_EXPORTS: Sequence[str] = [
    "FlextOracleOicApi",
    "FlextOracleOicCli",
    "FlextOracleOicClient",
    "FlextOracleOicConstants",
    "FlextOracleOicExtServices",
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
    "api",
    "c",
    "constants",
    "d",
    "e",
    "ext_client",
    "ext_services",
    "h",
    "logger",
    "m",
    "main",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "service",
    "settings",
    "t",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
