"""Oracle OIC Extension Exceptions - Unified Class Pattern.

FLEXT Unified Class Pattern: Single OracleOICExceptions class
with nested exception classes following FLEXT architectural standards.

This module provides Oracle OIC Extension-specific exceptions using modern patterns from flext-core.
All exceptions follow the FlextExceptionsMixin pattern with keyword-only arguments and
modern Python 3.13 type aliases for comprehensive error handling in Oracle OIC operations.

Copyright (c) 2025 FLEXT Contributors
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping
from enum import Enum
from typing import override

from flext_core import FlextExceptions, FlextTypes


class OracleOICExceptions:
    """Unified Oracle OIC Extension exceptions following FLEXT patterns.

    Single responsibility class with nested exception classes
    following the unified class pattern from FLEXT architectural standards.
    """

    class ErrorCodes(Enum):
        """Error codes for Oracle OIC Extension domain operations."""

        OIC_ERROR = "OIC_ERROR"
        OIC_VALIDATION_ERROR = "OIC_VALIDATION_ERROR"
        OIC_CONNECTION_ERROR = "OIC_CONNECTION_ERROR"
        OIC_AUTHENTICATION_ERROR = "OIC_AUTHENTICATION_ERROR"
        OIC_CONFIGURATION_ERROR = "OIC_CONFIGURATION_ERROR"
        OIC_API_ERROR = "OIC_API_ERROR"
        OIC_TIMEOUT_ERROR = "OIC_TIMEOUT_ERROR"
        OIC_AUTH_ERROR = "OIC_AUTH_ERROR"
        OIC_INTEGRATION_ERROR = "OIC_INTEGRATION_ERROR"
        OIC_WORKFLOW_ERROR = "OIC_WORKFLOW_ERROR"
        OIC_PATTERN_ERROR = "OIC_PATTERN_ERROR"
        OIC_TOKEN_ERROR = "OIC_TOKEN_ERROR"  # nosec B105

    # Base Oracle OIC Extension exception hierarchy
    class BaseError(FlextExceptions.BaseError):
        """Base Oracle OIC Extension error."""

    class ValidationError(FlextExceptions.BaseError):
        """Oracle OIC Extension validation error."""

    class OICConnectionError(FlextExceptions.BaseError):
        """Oracle OIC Extension connection error."""

    class AuthenticationError(FlextExceptions.BaseError):
        """Oracle OIC Extension authentication error."""

    class ConfigurationError(FlextExceptions.BaseError):
        """Oracle OIC Extension configuration error."""

    class ApiError(FlextExceptions.BaseError):
        """Oracle OIC Extension API error."""

    class OICTimeoutError(FlextExceptions.BaseError):
        """Oracle OIC Extension timeout error."""

    class TokenError(FlextExceptions.BaseError):
        """Oracle OIC Extension token error."""

    class IntegrationError(FlextExceptions.BaseError):
        """Oracle OIC Extension integration error."""

    class WorkflowError(FlextExceptions.BaseError):
        """Oracle OIC Extension workflow error."""

    class PatternError(FlextExceptions.BaseError):
        """Oracle OIC Extension pattern error."""

    # Domain-specific exceptions for Oracle OIC Extension business logic
    # Using modern FlextExceptionsMixin pattern with context support

    class DataValidationError(ValidationError):
        """Oracle OIC Extension data validation errors with field context."""

        @override
        def __init__(
            self,
            message: str,
            *,
            field_name: str | None = None,
            field_value: object | None = None,
            validation_rule: str | None = None,
            entity_name: str | None = None,
            code: str | None = None,
            context: Mapping[str, object] | None = None,
        ) -> None:
            """Initialize Oracle OIC Extension data validation error with field context."""
            context_dict: FlextTypes.Core.Dict = dict(context) if context else {}
            if field_name is not None:
                context_dict["field_name"] = field_name
            if field_value is not None:
                context_dict["field_value"] = field_value
            if validation_rule is not None:
                context_dict["validation_rule"] = validation_rule
            if entity_name is not None:
                context_dict["entity_name"] = entity_name

            super().__init__(
                message,
                code=code or OracleOICExceptions.ErrorCodes.OIC_VALIDATION_ERROR.value,
                context=context_dict,
            )

    class ApiRequestError(ApiError):
        """Oracle OIC Extension API request errors with HTTP context."""

        @override
        def __init__(
            self,
            message: str,
            *,
            status_code: int | None = None,
            response_body: str | None = None,
            entity_name: str | None = None,
            endpoint: str | None = None,
            method: str | None = None,
            code: str | None = None,
            context: Mapping[str, object] | None = None,
        ) -> None:
            """Initialize Oracle OIC Extension API request error with HTTP context."""
            context_dict: FlextTypes.Core.Dict = dict(context) if context else {}
            if status_code is not None:
                context_dict["status_code"] = status_code
            if response_body is not None:
                context_dict["response_body"] = response_body[
                    :500
                ]  # Truncate for safety
            if entity_name is not None:
                context_dict["entity_name"] = entity_name
            if endpoint is not None:
                context_dict["endpoint"] = endpoint
            if method is not None:
                context_dict["method"] = method

            super().__init__(
                message,
                code=code or OracleOICExceptions.ErrorCodes.OIC_API_ERROR.value,
                context=context_dict,
            )

    class ConfigError(ConfigurationError):
        """Oracle OIC Extension configuration errors with config context."""

        @override
        def __init__(
            self,
            message: str,
            *,
            config_key: str | None = None,
            config_value: object | None = None,
            config_section: str | None = None,
            valid_range: str | None = None,
            code: str | None = None,
            context: Mapping[str, object] | None = None,
        ) -> None:
            """Initialize Oracle OIC Extension configuration error with config context."""
            context_dict: FlextTypes.Core.Dict = dict(context) if context else {}
            if config_key is not None:
                context_dict["config_key"] = config_key
            if config_value is not None:
                context_dict["config_value"] = config_value
            if config_section is not None:
                context_dict["config_section"] = config_section
            if valid_range is not None:
                context_dict["valid_range"] = valid_range

            super().__init__(
                message,
                code=code
                or OracleOICExceptions.ErrorCodes.OIC_CONFIGURATION_ERROR.value,
                context=context_dict,
            )

    class IntegrationPatternError(PatternError):
        """Oracle OIC Extension integration pattern errors with pattern context."""

        @override
        def __init__(
            self,
            message: str,
            *,
            pattern_name: str | None = None,
            pattern_type: str | None = None,
            workflow_id: str | None = None,
            step_id: str | None = None,
            operation: str | None = None,
            code: str | None = None,
            context: Mapping[str, object] | None = None,
        ) -> None:
            """Initialize Oracle OIC Extension integration pattern error with pattern context."""
            context_dict: FlextTypes.Core.Dict = dict(context) if context else {}
            if pattern_name is not None:
                context_dict["pattern_name"] = pattern_name
            if pattern_type is not None:
                context_dict["pattern_type"] = pattern_type
            if workflow_id is not None:
                context_dict["workflow_id"] = workflow_id
            if step_id is not None:
                context_dict["step_id"] = step_id
            if operation is not None:
                context_dict["operation"] = operation

            super().__init__(
                message,
                code=code or OracleOICExceptions.ErrorCodes.OIC_PATTERN_ERROR.value,
                context=context_dict,
            )

    class WorkflowExecutionError(WorkflowError):
        """Oracle OIC Extension workflow execution errors with workflow context."""

        @override
        def __init__(
            self,
            message: str,
            *,
            workflow_id: str | None = None,
            execution_id: str | None = None,
            step_name: str | None = None,
            status: str | None = None,
            error_code: str | None = None,
            code: str | None = None,
            context: Mapping[str, object] | None = None,
        ) -> None:
            """Initialize Oracle OIC Extension workflow execution error with workflow context."""
            context_dict: FlextTypes.Core.Dict = dict(context) if context else {}
            if workflow_id is not None:
                context_dict["workflow_id"] = workflow_id
            if execution_id is not None:
                context_dict["execution_id"] = execution_id
            if step_name is not None:
                context_dict["step_name"] = step_name
            if status is not None:
                context_dict["status"] = status
            if error_code is not None:
                context_dict["error_code"] = error_code

            super().__init__(
                message,
                code=code or OracleOICExceptions.ErrorCodes.OIC_WORKFLOW_ERROR.value,
                context=context_dict,
            )

    class OAuth2TokenError(TokenError):
        """Oracle OIC Extension OAuth2 token errors with authentication context."""

        @override
        def __init__(
            self,
            message: str,
            *,
            token_type: str | None = None,
            client_id: str | None = None,
            scope: str | None = None,
            grant_type: str | None = None,
            expires_in: int | None = None,
            code: str | None = None,
            context: Mapping[str, object] | None = None,
        ) -> None:
            """Initialize Oracle OIC Extension OAuth2 token error with authentication context."""
            context_dict: FlextTypes.Core.Dict = dict(context) if context else {}
            if token_type is not None:
                context_dict["token_type"] = token_type
            if client_id is not None:
                context_dict["client_id"] = client_id
            if scope is not None:
                context_dict["scope"] = scope
            if grant_type is not None:
                context_dict["grant_type"] = grant_type
            if expires_in is not None:
                context_dict["expires_in"] = expires_in

            super().__init__(
                message,
                code=code or OracleOICExceptions.ErrorCodes.OIC_TOKEN_ERROR.value,
                context=context_dict,
            )


# Backward compatibility aliases
FlextOracleOicErrorCodes = OracleOICExceptions.ErrorCodes
FlextOracleOicError = OracleOICExceptions.BaseError
FlextOracleOicValidationError = OracleOICExceptions.ValidationError
FlextOracleOicConnectionError = OracleOICExceptions.OICConnectionError
FlextOracleOicAuthenticationError = OracleOICExceptions.AuthenticationError
FlextOracleOicConfigurationError = OracleOICExceptions.ConfigurationError
FlextOracleOicApiError = OracleOICExceptions.ApiError
FlextOracleOicTimeoutError = OracleOICExceptions.OICTimeoutError
FlextOracleOicTokenError = OracleOICExceptions.TokenError
FlextOracleOicIntegrationError = OracleOICExceptions.IntegrationError
FlextOracleOicWorkflowError = OracleOICExceptions.WorkflowError
FlextOracleOicPatternError = OracleOICExceptions.PatternError
FlextOracleOicDataValidationError = OracleOICExceptions.DataValidationError
FlextOracleOicApiRequestError = OracleOICExceptions.ApiRequestError
FlextOracleOicConfigError = OracleOICExceptions.ConfigError
FlextOracleOicIntegrationPatternError = OracleOICExceptions.IntegrationPatternError
FlextOracleOicWorkflowExecutionError = OracleOICExceptions.WorkflowExecutionError
FlextOracleOicOAuth2TokenError = OracleOICExceptions.OAuth2TokenError

# Convenience tuple for importing all exceptions
exceptions_all = (
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
    OracleOICExceptions,
)


__all__: FlextTypes.Core.StringList = [
    "FlextOracleOicApiError",
    "FlextOracleOicApiRequestError",
    "FlextOracleOicAuthenticationError",
    "FlextOracleOicConfigError",
    "FlextOracleOicConfigurationError",
    "FlextOracleOicConnectionError",
    "FlextOracleOicDataValidationError",
    "FlextOracleOicError",
    "FlextOracleOicErrorCodes",
    "FlextOracleOicIntegrationError",
    "FlextOracleOicIntegrationPatternError",
    "FlextOracleOicOAuth2TokenError",
    "FlextOracleOicPatternError",
    "FlextOracleOicTimeoutError",
    "FlextOracleOicTokenError",
    "FlextOracleOicValidationError",
    "FlextOracleOicWorkflowError",
    "FlextOracleOicWorkflowExecutionError",
    "OracleOICExceptions",
    "exceptions_all",
]
