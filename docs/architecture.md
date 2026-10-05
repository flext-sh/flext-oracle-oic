# Architecture

<!-- TOC START -->

- [Overview](#overview)
  - [Architecture Principles](#architecture-principles)
- [Current Implementation Analysis](#current-implementation-analysis)
  - [Implemented Components ✅](#implemented-components)
  - [Architecture Gaps ⚠️](#architecture-gaps)
  - [Module Organization](#module-organization)
- [Architecture Components](#architecture-components)
  - [Configuration Management](#configuration-management)
  - [Service Architecture](#service-architecture)
  - [Client Layer](#client-layer)
  - [Domain Models](#domain-models)
- [FLEXT Ecosystem Integration](#flext-ecosystem-integration)
  - [Currently Implemented ✅](#currently-implemented)
  - [Public Composition Boundary](#public-composition-boundary)
- [Critical Architecture Issues](#critical-architecture-issues)
  - [1. FLEXT Compliance Violations](#1-flext-compliance-violations)
  - [2. Oracle OIC Integration Gaps](#2-oracle-oic-integration-gaps)
- [Testing Architecture](#testing-architecture)
  - [Current Test Status (21% Coverage)](#current-test-status-21-coverage)
  - [Required Testing Strategy](#required-testing-strategy)
- [Roadmap to FLEXT Compliance](#roadmap-to-flext-compliance)
  - [Phase 1: Critical Fixes (Immediate)](#phase-1-critical-fixes-immediate)
  - [Phase 2: Oracle OIC Implementation (Months 2-3)](#phase-2-oracle-oic-implementation-months-2-3)
  - [Phase 3: Production Readiness (Month 4+)](#phase-3-production-readiness-month-4)
- [Integration with FLEXT Ecosystem](#integration-with-flext-ecosystem)
  - [Direct Dependencies](#direct-dependencies)
  - [Service Dependencies](#service-dependencies)
  - [Cross-References](#cross-references)
- [Related Documentation](#related-documentation)

<!-- TOC END -->

**flext-oracle-oic v0.12.0-dev** - Oracle Integration Cloud Architecture Analysis

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)

## Overview

This document provides an accurate analysis of the current architecture implementation
in flext-oracle-oic v0.12.0-dev, identifying both existing capabilities and areas
requiring FLEXT ecosystem compliance improvements.

### Architecture Principles

The library follows these core principles from the FLEXT ecosystem:

1. **Railway-Oriented Programming**: p.Result[T] for type-safe error handling
2. **Dependency Injection**: FlextContainer for service management
3. **Domain-Driven Design**: Declarative value and entity models for Oracle OIC concepts
4. **Clean Architecture**: Separation of concerns across layers
5. **Type Safety**: Complete Python 3.13+ type annotations

## Current Implementation Analysis

### Implemented Components ✅

**Configuration Management**

- Pydantic-based settings with environment variable support
- Type-safe configuration models for Oracle OIC connectivity
- Basic validation for connection parameters

**Service Foundation**

- Basic service class structure with organized modules
- Exception hierarchy for Oracle OIC-specific error handling
- Testing infrastructure with pytest configuration

**FLEXT Integration (Partial)**

- r usage for some error handling patterns
- FlextLogger integration for structured logging
- Basic import structure for FLEXT ecosystem components

### Architecture Gaps ⚠️

**FLEXT Ecosystem Compliance**

- The client, CLI, and service already use upstream HTTP, CLI, and `s` abstractions.
- Remaining facade-layer, composition, and type findings require current `make check`
  and `make mod` evidence; abstraction presence does not establish compliance.

**Oracle OIC Integration**

- OAuth, integration CRUD, orchestration, and health-check code paths exist.
- Successful configured Oracle execution is a separate validation requirement.
- Credential provisioning, response contracts, and service lifecycle behavior remain
  explicit runtime boundaries, not guarantees from model construction.

### Module Organization

**Public and Implementation Owners**

```
src/flext_oracle_oic/
├── __init__.py              # Generated public exports
├── _settings.py             # settings.OracleOic deployment inputs
├── _config.py               # Public config.OracleOic loading boundary
├── config/                 # Package metadata YAML, not root business rules
├── api.py                   # FlextOracleOicApi composition root
├── ext_client.py            # FlextOracleOicClient HTTP adapter
├── service.py               # FlextOracleOicService MRO facade
├── services/               # Domain service mixins
├── models.py                # m.OracleOic Pydantic contracts
├── main.py                  # FlextOracleOicCli transport
├── constants.py             # c facade
├── protocols.py             # p facade
├── typings.py               # t facade
└── utilities.py             # u facade
```

## Architecture Components

### Configuration Management

**FlextOracleOicSettings**

- Main configuration container using Pydantic
- Environment variable integration for Oracle OIC settings
- Type-safe configuration validation

Business configuration and deployment settings have distinct owners. The root
`config/oracle_oic.yaml` declares business rules; the package's
`src/flext_oracle_oic/config/oracle-oic.yaml` contains identity metadata. The public
`config.OracleOic` loader boundary exists, but the config owner must reconcile this
layout and prove its runtime loading before either file can be described as a complete
business-rule consumer. These offline examples validate `settings`, not that cutover.

**Connection Configuration**

- Base URL, API version, timeout settings
- HTTP connection parameters for Oracle Integration Cloud
- Request/response handling configuration

**Authentication Configuration**

- OAuth2 client credentials setup
- IDCS token URL configuration
- Secret management with Pydantic SecretStr

### Service Architecture

**Current Service Composition**

```text
FlextOracleOicApi -> FlextOracleOicService
FlextOracleOicService composes authentication, monitoring, orchestration,
integration lifecycle, integration CRUD, and service-base mixins.
The public s alias names FlextOracleOicService, not a settings class.
```

### Client Layer

**HTTP Client Implementation**

- Basic Oracle OIC REST API client wrapper
- Request/response handling with basic error management
- OAuth2 authentication preparation (incomplete)

**HTTP Boundary**

```text
FlextOracleOicClient uses the public FlextApi HTTP facade from flext_api.
Connection and OAuth inputs enter through m.OracleOic domain models.
```

### Domain Models

**Data Transfer Objects**

- `OICIntegrationInfo`: Integration metadata
- `OICConnectionInfo`: Connection parameters
- `OICAuthConfig`: Authentication configuration

**Declaration Boundaries**

- `OICAuthConfig` and `OICConnectionConfig` inherit upstream value-model presets.
- `OICIntegrationInfo` and `OICConnectionInfo` inherit upstream entity presets.
- Models declare data and validation; behavior belongs to utilities and services.
- These declarations do not establish an Oracle transaction or aggregate boundary.

## FLEXT Ecosystem Integration

### Currently Implemented ✅

**Typed Connection Validation and Railway Results**

```python
from flext_oracle_oic import m, r, settings

connection = m.OracleOic.OICConnectionConfig.model_validate(
    settings.OracleOic.model_dump(
        include=set(m.OracleOic.OICConnectionConfig.model_fields),
    ),
)
result = r[str].ok(connection.model_dump_json())
restored_connection = m.OracleOic.OICConnectionConfig.model_validate_json(
    result.unwrap(),
)
if restored_connection.base_url != settings.OracleOic.base_url:
    message = "Result did not preserve the configured connection URL"
    raise ValueError(message)
```

**FlextLogger Integration**

```python
from flext_oracle_oic import u

logger = u.fetch_logger(__name__)
logger.info("oic.connection.configuration.validated")
```

### Public Composition Boundary

**Public Service Composition**

```python
from flext_oracle_oic import FlextOracleOicApi, settings

api = FlextOracleOicApi(settings=settings)
connection_context = api.fetch_connection_context().unwrap()
if connection_context["base_url"] != settings.OracleOic.base_url:
    message = "Connection context did not preserve the configured URL"
    raise ValueError(message)
if connection_context["request_timeout"] != settings.OracleOic.request_timeout:
    message = "Connection context did not preserve the configured timeout"
    raise ValueError(message)
```

Pass the typed settings instance to the public API composition root. Reading its
connection context above is an offline operation, not proof that delegated service
operations or Oracle authentication succeed. The parent implementation lane owns the
remaining composition and runtime findings.

## Critical Architecture Issues

### 1. FLEXT Compliance Violations

**Existing Dependency Boundaries**

- `ext_client.py` imports the public `FlextApi` facade.
- `main.py` imports public `flext-cli` abstractions.
- `services/base.py` inherits upstream `s`; `service.py` composes the service mixins.

**Unified Class Pattern Violations**

- Use current `make mod` and runtime-census findings to identify remaining declaration
  and facade violations; the old `ext_services.py` module is not a current owner.

**Type Safety Issues**

- Current lint and type receipts come from `make check`; historical counts and extinct
  exception paths are not evidence that today's candidate passes or fails.

### 2. Oracle OIC Integration Gaps

**Authentication**

- OAuth2/IDCS framework incomplete
- No token lifecycle management
- Missing secure credential storage

**Integration Patterns**

- The orchestration service exposes app-driven, scheduled, and file-transfer operations.
- Validate their public result and Oracle execution contracts independently; an available
  method is not proof of a successful deployed integration.

**Enterprise Features**

- No circuit breaker pattern
- No exponential backoff retry strategy
- Monitoring and health-check methods exist; successful configured behavior still
  requires public runtime evidence.

## Testing Architecture

### Current Test Evidence

Coverage and execution counts must come from the current canonical test receipt, not
an old percentage. Executable Markdown tests exercise the public package contract;
they do not substitute for configured Oracle integration tests.

**Test Structure**

```

tests/
├── unit/                    # Basic unit tests
│   ├── test_config.py      # Configuration validation
│   ├── test_models.py      # Data model tests
│   ├── test_extension.py   # Extension pattern tests
│   └── test_basic.py       # Basic functionality tests
└── conftest.py             # Pytest configuration
```

**Testing Limitations**

- No integration tests with Oracle OIC APIs
- No contract testing for API compliance
- Offline tests must not replace Oracle evidence with mocks or dummy credentials
- Missing performance and security tests

### Required Testing Strategy

**Integration Testing**

- Real Oracle OIC API connectivity tests
- OAuth2/IDCS authentication flow validation
- Integration pattern execution verification

**Contract Testing**

- Oracle OIC REST API compliance validation
- Response schema verification
- Error handling contract validation

## Roadmap to FLEXT Compliance

### Phase 1: Critical Fixes (Immediate)

1. **Resolve Measured Findings**

   - Repair current lint, type, facade, and composition findings at their canonical owners
   - Preserve existing public HTTP, CLI, and service boundaries

2. **Validate Canonical Fixed Points**

   - Run generation, repair, formatting, and modernization through root Make verbs
   - Verify the resulting public consumer and rerun applicable checks

### Phase 2: Oracle OIC Implementation (Months 2-3)

1. **OAuth2/IDCS Authentication**

   - Complete Oracle cloud authentication
   - Token lifecycle management
   - Secure credential storage

2. **Integration Patterns**

   - App-driven orchestration
   - Scheduled orchestration
   - File transfer patterns

3. **Enterprise Features**

   - Circuit breaker implementation
   - Retry strategies
   - Monitoring and health checks

### Phase 3: Production Readiness (Month 4+)

1. **Comprehensive Testing**

   - Coverage against the configured policy with meaningful integration tests
   - Contract testing with Oracle OIC APIs
   - Performance benchmarking

2. **Documentation Completion**

   - Complete API reference
   - Integration examples
   - Troubleshooting guides

## Integration with FLEXT Ecosystem

### Direct Dependencies

- **[flext-core](https://github.com/flext-sh/flext/tree/0.12.0-dev/flext-core/README.md)**
  → Foundation patterns and railway programming
- **[flext-api](https://github.com/flext-sh/flext/tree/0.12.0-dev/flext-api/README.md)**
  → Existing HTTP client abstraction used by `FlextOracleOicClient`
- **[flext-cli](https://github.com/flext-sh/flext/tree/0.12.0-dev/flext-cli/README.md)**
  → Existing CLI command and result abstractions

### Service Dependencies

- **[flext-tap-oracle-oic](https://github.com/flext-sh/flext/tree/0.12.0-dev/flext-tap-oracle-oic/README.md)**
  → Depends on this for OIC data extraction
- **[flext-target-oracle-oic](https://github.com/flext-sh/flext/tree/0.12.0-dev/flext-target-oracle-oic/README.md)**
  → Depends on this for OIC data loading

### Cross-References

- **Oracle Integration**: Works with flext-oracle-wms for warehouse management
- **Authentication**: Integrates with flext-auth for unified authentication
- **Observability**: Uses flext-observability for monitoring and metrics

---

This analysis distinguishes implemented public contracts from validated runtime
behavior. Current canonical gate and configured Oracle receipts determine readiness.

## Related Documentation

**Within Project**:

- [Getting Started](getting-started.md) - Installation and basic usage
- [API Reference](api-reference/README.md) - Generated API documentation
- [Integration](integration.md) - Integration patterns
- [Troubleshooting](troubleshooting.md) - Common issues

**Across Projects**:

- [flext-core Foundation](https://github.com/flext-sh/flext/tree/0.12.0-dev/flext-core/docs/architecture/overview.md) -
  Clean architecture and CQRS patterns
- [flext-core Service Patterns](https://github.com/flext-sh/flext/tree/0.12.0-dev/flext-core/docs/guides/service-patterns.md) -
  Service patterns and dependency injection
- [flext-db-oracle Integration](https://github.com/flext-sh/flext/tree/0.12.0-dev/flext-db-oracle/AGENTS.md) -
  Oracle database integration

**External Resources**:

- [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
