# Style and Conventions for flext-oracle-oic-ext

## Code Style


- **Python 3.13+**: Use modern Python features
- **Type Hints**: 100% type coverage with MyPy strict mode
- **Pydantic 2.11+**: All models use Pydantic with ConfigDict
- **Async/Await**: Use async for Oracle OIC API calls
- **FlextResult**: All operations return FlextResult[T] for error handling


## Naming Conventions

- **Classes**: PascalCase (e.g., `OracleOICExtensionService`)
- **Methods**: snake_case (e.g., `list_integrations`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `DEFAULT_API_VERSION`)
- **Private methods**: Leading underscore (e.g., `_get_client`)
- **Modules**: snake_case (e.g., `ext_services.py`)


## Architecture Patterns

- **Unified Class Pattern**: Single class per module with nested helpers
- **EXTENSION Pattern**: Specialized services following FLEXT standards
- **Domain-Driven Design**: Clear separation of concerns

- **Dependency Injection**: Use FlextContainer for service registration

## Error Handling

- **FlextResult Pattern**: Never use try/except fallbacks
- **Explicit Error Checking**: Use `.is_failure` and `.success` properties

- **Type-Safe Extraction**: Use `.unwrap()` for safe value extraction
- **Structured Logging**: Use FlextLogger for all logging

## Documentation

- **Docstrings**: Google style with Args, Returns, Raises

- **Type Annotations**: Complete type coverage
- **Examples**: Include usage examples in docstrings
- **Copyright**: MIT license header in all files

## Testing


- **Test Coverage**: Minimum 75%, target 100%
- **Test Naming**: `test_<functionality>_<scenario>`
- **Fixtures**: Use pytest fixtures for test data
- **Mocking**: Mock external dependencies (Oracle OIC API)

## Configuration


- **Pydantic Models**: All config uses Pydantic validation
- **Environment Variables**: Support for env var overrides
- **Default Values**: Sensible defaults for all settings
- **Validation**: Business rule validation in models

## Import Organization

```python
# Standard library imports
from __future__ import annotations
import asyncio
from typing import Protocol, Self

# Third-party imports
from pydantic import ConfigDict, SecretStr

# FLEXT ecosystem imports
from flext_core import (
    FlextConstants,
    FlextLogger,
    FlextResult,
    FlextService,
    FlextTypes,

)

# Local imports
from flext_oracle_oic_ext.ext_client import OracleOICExtension
Client
from flext_oracle_oic_ext.ext_config import OracleOICExtensionSettings
```

## Constants Management

- **Centralized**: All constants in dedicated constants.py file
- **Inheritance**: Inherit from FlextConstants base class
- **Namespace**: Use nested classes for organization
- **No Duplication**: Single source of truth for all constants
