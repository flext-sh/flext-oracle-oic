"""FLEXT Oracle OIC Extension - EXTENSION Pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import importlib.metadata

from flext_core.metadata import build_metadata_exports

from flext_core import (
    E,
    F,
    FlextConfig,
    FlextLogger,
    FlextModels,
    FlextResult,
    FlextTypes,
    P,
    R,
    T,
    U,
    V,
)
from flext_oracle_oic.cli import app, main
from flext_oracle_oic.config import (
    FlextOracleOicExtConfig,
)
from flext_oracle_oic.constants import FlextOracleOicExtConstants
from flext_oracle_oic.container import (
    configure_flext_oracle_oic_ext_dependencies,
    get_flext_oracle_oic_ext_container,
    get_flext_oracle_oic_ext_service,
)
from flext_oracle_oic.exceptions import (
    FlextOracleOicApiError,
    FlextOracleOicApiRequestError,
    FlextOracleOicAuthenticationError,
    FlextOracleOicConfigError,
    FlextOracleOicConfigurationError,
    FlextOracleOicConnectionError,
    FlextOracleOicDataValidationError,
    FlextOracleOicError,
    FlextOracleOicErrorCodes,
    FlextOracleOicIntegrationError,
    FlextOracleOicIntegrationPatternError,
    FlextOracleOicOAuth2TokenError,
    FlextOracleOicPatternError,
    FlextOracleOicTimeoutError,
    FlextOracleOicTokenError,
    FlextOracleOicValidationError,
    FlextOracleOicWorkflowError,
    FlextOracleOicWorkflowExecutionError,
    exceptions_all,
)
from flext_oracle_oic.ext_client import (
    BaseOICAuthenticator,
    BaseOICClient,
    OICExtensionAuthenticator,
    OICTapAuthenticator,
    OICTargetAuthenticator,
    OracleOICExtensionClient,
)
from flext_oracle_oic.ext_config import (
    OICExtensionAuthConfig,
    OICExtensionConnectionConfig,
    OracleOICExtensionSettings,
)
from flext_oracle_oic.ext_exceptions import (
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
from flext_oracle_oic.ext_services import (
    HTTPClientProtocol,
    HTTPResponseProtocol,
    LifecycleManager,
    MonitoringService,
    OICIntegrationPatternService,
    OracleOICExtensionService,
)
from flext_oracle_oic.extension import OracleOICExtension
from flext_oracle_oic.factory import (
    FlextOracleOicExtDeprecationWarning,
    _show_deprecation_warning,
    create_development_oic_service,
    create_oic_extension_service,
    setup_oic_extension,
)
from flext_oracle_oic.models import FlextOracleOicExtModels
from flext_oracle_oic.protocols import FlextOracleOicExtProtocols
from flext_oracle_oic.utilities import FlextOracleOicExtUtilities

# Import VERSION after metadata setup to avoid circular imports
from flext_oracle_oic.version import VERSION

globals().update(build_metadata_exports(__file__))

OICAuthConfig = FlextOracleOicExtModels.OICAuthConfig
OICConnectionConfig = FlextOracleOicExtModels.OICConnectionConfig
OICIntegrationInfo = FlextOracleOicExtModels.OICIntegrationInfo
OICConnectionInfo = FlextOracleOicExtModels.OICConnectionInfo
IntegrationStatus = FlextOracleOicExtModels.IntegrationStatus
RequestParams = FlextOracleOicExtModels.RequestParams

try:
    __version__ = importlib.metadata.version("flext-oracle-oic")
    __version_info__: tuple[int | str, ...] = VERSION.version_info
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"


logger = FlextLogger(__name__)
__all__: FlextTypes.StringList = [
    "BaseOICAuthenticator",
    "BaseOICClient",
    "E",
    "F",
    "FlextConfig",
    "FlextLogger",
    "FlextModels",
    "FlextOracleOicApiError",
    "FlextOracleOicApiRequestError",
    "FlextOracleOicAuthenticationError",
    "FlextOracleOicConfigError",
    "FlextOracleOicConfigurationError",
    "FlextOracleOicConnectionError",
    "FlextOracleOicDataValidationError",
    "FlextOracleOicError",
    "FlextOracleOicErrorCodes",
    "FlextOracleOicExtConfig",
    "FlextOracleOicExtConstants",
    "FlextOracleOicExtDeprecationWarning",
    "FlextOracleOicExtModels",
    "FlextOracleOicExtProtocols",
    "FlextOracleOicExtUtilities",
    "FlextOracleOicIntegrationError",
    "FlextOracleOicIntegrationPatternError",
    "FlextOracleOicOAuth2TokenError",
    "FlextOracleOicPatternError",
    "FlextOracleOicTimeoutError",
    "FlextOracleOicTokenError",
    "FlextOracleOicValidationError",
    "FlextOracleOicWorkflowError",
    "FlextOracleOicWorkflowExecutionError",
    "FlextResult",
    "FlextTypes",
    "HTTPClientProtocol",
    "HTTPResponseProtocol",
    "IntegrationStatus",
    "LifecycleManager",
    "MonitoringService",
    "OICAPIError",
    "OICAuthConfig",
    "OICAuthenticationError",
    "OICConfigurationError",
    "OICConnectionConfig",
    "OICConnectionError",
    "OICConnectionInfo",
    "OICExtensionAuthConfig",
    "OICExtensionAuthenticator",
    "OICExtensionConnectionConfig",
    "OICIntegrationError",
    "OICIntegrationInfo",
    "OICIntegrationPatternService",
    "OICPatternError",
    "OICTapAuthenticator",
    "OICTargetAuthenticator",
    "OICTimeoutError",
    "OICTokenError",
    "OICValidationError",
    "OICWorkflowError",
    "OracleOICExtension",
    "OracleOICExtensionClient",
    "OracleOICExtensionError",
    "OracleOICExtensionService",
    "OracleOICExtensionSettings",
    "P",
    "R",
    "RequestParams",
    "T",
    "U",
    "V",
    "__version__",
    "__version_info__",
    "_show_deprecation_warning",
    "app",
    "configure_flext_oracle_oic_ext_dependencies",
    "create_development_oic_service",
    "create_oic_extension_service",
    "exceptions_all",
    "get_flext_oracle_oic_ext_container",
    "get_flext_oracle_oic_ext_service",
    "main",
    "setup_oic_extension",
]
