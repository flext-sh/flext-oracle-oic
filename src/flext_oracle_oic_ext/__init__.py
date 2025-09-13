"""FLEXT Oracle OIC Extension - EXTENSION Pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import importlib.metadata

from flext_core import FlextConfig, FlextLogger, FlextModels, FlextResult, FlextTypes

from flext_oracle_oic_ext.ext_client import (
    BaseOICAuthenticator,
    BaseOICClient,
    OICExtensionAuthenticator,
    OICTapAuthenticator,
    OICTargetAuthenticator,
    OracleOICExtensionClient,
)
from flext_oracle_oic_ext.ext_config import (
    OICExtensionAuthConfig,
    OICExtensionConnectionConfig,
    OracleOICExtensionSettings,
)
from flext_oracle_oic_ext.ext_exceptions import (
    OICAPIError,
    OICAuthenticationError,
    OICConfigurationError,
    OICConnectionError,
    OICIntegrationError,
    OICPatternError,
    OICTimeoutError,
    OICTokenError,
    OICValidationError,
    OICWorkflowError,
    OracleOICExtensionError,
)
from flext_oracle_oic_ext.ext_models import (
    OICAuthConfig,
    OICConnectionConfig,
    OICConnectionInfo,
    OICIntegrationInfo,
    RequestParams,
)
from flext_oracle_oic_ext.ext_services import (
    OICIntegrationPatternService,
    OracleOICExtensionService,
)
from flext_oracle_oic_ext.extension import OracleOICExtension
from flext_oracle_oic_ext.factory import (
    FlextOracleOicExtDeprecationWarning,
    _show_deprecation_warning,
    create_development_oic_service,
    create_oic_extension_service,
)

# Version information
try:
    __version__ = importlib.metadata.version("flext-oracle-oic-ext")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())

# Logger instance
logger = FlextLogger(__name__)


# Logger for this module
logger = FlextLogger(__name__)

# Version information
try:
    __version__ = importlib.metadata.version("flext-oracle-oic-ext")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())
__all__: FlextTypes.Core.StringList = [
    # Client classes
    "BaseOICAuthenticator",
    "BaseOICClient",
    # Foundation flext-core
    "FlextConfig",
    "FlextLogger",
    "FlextModels",
    # Factory functions
    "FlextOracleOicExtDeprecationWarning",
    "FlextResult",
    "FlextTypes",
    # Exception classes
    "OICAPIError",
    # Model classes
    "OICAuthConfig",
    "OICAuthenticationError",
    "OICConfigurationError",
    "OICConnectionConfig",
    "OICConnectionError",
    "OICConnectionInfo",
    # Configuration classes
    "OICExtensionAuthConfig",
    "OICExtensionAuthenticator",
    "OICExtensionConnectionConfig",
    "OICIntegrationError",
    "OICIntegrationInfo",
    # Service classes
    "OICIntegrationPatternService",
    "OICPatternError",
    "OICTapAuthenticator",
    "OICTargetAuthenticator",
    "OICTimeoutError",
    "OICTokenError",
    "OICValidationError",
    "OICWorkflowError",
    # Extension classes
    "OracleOICExtension",
    "OracleOICExtensionClient",
    "OracleOICExtensionError",
    "OracleOICExtensionService",
    "OracleOICExtensionSettings",
    "RequestParams",
    # Version info
    "__version__",
    "__version_info__",
    "_show_deprecation_warning",
    "create_development_oic_service",
    "create_development_oic_service",
    "create_oic_extension_service",
    # Utility functions
    "create_oic_extension_service",
]
