"""FLEXT Oracle OIC Extension - EXTENSION Pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import importlib.metadata

from flext_core import (
    FlextConfig,
    FlextLogger,
    FlextModels,
    FlextResult,
    FlextTypes,
)
from flext_oracle_oic_ext.cli import app, main
from flext_oracle_oic_ext.constants import FlextOracleOicExtConstants
from flext_oracle_oic_ext.container import (
    configure_flext_oracle_oic_ext_dependencies,
    get_flext_oracle_oic_ext_container,
    get_flext_oracle_oic_ext_service,
)
from flext_oracle_oic_ext.exceptions import (
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
    IntegrationStatus,
    OICAuthConfig,
    OICConnectionConfig,
    OICConnectionInfo,
    OICIntegrationInfo,
    RequestParams,
)
from flext_oracle_oic_ext.ext_services import (
    HTTPClientProtocol,
    HTTPResponseProtocol,
    LifecycleManager,
    MonitoringService,
    OICIntegrationPatternService,
    OracleOICExtensionService,
)
from flext_oracle_oic_ext.extension import OracleOICExtension
from flext_oracle_oic_ext.factory import (
    FlextOracleOicExtDeprecationWarning,
    _show_deprecation_warning,
    create_development_oic_service,
    create_oic_extension_service,
    setup_oic_extension,
)

# Version information
try:
    __version__ = importlib.metadata.version("flext-oracle-oic-ext")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())

# Logger instance
logger = FlextLogger(__name__)
__all__: FlextTypes.Core.StringList = [
    "BaseOICAuthenticator",
    "BaseOICClient",
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
    "FlextOracleOicExtConstants",
    "FlextOracleOicExtDeprecationWarning",
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
    "RequestParams",
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
