"""FLEXT Oracle OIC Extension - EXTENSION Pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import (
    FlextDecorators as d,
    FlextExceptions as e,
    FlextHandlers as h,
    FlextMixins as x,
    FlextResult as r,
    FlextService as s,
)
from flext_oracle_oic.__version__ import __version__, __version_info__
from flext_oracle_oic.api import FlextOracleOicApi
from flext_oracle_oic.constants import (
    FlextOracleOicConstants,
    FlextOracleOicConstants as c,
)
from flext_oracle_oic.ext_client import (
    FlextOracleOicClient,
)
from flext_oracle_oic.factory import (
    FlextOracleOicDeprecationWarning,
    FlextOracleOicFactory,
    create_development_oic_service,
    create_oic_extension_service,
    setup_oic_extension,
)
from flext_oracle_oic.models import FlextOracleOicModels, FlextOracleOicModels as m
from flext_oracle_oic.protocols import (
    FlextOracleOicProtocols,
    FlextOracleOicProtocols as p,
)
from flext_oracle_oic.service import (
    FlextOracleOicService,
)
from flext_oracle_oic.settings import (
    FlextOracleOicSettings,
)
from flext_oracle_oic.typings import FlextOracleOicTypes, FlextOracleOicTypes as t
from flext_oracle_oic.utilities import (
    FlextOracleOicUtilities,
    FlextOracleOicUtilities as u,
)

__all__ = [
    "FlextOracleOicApi",
    "FlextOracleOicClient",
    "FlextOracleOicConstants",
    "FlextOracleOicDeprecationWarning",
    "FlextOracleOicFactory",
    "FlextOracleOicModels",
    "FlextOracleOicProtocols",
    "FlextOracleOicService",
    "FlextOracleOicSettings",
    "FlextOracleOicTypes",
    "FlextOracleOicUtilities",
    "__version__",
    "__version_info__",
    # Domain-specific aliases
    "c",
    "create_development_oic_service",
    "create_oic_extension_service",
    # Global aliases
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "setup_oic_extension",
    "t",
    "u",
    "x",
]
