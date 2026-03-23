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

**Configuration Management for flext-oracle-oic v0.9.9**

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)

## Overview

flext-oracle-oic provides Pydantic-based configuration management following FLEXT ecosystem patterns. The current implementation offers basic configuration structure with type safety and validation.

> **Implementation Status**: Version 0.9.9 provides foundation configuration models. Full Oracle OIC integration and enterprise features are planned for future releases.

## Current Configuration Components

### Connection Configuration

Configure Oracle Integration Cloud connection parameters using `FlextOracleOicConnectionSettings`:

```python
from flext_oracle_oic import FlextOracleOicConnectionSettings

# Basic connection configuration
connection_config = FlextOracleOicConnectionSettings(
    base_url="https://your-instance.integration.ocp.oraclecloud.com",
    api_version="v1",
    request_timeout=30,
)
```

**Available Parameters:**

- `base_url` (required): Oracle OIC instance URL
- `api_version` (optional): API version, defaults to "v1"
- `request_timeout` (optional): HTTP timeout in seconds, defaults to 30

### Authentication Configuration

Configure OAuth2/IDCS authentication using `FlextOracleOicAuthSettings`:

```python
from flext_oracle_oic import FlextOracleOicAuthSettings

# OAuth2 authentication setup
auth_config = FlextOracleOicAuthSettings(
    oauth_client_id="your_client_id",
    oauth_client_secret="your_client_secret",
    oauth_token_url="https://your-idcs.identity.oraclecloud.com/oauth2/v1/token",
)
```

**Available Parameters:**

- `oauth_client_id` (required): OAuth2 client identifier from Oracle IDCS
- `oauth_client_secret` (required): OAuth2 client secret (SecretStr type)
- `oauth_token_url` (required): OAuth2 token endpoint URL
- Additional OAuth2 parameters (implementation varies by actual fields in models)

### Main Settings Container

Combine configuration components using `OracleOicExtensionSettings`:

```python
from flext_oracle_oic import OracleOicExtensionSettings

# Complete configuration
settings = OracleOicExtensionSettings(connection=connection_config, auth=auth_config)
```

**Primary Configuration Object:**

- `connection` (required): Connection configuration t.NormalizedValue
- `auth` (optional): Authentication configuration t.NormalizedValue
- Additional settings based on actual implementation

## Environment Variables

Environment variables can be used for configuration, though the current implementation requires manual handling:

### Oracle OIC Connection Variables

```bash
# Required Oracle OIC connection settings
export ORACLE_OIC_BASE_URL="https://your-instance.integration.ocp.oraclecloud.com"
export ORACLE_OIC_API_VERSION="v1"
export ORACLE_OIC_REQUEST_TIMEOUT="30"

# OAuth2/IDCS Authentication
export ORACLE_OIC_OAUTH_CLIENT_ID="your_oauth_client_id"
export ORACLE_OIC_OAUTH_CLIENT_SECRET="your_oauth_client_secret"
export ORACLE_OIC_OAUTH_TOKEN_URL="https://your-idcs.identity.oraclecloud.com/oauth2/v1/token"
```

### Loading from Environment

```python
import os
from flext_oracle_oic import (
    OracleOicExtensionSettings,
    FlextOracleOicConnectionSettings,
    FlextOracleOicAuthSettings,
)

# Manual environment variable loading (current approach)
connection_config = FlextOracleOicConnectionSettings(
    base_url=os.getenv("ORACLE_OIC_BASE_URL"),
    api_version=os.getenv("ORACLE_OIC_API_VERSION", "v1"),
    request_timeout=int(os.getenv("ORACLE_OIC_REQUEST_TIMEOUT", "30")),
)

auth_config = FlextOracleOicAuthSettings(
    oauth_client_id=os.getenv("ORACLE_OIC_OAUTH_CLIENT_ID"),
    oauth_client_secret=os.getenv("ORACLE_OIC_OAUTH_CLIENT_SECRET"),
    oauth_token_url=os.getenv("ORACLE_OIC_OAUTH_TOKEN_URL"),
)

settings = OracleOicExtensionSettings(connection=connection_config, auth=auth_config)
```

## Configuration Validation

Pydantic automatically validates configuration objects:

```python
from flext_oracle_oic import (
    OracleOicExtensionSettings,
    FlextOracleOicConnectionSettings,
)

try:
    # Invalid configuration - missing required base_url
    connection_config = FlextOracleOicConnectionSettings()  # Missing base_url
except ValueError as e:
    print(f"Configuration validation error: {e}")

try:
    # Valid configuration
    connection_config = FlextOracleOicConnectionSettings(
        base_url="https://valid-oic-instance.integration.ocp.oraclecloud.com"
    )
    print("✅ Configuration valid")
except ValueError as e:
    print(f"❌ Configuration error: {e}")
```

### Current Validation Rules

Based on the actual Pydantic models implementation:

- **base_url**: Must be provided (required field)
- **oauth_client_id**: Must be provided if auth config is used
- **oauth_client_secret**: Must be provided if auth config is used
- **oauth_token_url**: Must be provided if auth config is used
- **request_timeout**: Must be positive integer (if specified)

## Current Implementation Limitations

### Available Features ✅

- **Pydantic Type Safety**: Automatic validation and type conversion
- **Basic Configuration Models**: Connection and authentication structures
- **Environment Variable Support**: Manual loading from environment
- **Secret String Support**: OAuth2 client secrets use SecretStr

### Missing Features ⚠️

- **Automatic Environment Loading**: No built-in environment variable binding
- **Configuration File Support**: No direct JSON/YAML file loading
- **Environment-Specific Configs**: No dev/staging/prod separation
- **Dynamic Configuration**: No runtime configuration updates
- **Secure Storage Integration**: No Vault or secret manager integration

## Security Considerations

### Current Security Status

**Secret Handling:**

```python
from pydantic import SecretStr
from flext_oracle_oic import FlextOracleOicAuthSettings

# SecretStr prevents accidental logging
auth_config = FlextOracleOicAuthSettings(
    oauth_client_id="public_client_id",
    oauth_client_secret="secret_value",  # Handled as SecretStr internally
    oauth_token_url="https://idcs.example.com/oauth2/v1/token",
)

# Secret is protected from accidental exposure
print(auth_config.oauth_client_secret)  # Shows SecretStr('**********')
```

**Security Recommendations:**

- Use environment variables for all sensitive configuration
- Implement secret rotation for OAuth2 credentials
- Consider Oracle Cloud Vault for production secret management
- Avoid storing secrets in configuration files or version control

## Development Workflow

### Basic Development Setup

```python
import os
from flext_oracle_oic import (
    OracleOicExtensionSettings,
    FlextOracleOicConnectionSettings,
    FlextOracleOicAuthSettings,
)


# Development configuration with environment variables
def create_dev_config():
    connection = FlextOracleOicConnectionSettings(
        base_url=os.getenv("DEV_ORACLE_OIC_BASE_URL", "https://dev-instance.com"),
        api_version="v1",
        request_timeout=60,  # Longer timeout for development
    )

    auth = FlextOracleOicAuthSettings(
        oauth_client_id=os.getenv("DEV_OIC_CLIENT_ID"),
        oauth_client_secret=os.getenv("DEV_OIC_CLIENT_SECRET"),
        oauth_token_url=os.getenv("DEV_OIC_TOKEN_URL"),
    )

    return OracleOicExtensionSettings(connection=connection, auth=auth)


# Create development configuration
dev_settings = create_dev_config()
```

## Troubleshooting

### Common Configuration Issues

**Missing Required Fields:**

```python
from flext_oracle_oic import FlextOracleOicConnectionSettings

# ❌ This will fail - base_url is required
try:
    config = FlextOracleOicConnectionSettings(api_version="v1")
except ValueError as e:
    print(f"Error: {e}")  # Field required error

# ✅ This will work - base_url provided
config = FlextOracleOicConnectionSettings(
    base_url="https://your-instance.integration.ocp.oraclecloud.com"
)
```

**Type Validation Errors:**

```python
# ❌ Wrong type for request_timeout
try:
    config = FlextOracleOicConnectionSettings(
        base_url="https://example.com",
        request_timeout="invalid",  # Should be integer
    )
except ValueError as e:
    print(f"Type error: {e}")

# ✅ Correct type
config = FlextOracleOicConnectionSettings(
    base_url="https://example.com", request_timeout=30
)
```

### Configuration Debugging

```python
from flext_oracle_oic import OracleOicExtensionSettings

# Create and inspect configuration
settings = OracleOicExtensionSettings(connection=connection_config, auth=auth_config)

# Debug connection settings
print(f"Base URL: {settings.connection.base_url}")
print(f"API Version: {settings.connection.api_version}")
print(f"Timeout: {settings.connection.request_timeout}")

# Debug auth settings (careful with secrets)
if settings.auth:
    print(f"Client ID: {settings.auth.oauth_client_id}")
    print(f"Token URL: {settings.auth.oauth_token_url}")
    # oauth_client_secret is SecretStr - won't print actual value
```

## Future Enhancements

The configuration system will be enhanced in future releases with:

- **Automatic Environment Binding**: Direct Pydantic Settings integration
- **Configuration File Support**: JSON, YAML, and TOML file loading
- **Environment-Specific Configs**: Development, staging, production profiles
- **Oracle Cloud Integration**: Native Oracle Vault and IDCS integration
- **Dynamic Configuration**: Runtime configuration updates and validation

______________________________________________________________________

This configuration guide reflects the actual implementation status as of September 17, 2025. The basic Pydantic configuration foundation is implemented, with advanced features planned for future releases.
