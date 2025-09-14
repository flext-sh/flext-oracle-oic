# Architecture

**Current Architecture Overview for flext-oracle-oic-ext v0.9.0**

## Current Implementation Status

### What's Actually Implemented

This document describes the **actual current architecture** as of September 2025, not future plans or aspirational designs.

#### ✅ Basic Structure
- **Configuration layer** using Pydantic models
- **Service layer** with basic class structure
- **Exception hierarchy** for Oracle OIC specific errors
- **Basic HTTP client framework** (with FLEXT compliance issues)
- **Test infrastructure** with pytest setup

#### ⚠️ Partial Implementation
- **FLEXT-core integration** - Uses FlextResult and FlextLogger
- **OAuth2 authentication structure** - Framework exists, needs implementation
- **CLI structure** - Basic setup with FLEXT violations

#### ❌ Not Yet Implemented
- **Clean Architecture layers** - No domain/application/infrastructure separation
- **Domain-Driven Design** - No rich domain models
- **Real Oracle OIC API integration** - No actual OIC connectivity
- **WMS integration** - No warehouse management functionality
- **Enterprise Integration Patterns** - No EIP implementation

## Current Module Structure

```
src/flext_oracle_oic_ext/
├── __init__.py              # Module exports and version info
├── ext_config.py            # Pydantic configuration models
├── ext_exceptions.py        # Exception hierarchy for Oracle OIC
├── ext_client.py            # Basic HTTP client (needs FLEXT compliance)
├── ext_services.py          # Service layer (basic implementation)
├── ext_models.py            # Data models using Pydantic
├── cli.py                   # CLI implementation (FLEXT violations)
├── extension.py             # Legacy extension pattern
├── factory.py               # Service factory methods
├── container.py             # Basic container (needs DI implementation)
├── main.py                  # Main entry point
└── typings.py               # Type definitions
```

## Current Class Relationships

### Configuration Layer
- **OracleOICExtensionSettings**: Main configuration container
- **OICExtensionConnectionConfig**: HTTP connection settings
- **OICExtensionAuthConfig**: OAuth2 authentication configuration

### Service Layer
- **OracleOICExtensionService**: Main service class (basic implementation)
- **OICIntegrationPatternService**: Pattern service (placeholder)
- **LifecycleManager**: Basic lifecycle management
- **MonitoringService**: Basic monitoring framework

### Client Layer
- **OracleOICExtensionClient**: HTTP client wrapper
- **BaseOICAuthenticator**: Authentication base class
- **OICExtensionAuthenticator**: OAuth2 authenticator implementation

### Data Layer
- **OICIntegrationInfo**: Integration metadata model
- **OICConnectionInfo**: Connection information model
- **OICAuthConfig**: Authentication configuration model

## Current FLEXT Integration

### ✅ Currently Used
- **FlextResult**: Used for error handling patterns
- **FlextLogger**: Used for logging throughout modules
- **FlextTypes**: Used for type annotations

### ❌ Missing FLEXT Integration
- **FlextContainer**: No dependency injection implementation
- **FlextDomainService**: Not using proper service base classes
- **flext-api**: Using direct httpx instead (violation)
- **flext-cli**: Using direct typer instead (violation)
- **flext-auth**: No integration with FLEXT authentication

## Critical Issues to Address

### 1. FLEXT Compliance Violations
```python
# ❌ Current violation in ext_client.py
import httpx  # Should use flext-api instead

# ❌ Current violation in cli.py
import typer  # Should use flext-cli instead

# ✅ Required FLEXT pattern
from flext_api import FlextApiClient
from flext_cli import FlextCliApi
```

### 2. Architecture Violations
- **Multiple classes per module** in ext_services.py (4 classes)
- **No unified class pattern** - Missing nested helper classes
- **Missing dependency injection** - Not using FlextContainer
- **Language inconsistency** - Portuguese comments mixed with English

### 3. Missing Domain Logic
- **No domain entities** - Only basic data models
- **No business rules** - Missing Oracle OIC domain logic
- **No value objects** - Simple dictionaries instead of rich models
- **No domain services** - Basic CRUD operations only

## Planned Architecture Improvements

### Phase 1: FLEXT Compliance
- Replace httpx with flext-api client abstractions
- Replace typer with flext-cli patterns
- Implement proper dependency injection with FlextContainer
- Convert to unified class pattern (one class per module)

### Phase 2: Clean Architecture
- Separate domain/application/infrastructure layers
- Implement rich domain models for Oracle OIC concepts
- Add proper repository patterns for data access
- Create application services for use case orchestration

### Phase 3: Oracle OIC Integration
- Implement real Oracle OIC REST API clients
- Add OAuth2/IDCS authentication with Oracle Cloud Identity
- Create integration pattern execution engine
- Add workflow orchestration capabilities

## Testing Architecture

### Current Test Structure
```
tests/
├── unit/                    # Unit tests (basic)
├── conftest.py             # Test configuration and fixtures
├── test_basic.py           # Basic functionality tests
├── test_config.py          # Configuration validation tests
├── test_models.py          # Model tests
└── test_extension.py       # Extension pattern tests
```

### Testing Limitations
- **No integration tests** with real Oracle OIC APIs
- **Basic unit tests** only test configuration and models
- **No end-to-end tests** - No complete workflow testing
- **Mock-based testing** - No real system integration

## Configuration Management

### Current Implementation
- **Pydantic models** for type-safe configuration
- **Environment variable support** for settings
- **Basic validation** for required fields
- **Secret handling** using Pydantic SecretStr

### Missing Features
- **Environment-specific configuration** (dev/staging/prod)
- **Configuration validation** against Oracle OIC requirements
- **Secure credential management** integration
- **Dynamic configuration updates**

## Error Handling

### Current Implementation
- **FlextResult patterns** for some operations
- **Custom exception hierarchy** for Oracle OIC errors
- **Basic error context** in exception messages

### Missing Features
- **Complete FlextResult usage** - Some functions still use direct exceptions
- **Error recovery strategies** - No retry or fallback mechanisms
- **Detailed error context** - Limited troubleshooting information
- **Error monitoring integration** - No observability for failures

## Future Architecture Vision

While the current implementation is basic, the planned architecture follows these principles:

- **Clean Architecture** with proper layer separation
- **Domain-Driven Design** with rich Oracle OIC domain models
- **FLEXT ecosystem integration** using all foundation libraries
- **Real Oracle OIC API integration** with production-ready patterns
- **Enterprise Integration Patterns** implementation
- **Comprehensive testing** with real Oracle systems

---

**Note**: This document describes the current state as of September 2025. It will be updated as the architecture evolves and FLEXT compliance issues are resolved.