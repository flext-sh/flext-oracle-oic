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
            **kwargs: object,
        ) -> None:
            """Initialize Oracle OIC Extension data validation error with field context."""
            # Store domain-specific attributes before extracting common kwargs
            self.field_name = field_name
            self.field_value = field_value
            self.validation_rule = validation_rule
            self.entity_name = entity_name

            # Extract common parameters using helper
            base_context, correlation_id, error_code = self._extract_common_kwargs(
                kwargs
            )

            # Build context with validation-specific fields
            context = self._build_context(
                base_context,
                field_name=field_name,
                field_value=field_value,
                validation_rule=validation_rule,
                entity_name=entity_name,
            )

            # Call parent with complete error information
            super().__init__(
                message,
                code=error_code
                or OracleOICExceptions.ErrorCodes.OIC_VALIDATION_ERROR.value,
                context=context,
                correlation_id=correlation_id,
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
            **kwargs: object,
        ) -> None:
            """Initialize Oracle OIC Extension API request error with HTTP context."""
            # Store domain-specific attributes before extracting common kwargs
            self.status_code = status_code
            self.response_body = response_body
            self.entity_name = entity_name
            self.endpoint = endpoint
            self.method = method

            # Extract common parameters using helper
            base_context, correlation_id, error_code = self._extract_common_kwargs(
                kwargs
            )

            # Build context with API-specific fields
            context = self._build_context(
                base_context,
                status_code=status_code,
                response_body=response_body[:500]
                if response_body is not None
                else None,  # Truncate for safety
                entity_name=entity_name,
                endpoint=endpoint,
                method=method,
            )

            # Call parent with complete error information
            super().__init__(
                message,
                code=error_code or OracleOICExceptions.ErrorCodes.OIC_API_ERROR.value,
                context=context,
                correlation_id=correlation_id,
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
            **kwargs: object,
        ) -> None:
            """Initialize Oracle OIC Extension configuration error with config context."""
            # Store domain-specific attributes before extracting common kwargs
            self.config_key = config_key
            self.config_value = config_value
            self.config_section = config_section
            self.valid_range = valid_range

            # Extract common parameters using helper
            base_context, correlation_id, error_code = self._extract_common_kwargs(
                kwargs
            )

            # Build context with configuration-specific fields
            context = self._build_context(
                base_context,
                config_key=config_key,
                config_value=config_value,
                config_section=config_section,
                valid_range=valid_range,
            )

            # Call parent with complete error information
            super().__init__(
                message,
                code=error_code
                or OracleOICExceptions.ErrorCodes.OIC_CONFIGURATION_ERROR.value,
                context=context,
                correlation_id=correlation_id,
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
            **kwargs: object,
        ) -> None:
            """Initialize Oracle OIC Extension integration pattern error with pattern context."""
            # Store domain-specific attributes before extracting common kwargs
            self.pattern_name = pattern_name
            self.pattern_type = pattern_type
            self.workflow_id = workflow_id
            self.step_id = step_id
            self.operation = operation

            # Extract common parameters using helper
            base_context, correlation_id, error_code = self._extract_common_kwargs(
                kwargs
            )

            # Build context with pattern-specific fields
            context = self._build_context(
                base_context,
                pattern_name=pattern_name,
                pattern_type=pattern_type,
                workflow_id=workflow_id,
                step_id=step_id,
                operation=operation,
            )

            # Call parent with complete error information
            super().__init__(
                message,
                code=error_code
                or OracleOICExceptions.ErrorCodes.OIC_PATTERN_ERROR.value,
                context=context,
                correlation_id=correlation_id,
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
            **kwargs: object,
        ) -> None:
            """Initialize Oracle OIC Extension workflow execution error with workflow context."""
            # Store domain-specific attributes before extracting common kwargs
            self.workflow_id = workflow_id
            self.execution_id = execution_id
            self.step_name = step_name
            self.status = status
            self.error_code = error_code

            # Extract common parameters using helper
            base_context, correlation_id, code = self._extract_common_kwargs(kwargs)

            # Build context with workflow-specific fields
            context = self._build_context(
                base_context,
                workflow_id=workflow_id,
                execution_id=execution_id,
                step_name=step_name,
                status=status,
                error_code=error_code,
            )

            # Call parent with complete error information
            super().__init__(
                message,
                code=code or OracleOICExceptions.ErrorCodes.OIC_WORKFLOW_ERROR.value,
                context=context,
                correlation_id=correlation_id,
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
            **kwargs: object,
        ) -> None:
            """Initialize Oracle OIC Extension OAuth2 token error with authentication context."""
            # Store domain-specific attributes before extracting common kwargs
            self.token_type = token_type
            self.client_id = client_id
            self.scope = scope
            self.grant_type = grant_type
            self.expires_in = expires_in

            # Extract common parameters using helper
            base_context, correlation_id, error_code = self._extract_common_kwargs(
                kwargs
            )

            # Build context with OAuth2-specific fields
            context = self._build_context(
                base_context,
                token_type=token_type,
                client_id=client_id,
                scope=scope,
                grant_type=grant_type,
                expires_in=expires_in,
            )

            # Call parent with complete error information
            super().__init__(
                message,
                code=error_code or OracleOICExceptions.ErrorCodes.OIC_TOKEN_ERROR.value,
                context=context,
                correlation_id=correlation_id,
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


__all__: FlextTypes.StringList = [
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
