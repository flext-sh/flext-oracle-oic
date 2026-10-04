# Configuration

<!-- TOC START -->

- [Overview](#overview)
- [Current Configuration Components](#current-configuration-components)
  - [Connection Configuration](#connection-configuration)
  - [Authentication Configuration](#authentication-configuration)
  - [Main Settings Container](#main-settings-container)
- [Environment Variables](#environment-variables)
  - [Oracle OIC Connection Variables](#oracle-oic-connection-variables)
  - [Loading from Environment](#loading-from-environment)
- [Configuration Validation](#configuration-validation)
  - [Current Validation Rules](#current-validation-rules)
- [Current Implementation Limitations](#current-implementation-limitations)
  - [Available Features ✅](#available-features)
  - [Missing Features ⚠️](#missing-features)
- [Security Considerations](#security-considerations)
  - [Current Security Status](#current-security-status)
- [Development Workflow](#development-workflow)
  - [Basic Development Setup](#basic-development-setup)
- [Troubleshooting](#troubleshooting)
  - [Common Configuration Issues](#common-configuration-issues)
  - [Configuration Debugging](#configuration-debugging)
- [Future Enhancements](#future-enhancements)

<!-- TOC END -->

**Configuration Management for flext-oracle-oic v0.12.0-dev**

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)

## Overview

flext-oracle-oic provides Pydantic-based configuration management following FLEXT
ecosystem patterns. The current implementation offers basic configuration structure with
type safety and validation.

> **Implementation Status**: Version 0.9.9 provides foundation configuration models.
> Full Oracle OIC integration and enterprise features are planned for future releases.

## Current Configuration Components

### Connection Configuration

Configure Oracle Integration Cloud connection parameters using
`m.OracleOic.OICConnectionConfig`:

```python
from flext_oracle_oic import m, settings

connection_config = m.OracleOic.OICConnectionConfig.model_validate(
    settings.OracleOic.model_dump(
        include=set(m.OracleOic.OICConnectionConfig.model_fields),
    ),
)
```

**Available Parameters:**

- `base_url` (required): Oracle OIC instance URL
- `api_version`: API version from `settings.OracleOic.api_version`
- `request_timeout`: HTTP timeout from `settings.OracleOic.request_timeout`

### Authentication Configuration

Validate OAuth2/IDCS authentication using `m.OracleOic.OICAuthConfig`:

```python
from flext_oracle_oic import m, settings

auth_config = m.OracleOic.OICAuthConfig.model_validate(
    settings.OracleOic.model_dump(include=set(m.OracleOic.OICAuthConfig.model_fields)),
)
```

**Available Parameters:**

- `oauth_client_id` (required): OAuth2 client identifier from Oracle IDCS
- `oauth_client_secret` (required): OAuth2 client secret (SecretStr type)
- `oauth_token_url` (required): OAuth2 token endpoint URL
- Additional OAuth2 parameters (implementation varies by actual fields in models)

### Main Settings Container

Connection, authentication, and feature inputs share `FlextOracleOicSettings.OracleOic`:

```python
from flext_oracle_oic import FlextOracleOicSettings, settings

runtime_settings = FlextOracleOicSettings.model_validate(settings.model_dump())
if runtime_settings.OracleOic != settings.OracleOic:
    message = "Settings validation did not preserve the configured namespace"
    raise ValueError(message)
```

**Primary Configuration Object:**

- `OracleOic`: Typed namespace for connection, authentication, and feature inputs.
- Domain models validate the fields selected from this namespace.
- Flat connection/auth keywords are not the settings contract and may be ignored.

## Environment Variables

Settings bind environment inputs automatically using `FLEXT_ORACLE_OIC_` and the
`__` namespace delimiter. Provision credentials outside version control.

### Oracle OIC Connection Variables

```bash
# Require the deployment's configured inputs rather than providing dummy defaults.
: "${FLEXT_ORACLE_OIC_ORACLEOIC__BASE_URL:?Set the OIC instance URL}"
: "${FLEXT_ORACLE_OIC_ORACLEOIC__OAUTH_CLIENT_ID:?Set the OAuth client ID}"
: "${FLEXT_ORACLE_OIC_ORACLEOIC__OAUTH_CLIENT_SECRET:?Set the OAuth secret}"
: "${FLEXT_ORACLE_OIC_ORACLEOIC__OAUTH_TOKEN_URL:?Set the OAuth token endpoint}"
```

### Loading from Environment

```python
from flext_oracle_oic import FlextOracleOicSettings

# Construct after deployment inputs have been provisioned.
runtime_settings = FlextOracleOicSettings()
```

## Configuration Validation

Pydantic automatically validates configuration objects:

```python
from flext_oracle_oic import m, settings

connection_config = m.OracleOic.OICConnectionConfig.model_validate(
    settings.OracleOic.model_dump(
        include=set(m.OracleOic.OICConnectionConfig.model_fields),
    ),
)
if connection_config.request_timeout != settings.OracleOic.request_timeout:
    message = "Connection validation did not preserve the configured timeout"
    raise ValueError(message)
```

### Current Validation Rules

Based on the actual Pydantic models implementation:

- **base_url**: Required string at the domain-model boundary; no URL/nonempty
  validator is declared there. Construction is not a connectivity check.
- **oauth_client_id**: Must be provided if auth settings is used
- **oauth_client_secret**: Must be provided if auth settings is used
- **oauth_token_url**: Must be provided if auth settings is used
- **request_timeout**: Must be positive integer (if specified)

## Current Implementation Limitations

### Available Features ✅

- **Pydantic Type Safety**: Automatic validation and type conversion
- **Basic Configuration Models**: Connection and authentication structures
- **Environment Variable Support**: Automatic namespaced settings binding
- **Secret String Support**: OAuth2 client secrets use SecretStr

### Missing Features ⚠️

- **Configuration File Support**: No direct JSON/YAML file loading
- **Environment-Specific Configs**: No dev/staging/prod separation
- **Dynamic Configuration**: No runtime configuration updates
- **Secure Storage Integration**: No Vault or secret manager integration

## Security Considerations

### Current Security Status

**Secret Handling:**

```python
from flext_oracle_oic import m, settings

auth_config = m.OracleOic.OICAuthConfig.model_validate(
    settings.OracleOic.model_dump(include=set(m.OracleOic.OICAuthConfig.model_fields)),
)

# Validate secret preservation without logging either settings or the secret.
if (
    auth_config.oauth_client_secret.get_secret_value()
    != settings.OracleOic.oauth_client_secret
):
    message = "Authentication validation did not preserve the configured secret"
    raise ValueError(message)
```

**Security Recommendations:**

- Use environment variables for all sensitive configuration
- Implement secret rotation for OAuth2 credentials
- Consider Oracle Cloud Vault for production secret management
- Avoid storing secrets in configuration files or version control

## Development Workflow

### Basic Development Setup

```python
from flext_oracle_oic import FlextOracleOicSettings, settings

# Use the same namespace in development and deployment.
dev_settings = FlextOracleOicSettings.model_validate(settings.model_dump())
if dev_settings.OracleOic.request_timeout != settings.OracleOic.request_timeout:
    message = "Development settings did not preserve the configured timeout"
    raise ValueError(message)
```

## Troubleshooting

### Common Configuration Issues

**Missing Required Domain Fields:**

```python
from flext_oracle_oic import e, m, settings

# Missing required domain fields produce structured Pydantic errors.
try:
    m.OracleOic.OICConnectionConfig.model_validate({})
except e.PydanticValidationError as error:
    if not any(item["loc"] == ("base_url",) for item in error.errors()):
        message = "Expected a missing base_url validation error"
        raise ValueError(message) from error
else:
    message = "Missing base_url must fail domain validation"
    raise AssertionError(message)

connection_config = m.OracleOic.OICConnectionConfig.model_validate(
    settings.OracleOic.model_dump(
        include=set(m.OracleOic.OICConnectionConfig.model_fields),
    ),
)
```

**Type Validation Errors:**

```python
from flext_oracle_oic import e, m, settings

connection_data = settings.OracleOic.model_dump(
    include=set(m.OracleOic.OICConnectionConfig.model_fields),
)
connection_data["request_timeout"] = "invalid"
try:
    m.OracleOic.OICConnectionConfig.model_validate(connection_data)
except e.PydanticValidationError as error:
    if not any(item["loc"] == ("request_timeout",) for item in error.errors()):
        message = "Expected an invalid timeout validation error"
        raise ValueError(message) from error
else:
    message = "Invalid timeout must fail domain validation"
    raise AssertionError(message)
```

### Configuration Debugging

```python
from flext_oracle_oic import settings

# Debug connection settings
print(f"Base URL: {settings.OracleOic.base_url}")
print(f"API Version: {settings.OracleOic.api_version}")
print(f"Timeout: {settings.OracleOic.request_timeout}")

# Debug auth settings (careful with secrets)
print(f"Client ID: {settings.OracleOic.oauth_client_id}")
print(f"Token URL: {settings.OracleOic.oauth_token_url}")
# oauth_client_secret is stored as a plain string in the current settings model
```

## Future Enhancements

The configuration system will be enhanced in future releases with:

- **Configuration File Support**: JSON, YAML, and TOML file loading
- **Environment-Specific Configs**: Development, staging, production profiles
- **Oracle Cloud Integration**: Native Oracle Vault and IDCS integration
- **Dynamic Configuration**: Runtime configuration updates and validation

---

This configuration guide reflects the actual implementation status as of April 14, 2026.
The basic Pydantic configuration foundation is implemented, with advanced features
planned for future releases.
