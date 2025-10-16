"""FLEXT Oracle OIC Extension - EXTENSION Pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_oracle_oic.__version__ import __version__, __version_info__
from flext_oracle_oic.api import FlextOracleOicApi
from flext_oracle_oic.config import (
    FlextOracleOicConfig,
)
from flext_oracle_oic.constants import FlextOracleOicConstants
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
from flext_oracle_oic.models import (
    FlextOracleOicModels,
)
from flext_oracle_oic.protocols import FlextOracleOicProtocols
from flext_oracle_oic.service import (
    FlextOracleOicService,
)
from flext_oracle_oic.utilities import FlextOracleOicUtilities

__all__ = [
    "FlextOracleOicApi",
    "FlextOracleOicClient",
    "FlextOracleOicConfig",
    "FlextOracleOicConstants",
    "FlextOracleOicDeprecationWarning",
    "FlextOracleOicFactory",
    "FlextOracleOicModels",
    "FlextOracleOicProtocols",
    "FlextOracleOicService",
    "FlextOracleOicUtilities",
    "__version__",
    "__version_info__",
    "create_development_oic_service",
    "create_oic_extension_service",
    "setup_oic_extension",
]
