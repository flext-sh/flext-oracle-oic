# flext-oracle-oic-ext Project Overview

## Purpose

Oracle OIC (Oracle Integration Cloud) Extension for the FLEXT ecosystem. Provides enterprise-grade integration capabilities with Oracle OIC platform, including authentication, connection management, integration lifecycle, and monitoring services.

## Tech Stack

- **Python**: 3.13+
- **Pydantic**: 2.11+ for data validation and models
- **FlextCore**: Foundation layer for result handling, logging, configuration
- **Async/Await**: For Oracle OIC API interactions
- **OAuth2**: IDCS authentication integration

## Code Style & Conventions

- **Unified Class Pattern**: Single class per module with nested helpers
- **FlextResult Pattern**: All operations return FlextResult[T] for type-safe error handling
- **EXTENSION Pattern**: Specialized services following FLEXT architectural standards
- **Type Safety**: 100% MyPy compliance with strict typing
- **Pydantic Models**: All data models use Pydantic with ConfigDict validation

## Project Structure

```
src/flext_oracle_oic_ext/
├── __init__.py              # Main exports
├── cli.py                   # CLI interface
├── container.py             # Dependency injection
├── extension.py             # Main extension class
├── factory.py               # Service factory
├── main.py                  # Entry point
├── ext_client.py            # Oracle OIC API client
├── ext_config.py            # Configuration models
├── ext_models.py            # Domain models
├── ext_services.py          # Business services
├── ext_exceptions.py        # Custom exceptions
├── exceptions.py            # General exceptions
└── typings.py               # Type definitions
```

## Quality Commands

- `make validate` - Complete validation pipeline (lint + type + security + test)
- `make check` - Quick validation (lint + type)
- `make test` - Run tests with coverage
- `make lint` - Ruff linting
- `make type-check` - MyPy type checking
- `make format` - Auto-format code

## Entry Points

- `flext-oracle-oic-ext` - Main CLI command
- `python -m flext_oracle_oic_ext` - Module execution

## Key Features

- Oracle OIC integration management
- OAuth2 authentication with IDCS
- Integration lifecycle management (activate/deactivate)
- Connection monitoring and health checks
- Enterprise patterns (Message Router, Scatter-Gather)
- Comprehensive error handling with FlextResult
