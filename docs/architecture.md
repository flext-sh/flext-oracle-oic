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
  - [Missing FLEXT Integration ❌](#missing-flext-integration)
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

This document provides an accurate analysis of the current architecture implementation in flext-oracle-oic v0.12.0-dev, identifying both existing capabilities and areas requiring FLEXT ecosystem compliance improvements.

### Architecture Principles

The library follows these core principles from the FLEXT ecosystem:

1. **Railway-Oriented Programming**: p.Result[T] for type-safe error handling
1. **Dependency Injection**: FlextContainer for service management
1. **Domain-Driven Design**: Rich domain models for Oracle OIC concepts
1. **Clean Architecture**: Separation of concerns across layers
1. **Type Safety**: Complete Python 3.13+ type annotations

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

- Missing s inheritance (critical requirement)
- Direct httpx/typer imports violate FLEXT abstraction patterns
- Incomplete FlextContainer dependency injection implementation
- Multiple classes per module violate unified class pattern

**Oracle OIC Integration**

- No actual Oracle Integration Cloud API connectivity
- OAuth2/IDCS authentication framework incomplete
- Missing integration pattern execution engine
- No enterprise features (circuit breaker, retry patterns)

### Module Organization

**Current Structure (2,937 lines across 13 modules)**

```
src/flext_oracle_oic/
├── __init__.py              # Module exports and version (65 lines)
├── ext_config.py            # Pydantic configuration models (215 lines)
├── ext_exceptions.py        # Exception hierarchy (89 lines)
├── ext_client.py            # HTTP client wrapper (312 lines)
├── ext_services.py          # Service layer (445 lines)
├── ext_models.py            # Data models using Pydantic (267 lines)
├── cli.py                   # CLI implementation (198 lines)
├── extension.py             # Extension pattern base (156 lines)
├── factory.py               # Service factory methods (89 lines)
├── container.py             # Basic container (134 lines)
├── main.py                  # Main entry point (78 lines)
├── typings.py               # Type definitions (123 lines)
└── version.py               # Version management (45 lines)
```

## Architecture Components

### Configuration Management

**OracleOicExtensionSettings**

- Main configuration container using Pydantic
- Environment variable integration for Oracle OIC settings
- Type-safe configuration validation

**Connection Configuration**

- Base URL, API version, timeout settings
- HTTP connection parameters for Oracle Integration Cloud
- Request/response handling configuration

**Authentication Configuration**

- OAuth2 client credentials setup
- IDCS token URL configuration
- Secret management with Pydantic SecretStr

### Service Architecture

**Current Service Classes (FLEXT Compliance Issues)**

```python
# ext_services.py contains multiple classes (violates FLEXT unified pattern)
class OracleOicExtensionService        # Main service class
class OICIntegrationPatternService     # Integration patterns
class LifecycleManager                 # Service lifecycle
class MonitoringService                # Basic monitoring

# Required FLEXT pattern: Single unified class per module
class OracleOicIntegrationService(s):
    """Unified service with nested helpers."""

    class _IntegrationHelper:
        """Nested pattern execution logic."""

    class _MonitoringHelper:
        """Nested monitoring and lifecycle management."""
```

### Client Layer

**HTTP Client Implementation**

- Basic Oracle OIC REST API client wrapper
- Request/response handling with basic error management
- OAuth2 authentication preparation (incomplete)

**FLEXT Compliance Issue**

```python
# ❌ Current violation in ext_client.py:12
import httpx  # Direct dependency violates FLEXT abstraction

# ✅ Required FLEXT pattern
from flext_api import FlextApiClient
```

### Domain Models

**Data Transfer Objects**

- `OICIntegrationInfo`: Integration metadata
- `OICConnectionInfo`: Connection parameters
- `OICAuthConfig`: Authentication configuration

**Missing Domain-Driven Design**

- No rich domain entities for Oracle OIC concepts
- No value objects for business rules
- No aggregate roots for consistency boundaries

## FLEXT Ecosystem Integration

### Currently Implemented ✅

**r Railway Pattern (Partial)**

```python
from flext_core import FlextBus
from flext_core import FlextSettings
from flext_core import FlextConstants
from flext_core import FlextContainer
from flext_core import FlextContext
from flext_core import d
from flext_core import FlextDispatcher
from flext_core import e
from flext_core import h
from flext_core import x
from flext_core import FlextModels
from flext_core import FlextProcessors
from flext_core import p
from flext_core import FlextRegistry
from flext_core import r, p
from flext_core import u
from flext_core import s
from flext_core import t
from flext_core import u


def validate_connection(settings: dict) -> p.Result[ConnectionInfo]:
    """Example of current r usage."""
    if not settings.get("base_url"):
        return r[ConnectionInfo].fail("Base URL required")
    return r[ConnectionInfo].ok(ConnectionInfo(**settings))
```

**FlextLogger Integration**

```python
from flext_core import FlextBus
from flext_core import FlextSettings
from flext_core import FlextConstants
from flext_core import FlextContainer
from flext_core import FlextContext
from flext_core import d
from flext_core import FlextDispatcher
from flext_core import e
from flext_core import h
from flext_core import x
from flext_core import FlextModels
from flext_core import FlextProcessors
from flext_core import p
from flext_core import FlextRegistry
from flext_core import r, p
from flext_core import u
from flext_core import s
from flext_core import t
from flext_core import u


class ServiceClass:
    def __init__(self):
        self.logger = u.fetch_logger(__name__)
```

### Missing FLEXT Integration ❌

**s Inheritance**

```python
# ❌ Current implementation
class OracleOicExtensionService:
    pass


# ✅ Required FLEXT pattern
class OracleOicIntegrationService(s):
    pass
```

**FlextContainer Dependency Injection**

```python
# ❌ Current: Manual service creation
service = OracleOicExtensionService(settings)

# ✅ Required: Container-managed dependencies
container = FlextContainer.get_global()
service = container.resolve("oic_service").unwrap()
```

## Critical Architecture Issues

### 1. FLEXT Compliance Violations

**Direct Import Dependencies**

- `ext_client.py:12` - Direct `httpx` import (should use flext-api)
- `main.py:15` - Direct `typer` import (should use flext-cli)

**Unified Class Pattern Violations**

- `ext_services.py` contains 4 classes (should be 1 unified class)
- Helper functions outside classes (should be nested classes)

**Type Safety Issues**

- 2 MyPy errors in `exceptions.py:283` and `test_models.py:61`

### 2. Oracle OIC Integration Gaps

**Authentication**

- OAuth2/IDCS framework incomplete
- No token lifecycle management
- Missing secure credential storage

**Integration Patterns**

- No app-driven orchestration implementation
- No scheduled orchestration capabilities
- Missing file transfer pattern support

**Enterprise Features**

- No circuit breaker pattern
- No exponential backoff retry strategy
- Missing monitoring and health checks

## Testing Architecture

### Current Test Status (21% Coverage)

**Test Structure**

```
tests/
├── unit/                    # Basic unit tests
│   ├── test_config.py      # Configuration validation
│   ├── test_models.py      # Data model tests
│   └── test_extension.py   # Extension pattern tests
├── conftest.py             # Pytest configuration
└── test_basic.py           # Basic functionality tests
```

**Testing Limitations**

- No integration tests with Oracle OIC APIs
- No contract testing for API compliance
- Limited mock strategy for Oracle cloud services
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

1. **Fix MyPy Errors**

   - Resolve `exceptions.py:283` OIC_TOKEN_ERROR issue
   - Fix `test_models.py:61` type mismatch

1. **Replace Direct Imports**

   - Replace `httpx` with `flext-api` patterns
   - Replace `typer` with `flext-cli` patterns

1. **Implement s**

   - Convert service classes to inherit from s
   - Implement unified class pattern with nested helpers

### Phase 2: Oracle OIC Implementation (Months 2-3)

1. **OAuth2/IDCS Authentication**

   - Complete Oracle cloud authentication
   - Token lifecycle management
   - Secure credential storage

1. **Integration Patterns**

   - App-driven orchestration
   - Scheduled orchestration
   - File transfer patterns

1. **Enterprise Features**

   - Circuit breaker implementation
   - Retry strategies
   - Monitoring and health checks

### Phase 3: Production Readiness (Month 4+)

1. **Comprehensive Testing**

   - 70%+ coverage with integration tests
   - Contract testing with Oracle OIC APIs
   - Performance benchmarking

1. **Documentation Completion**

   - Complete API reference
   - Integration examples
   - Troubleshooting guides

## Integration with FLEXT Ecosystem

### Direct Dependencies

- **[flext-core](https://github.com/organization/flext/tree/main/flext-core/README.md)** → Foundation patterns and railway programming
- **[flext-api](https://github.com/organization/flext/tree/main/flext-api/README.md)** → HTTP client abstractions (needs implementation)
- **[flext-cli](https://github.com/organization/flext/tree/main/flext-cli/README.md)** → CLI interface patterns (needs implementation)

### Service Dependencies

- **[flext-tap-oracle-oic](https://github.com/organization/flext/tree/main/flext-tap-oracle-oic/README.md)** → Depends on this for OIC data extraction
- **[flext-target-oracle-oic](https://github.com/organization/flext/tree/main/flext-target-oracle-oic/README.md)** → Depends on this for OIC data loading

### Cross-References

- **Oracle Integration**: Works with flext-oracle-wms for warehouse management
- **Authentication**: Integrates with flext-auth for unified authentication
- **Observability**: Uses flext-observability for monitoring and metrics

______________________________________________________________________

This architecture analysis reflects the actual implementation status as of April 14, 2026. The library provides foundation configuration and basic service structure, with significant FLEXT compliance improvements needed before production use.

## Related Documentation

**Within Project**:

- [Getting Started](getting-started.md) - Installation and basic usage
- [API Reference](api-reference.md) - Complete API documentation
- [Integration](integration.md) - Integration patterns
- [Troubleshooting](troubleshooting.md) - Common issues

**Across Projects**:

- [flext-core Foundation](https://github.com/organization/flext/tree/main/flext-core/docs/architecture/overview.md) - Clean architecture and CQRS patterns
- [flext-core Service Patterns](https://github.com/organization/flext/tree/main/flext-core/docs/guides/service-patterns.md) - Service patterns and dependency injection
- [flext-db-oracle Integration](https://github.com/organization/flext/tree/main/flext-db-oracle/AGENTS.md) - Oracle database integration

**External Resources**:

- [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
