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
  - [Current Version (v0.12.0-dev)](#current-version-v0120-dev)
  - [Future Versions](#future-versions)
- [Related Documentation](#related-documentation)

<!-- TOC END -->

**flext-oracle-oic v0.12.0-dev** - Available APIs and Components

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)

> **Implementation Status**: Version 0.9.9 provides basic configuration and service
> structure. Full Oracle OIC integration capabilities are in development.

## Public API Overview

The current implementation provides foundation configuration classes and basic service
structure. All public APIs are available through the main module import.

```python
from flext_oracle_oic import FlextOracleOicApi, settings

api = FlextOracleOicApi(settings=settings)
assert api.fetch_connection_context().unwrap()["base_url"] == settings.OracleOic.base_url
```

## Configuration API

### FlextOracleOicSettings

Main configuration container for Oracle OIC extension settings.

```python
from flext_oracle_oic import FlextOracleOicSettings, settings

# Validate the same namespaced settings the runtime consumes.
runtime_settings = FlextOracleOicSettings.model_validate(settings.model_dump())
```

**Constructor Parameters:**

- `OracleOic` contains the connection, authentication, and feature settings.
- Settings are loaded from the environment; domain models validate their ranges.
- Flat connection or authentication keywords are not the namespaced settings contract.

### OICConnectionConfig

HTTP connection configuration for Oracle Integration Cloud.

```python
from flext_oracle_oic import m, settings

connection_config = m.OracleOic.OICConnectionConfig.model_validate(
    settings.OracleOic.model_dump(
        include=set(m.OracleOic.OICConnectionConfig.model_fields)
    ),
)
```

**Constructor Parameters:**

- `settings.OracleOic.base_url` selects the Oracle OIC instance.
- `settings.OracleOic.api_version` selects the API version.
- `settings.OracleOic.request_timeout` controls the request timeout.
- Defaults and validation constraints belong to the settings and model owners.

### OICAuthConfig

OAuth2/IDCS authentication configuration for Oracle cloud integration.

```python
from flext_oracle_oic import m, settings

auth_config = m.OracleOic.OICAuthConfig.model_validate(
    settings.OracleOic.model_dump(include=set(m.OracleOic.OICAuthConfig.model_fields))
)
```

**Constructor Parameters:**

- Supply credentials through the declared environment settings, never literal examples.
- The prefix is `FLEXT_ORACLE_OIC_`, with `__` separating the namespace and field.
- The domain authentication model wraps the secret in `SecretStr`; do not print it.
- Model construction alone does not prove successful authentication or connectivity.

## Available Components

> **Important**: The following components exist in the codebase but may have limited or
> placeholder functionality. Refer to source code for actual implementation details.

### Service Classes (Implementation Status Varies)

```python
from flext_oracle_oic import FlextOracleOicApi, settings

api = FlextOracleOicApi(settings=settings)
assert api.fetch_features_context().unwrap()["verify_ssl"] == settings.OracleOic.verify_ssl
```

**Usage Note**: Current service implementations provide basic structure. Full Oracle OIC
integration capabilities are in development.

### Client Components (FLEXT Compliance Issues)

```python
from flext_oracle_oic import FlextOracleOicClient, m, settings

connection_config = m.OracleOic.OICConnectionConfig.model_validate(
    settings.OracleOic.model_dump(
        include=set(m.OracleOic.OICConnectionConfig.model_fields)
    )
)
auth_config = m.OracleOic.OICAuthConfig.model_validate(
    settings.OracleOic.model_dump(include=set(m.OracleOic.OICAuthConfig.model_fields))
)
client = FlextOracleOicClient(
    connection_config=connection_config, auth_config=auth_config
)
```

`FlextOracleOicClient` accepts both validated connection and authentication models.
Construction does not contact Oracle; network operations require configured credentials
and a reachable instance. HTTP operations use the upstream `FlextApi` facade.

### Data Models

Basic Pydantic data models are available:

```python
from flext_oracle_oic import m

integration_fields = tuple(m.OracleOic.OICIntegrationInfo.model_fields)
```

## Exception Hierarchy

Oracle OIC-specific exception classes:

```python
from flext_oracle_oic import e

# Structured exception classes via the shared `e` facade
base_error = e.BaseError  # Base exception
auth_error = e.AuthenticationError  # Authentication failures
config_error = e.ConfigurationError  # Configuration issues
connection_error = e.ConnectionError  # Connection problems
```

**Implementation Note**: Exception hierarchy provides structured error handling for
Oracle OIC operations.

## Factory and Utility Functions

Use the public `FlextOracleOicApi` composition root rather than undocumented factory
functions. Successful network operations require configured Oracle credentials and a
reachable instance.

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
- Missing s inheritance across service classes
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
1. Implement s inheritance
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
from flext_oracle_oic import FlextOracleOicSettings, settings

runtime_settings = FlextOracleOicSettings.model_validate(settings.model_dump())
assert runtime_settings.OracleOic == settings.OracleOic
```

### API Stability

- **Configuration Classes**: Stable API, backward compatibility maintained
- **Exception Classes**: Stable hierarchy, names and structure preserved
- **Service Classes**: Subject to change during FLEXT compliance refactoring
- **Client Classes**: Will be refactored for FLEXT compliance

## Usage Recommendations

### Current Version (v0.12.0-dev)

```python
from flext_oracle_oic import m, settings

connection_config = m.OracleOic.OICConnectionConfig.model_validate(
    settings.OracleOic.model_dump(
        include=set(m.OracleOic.OICConnectionConfig.model_fields)
    )
)
assert connection_config.base_url == settings.OracleOic.base_url
```

### Future Versions

API will be enhanced with:

- Complete Oracle OIC integration capabilities
- FLEXT ecosystem compliance
- Professional enterprise features
- Comprehensive testing and validation

---

This API reference reflects the actual implementation status as of April 14, 2026.
Version 0.9.9 provides foundation configuration and basic service structure, with
significant enhancements planned for FLEXT compliance and Oracle OIC integration.

## Related Documentation

**Within Project**:

- [Getting Started](getting-started.md) - Installation and basic usage
- [Architecture](architecture.md) - Architecture and design patterns
- [Integration](integration.md) - Integration patterns
- [Troubleshooting](troubleshooting.md) - Common issues

**Across Projects**:

- [flext-core Foundation](https://github.com/flext-sh/flext/tree/0.12.0-dev/flext-core/docs/api-reference/foundation.md) -
  Core APIs and patterns
- [flext-core Railway-Oriented Programming](https://github.com/flext-sh/flext/tree/0.12.0-dev/flext-core/docs/guides/railway-oriented-programming.md) -
  r patterns
- [flext-db-oracle Integration](https://github.com/flext-sh/flext/tree/0.12.0-dev/flext-db-oracle/AGENTS.md) -
  Oracle database integration

**External Resources**:

- [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
