# API Reference

<!-- TOC START -->

- [Public API Overview](#public-api-overview)
- [Configuration API](#configuration-api)
  - [OracleOicExtensionSettings](#oracleoicextensionsettings)
  - [FlextOracleOicConnectionSettings](#flextoracleoicconnectionsettings)
  - [FlextOracleOicAuthSettings](#flextoracleoicauthsettings)
- [Available Components](#available-components)
  - [Service Classes (Implementation Status Varies)](#service-classes-implementation-status-varies)
  - [Client Components (FLEXT Compliance Issues)](#client-components-flext-compliance-issues)
  - [Data Models](#data-models)
- [Exception Hierarchy](#exception-hierarchy)
- [Factory and Utility Functions](#factory-and-utility-functions)
- [Current Implementation Limitations](#current-implementation-limitations)
  - [Available Features ✅](#available-features)
  - [Critical Issues ❌](#critical-issues)
  - [Development Roadmap](#development-roadmap)
- [API Compatibility](#api-compatibility)
  - [Import Patterns](#import-patterns)
  - [API Stability](#api-stability)
- [Usage Recommendations](#usage-recommendations)
  - [Current Version (v0.9.9)](#current-version-v099)
  - [Future Versions](#future-versions)
- [Related Documentation](#related-documentation)

<!-- TOC END -->

**flext-oracle-oic v0.9.9** - Available APIs and Components

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)

> **Implementation Status**: Version 0.9.9 provides basic configuration and service structure. Full Oracle OIC integration capabilities are in development.

## Public API Overview

The current implementation provides foundation configuration classes and basic service structure. All public APIs are available through the main module import.

```python
from flext_oracle_oic import (
    # Configuration classes
    OracleOicExtensionSettings,
    FlextOracleOicConnectionSettings,
    FlextOracleOicAuthSettings,

    # Basic service classes (implementation varies)
    # Additional components available but may have limited functionality
)
```

## Configuration API

### OracleOicExtensionSettings

Main configuration container for Oracle OIC extension settings.

```python
from flext_oracle_oic import OracleOicExtensionSettings, FlextOracleOicConnectionSettings

# Basic configuration creation
settings = OracleOicExtensionSettings(
    connection=FlextOracleOicConnectionSettings(
        base_url="https://your-instance.integration.ocp.oraclecloud.com"
    )
)
```

**Constructor Parameters:**

- `connection: FlextOracleOicConnectionSettings` (required) - Connection configuration
- `auth: FlextOracleOicAuthSettings` (optional) - Authentication configuration
- Additional parameters may vary based on actual implementation

### FlextOracleOicConnectionSettings

HTTP connection configuration for Oracle Integration Cloud.

```python
from flext_oracle_oic import FlextOracleOicConnectionSettings

# Basic connection configuration
config = FlextOracleOicConnectionSettings(
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

### FlextOracleOicAuthSettings

OAuth2/IDCS authentication configuration for Oracle cloud integration.

```python
from flext_oracle_oic import FlextOracleOicAuthSettings

# OAuth2 authentication setup
auth_config = FlextOracleOicAuthSettings(
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
from flext_oracle_oic.ext_services import (
    OracleOicExtensionService,    # Main service class
    OICIntegrationPatternService, # Integration patterns (basic)
    LifecycleManager,            # Lifecycle management (basic)
    MonitoringService            # Monitoring (basic)
)
```

**Usage Note**: Current service implementations provide basic structure. Full Oracle OIC integration capabilities are in development.

### Client Components (FLEXT Compliance Issues)

```python
# HTTP client wrapper (needs FLEXT compliance fixes)
from flext_oracle_oic.ext_client import OracleOicExtensionClient

# Authentication components (basic implementation)
from flext_oracle_oic.ext_services import (
    BaseOICAuthenticator,
    FlextOracleOicAuthenticator
)
```

**Critical Issue**: Current client implementation uses direct `httpx` imports (line 12 in `ext_client.py`) which violates FLEXT ecosystem standards. Will be refactored to use `flext-api` patterns.

### Data Models

Basic Pydantic data models are available:

```python
from flext_oracle_oic.ext_models import (
    OICIntegrationInfo,  # Integration metadata
    OICConnectionInfo,   # Connection information
    # Additional models based on actual implementation
)
```

## Exception Hierarchy

Oracle OIC-specific exception classes:

```python
from flext_oracle_oic.ext_exceptions import (
    OracleOicExtensionError,    # Base exception
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
from flext_oracle_oic.factory import (
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
- Missing FlextService inheritance across service classes
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
1. Replace direct httpx/typer imports with FLEXT abstractions
1. Implement FlextService inheritance
1. Convert to unified class pattern (single class per module)

**Phase 2: Oracle OIC Implementation**

1. Complete OAuth2/IDCS authentication with Oracle Cloud Identity
1. Implement real Oracle OIC REST API integration
1. Add integration pattern execution engine
1. Enterprise features (circuit breaker, retry, monitoring)

**Phase 3: Production Readiness**

1. Comprehensive testing with real Oracle OIC instances
1. Contract testing for API compliance
1. Performance optimization and monitoring
1. Complete documentation and examples

## API Compatibility

### Import Patterns

```python
# Recommended import pattern for current version
from flext_oracle_oic import (
    OracleOicExtensionSettings,
    FlextOracleOicConnectionSettings,
    FlextOracleOicAuthSettings
)

# Create basic configuration
settings = OracleOicExtensionSettings(
    connection=FlextOracleOicConnectionSettings(
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

### Current Version (v0.9.9)

```python
# Safe to use for configuration and basic setup
from flext_oracle_oic import (
    OracleOicExtensionSettings,
    FlextOracleOicConnectionSettings,
    FlextOracleOicAuthSettings
)

# Configuration validation and type safety works correctly
try:
    config = FlextOracleOicConnectionSettings(
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

______________________________________________________________________

This API reference reflects the actual implementation status as of September 17, 2025. Version 0.9.9 provides foundation configuration and basic service structure, with significant enhancements planned for FLEXT compliance and Oracle OIC integration.

## Related Documentation

**Within Project**:

- [Getting Started](getting-started.md) - Installation and basic usage
- [Architecture](architecture.md) - Architecture and design patterns
- [Integration](integration.md) - Integration patterns
- [Troubleshooting](troubleshooting.md) - Common issues

**Across Projects**:

- [flext-core Foundation](https://github.com/organization/flext/tree/main/flext-core/docs/api-reference/foundation.md) - Core APIs and patterns
- [flext-core Railway-Oriented Programming](https://github.com/organization/flext/tree/main/flext-core/docs/guides/railway-oriented-programming.md) - FlextResult patterns
- [flext-db-oracle Integration](https://github.com/organization/flext/tree/main/flext-db-oracle/CLAUDE.md) - Oracle database integration

**External Resources**:

- [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
