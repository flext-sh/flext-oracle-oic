# Getting Started

**flext-oracle-oic v0.9.9** - Oracle Integration Cloud client library for the FLEXT ecosystem

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)

## Prerequisites

### Required Software

- **Python 3.13+** with Poetry for dependency management
- **FLEXT workspace** setup with access to [flext-core](https://github.com/organization/flext/tree/main/flext-core/README.md)
- **Git** for version control

### Optional for Testing

- Oracle Integration Cloud instance access
- OAuth2/IDCS credentials for Oracle cloud

### Knowledge Requirements

- Basic understanding of Oracle Integration Cloud concepts
- Familiarity with FLEXT ecosystem patterns (FlextResult, FlextService)
- Python experience with Pydantic and type annotations

## Installation

### Development Installation (Recommended)

```bash
# Navigate to FLEXT workspace
cd /path/to/flext/workspace
git clone <repository-url> flext-oracle-oic
cd flext-oracle-oic

# Install dependencies with development tools
poetry install --with dev,test

# Verify FLEXT-core access
python -c "from flext_core import FlextBus
from flext_core import FlextConfig
from flext_core import FlextConstants
from flext_core import FlextContainer
from flext_core import FlextContext
from flext_core import FlextDecorators
from flext_core import FlextDispatcher
from flext_core import FlextExceptions
from flext_core import h
from flext_core import FlextLogger
from flext_core import x
from flext_core import FlextModels
from flext_core import FlextProcessors
from flext_core import p
from flext_core import FlextRegistry
from flext_core import FlextResult
from flext_core import FlextRuntime
from flext_core import FlextService
from flext_core import t
from flext_core import u; print('FLEXT-Core accessible')"

# Verify installation
python -c "from flext_oracle_oic import OracleOicExtensionSettings; print('Import successful')"
```

### Environment Setup

```bash
# Set Python path for FLEXT workspace access
export PYTHONPATH="$PWD/src:$PYTHONPATH"

# Optional: Oracle OIC testing environment
export ORACLE_OIC_BASE_URL="https://your-instance.integration.ocp.oraclecloud.com"
export ORACLE_OIC_CLIENT_ID="your_oauth_client_id"
export ORACLE_OIC_CLIENT_SECRET="your_oauth_client_secret"
export ORACLE_OIC_TOKEN_URL="https://your-idcs.identity.oraclecloud.com/oauth2/v1/token"
```

## Basic Usage

### Configuration Management

The library provides Pydantic-based configuration following FLEXT patterns:

```python
from flext_oracle_oic import (
    OracleOicExtensionSettings,
    FlextOracleOicConnectionConfig,
    FlextOracleOicAuthConfig
)

# Create configuration following FLEXT patterns
settings = OracleOicExtensionSettings(
    connection=FlextOracleOicConnectionConfig(
        base_url="https://your-oic-instance.integration.ocp.oraclecloud.com",
        api_version="v1",
        request_timeout=30
    ),
    auth=FlextOracleOicAuthConfig(
        oauth_client_id="your_client_id",
        oauth_client_secret="your_client_secret",
        oauth_token_url="https://your-idcs.identity.oraclecloud.com/oauth2/v1/token"
    )
)

print(f"Configuration created: {settings.connection.base_url}")
```

### Current Capabilities

> **Important**: Version 0.9.9 provides foundation configuration and basic service structure:

```python
# Import available components
from flext_oracle_oic.ext_config import OracleOicExtensionSettings
from flext_oracle_oic.ext_models import FlextOracleOicConnectionConfig, FlextOracleOicAuthConfig

# Basic configuration validation
try:
    config = OracleOicExtensionSettings(
        connection=FlextOracleOicConnectionConfig(
            base_url="https://test.integration.ocp.oraclecloud.com",
            api_version="v1"
        )
    )
    print("✅ Configuration valid")
except Exception as e:
    print(f"❌ Configuration error: {e}")
```

## Development Commands

### Essential Commands

```bash
# Setup development environment
make setup                 # Complete development environment setup
poetry install --with dev,test

# Quality gates (run before commits)
make validate              # Complete validation pipeline (lint + type + test)
make check                 # Quick validation (lint + type-check only)
make lint                  # Ruff linting with zero tolerance
make type-check            # MyPy strict mode type checking
make test                  # Run test suite with coverage
make format                # Auto-format code with Ruff

# Development shortcuts
make t                     # Alias for test
make l                     # Alias for lint
make tc                    # Alias for type-check
make v                     # Alias for validate
```

### Testing Commands

```bash
# Run tests with coverage analysis
PYTHONPATH=src python -m pytest tests/ --cov=src --cov-report=term-missing

# Run specific test categories
pytest tests/unit/ -v                    # Unit tests only
pytest tests/integration/ -v             # Integration tests (when available)
pytest -m "not slow" -v                  # Skip slow tests

# Coverage reporting
pytest tests/ --cov=src --cov-report=html:coverage-report
```

## Current Implementation Status

### Available Features ✅

- **Configuration Management**: Pydantic models for Oracle OIC settings
- **Basic Service Structure**: Foundation classes and module organization
- **FLEXT Integration**: Imports and basic patterns (needs completion)

### Planned Features 🚧

- **FlextService Implementation**: Complete FLEXT compliance (critical requirement)
- **OAuth2/IDCS Authentication**: Full Oracle cloud authentication
- **Integration Patterns**: App-driven orchestration, scheduled orchestration
- **Enterprise Features**: Circuit breaker, retry patterns, monitoring

### Known Limitations ⚠️

1. **FLEXT Compliance Violations**:
   - Direct `httpx` import in `ext_client.py:12` (should use flext-api)
   - Direct `typer` import in `main.py:15` (should use flext-cli)
   - Missing FlextService inheritance

2. **Type Safety Issues**:
   - 2 MyPy errors in `exceptions.py:283` and `test_models.py:61`

3. **Test Coverage**:
   - Current: 21% coverage (measured)
   - Target: 70%+ with integration tests

## Troubleshooting

### Common Installation Issues

**Import Errors from FLEXT-Core**

```bash
# Verify FLEXT workspace structure
ls -la ../flext-core/src/flext_core/
export PYTHONPATH="$(pwd)/../flext-core/src:$PYTHONPATH"
python -c "from flext_core import FlextBus
from flext_core import FlextConfig
from flext_core import FlextConstants
from flext_core import FlextContainer
from flext_core import FlextContext
from flext_core import FlextDecorators
from flext_core import FlextDispatcher
from flext_core import FlextExceptions
from flext_core import h
from flext_core import FlextLogger
from flext_core import x
from flext_core import FlextModels
from flext_core import FlextProcessors
from flext_core import p
from flext_core import FlextRegistry
from flext_core import FlextResult
from flext_core import FlextRuntime
from flext_core import FlextService
from flext_core import t
from flext_core import u; print('Success')"
```

**Quality Gate Failures**

```bash
# Check specific issues
make lint 2>&1 | head -20              # Show linting errors
make type-check 2>&1 | head -20        # Show type errors
make test 2>&1 | head -20              # Show test failures

# Fix common issues
ruff check --fix src/                  # Auto-fix linting
mypy src/ --show-error-codes           # Show specific type errors
```

**Poetry Dependency Issues**

```bash
# Reset poetry environment
poetry env remove python
poetry install --with dev,test
poetry shell
```

### Development Issues

**FLEXT Pattern Violations**

```bash
# Check for direct imports (violations)
grep -r "import httpx\|import typer" src/
grep -r "from httpx\|from typer" src/

# Should be replaced with:
# from flext_api import FlextApiClient
# from flext_cli import FlextCliCommands
```

## Next Steps

1. **Review Current Implementation**: See [architecture.md](architecture.md) for detailed analysis
2. **Check Development Roadmap**: See [../TODO.md](../TODO.md) for evidence-based development plan
3. **Understand FLEXT Patterns**: Review [flext-core documentation](https://github.com/organization/flext/tree/main/flext-core/README.md)
4. **Review Configuration**: See [configuration.md](configuration.md) for detailed settings

## Getting Help

### Resources

- **Documentation**: Complete docs in [docs/](../docs/) directory
- **FLEXT Ecosystem**: See [workspace README](../../README.md) for context
- **API Reference**: See [api-reference.md](api-reference.md) for available APIs

### Support Channels

- **Issues**: Create GitHub issue with detailed error information
- **Questions**: Check existing documentation and README files first
- **Contributing**: Follow development guidelines in [../TODO.md](../TODO.md)

---

This guide reflects the actual current implementation status as of September 17, 2025. The library is in early development (v0.9.9) with foundation configuration and basic service structure implemented. Full Oracle OIC integration capabilities are planned for future releases following the evidence-based roadmap in TODO.md.

## Related Documentation

**Within Project**:

- [Architecture](architecture.md) - Architecture and design patterns
- [API Reference](api-reference.md) - Complete API documentation
- [Integration](integration.md) - Integration patterns
- [Troubleshooting](troubleshooting.md) - Common issues

**Across Projects**:

- [flext-core Foundation](https://github.com/organization/flext/tree/main/flext-core/docs/architecture/overview.md) - Clean architecture and CQRS patterns
- [flext-core Service Patterns](https://github.com/organization/flext/tree/main/flext-core/docs/guides/service-patterns.md) - Service patterns and dependency injection
- [flext-db-oracle Integration](https://github.com/organization/flext/tree/main/flext-db-oracle/CLAUDE.md) - Oracle database integration

**External Resources**:

- [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
