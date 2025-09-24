"""Comprehensive tests for Oracle OIC Extension exceptions.

Tests all exception classes and error patterns to achieve 100% coverage
of the exceptions.py module following FLEXT architectural patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_oracle_oic_ext import (
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
    __all__ as exceptions_all,
)


class TestFlextOracleOicErrorCodes:
    """Test error codes enumeration."""

    def test_all_error_codes_exist(self) -> None:
        """Test all expected error codes are defined."""
        expected_codes = {
            "OIC_ERROR",
            "OIC_VALIDATION_ERROR",
            "OIC_CONNECTION_ERROR",
            "OIC_AUTHENTICATION_ERROR",
            "OIC_CONFIGURATION_ERROR",
            "OIC_API_ERROR",
            "OIC_TIMEOUT_ERROR",
            "OIC_AUTH_ERROR",
            "OIC_INTEGRATION_ERROR",
            "OIC_WORKFLOW_ERROR",
            "OIC_PATTERN_ERROR",
            "OIC_TOKEN_ERROR",
        }

        actual_codes = {code.value for code in FlextOracleOicErrorCodes}
        assert actual_codes == expected_codes

    def test_error_code_values(self) -> None:
        """Test error codes have correct string values."""
        assert FlextOracleOicErrorCodes.OIC_ERROR.value == "OIC_ERROR"
        assert (
            FlextOracleOicErrorCodes.OIC_VALIDATION_ERROR.value
            == "OIC_VALIDATION_ERROR"
        )
        assert (
            FlextOracleOicErrorCodes.OIC_CONNECTION_ERROR.value
            == "OIC_CONNECTION_ERROR"
        )
        assert (
            FlextOracleOicErrorCodes.OIC_AUTHENTICATION_ERROR.value
            == "OIC_AUTHENTICATION_ERROR"
        )
        assert (
            FlextOracleOicErrorCodes.OIC_CONFIGURATION_ERROR.value
            == "OIC_CONFIGURATION_ERROR"
        )
        assert FlextOracleOicErrorCodes.OIC_API_ERROR.value == "OIC_API_ERROR"
        assert FlextOracleOicErrorCodes.OIC_TIMEOUT_ERROR.value == "OIC_TIMEOUT_ERROR"
        assert FlextOracleOicErrorCodes.OIC_AUTH_ERROR.value == "OIC_AUTH_ERROR"
        assert (
            FlextOracleOicErrorCodes.OIC_INTEGRATION_ERROR.value
            == "OIC_INTEGRATION_ERROR"
        )
        assert FlextOracleOicErrorCodes.OIC_WORKFLOW_ERROR.value == "OIC_WORKFLOW_ERROR"
        assert FlextOracleOicErrorCodes.OIC_PATTERN_ERROR.value == "OIC_PATTERN_ERROR"
        assert FlextOracleOicErrorCodes.OIC_TOKEN_ERROR.value == "OIC_TOKEN_ERROR"


class TestBaseExceptions:
    """Test base exception classes."""

    def test_flext_oracle_oic_error(self) -> None:
        """Test base Oracle OIC error."""
        error = FlextOracleOicError("Test error")
        assert str(error) == "[GENERIC_ERROR] Test error"
        assert isinstance(error, Exception)

    def test_flext_oracle_oic_validation_error(self) -> None:
        """Test Oracle OIC validation error."""
        error = FlextOracleOicValidationError("Validation failed")
        assert str(error) == "[GENERIC_ERROR] Validation failed"
        assert isinstance(error, Exception)

    def test_flext_oracle_oic_connection_error(self) -> None:
        """Test Oracle OIC connection error."""
        error = FlextOracleOicConnectionError("Connection failed")
        assert str(error) == "[GENERIC_ERROR] Connection failed"
        assert isinstance(error, Exception)

    def test_flext_oracle_oic_authentication_error(self) -> None:
        """Test Oracle OIC authentication error."""
        error = FlextOracleOicAuthenticationError("Auth failed")
        assert str(error) == "[GENERIC_ERROR] Auth failed"
        assert isinstance(error, Exception)

    def test_flext_oracle_oic_configuration_error(self) -> None:
        """Test Oracle OIC configuration error."""
        error = FlextOracleOicConfigurationError("Config invalid")
        assert str(error) == "[GENERIC_ERROR] Config invalid"
        assert isinstance(error, Exception)

    def test_flext_oracle_oic_api_error(self) -> None:
        """Test Oracle OIC API error."""
        error = FlextOracleOicApiError("API call failed")
        assert str(error) == "[GENERIC_ERROR] API call failed"
        assert isinstance(error, Exception)

    def test_flext_oracle_oic_timeout_error(self) -> None:
        """Test Oracle OIC timeout error."""
        error = FlextOracleOicTimeoutError("Request timed out")
        assert str(error) == "[GENERIC_ERROR] Request timed out"
        assert isinstance(error, Exception)

    def test_flext_oracle_oic_token_error(self) -> None:
        """Test Oracle OIC token error."""
        error = FlextOracleOicTokenError("Token invalid")
        assert str(error) == "[GENERIC_ERROR] Token invalid"
        assert isinstance(error, Exception)

    def test_flext_oracle_oic_integration_error(self) -> None:
        """Test Oracle OIC integration error."""
        error = FlextOracleOicIntegrationError("Integration failed")
        assert str(error) == "[GENERIC_ERROR] Integration failed"
        assert isinstance(error, Exception)

    def test_flext_oracle_oic_workflow_error(self) -> None:
        """Test Oracle OIC workflow error."""
        error = FlextOracleOicWorkflowError("Workflow failed")
        assert str(error) == "[GENERIC_ERROR] Workflow failed"
        assert isinstance(error, Exception)

    def test_flext_oracle_oic_pattern_error(self) -> None:
        """Test Oracle OIC pattern error."""
        error = FlextOracleOicPatternError("Pattern invalid")
        assert str(error) == "[GENERIC_ERROR] Pattern invalid"
        assert isinstance(error, Exception)


class TestFlextOracleOicDataValidationError:
    """Test data validation error with context."""

    def test_basic_validation_error(self) -> None:
        """Test basic validation error creation."""
        error = FlextOracleOicDataValidationError("Field validation failed")
        assert str(error) == "[OIC_VALIDATION_ERROR] Field validation failed"
        assert hasattr(error, "code")
        assert hasattr(error, "context")

    def test_validation_error_with_field_context(self) -> None:
        """Test validation error with field context."""
        error = FlextOracleOicDataValidationError(
            "Invalid field value",
            field_name="oauth_client_id",
            field_value="invalid_id",
            validation_rule="required_string",
            entity_name="OICAuthConfig",
        )

        assert str(error) == "[OIC_VALIDATION_ERROR] Invalid field value"
        assert error.code == FlextOracleOicErrorCodes.OIC_VALIDATION_ERROR.value
        assert "field_name" in error.context
        assert error.context["field_name"] == "oauth_client_id"
        assert error.context["field_value"] == "invalid_id"
        assert error.context["validation_rule"] == "required_string"
        assert error.context["entity_name"] == "OICAuthConfig"

    def test_validation_error_with_custom_code(self) -> None:
        """Test validation error with custom error code."""
        error = FlextOracleOicDataValidationError(
            "Custom validation error",
            code="CUSTOM_VALIDATION_ERROR",
        )

        assert error.code == "CUSTOM_VALIDATION_ERROR"

    def test_validation_error_with_custom_context(self) -> None:
        """Test validation error with custom context."""
        custom_context = {"custom_field": "custom_value", "another_field": 123}
        error = FlextOracleOicDataValidationError(
            "Custom context error",
            field_name="test_field",
            context=custom_context,
        )

        assert "custom_field" in error.context
        assert "another_field" in error.context
        assert "field_name" in error.context
        assert error.context["custom_field"] == "custom_value"
        assert error.context["another_field"] == 123
        assert error.context["field_name"] == "test_field"

    def test_validation_error_with_none_values(self) -> None:
        """Test validation error handles None values properly."""
        error = FlextOracleOicDataValidationError(
            "Error with None values",
            field_name=None,
            field_value=None,
            validation_rule=None,
            entity_name=None,
        )

        # None values should not be added to context
        assert "field_name" not in error.context
        assert "field_value" not in error.context
        assert "validation_rule" not in error.context
        assert "entity_name" not in error.context


class TestFlextOracleOicApiRequestError:
    """Test API request error with HTTP context."""

    def test_basic_api_request_error(self) -> None:
        """Test basic API request error creation."""
        error = FlextOracleOicApiRequestError("API request failed")
        assert str(error) == "[OIC_API_ERROR] API request failed"
        assert error.code == FlextOracleOicErrorCodes.OIC_API_ERROR.value

    def test_api_request_error_with_http_context(self) -> None:
        """Test API request error with HTTP context."""
        error = FlextOracleOicApiRequestError(
            "HTTP 404 error",
            status_code=404,
            response_body='{"error": "Not found"}',
            entity_name="Integration",
            endpoint="/integrations/test_id",
            method="GET",
        )

        assert str(error) == "[OIC_API_ERROR] HTTP 404 error"
        assert error.context["status_code"] == 404
        assert error.context["response_body"] == '{"error": "Not found"}'
        assert error.context["entity_name"] == "Integration"
        assert error.context["endpoint"] == "/integrations/test_id"
        assert error.context["method"] == "GET"

    def test_api_request_error_response_body_truncation(self) -> None:
        """Test API request error truncates long response bodies."""
        long_response = "x" * 1000  # 1000 character response
        error = FlextOracleOicApiRequestError(
            "Long response error",
            response_body=long_response,
        )

        # Should be truncated to 500 characters
        response_body = error.context["response_body"]
        assert isinstance(response_body, str)
        assert len(response_body) == 500
        assert response_body == "x" * 500

    def test_api_request_error_with_custom_code(self) -> None:
        """Test API request error with custom error code."""
        error = FlextOracleOicApiRequestError(
            "Custom API error",
            code="CUSTOM_API_ERROR",
        )

        assert error.code == "CUSTOM_API_ERROR"

    def test_api_request_error_with_none_values(self) -> None:
        """Test API request error handles None values properly."""
        error = FlextOracleOicApiRequestError(
            "Error with None values",
            status_code=None,
            response_body=None,
            entity_name=None,
            endpoint=None,
            method=None,
        )

        # None values should not be added to context
        assert "status_code" not in error.context
        assert "response_body" not in error.context
        assert "entity_name" not in error.context
        assert "endpoint" not in error.context
        assert "method" not in error.context


class TestFlextOracleOicConfigError:
    """Test configuration error with config context."""

    def test_basic_config_error(self) -> None:
        """Test basic configuration error creation."""
        error = FlextOracleOicConfigError("Configuration invalid")
        assert str(error) == "[OIC_CONFIGURATION_ERROR] Configuration invalid"
        assert error.code == FlextOracleOicErrorCodes.OIC_CONFIGURATION_ERROR.value

    def test_config_error_with_config_context(self) -> None:
        """Test configuration error with config context."""
        error = FlextOracleOicConfigError(
            "Invalid timeout value",
            config_key="request_timeout",
            config_value=0,
            config_section="connection",
            valid_range="1-300 seconds",
        )

        assert str(error) == "[OIC_CONFIGURATION_ERROR] Invalid timeout value"
        assert error.context["config_key"] == "request_timeout"
        assert error.context["config_value"] == 0
        assert error.context["config_section"] == "connection"
        assert error.context["valid_range"] == "1-300 seconds"

    def test_config_error_with_custom_code(self) -> None:
        """Test configuration error with custom error code."""
        error = FlextOracleOicConfigError(
            "Custom config error",
            code="CUSTOM_CONFIG_ERROR",
        )

        assert error.code == "CUSTOM_CONFIG_ERROR"

    def test_config_error_with_none_values(self) -> None:
        """Test configuration error handles None values properly."""
        error = FlextOracleOicConfigError(
            "Error with None values",
            config_key=None,
            config_value=None,
            config_section=None,
            valid_range=None,
        )

        # None values should not be added to context
        assert "config_key" not in error.context
        assert "config_value" not in error.context
        assert "config_section" not in error.context
        assert "valid_range" not in error.context


class TestFlextOracleOicIntegrationPatternError:
    """Test integration pattern error with pattern context."""

    def test_basic_integration_pattern_error(self) -> None:
        """Test basic integration pattern error creation."""
        error = FlextOracleOicIntegrationPatternError("Pattern execution failed")
        assert str(error) == "[OIC_PATTERN_ERROR] Pattern execution failed"
        assert error.code == FlextOracleOicErrorCodes.OIC_PATTERN_ERROR.value

    def test_integration_pattern_error_with_pattern_context(self) -> None:
        """Test integration pattern error with pattern context."""
        error = FlextOracleOicIntegrationPatternError(
            "Message routing pattern failed",
            pattern_name="MessageRouter",
            pattern_type="Enterprise",
            workflow_id="workflow_123",
            step_id="route_step_1",
            operation="route_message",
        )

        assert str(error) == "[OIC_PATTERN_ERROR] Message routing pattern failed"
        assert error.context["pattern_name"] == "MessageRouter"
        assert error.context["pattern_type"] == "Enterprise"
        assert error.context["workflow_id"] == "workflow_123"
        assert error.context["step_id"] == "route_step_1"
        assert error.context["operation"] == "route_message"

    def test_integration_pattern_error_with_custom_code(self) -> None:
        """Test integration pattern error with custom error code."""
        error = FlextOracleOicIntegrationPatternError(
            "Custom pattern error",
            code="CUSTOM_PATTERN_ERROR",
        )

        assert error.code == "CUSTOM_PATTERN_ERROR"

    def test_integration_pattern_error_with_none_values(self) -> None:
        """Test integration pattern error handles None values properly."""
        error = FlextOracleOicIntegrationPatternError(
            "Error with None values",
            pattern_name=None,
            pattern_type=None,
            workflow_id=None,
            step_id=None,
            operation=None,
        )

        # None values should not be added to context
        assert "pattern_name" not in error.context
        assert "pattern_type" not in error.context
        assert "workflow_id" not in error.context
        assert "step_id" not in error.context
        assert "operation" not in error.context


class TestFlextOracleOicWorkflowExecutionError:
    """Test workflow execution error with workflow context."""

    def test_basic_workflow_execution_error(self) -> None:
        """Test basic workflow execution error creation."""
        error = FlextOracleOicWorkflowExecutionError("Workflow step failed")
        assert str(error) == "[OIC_WORKFLOW_ERROR] Workflow step failed"
        assert error.code == FlextOracleOicErrorCodes.OIC_WORKFLOW_ERROR.value

    def test_workflow_execution_error_with_workflow_context(self) -> None:
        """Test workflow execution error with workflow context."""
        error = FlextOracleOicWorkflowExecutionError(
            "Transformation step failed",
            workflow_id="transform_workflow_456",
            execution_id="exec_789",
            step_name="data_transform",
            status="FAILED",
            error_code="TRANSFORM_ERROR",
        )

        assert str(error) == "[OIC_WORKFLOW_ERROR] Transformation step failed"
        assert error.context["workflow_id"] == "transform_workflow_456"
        assert error.context["execution_id"] == "exec_789"
        assert error.context["step_name"] == "data_transform"
        assert error.context["status"] == "FAILED"
        assert error.context["error_code"] == "TRANSFORM_ERROR"

    def test_workflow_execution_error_with_custom_code(self) -> None:
        """Test workflow execution error with custom error code."""
        error = FlextOracleOicWorkflowExecutionError(
            "Custom workflow error",
            code="CUSTOM_WORKFLOW_ERROR",
        )

        assert error.code == "CUSTOM_WORKFLOW_ERROR"

    def test_workflow_execution_error_with_none_values(self) -> None:
        """Test workflow execution error handles None values properly."""
        error = FlextOracleOicWorkflowExecutionError(
            "Error with None values",
            workflow_id=None,
            execution_id=None,
            step_name=None,
            status=None,
            error_code=None,
        )

        # None values should not be added to context
        assert "workflow_id" not in error.context
        assert "execution_id" not in error.context
        assert "step_name" not in error.context
        assert "status" not in error.context
        assert "error_code" not in error.context


class TestFlextOracleOicOAuth2TokenError:
    """Test OAuth2 token error with authentication context."""

    def test_basic_oauth2_token_error(self) -> None:
        """Test basic OAuth2 token error creation."""
        error = FlextOracleOicOAuth2TokenError("Token refresh failed")
        assert str(error) == "[OIC_TOKEN_ERROR] Token refresh failed"
        assert error.code == FlextOracleOicErrorCodes.OIC_TOKEN_ERROR.value

    def test_oauth2_token_error_with_auth_context(self) -> None:
        """Test OAuth2 token error with authentication context."""
        error = FlextOracleOicOAuth2TokenError(
            "Access token expired",
            token_type="bearer",
            client_id="client_123",
            scope="read write",
            grant_type="client_credentials",
            expires_in=3600,
        )

        assert str(error) == "[OIC_TOKEN_ERROR] Access token expired"
        assert error.context["token_type"] == "bearer"
        assert error.context["client_id"] == "client_123"
        assert error.context["scope"] == "read write"
        assert error.context["grant_type"] == "client_credentials"
        assert error.context["expires_in"] == 3600

    def test_oauth2_token_error_with_custom_code(self) -> None:
        """Test OAuth2 token error with custom error code."""
        error = FlextOracleOicOAuth2TokenError(
            "Custom token error",
            code="CUSTOM_TOKEN_ERROR",
        )

        assert error.code == "CUSTOM_TOKEN_ERROR"

    def test_oauth2_token_error_with_none_values(self) -> None:
        """Test OAuth2 token error handles None values properly."""
        error = FlextOracleOicOAuth2TokenError(
            "Error with None values",
            token_type=None,
            client_id=None,
            scope=None,
            grant_type=None,
            expires_in=None,
        )

        # None values should not be added to context
        assert "token_type" not in error.context
        assert "client_id" not in error.context
        assert "scope" not in error.context
        assert "grant_type" not in error.context
        assert "expires_in" not in error.context


class TestExceptionInheritance:
    """Test exception inheritance patterns."""

    def test_data_validation_error_inheritance(self) -> None:
        """Test data validation error inherits from validation error."""
        error = FlextOracleOicDataValidationError("Test error")
        assert isinstance(error, FlextOracleOicValidationError)

    def test_api_request_error_inheritance(self) -> None:
        """Test API request error inherits from API error."""
        error = FlextOracleOicApiRequestError("Test error")
        assert isinstance(error, FlextOracleOicApiError)

    def test_config_error_inheritance(self) -> None:
        """Test config error inherits from configuration error."""
        error = FlextOracleOicConfigError("Test error")
        assert isinstance(error, FlextOracleOicConfigurationError)

    def test_integration_pattern_error_inheritance(self) -> None:
        """Test integration pattern error inherits from pattern error."""
        error = FlextOracleOicIntegrationPatternError("Test error")
        assert isinstance(error, FlextOracleOicPatternError)

    def test_workflow_execution_error_inheritance(self) -> None:
        """Test workflow execution error inherits from workflow error."""
        error = FlextOracleOicWorkflowExecutionError("Test error")
        assert isinstance(error, FlextOracleOicWorkflowError)

    def test_oauth2_token_error_inheritance(self) -> None:
        """Test OAuth2 token error inherits from token error."""
        error = FlextOracleOicOAuth2TokenError("Test error")
        assert isinstance(error, FlextOracleOicTokenError)


class TestExceptionModuleExports:
    """Test module exports are correct."""

    def test_all_exports_exist(self) -> None:
        """Test all expected exports exist in __all__."""
        expected_exports = {
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
        }

        actual_exports = set(exceptions_all)
        assert actual_exports == expected_exports
