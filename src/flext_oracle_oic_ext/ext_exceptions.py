"""Oracle OIC Extension Legacy Exceptions - EXTENSION Pattern.

FLEXT Unified Class Pattern: This module provides backward compatibility
with the legacy exception structure while redirecting to the unified
OracleOICExceptions class.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextTypes
from flext_oracle_oic_ext.exceptions import OracleOICExceptions


class OracleOICExtensionExceptions:
    """Unified Oracle OIC Extension exceptions following FLEXT patterns.

    Single responsibility class that provides backward compatibility
    with legacy exception names while using the unified exceptions internally.
    """

    # Backward compatibility aliases to unified exceptions
    BaseError = OracleOICExceptions.BaseError
    AuthenticationError = OracleOICExceptions.AuthenticationError
    TokenError = OracleOICExceptions.TokenError
    ConnectionError = OracleOICExceptions.OICConnectionError
    TimeoutError = OracleOICExceptions.OICTimeoutError
    ApiError = OracleOICExceptions.ApiError
    ValidationError = OracleOICExceptions.ValidationError
    IntegrationError = OracleOICExceptions.IntegrationError
    WorkflowError = OracleOICExceptions.WorkflowError
    ConfigurationError = OracleOICExceptions.ConfigurationError
    PatternError = OracleOICExceptions.PatternError


# Legacy compatibility - these should use the unified exceptions
OracleOICExtensionError = OracleOICExtensionExceptions.BaseError
OICAuthenticationError = OracleOICExtensionExceptions.AuthenticationError
OICTokenError = OracleOICExtensionExceptions.TokenError
OICConnectionError = OracleOICExtensionExceptions.ConnectionError
OICTimeoutError = OracleOICExtensionExceptions.TimeoutError
OICAPIError = OracleOICExtensionExceptions.ApiError
OICValidationError = OracleOICExtensionExceptions.ValidationError
OICIntegrationError = OracleOICExtensionExceptions.IntegrationError
OICWorkflowError = OracleOICExtensionExceptions.WorkflowError
OICConfigurationError = OracleOICExtensionExceptions.ConfigurationError
OICPatternError = OracleOICExtensionExceptions.PatternError


# Exports following EXTENSION pattern
__all__: FlextTypes.Core.StringList = [
    "OICAPIError",
    "OICAuthenticationError",
    "OICConfigurationError",
    "OICConnectionError",
    "OICIntegrationError",
    "OICPatternError",
    "OICTimeoutError",
    "OICTokenError",
    "OICValidationError",
    "OICWorkflowError",
    "OracleOICExtensionError",
    "OracleOICExtensionExceptions",
]
