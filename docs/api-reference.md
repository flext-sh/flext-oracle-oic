# API Reference

**flext-oracle-oic-ext v0.9.0** - Available APIs and Components

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)

> **Implementation Status**: Version 0.9.0 provides basic configuration and service structure. Full Oracle OIC integration capabilities are in development.

## Public API Overview

The current implementation provides foundation configuration classes and basic service structure. All public APIs are available through the main module import.

```python
from flext_oracle_oic_ext import (
    # Configuration classes
    OracleOICExtensionSettings,
    OICExtensionConnectionConfig,
    OICExtensionAuthConfig,

    # Basic service classes (implementation varies)
    # Additional components available but may have limited functionality
)
```

## Configuration API

### OracleOICExtensionSettings

Main configuration container for Oracle OIC extension settings.

```python
from flext_oracle_oic_ext import OracleOICExtensionSettings, OICExtensionConnectionConfig

# Basic configuration creation
settings = OracleOICExtensionSettings(
    connection=OICExtensionConnectionConfig(
        base_url="https://your-instance.integration.ocp.oraclecloud.com"
    )
)
```

**Constructor Parameters:**
- `connection: OICExtensionConnectionConfig` (required) - Connection configuration
- `auth: OICExtensionAuthConfig` (optional) - Authentication configuration
- Additional parameters may vary based on actual implementation

### OICExtensionConnectionConfig

HTTP connection configuration for Oracle Integration Cloud.

```python
from flext_oracle_oic_ext import OICExtensionConnectionConfig

# Basic connection configuration
config = OICExtensionConnectionConfig(
    base_url="https://your-instance.integration.ocp.oraclecloud.com",
    api_version="v1",
    request_timeout=30
)
```

**Constructor Parameters:**
- `base_url: str` (required) - Oracle OIC instance base URL
- `api_version: str` (optional) - API version, defaults to "v1"
- `request_timeout: int` (optional) - Request timeout in seconds, defaults to 30
- Additional parameters based on actual Pydantic model implementation

### OICExtensionAuthConfig

OAuth2/IDCS authentication configuration for Oracle cloud integration.

```python
from flext_oracle_oic_ext import OICExtensionAuthConfig

# OAuth2 authentication setup
auth_config = OICExtensionAuthConfig(
    oauth_client_id="your_client_id",
    oauth_client_secret="your_client_secret",
    oauth_token_url="https://your-idcs.identity.oraclecloud.com/oauth2/v1/token"
)
```

**Constructor Parameters:**
- `oauth_client_id: str` (required) - OAuth2 client ID from Oracle IDCS
- `oauth_client_secret: str` (required) - OAuth2 client secret (uses SecretStr)
- `oauth_token_url: str` (required) - OAuth2 token endpoint URL
- Additional OAuth2 parameters may be available based on implementation

## Available Components

> **Important**: The following components exist in the codebase but may have limited or placeholder functionality. Refer to source code for actual implementation details.

### Service Classes (Implementation Status Varies)

```python
# These components may be available for import but implementation varies
from flext_oracle_oic_ext.ext_services import (
    OracleOICExtensionService,    # Main service class
    OICIntegrationPatternService, # Integration patterns (basic)
    LifecycleManager,            # Lifecycle management (basic)
    MonitoringService            # Monitoring (basic)
)
```

**Usage Note**: Current service implementations provide basic structure. Full Oracle OIC integration capabilities are in development.

### Client Components (FLEXT Compliance Issues)

```python
# HTTP client wrapper (needs FLEXT compliance fixes)
from flext_oracle_oic_ext.ext_client import OracleOICExtensionClient

# Authentication components (basic implementation)
from flext_oracle_oic_ext.ext_services import (
    BaseOICAuthenticator,
    OICExtensionAuthenticator
)
```

**Critical Issue**: Current client implementation uses direct `httpx` imports (line 12 in `ext_client.py`) which violates FLEXT ecosystem standards. Will be refactored to use `flext-api` patterns.

### Data Models

Basic Pydantic data models are available:

```python
from flext_oracle_oic_ext.ext_models import (
    OICIntegrationInfo,  # Integration metadata
    OICConnectionInfo,   # Connection information
    # Additional models based on actual implementation
)
```

## Exception Hierarchy

Oracle OIC-specific exception classes:

```python
from flext_oracle_oic_ext.ext_exceptions import (
    OracleOICExtensionError,    # Base exception
    OICAPIError,                # API operation errors
    OICAuthenticationError,     # Authentication failures
    OICConfigurationError,      # Configuration issues
    OICConnectionError,         # Connection problems
    OICTokenError,              # Token management errors
    # Additional exceptions based on actual implementation
)
```

**Implementation Note**: Exception hierarchy provides structured error handling for Oracle OIC operations.

## Factory and Utility Functions

```python
from flext_oracle_oic_ext.factory import (
    # Factory functions for service creation
    # Implementation details vary
)
```

## Current Implementation Limitations

### Available Features ✅
- **Configuration Management**: Pydantic models with type safety
- **Basic Service Structure**: Foundation classes and module organization
- **Exception Hierarchy**: Oracle OIC-specific error handling
- **Module Organization**: Structured codebase with clear separation

### Critical Issues ❌

**FLEXT Compliance Violations:**
- Direct `httpx` import in `ext_client.py:12` (should use flext-api)
- Direct `typer` import in `main.py:15` (should use flext-cli)
- Missing FlextDomainService inheritance across service classes
- Multiple classes per module violate FLEXT unified class pattern

**Oracle OIC Integration Gaps:**
- No actual Oracle Integration Cloud API connectivity
- OAuth2/IDCS authentication framework incomplete
- No integration pattern execution capabilities
- Missing enterprise features (circuit breaker, retry patterns)

**Type Safety Issues:**
- 2 MyPy errors: `exceptions.py:283` and `test_models.py:61`

### Development Roadmap

**Phase 1: FLEXT Compliance (Critical)**
1. Fix MyPy errors in exceptions and test files
2. Replace direct httpx/typer imports with FLEXT abstractions
3. Implement FlextDomainService inheritance
4. Convert to unified class pattern (single class per module)

**Phase 2: Oracle OIC Implementation**
1. Complete OAuth2/IDCS authentication with Oracle Cloud Identity
2. Implement real Oracle OIC REST API integration
3. Add integration pattern execution engine
4. Enterprise features (circuit breaker, retry, monitoring)

**Phase 3: Production Readiness**
1. Comprehensive testing with real Oracle OIC instances
2. Contract testing for API compliance
3. Performance optimization and monitoring
4. Complete documentation and examples

## API Compatibility

### Import Patterns

```python
# Recommended import pattern for current version
from flext_oracle_oic_ext import (
    OracleOICExtensionSettings,
    OICExtensionConnectionConfig,
    OICExtensionAuthConfig
)

# Create basic configuration
settings = OracleOICExtensionSettings(
    connection=OICExtensionConnectionConfig(
        base_url="https://your-instance.integration.ocp.oraclecloud.com"
    )
)
```

### API Stability

- **Configuration Classes**: Stable API, backward compatibility maintained
- **Exception Classes**: Stable hierarchy, names and structure preserved
- **Service Classes**: Subject to change during FLEXT compliance refactoring
- **Client Classes**: Will be refactored for FLEXT compliance

## Usage Recommendations

### Current Version (v0.9.0)

```python
# Safe to use for configuration and basic setup
from flext_oracle_oic_ext import (
    OracleOICExtensionSettings,
    OICExtensionConnectionConfig,
    OICExtensionAuthConfig
)

# Configuration validation and type safety works correctly
try:
    config = OICExtensionConnectionConfig(
        base_url="https://test-instance.integration.ocp.oraclecloud.com"
    )
    print("✅ Configuration valid")
except ValueError as e:
    print(f"❌ Configuration error: {e}")
```

### Future Versions

API will be enhanced with:
- Complete Oracle OIC integration capabilities
- FLEXT ecosystem compliance
- Professional enterprise features
- Comprehensive testing and validation

---

This API reference reflects the actual implementation status as of September 17, 2025. Version 0.9.0 provides foundation configuration and basic service structure, with significant enhancements planned for FLEXT compliance and Oracle OIC integration.