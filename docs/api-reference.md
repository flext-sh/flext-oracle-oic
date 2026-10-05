# API Reference

<!-- TOC START -->

- [Public API Overview](#public-api-overview)
- [Configuration API](#configuration-api)
  - [FlextOracleOicSettings](#flextoracleoicsettings)
  - [OICConnectionConfig](#oicconnectionconfig)
  - [OICAuthConfig](#oicauthconfig)
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

> **Implementation Status**: Public settings, domain models, client, and service
> operations exist. Offline examples validate these contracts, not successful Oracle
> authentication or deployed integration behavior.

## Public API Overview

The current implementation provides foundation configuration classes and basic service
structure. All public APIs are available through the main module import.

```python
from flext_oracle_oic import FlextOracleOicApi, settings

api = FlextOracleOicApi(settings=settings)
connection_context = api.fetch_connection_context().unwrap()
if connection_context["base_url"] != settings.OracleOic.base_url:
    message = "Connection context did not preserve the configured URL"
    raise ValueError(message)
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
        include=set(m.OracleOic.OICConnectionConfig.model_fields),
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
    settings.OracleOic.model_dump(include=set(m.OracleOic.OICAuthConfig.model_fields)),
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
features_context = api.fetch_features_context().unwrap()
if features_context["verify_ssl"] != settings.OracleOic.verify_ssl:
    message = "Feature context did not preserve configured TLS verification"
    raise ValueError(message)
```

**Usage Note**: Current service implementations provide basic structure. Full Oracle OIC
integration capabilities are in development.

### Client Components (FLEXT Compliance Issues)

```python
from flext_oracle_oic import FlextOracleOicClient, m, settings

connection_config = m.OracleOic.OICConnectionConfig.model_validate(
    settings.OracleOic.model_dump(
        include=set(m.OracleOic.OICConnectionConfig.model_fields),
    ),
)
auth_config = m.OracleOic.OICAuthConfig.model_validate(
    settings.OracleOic.model_dump(include=set(m.OracleOic.OICAuthConfig.model_fields)),
)
client = FlextOracleOicClient(
    connection_config=connection_config,
    auth_config=auth_config,
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
connection_error = e.FlextConnectionError  # Connection problems
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

- The client uses `FlextApi`, the CLI uses `flext-cli`, and the service base inherits
  the upstream `s`; those integrations do not need replacement.
- Remaining facade, composition, and type findings are measured by `make check` and
  `make mod`, not by historical file/line counts in this reference.

**Oracle OIC Integration Gaps:**

- OAuth, integration CRUD, orchestration, and health-check paths are implemented.
- Their existence does not prove successful operations against a configured Oracle
  instance. Validate credentials, response contracts, and lifecycle behavior through
  the public consumer before claiming network readiness.

**Type Safety Issues:**

- `make check` runs the configured lint and type owners; inspect its current receipts.
  Passing the offline examples does not establish a zero-finding project baseline.

### Development Roadmap

**Phase 1: FLEXT Compliance (Critical)**

1. Resolve current lint, type, facade, and composition findings at their owners.
1. Preserve existing HTTP, CLI, and service abstractions while repairing their contracts.
1. Regenerate managed surfaces and verify repeated canonical fixed points.

**Phase 2: Oracle OIC Implementation**

1. Complete OAuth2/IDCS authentication with Oracle Cloud Identity
1. Validate existing Oracle OIC REST operations against the configured service.
1. Verify orchestration and monitoring results through their public contracts.
1. Measure remaining resilience requirements before adding new mechanisms.

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
if runtime_settings.OracleOic != settings.OracleOic:
    message = "Settings validation did not preserve the configured namespace"
    raise ValueError(message)
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
        include=set(m.OracleOic.OICConnectionConfig.model_fields),
    ),
)
if connection_config.base_url != settings.OracleOic.base_url:
    message = "Connection validation did not preserve the configured URL"
    raise ValueError(message)
```

### Future Versions

API will be enhanced with:

- Complete Oracle OIC integration capabilities
- FLEXT ecosystem compliance
- Professional enterprise features
- Comprehensive testing and validation

---

This reference describes public source contracts. Readiness requires current canonical
gate receipts and successful configured runtime validation, not API presence alone.

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
