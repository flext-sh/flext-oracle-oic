# API Reference

**flext-oracle-oic-ext v0.9.0 API Documentation**

> **Status**: Early Development - Many APIs are basic implementations and subject to change

## Configuration Classes

### OracleOICExtensionSettings

Main configuration container for Oracle OIC extension settings.

```python
from flext_oracle_oic_ext import OracleOICExtensionSettings

settings = OracleOICExtensionSettings(
    connection=OICExtensionConnectionConfig(...),
    auth=OICExtensionAuthConfig(...),
    enable_monitoring=True,
    enable_enterprise_patterns=True
)
```

**Attributes:**
- `connection: OICExtensionConnectionConfig` - Connection configuration
- `auth: OICExtensionAuthConfig` - Authentication configuration
- `enable_monitoring: bool` - Enable monitoring features (default: True)
- `enable_enterprise_patterns: bool` - Enable enterprise patterns (default: True)

### OICExtensionConnectionConfig

HTTP connection configuration for Oracle OIC.

```python
from flext_oracle_oic_ext import OICExtensionConnectionConfig

config = OICExtensionConnectionConfig(
    base_url="https://your-instance.integration.ocp.oraclecloud.com",
    api_version="v1",
    request_timeout=30,
    max_retries=3
)
```

**Attributes:**
- `base_url: str` - Oracle OIC instance base URL
- `api_version: str` - API version (default: "v1")
- `request_timeout: int` - Request timeout in seconds (default: 30)
- `max_retries: int` - Maximum retry attempts (default: 3)

### OICExtensionAuthConfig

OAuth2/IDCS authentication configuration.

```python
from flext_oracle_oic_ext import OICExtensionAuthConfig

auth_config = OICExtensionAuthConfig(
    oauth_client_id="your_client_id",
    oauth_client_secret="your_client_secret",
    oauth_token_url="https://your-idcs.identity.oraclecloud.com/oauth2/v1/token",
    oauth_client_aud="your_audience",
    oauth_scope="your_scope"
)
```

**Attributes:**
- `oauth_client_id: str` - OAuth2 client ID
- `oauth_client_secret: str` - OAuth2 client secret
- `oauth_token_url: str` - OAuth2 token endpoint URL
- `oauth_client_aud: str` - OAuth2 audience (optional)
- `oauth_scope: str` - OAuth2 scope (optional)

## Service Classes

### OracleOICExtensionService

Main service class for Oracle OIC operations.

```python
from flext_oracle_oic_ext import OracleOICExtensionService, OracleOICExtensionSettings

service = OracleOICExtensionService(settings)
```

**Methods:**

#### `__init__(settings: OracleOICExtensionSettings) -> None`
Initialize the service with configuration settings.

> **Note**: Current implementation provides basic structure only. Full Oracle OIC integration in development.

### OICIntegrationPatternService

Service for integration pattern operations (basic implementation).

```python
from flext_oracle_oic_ext import OICIntegrationPatternService

pattern_service = OICIntegrationPatternService()
```

> **Status**: Placeholder implementation - Integration patterns not yet implemented

### LifecycleManager

Basic lifecycle management for Oracle OIC operations.

```python
from flext_oracle_oic_ext import LifecycleManager

manager = LifecycleManager(settings)
```

**Methods:**

#### `__init__(settings: OracleOICExtensionSettings) -> None`
Initialize lifecycle manager with settings.

### MonitoringService

Basic monitoring service for Oracle OIC operations.

```python
from flext_oracle_oic_ext import MonitoringService
import requests

session = requests.Session()
monitoring = MonitoringService(session)
```

**Methods:**

#### `__init__(client: HTTPClientProtocol) -> None`
Initialize monitoring service with HTTP client.

> **Note**: Currently requires a requests.Session object. Will be updated to use FLEXT patterns.

## Client Classes

### OracleOICExtensionClient

HTTP client for Oracle OIC API operations.

```python
from flext_oracle_oic_ext import OracleOICExtensionClient

client = OracleOICExtensionClient(connection_config, auth_config)
```

> **Critical Issue**: Currently uses direct httpx which violates FLEXT standards. Will be refactored to use flext-api.

### BaseOICAuthenticator

Abstract base class for Oracle OIC authentication.

```python
from flext_oracle_oic_ext import BaseOICAuthenticator

# This is an abstract class - use concrete implementations
```

**Abstract Methods:**
- `get_oauth_scopes() -> str` - Get OAuth2 scopes for authentication

### OICExtensionAuthenticator

OAuth2 authenticator implementation for Oracle OIC.

```python
from flext_oracle_oic_ext import OICExtensionAuthenticator

authenticator = OICExtensionAuthenticator(auth_config)
```

**Methods:**

#### `get_oauth_scopes() -> str`
Returns OAuth2 scopes for Oracle OIC authentication.

> **Status**: Basic implementation - Full OAuth2/IDCS integration in development

## Data Models

### OICIntegrationInfo

Model for Oracle OIC integration information.

```python
from flext_oracle_oic_ext import OICIntegrationInfo

integration = OICIntegrationInfo(
    integration_id="int_001",
    name="Test Integration",
    version="1.0.0",
    status=IntegrationStatus.ACTIVE
)
```

**Attributes:**
- `integration_id: str` - Unique integration identifier
- `name: str` - Integration display name
- `version: str` - Integration version
- `status: IntegrationStatus` - Current status

### OICConnectionInfo

Model for Oracle OIC connection information.

```python
from flext_oracle_oic_ext import OICConnectionInfo

connection = OICConnectionInfo(
    connection_id="conn_001",
    name="Test Connection",
    connection_type="REST",
    endpoint_url="https://api.example.com"
)
```

**Attributes:**
- `connection_id: str` - Unique connection identifier
- `name: str` - Connection display name
- `connection_type: str` - Type of connection
- `endpoint_url: str` - Connection endpoint URL

### IntegrationStatus

Enumeration for integration status values.

```python
from flext_oracle_oic_ext import IntegrationStatus

# Available status values:
IntegrationStatus.ACTIVE     # Integration is active
IntegrationStatus.INACTIVE   # Integration is inactive
IntegrationStatus.DRAFT      # Integration is in draft state
IntegrationStatus.ERROR      # Integration has errors
```

## Exception Classes

### OracleOICExtensionError

Base exception for Oracle OIC extension errors.

```python
from flext_oracle_oic_ext import OracleOICExtensionError

try:
    # Some Oracle OIC operation
    pass
except OracleOICExtensionError as e:
    print(f"Oracle OIC error: {e}")
```

### Specific Exception Types

```python
from flext_oracle_oic_ext import (
    OICAPIError,              # API operation errors
    OICAuthenticationError,   # Authentication failures
    OICConfigurationError,    # Configuration issues
    OICConnectionError,       # Connection problems
    OICIntegrationError,      # Integration execution errors
    OICPatternError,          # Integration pattern errors
    OICTimeoutError,          # Timeout errors
    OICTokenError,            # Token management errors
    OICValidationError,       # Data validation errors
    OICWorkflowError          # Workflow execution errors
)
```

## Factory Functions

### create_oic_extension_service

Factory function to create OracleOICExtensionService instances.

```python
from flext_oracle_oic_ext import create_oic_extension_service

# Create service with default configuration
service_result = create_oic_extension_service()
if service_result.is_success:
    service = service_result.unwrap()
```

**Returns:** `FlextResult[OracleOICExtensionService]`

### create_development_oic_service

Factory function for development/testing scenarios.

```python
from flext_oracle_oic_ext import create_development_oic_service

# Create development service
dev_service_result = create_development_oic_service()
if dev_service_result.is_success:
    service = dev_service_result.unwrap()
```

**Returns:** `FlextResult[OracleOICExtensionService]`

## CLI Interface

### Extension Commands

The extension provides CLI commands through the OracleOICExtension class:

```bash
# Lifecycle commands
oracle-oic-ext lifecycle:activate
oracle-oic-ext lifecycle:deactivate
oracle-oic-ext lifecycle:status

# Monitoring commands
oracle-oic-ext monitor:health
oracle-oic-ext monitor:performance
oracle-oic-ext monitor:errors
oracle-oic-ext monitor:usage

# Extraction commands
oracle-oic-ext extract:artifacts
oracle-oic-ext extract:logs
oracle-oic-ext extract:metadata
```

> **Critical Issue**: CLI implementation uses direct typer which violates FLEXT standards. Will be refactored to use flext-cli.

## Current Limitations

### API Limitations
- **No real Oracle OIC API calls** - Basic structure only
- **Authentication incomplete** - OAuth2/IDCS integration in development
- **Pattern operations not implemented** - Enterprise Integration Patterns pending
- **WMS integration missing** - No warehouse management functionality

### FLEXT Compliance Issues
- **Direct httpx usage** - Violates FLEXT standards (should use flext-api)
- **Direct typer usage** - Violates FLEXT standards (should use flext-cli)
- **Missing dependency injection** - Not using FlextContainer
- **Incomplete FlextResult usage** - Some methods still use direct exceptions

### Architecture Issues
- **Multiple classes per module** - Violates unified class pattern
- **Missing domain models** - Basic data models only
- **No Clean Architecture layers** - Flat service structure
- **Language inconsistency** - Portuguese comments in code

## Migration Notes

### Upcoming API Changes
- **HTTP client refactoring** - Will use flext-api instead of httpx
- **CLI refactoring** - Will use flext-cli instead of typer
- **Authentication refactoring** - Will integrate with flext-auth
- **Service refactoring** - Will follow unified class pattern

### Backward Compatibility
- Current API structure will be maintained during refactoring
- Configuration classes will remain compatible
- Exception hierarchy will be preserved
- Factory functions will continue to work

---

**Note**: This API reference reflects the current implementation as of September 2025. Many features are in early development and will be enhanced in future releases.