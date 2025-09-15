"""Oracle OIC Extension Exceptions - EXTENSION Pattern.

This module establishes the EXTENSION PEP8 pattern for specialized
Oracle OIC exceptions using flext-core factory pattern.


Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextTypes

# ================================
# EXTENSION Pattern: Specialized Exceptions
# ================================


class OracleOICExtensionError(Exception):
    """Base exception for Oracle OIC Extension errors.

    Padrão EXTENSION: Exceção base para todas as operações Oracle OIC Extension
    seguindo hierarquia enterprise de erros.
    """


# Authentication exceptions
class OICAuthenticationError(OracleOICExtensionError):
    """OAuth2 authentication with Oracle OIC failed."""


class OICTokenError(OracleOICExtensionError):
    """OAuth2 token operation failed."""


# Connection exceptions
class OICConnectionError(OracleOICExtensionError):
    """Connection to Oracle OIC instance failed."""


class OICTimeoutError(OracleOICExtensionError):
    """Oracle OIC request timeout exceeded."""


# API exceptions
class OICAPIError(OracleOICExtensionError):
    """Oracle OIC REST API operation failed."""


class OICValidationError(OracleOICExtensionError):
    """Oracle OIC data validation failed."""


# Integration exceptions
class OICIntegrationError(OracleOICExtensionError):
    """Oracle OIC integration operation failed."""


class OICWorkflowError(OracleOICExtensionError):
    """Oracle OIC workflow execution failed."""


# Configuration exceptions
class OICConfigurationError(OracleOICExtensionError):
    """Oracle OIC extension configuration error."""


# Pattern exceptions
class OICPatternError(OracleOICExtensionError):
    """Oracle OIC enterprise pattern execution failed."""


# Exports following EXTENSION pattern
__all__: FlextTypes.Core.StringList = [
    # API
    "OICAPIError",
    # Authentication
    "OICAuthenticationError",
    # Configuration
    "OICConfigurationError",
    # Connection
    "OICConnectionError",
    # Integration
    "OICIntegrationError",
    # Pattern
    "OICPatternError",
    "OICTimeoutError",
    "OICTokenError",
    "OICValidationError",
    "OICWorkflowError",
    # Base exception
    "OracleOICExtensionError",
]
