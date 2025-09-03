# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**flext-oracle-oic-ext** is an Oracle Integration Cloud (OIC) extension library within the FLEXT ecosystem. It implements the **EXTENSION Pattern** with advanced enterprise integration capabilities and clean architecture principles. The project provides Oracle OIC REST API integration, OAuth2 authentication, and extensible configuration management.

## Architecture & Design

### EXTENSION Pattern Implementation

- **Extension Pattern**: Implements standardized EXTENSION pattern for Oracle OIC-specific functionality
- **Foundation**: Built on `flext-core` for FlextResult patterns, FlextSettings, dependency injection, and logging
- **Clean Architecture**: Strict layer separation following DDD principles with clear domain boundaries
- **Type Safety**: Comprehensive type hints and strict MyPy configuration for enterprise reliability

### Core Components

Located in `src/flext_oracle_oic_ext/`:

- **OracleOICExtensionService**: Main service class implementing business logic (`ext_services.py`)
- **OracleOICExtensionClient**: REST API client with authentication (`ext_client.py`)
- **OracleOICExtensionSettings**: Configuration management with Pydantic validation (`ext_config.py`)
- **OICExtensionAuthenticator**: OAuth2/IDCS authentication handler (`ext_client.py`)
- **Extension Models**: Business domain models with validation (`ext_models.py`)
- **Custom Exceptions**: Specific error handling for OIC operations (`ext_exceptions.py`)

### Development Architecture

```
src/flext_oracle_oic_ext/
├── __init__.py              # Public API with EXTENSION pattern exports
├── ext_config.py            # Settings and configuration classes
├── ext_client.py            # API clients and authentication
├── ext_services.py          # Main business logic services
├── ext_models.py            # Domain models and data structures
├── ext_exceptions.py        # Custom exception hierarchy
├── extension.py             # Legacy extension class (backward compatibility)
├── legacy.py                # Legacy imports and deprecation warnings
├── main.py                  # CLI entry point
└── cli.py                   # Command-line interface implementation
```

## Essential Development Commands

### Quality Gates (Always run before committing)

```bash
# Complete validation pipeline
make validate                # lint + type-check + security + test

# Quick health check
make check                   # lint + type-check only

# Individual quality checks
make lint                    # Ruff linting (strict configuration)
make type-check              # MyPy strict mode
make security                # Bandit security scanning + pip-audit
make format                  # Auto-format code with Ruff
```

### Testing Commands

```bash
# Core testing
make test                    # Run all tests with 90% coverage requirement
make test-unit               # Unit tests only (fast)
make test-integration        # Integration tests only
make test-fast               # Skip coverage for speed

# OIC-specific testing
make test-oic                # OIC connectivity and API tests
make test-patterns           # Integration pattern tests

# Coverage reporting
make coverage-html           # Generate HTML coverage report
```

### Setup and Installation

```bash
# Complete project setup
make setup                   # Install dependencies + pre-commit hooks
make install                 # Install dependencies with Poetry
make install-dev             # Install with dev dependencies

# Development utilities
make shell                   # Open Python shell with project loaded
make pre-commit              # Run pre-commit hooks manually
```

### OIC Operations

```bash
# OIC connectivity testing
make oic-test                # Test API connectivity
make oic-auth                # Test OAuth2 authentication
make oic-patterns            # Test integration patterns
make oic-deploy              # Test deployment capabilities
```

### Build and Maintenance

```bash
# Build operations
make build                   # Build distribution packages
make clean                   # Remove build artifacts
make clean-all               # Deep clean including virtual environment

# Dependency management
make deps-update             # Update all dependencies
make deps-audit              # Security audit of dependencies
make deps-show               # Show dependency tree

# Project health
make doctor                  # Full health check and diagnostics
make diagnose                # Show project diagnostics
```

## Testing Strategy

### Test Structure

```
tests/
├── conftest.py              # Pytest configuration and fixtures
├── test_basic_import.py     # Basic import and module loading tests
├── test_extension.py        # Main extension functionality tests
├── test_e2e_complete.py     # End-to-end integration tests
├── test_generate_config.py  # Configuration generation tests
└── unit/
    └── test_version.py      # Version information tests
```

### Test Categories

- **Unit Tests**: Fast tests with mocking (marked with `@pytest.mark.unit`)
- **Integration Tests**: Tests with external dependencies (marked with `@pytest.mark.integration`)
- **OIC Tests**: Oracle Integration Cloud specific tests
- **Slow Tests**: Long-running tests (marked with `@pytest.mark.slow`)
- **E2E Tests**: Complete workflow validation

### Running Tests

```bash
# All tests with coverage (90% minimum required)
make test

# Test categories using pytest markers
pytest -m unit              # Unit tests only
pytest -m integration       # Integration tests only
pytest -m "not slow"        # Exclude slow tests

# Specific test files
pytest tests/test_extension.py -v
pytest tests/unit/test_version.py -v

# Coverage reporting
make coverage-html          # HTML report in reports/coverage/
```

## Configuration

### Settings Architecture

Configuration follows the EXTENSION Pattern with Pydantic validation:

- **OracleOICExtensionSettings**: Main settings class (`ext_config.py:50`)
- **OICExtensionConnectionConfig**: Connection settings (`ext_config.py:19`)
- **OICExtensionAuthConfig**: OAuth2 authentication settings (`ext_config.py:34`)

### Key Configuration Files

- `config.json`: Main configuration (see `config.json.example`)
- `pyproject.toml`: Project dependencies and tool configuration
- Environment variables: Loaded automatically by FlextSettings

## Code Quality Standards

### Zero Tolerance Quality Gates

- **Test Coverage**: Minimum 90% required (enforced by pytest)
- **Type Safety**: Strict MyPy configuration with comprehensive type hints
- **Linting**: Ruff with strict rules for code quality
- **Security**: Bandit + pip-audit for vulnerability scanning

### Architecture Patterns

1. **EXTENSION Pattern**: Standardized structure for Oracle OIC functionality
2. **FlextResult Pattern**: Railway-oriented programming for error handling
3. **FlextSettings**: Pydantic-based configuration with validation
4. **Clean Architecture**: Clear separation between domain, application, and infrastructure layers

## Development Patterns

### Using FlextResult

```python
from flext_core import FlextResult
from flext_oracle_oic_ext import OracleOICExtensionService

def process_oic_integration() -> FlextResult[str]:
    service = OracleOICExtensionService(settings)
    return service.process_integration()
```

### Configuration Usage

```python
from flext_oracle_oic_ext import OracleOICExtensionSettings

# Auto-loads from environment variables
settings = OracleOICExtensionSettings()

# Access nested configurations
connection_config = settings.connection
auth_config = settings.auth
```

### Service Initialization

```python
from flext_oracle_oic_ext import (
    create_oic_extension_service,
    create_development_oic_service
)

# Production service
service_result = create_oic_extension_service()
if service_result.is_success():
    service = service_result.value

# Development service
dev_service_result = create_development_oic_service()
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Check flext-core dependency installation
2. **Configuration Validation**: Use Pydantic validation for settings
3. **Type Errors**: Run `make type-check` for MyPy issues
4. **Test Failures**: Use `make test` for coverage validation

### Diagnostic Commands

```bash
# Project health check
make doctor

# Validate configuration
poetry run python -c "from flext_oracle_oic_ext import OracleOICExtensionSettings; print(OracleOICExtensionSettings())"

# Check dependency issues
make deps-audit

# Full validation pipeline
make validate
```

## Dependencies

### Core FLEXT Dependencies

- **flext-core**: Foundation patterns, FlextResult, FlextSettings, logging
- **flext-observability**: Monitoring and observability (path dependency)

### External Dependencies

- **pydantic**: Data validation and settings management
- **httpx**: Modern HTTP client for API operations
- **tenacity**: Retry logic and resilience patterns
- **typer**: CLI framework for command-line interface
