"""Oracle OIC Extension Legacy Compatibility Layer.

This module provides backward compatibility with older Oracle OIC extension exception patterns.
It maps legacy exception names to their modern FlextErrorMixin equivalents.

⚠️  DEPRECATION WARNING: This module is for backward compatibility only.
    Use the modern exceptions from flext_oracle_oic_ext.exceptions instead.

Copyright (c) 2025 FLEXT Contributors
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import warnings
from collections.abc import Mapping

# Import modern exception system
from flext_oracle_oic_ext.exceptions import (
    FlextOracleOicApiRequestError,
    FlextOracleOicAuthenticationError,
    FlextOracleOicConfigError,
    FlextOracleOicConnectionError,
    FlextOracleOicDataValidationError,
    FlextOracleOicError,
    FlextOracleOicErrorCodes,
    FlextOracleOicIntegrationError,
    FlextOracleOicIntegrationPatternError,
    FlextOracleOicOAuth2TokenError,
    FlextOracleOicTimeoutError,
    FlextOracleOicWorkflowExecutionError,
)


def _issue_deprecation_warning(legacy_name: str, modern_name: str) -> None:
    """Issue deprecation warning for legacy exception usage."""
    warnings.warn(
      f"{legacy_name} is deprecated. Use {modern_name} from "
      f"flext_oracle_oic_ext.exceptions instead.",
      DeprecationWarning,
      stacklevel=3,
    )


# Legacy exception facade functions for backward compatibility
def OracleOICExtensionError(  # noqa: N802
    message: str,
    *,
    code: FlextOracleOicErrorCodes | None = FlextOracleOicErrorCodes.OIC_ERROR,
    context: Mapping[str, object] | None = None,
) -> FlextOracleOicError:
    """Legacy OracleOICExtensionError facade."""
    _issue_deprecation_warning("OracleOICExtensionError", "FlextOracleOicError")
    return FlextOracleOicError(message, code=code, context=context)


def OICAuthenticationError(  # noqa: N802
    message: str,
    *,
    code: FlextOracleOicErrorCodes
    | None = FlextOracleOicErrorCodes.OIC_AUTHENTICATION_ERROR,
    context: Mapping[str, object] | None = None,
) -> FlextOracleOicAuthenticationError:
    """Legacy OICAuthenticationError facade."""
    _issue_deprecation_warning(
      "OICAuthenticationError", "FlextOracleOicAuthenticationError",
    )
    return FlextOracleOicAuthenticationError(message, code=code, context=context)


def OICTokenError(  # noqa: N802
    message: str,
    *,
    token_type: str | None = None,
    client_id: str | None = None,
    scope: str | None = None,
    grant_type: str | None = None,
    expires_in: int | None = None,
    code: FlextOracleOicErrorCodes | None = FlextOracleOicErrorCodes.OIC_TOKEN_ERROR,
    context: Mapping[str, object] | None = None,
) -> FlextOracleOicOAuth2TokenError:
    """Legacy OICTokenError facade."""
    _issue_deprecation_warning("OICTokenError", "FlextOracleOicOAuth2TokenError")
    return FlextOracleOicOAuth2TokenError(
      message,
      token_type=token_type,
      client_id=client_id,
      scope=scope,
      grant_type=grant_type,
      expires_in=expires_in,
      code=code,
      context=context,
    )


def OICConnectionError(  # noqa: N802
    message: str,
    *,
    code: FlextOracleOicErrorCodes
    | None = FlextOracleOicErrorCodes.OIC_CONNECTION_ERROR,
    context: Mapping[str, object] | None = None,
) -> FlextOracleOicConnectionError:
    """Legacy OICConnectionError facade."""
    _issue_deprecation_warning("OICConnectionError", "FlextOracleOicConnectionError")
    return FlextOracleOicConnectionError(message, code=code, context=context)


def OICTimeoutError(  # noqa: N802
    message: str,
    *,
    code: FlextOracleOicErrorCodes | None = FlextOracleOicErrorCodes.OIC_TIMEOUT_ERROR,
    context: Mapping[str, object] | None = None,
) -> FlextOracleOicTimeoutError:
    """Legacy OICTimeoutError facade."""
    _issue_deprecation_warning("OICTimeoutError", "FlextOracleOicTimeoutError")
    return FlextOracleOicTimeoutError(message, code=code, context=context)


def OICAPIError(  # noqa: N802
    message: str,
    *,
    status_code: int | None = None,
    response_body: str | None = None,
    entity_name: str | None = None,
    endpoint: str | None = None,
    method: str | None = None,
    code: FlextOracleOicErrorCodes | None = FlextOracleOicErrorCodes.OIC_API_ERROR,
    context: Mapping[str, object] | None = None,
) -> FlextOracleOicApiRequestError:
    """Legacy OICAPIError facade."""
    _issue_deprecation_warning("OICAPIError", "FlextOracleOicApiRequestError")
    return FlextOracleOicApiRequestError(
      message,
      status_code=status_code,
      response_body=response_body,
      entity_name=entity_name,
      endpoint=endpoint,
      method=method,
      code=code,
      context=context,
    )


def OICValidationError(  # noqa: N802
    message: str,
    *,
    field_name: str | None = None,
    field_value: object | None = None,
    validation_rule: str | None = None,
    entity_name: str | None = None,
    code: FlextOracleOicErrorCodes
    | None = FlextOracleOicErrorCodes.OIC_VALIDATION_ERROR,
    context: Mapping[str, object] | None = None,
) -> FlextOracleOicDataValidationError:
    """Legacy OICValidationError facade."""
    _issue_deprecation_warning(
      "OICValidationError", "FlextOracleOicDataValidationError",
    )
    return FlextOracleOicDataValidationError(
      message,
      field_name=field_name,
      field_value=field_value,
      validation_rule=validation_rule,
      entity_name=entity_name,
      code=code,
      context=context,
    )


def OICIntegrationError(  # noqa: N802
    message: str,
    *,
    code: FlextOracleOicErrorCodes
    | None = FlextOracleOicErrorCodes.OIC_INTEGRATION_ERROR,
    context: Mapping[str, object] | None = None,
) -> FlextOracleOicIntegrationError:
    """Legacy OICIntegrationError facade."""
    _issue_deprecation_warning("OICIntegrationError", "FlextOracleOicIntegrationError")
    return FlextOracleOicIntegrationError(message, code=code, context=context)


def OICWorkflowError(  # noqa: N802
    message: str,
    *,
    workflow_id: str | None = None,
    execution_id: str | None = None,
    step_name: str | None = None,
    status: str | None = None,
    error_code: str | None = None,
    code: FlextOracleOicErrorCodes | None = FlextOracleOicErrorCodes.OIC_WORKFLOW_ERROR,
    context: Mapping[str, object] | None = None,
) -> FlextOracleOicWorkflowExecutionError:
    """Legacy OICWorkflowError facade."""
    _issue_deprecation_warning(
      "OICWorkflowError", "FlextOracleOicWorkflowExecutionError",
    )
    return FlextOracleOicWorkflowExecutionError(
      message,
      workflow_id=workflow_id,
      execution_id=execution_id,
      step_name=step_name,
      status=status,
      error_code=error_code,
      code=code,
      context=context,
    )


def OICConfigurationError(  # noqa: N802
    message: str,
    *,
    config_key: str | None = None,
    config_value: object | None = None,
    config_section: str | None = None,
    valid_range: str | None = None,
    code: FlextOracleOicErrorCodes
    | None = FlextOracleOicErrorCodes.OIC_CONFIGURATION_ERROR,
    context: Mapping[str, object] | None = None,
) -> FlextOracleOicConfigError:
    """Legacy OICConfigurationError facade."""
    _issue_deprecation_warning("OICConfigurationError", "FlextOracleOicConfigError")
    return FlextOracleOicConfigError(
      message,
      config_key=config_key,
      config_value=config_value,
      config_section=config_section,
      valid_range=valid_range,
      code=code,
      context=context,
    )


def OICPatternError(  # noqa: N802
    message: str,
    *,
    pattern_name: str | None = None,
    pattern_type: str | None = None,
    workflow_id: str | None = None,
    step_id: str | None = None,
    operation: str | None = None,
    code: FlextOracleOicErrorCodes | None = FlextOracleOicErrorCodes.OIC_PATTERN_ERROR,
    context: Mapping[str, object] | None = None,
) -> FlextOracleOicIntegrationPatternError:
    """Legacy OICPatternError facade."""
    _issue_deprecation_warning(
      "OICPatternError", "FlextOracleOicIntegrationPatternError",
    )
    return FlextOracleOicIntegrationPatternError(
      message,
      pattern_name=pattern_name,
      pattern_type=pattern_type,
      workflow_id=workflow_id,
      step_id=step_id,
      operation=operation,
      code=code,
      context=context,
    )


# Legacy API functions for Oracle OIC extension patterns
def create_legacy_error_context(
    operation: str,
    entity_id: str | None = None,
    entity_type: str | None = None,
    **kwargs: object,
) -> dict[str, object]:
    """Create legacy error context for backward compatibility."""
    _issue_deprecation_warning(
      "create_legacy_error_context",
      "direct context dict creation",
    )
    context: dict[str, object] = {"operation": operation}
    if entity_id is not None:
      context["entity_id"] = entity_id
    if entity_type is not None:
      context["entity_type"] = entity_type
    context.update(kwargs)
    return context


def get_legacy_error_code(error_type: str) -> FlextOracleOicErrorCodes:
    """Get legacy error code mapping for backward compatibility."""
    _issue_deprecation_warning(
      "get_legacy_error_code",
      "FlextOracleOicErrorCodes enum directly",
    )
    mapping = {
      "authentication": FlextOracleOicErrorCodes.OIC_AUTHENTICATION_ERROR,
      "connection": FlextOracleOicErrorCodes.OIC_CONNECTION_ERROR,
      "api": FlextOracleOicErrorCodes.OIC_API_ERROR,
      "validation": FlextOracleOicErrorCodes.OIC_VALIDATION_ERROR,
      "integration": FlextOracleOicErrorCodes.OIC_INTEGRATION_ERROR,
      "workflow": FlextOracleOicErrorCodes.OIC_WORKFLOW_ERROR,
      "configuration": FlextOracleOicErrorCodes.OIC_CONFIGURATION_ERROR,
      "pattern": FlextOracleOicErrorCodes.OIC_PATTERN_ERROR,
      "token": FlextOracleOicErrorCodes.OIC_TOKEN_ERROR,
      "timeout": FlextOracleOicErrorCodes.OIC_TIMEOUT_ERROR,
    }
    return mapping.get(error_type.lower(), FlextOracleOicErrorCodes.OIC_ERROR)


# Legacy constants for Oracle OIC extension operations
LEGACY_OIC_ERROR_MAPPING = {
    "OracleOICExtensionError": "FlextOracleOicError",
    "OICAuthenticationError": "FlextOracleOicAuthenticationError",
    "OICTokenError": "FlextOracleOicOAuth2TokenError",
    "OICConnectionError": "FlextOracleOicConnectionError",
    "OICTimeoutError": "FlextOracleOicTimeoutError",
    "OICAPIError": "FlextOracleOicApiRequestError",
    "OICValidationError": "FlextOracleOicDataValidationError",
    "OICIntegrationError": "FlextOracleOicIntegrationError",
    "OICWorkflowError": "FlextOracleOicWorkflowExecutionError",
    "OICConfigurationError": "FlextOracleOicConfigError",
    "OICPatternError": "FlextOracleOicIntegrationPatternError",
}

LEGACY_OIC_OPERATIONS = [
    "activate_integration",
    "deactivate_integration",
    "deploy_integration",
    "monitor_integration",
    "extract_artifacts",
    "extract_logs",
    "extract_metadata",
    "validate_workflow",
    "execute_pattern",
]

__all__: list[str] = [
    # Legacy constants
    "LEGACY_OIC_ERROR_MAPPING",
    "LEGACY_OIC_OPERATIONS",
    # Legacy exception facades
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
    # Legacy utility functions
    "create_legacy_error_context",
    "get_legacy_error_code",
]
