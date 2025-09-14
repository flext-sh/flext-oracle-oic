# Configuration

**Configuration guide for flext-oracle-oic-ext v0.9.0**

## Overview

flext-oracle-oic-ext uses Pydantic models for type-safe configuration management. All configuration can be provided through code, environment variables, or configuration files.

## Basic Configuration

### Connection Configuration

Configure Oracle Integration Cloud connection parameters:

```python
from flext_oracle_oic_ext import OICExtensionConnectionConfig

connection_config = OICExtensionConnectionConfig(
    base_url="https://your-instance.integration.ocp.oraclecloud.com",
    api_version="v1",
    request_timeout=30,
    max_retries=3
)
```

**Parameters:**
- `base_url` (required): Oracle OIC instance URL
- `api_version` (optional): API version, defaults to "v1"
- `request_timeout` (optional): HTTP timeout in seconds, defaults to 30
- `max_retries` (optional): Retry attempts, defaults to 3

### Authentication Configuration

Configure OAuth2/IDCS authentication:

```python
from flext_oracle_oic_ext import OICExtensionAuthConfig

auth_config = OICExtensionAuthConfig(
    oauth_client_id="your_client_id",
    oauth_client_secret="your_client_secret",
    oauth_token_url="https://your-idcs.identity.oraclecloud.com/oauth2/v1/token",
    oauth_client_aud="optional_audience",
    oauth_scope="optional_scope"
)
```

**Parameters:**
- `oauth_client_id` (required): OAuth2 client identifier
- `oauth_client_secret` (required): OAuth2 client secret
- `oauth_token_url` (required): OAuth2 token endpoint URL
- `oauth_client_aud` (optional): OAuth2 audience parameter
- `oauth_scope` (optional): OAuth2 scope parameter

### Main Settings

Combine connection and authentication configuration:

```python
from flext_oracle_oic_ext import OracleOICExtensionSettings

settings = OracleOICExtensionSettings(
    connection=connection_config,
    auth=auth_config,
    enable_monitoring=True,
    enable_enterprise_patterns=True
)
```

**Parameters:**
- `connection` (required): Connection configuration object
- `auth` (required): Authentication configuration object
- `enable_monitoring` (optional): Enable monitoring features, defaults to True
- `enable_enterprise_patterns` (optional): Enable pattern features, defaults to True

## Environment Variables

Configuration can be loaded from environment variables using the `from_dict` method:

### Required Environment Variables

```bash
# Oracle OIC Connection
export ORACLE_OIC_BASE_URL="https://your-instance.integration.ocp.oraclecloud.com"
export ORACLE_OIC_API_VERSION="v1"
export ORACLE_OIC_REQUEST_TIMEOUT="30"
export ORACLE_OIC_MAX_RETRIES="3"

# OAuth2/IDCS Authentication
export ORACLE_OIC_OAUTH_CLIENT_ID="your_client_id"
export ORACLE_OIC_OAUTH_CLIENT_SECRET="your_client_secret"
export ORACLE_OIC_OAUTH_TOKEN_URL="https://your-idcs.identity.oraclecloud.com/oauth2/v1/token"

# Optional OAuth2 parameters
export ORACLE_OIC_OAUTH_CLIENT_AUD="your_audience"
export ORACLE_OIC_OAUTH_SCOPE="your_scope"

# Feature flags
export ORACLE_OIC_ENABLE_MONITORING="true"
export ORACLE_OIC_ENABLE_ENTERPRISE_PATTERNS="true"
```

### Loading from Environment

```python
import os
from flext_oracle_oic_ext import OracleOICExtensionSettings

# Create configuration dictionary from environment
config_dict = {
    "base_url": os.getenv("ORACLE_OIC_BASE_URL"),
    "api_version": os.getenv("ORACLE_OIC_API_VERSION", "v1"),
    "request_timeout": int(os.getenv("ORACLE_OIC_REQUEST_TIMEOUT", "30")),
    "max_retries": int(os.getenv("ORACLE_OIC_MAX_RETRIES", "3")),
    "oauth_client_id": os.getenv("ORACLE_OIC_OAUTH_CLIENT_ID"),
    "oauth_client_secret": os.getenv("ORACLE_OIC_OAUTH_CLIENT_SECRET"),
    "oauth_token_url": os.getenv("ORACLE_OIC_OAUTH_TOKEN_URL"),
    "oauth_client_aud": os.getenv("ORACLE_OIC_OAUTH_CLIENT_AUD"),
    "oauth_scope": os.getenv("ORACLE_OIC_OAUTH_SCOPE"),
}

# Create settings from dictionary
settings = OracleOICExtensionSettings.from_dict(config_dict)
```

## Configuration Files

### JSON Configuration

Create a `config.json` file:

```json
{
    "base_url": "https://your-instance.integration.ocp.oraclecloud.com",
    "api_version": "v1",
    "request_timeout": 30,
    "max_retries": 3,
    "oauth_client_id": "your_client_id",
    "oauth_client_secret": "your_client_secret",
    "oauth_token_url": "https://your-idcs.identity.oraclecloud.com/oauth2/v1/token",
    "oauth_client_aud": "your_audience",
    "oauth_scope": "your_scope",
    "enable_monitoring": true,
    "enable_enterprise_patterns": true
}
```

Load configuration from file:

```python
import json
from flext_oracle_oic_ext import OracleOICExtensionSettings

# Load from JSON file
with open("config.json", "r") as f:
    config_dict = json.load(f)

settings = OracleOICExtensionSettings.from_dict(config_dict)
```

## Validation

Configuration objects are automatically validated using Pydantic:

```python
from flext_oracle_oic_ext import OracleOICExtensionSettings

try:
    # Invalid configuration (missing required fields)
    settings = OracleOICExtensionSettings.from_dict({
        "base_url": "",  # Empty base_url
        "oauth_client_id": "",  # Empty client_id
    })
except ValueError as e:
    print(f"Configuration validation error: {e}")
```

### Validation Rules

- **base_url**: Must be a valid HTTPS URL
- **oauth_client_id**: Cannot be empty
- **oauth_client_secret**: Cannot be empty
- **oauth_token_url**: Must be a valid HTTPS URL
- **request_timeout**: Must be positive integer
- **max_retries**: Must be non-negative integer

## Security Considerations

### Secret Management

**Current Implementation:**
- OAuth2 client secrets stored as plain strings
- No encryption or secure storage

**Recommendations:**
- Use environment variables for secrets
- Consider secret management systems (Vault, AWS Secrets Manager)
- Avoid storing secrets in configuration files
- Use secure credential rotation practices

### Example with Secret Management

```python
import os
from flext_oracle_oic_ext import OracleOICExtensionSettings

# Load secrets from secure source
def get_secret(key: str) -> str:
    # Implement your secret management logic
    return os.getenv(key)  # Simplified example

config_dict = {
    "base_url": "https://your-instance.integration.ocp.oraclecloud.com",
    "oauth_client_id": get_secret("ORACLE_OIC_CLIENT_ID"),
    "oauth_client_secret": get_secret("ORACLE_OIC_CLIENT_SECRET"),
    "oauth_token_url": "https://your-idcs.identity.oraclecloud.com/oauth2/v1/token",
}

settings = OracleOICExtensionSettings.from_dict(config_dict)
```

## Development vs Production

### Development Configuration

```python
# Development settings with relaxed timeouts
dev_settings = OracleOICExtensionSettings.from_dict({
    "base_url": "https://dev-oic.integration.ocp.oraclecloud.com",
    "api_version": "v1",
    "request_timeout": 60,  # Longer timeout for development
    "max_retries": 1,       # Fewer retries for faster feedback
    "oauth_client_id": "dev_client_id",
    "oauth_client_secret": "dev_client_secret",
    "oauth_token_url": "https://dev-idcs.identity.oraclecloud.com/oauth2/v1/token",
    "enable_monitoring": False,  # Disable monitoring in dev
})
```

### Production Configuration

```python
# Production settings with appropriate timeouts and monitoring
prod_settings = OracleOICExtensionSettings.from_dict({
    "base_url": "https://prod-oic.integration.ocp.oraclecloud.com",
    "api_version": "v1",
    "request_timeout": 30,
    "max_retries": 3,
    "oauth_client_id": get_secret("PROD_OIC_CLIENT_ID"),
    "oauth_client_secret": get_secret("PROD_OIC_CLIENT_SECRET"),
    "oauth_token_url": "https://prod-idcs.identity.oraclecloud.com/oauth2/v1/token",
    "enable_monitoring": True,   # Enable monitoring in production
    "enable_enterprise_patterns": True,
})
```

## Troubleshooting

### Common Configuration Issues

**1. Invalid URL Format**
```python
# ❌ Incorrect
base_url = "http://insecure-url.com"  # HTTP not allowed

# ✅ Correct
base_url = "https://secure-url.com"
```

**2. Missing Required Fields**
```python
# ❌ Incorrect - missing oauth_client_secret
config = {
    "base_url": "https://example.com",
    "oauth_client_id": "client_id",
    # oauth_client_secret missing
}

# ✅ Correct - all required fields present
config = {
    "base_url": "https://example.com",
    "oauth_client_id": "client_id",
    "oauth_client_secret": "client_secret",
    "oauth_token_url": "https://idcs.example.com/oauth2/v1/token",
}
```

**3. Type Conversion Errors**
```python
# ❌ Incorrect - string instead of integer
config = {
    "request_timeout": "30",  # Should be integer
}

# ✅ Correct - proper integer type
config = {
    "request_timeout": 30,
}
```

### Debugging Configuration

```python
from flext_oracle_oic_ext import OracleOICExtensionSettings

# Create settings
settings = OracleOICExtensionSettings.from_dict(config_dict)

# Debug connection configuration
print(f"Base URL: {settings.connection.base_url}")
print(f"API Version: {settings.connection.api_version}")
print(f"Timeout: {settings.connection.request_timeout}")

# Debug authentication configuration (be careful with secrets)
print(f"Client ID: {settings.auth.oauth_client_id}")
print(f"Token URL: {settings.auth.oauth_token_url}")
# Never print client_secret in logs!

# Debug feature flags
print(f"Monitoring enabled: {settings.enable_monitoring}")
print(f"Enterprise patterns enabled: {settings.enable_enterprise_patterns}")
```

---

**Note**: Configuration management is currently basic and will be enhanced with environment-specific settings, secure credential management, and dynamic configuration updates in future releases.