# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT Oracle OIC Extension - EXTENSION Pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import d, e, h, r, x

    from flext_oracle_oic.__version__ import *
    from flext_oracle_oic.api import *
    from flext_oracle_oic.constants import *
    from flext_oracle_oic.ext_client import *
    from flext_oracle_oic.ext_services import *
    from flext_oracle_oic.main import *
    from flext_oracle_oic.models import *
    from flext_oracle_oic.protocols import *
    from flext_oracle_oic.service import *
    from flext_oracle_oic.settings import *
    from flext_oracle_oic.typings import *
    from flext_oracle_oic.utilities import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "FlextOracleOicApi": "flext_oracle_oic.api",
    "FlextOracleOicCli": "flext_oracle_oic.main",
    "FlextOracleOicClient": "flext_oracle_oic.ext_client",
    "FlextOracleOicConstants": "flext_oracle_oic.constants",
    "FlextOracleOicExtServices": "flext_oracle_oic.ext_services",
    "FlextOracleOicModels": "flext_oracle_oic.models",
    "FlextOracleOicProtocols": "flext_oracle_oic.protocols",
    "FlextOracleOicService": "flext_oracle_oic.service",
    "FlextOracleOicSettings": "flext_oracle_oic.settings",
    "FlextOracleOicTypes": "flext_oracle_oic.typings",
    "FlextOracleOicUtilities": "flext_oracle_oic.utilities",
    "__author__": "flext_oracle_oic.__version__",
    "__author_email__": "flext_oracle_oic.__version__",
    "__description__": "flext_oracle_oic.__version__",
    "__license__": "flext_oracle_oic.__version__",
    "__title__": "flext_oracle_oic.__version__",
    "__url__": "flext_oracle_oic.__version__",
    "__version__": "flext_oracle_oic.__version__",
    "__version_info__": "flext_oracle_oic.__version__",
    "api": "flext_oracle_oic.api",
    "c": ("flext_oracle_oic.constants", "FlextOracleOicConstants"),
    "constants": "flext_oracle_oic.constants",
    "d": "flext_core",
    "e": "flext_core",
    "ext_client": "flext_oracle_oic.ext_client",
    "ext_services": "flext_oracle_oic.ext_services",
    "h": "flext_core",
    "logger": "flext_oracle_oic.ext_services",
    "m": ("flext_oracle_oic.models", "FlextOracleOicModels"),
    "main": "flext_oracle_oic.main",
    "models": "flext_oracle_oic.models",
    "p": ("flext_oracle_oic.protocols", "FlextOracleOicProtocols"),
    "protocols": "flext_oracle_oic.protocols",
    "r": "flext_core",
    "s": ("flext_oracle_oic.service", "FlextOracleOicService"),
    "service": "flext_oracle_oic.service",
    "settings": "flext_oracle_oic.settings",
    "t": ("flext_oracle_oic.typings", "FlextOracleOicTypes"),
    "typings": "flext_oracle_oic.typings",
    "u": ("flext_oracle_oic.utilities", "FlextOracleOicUtilities"),
    "utilities": "flext_oracle_oic.utilities",
    "x": "flext_core",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
