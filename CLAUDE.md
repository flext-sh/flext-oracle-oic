# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**flext-oracle-oic-ext** is an Oracle Integration Cloud (OIC) extension library within the FLEXT ecosystem. It provides advanced enterprise integration patterns, workflow orchestration, and OIC REST API integration capabilities. The project implements consolidated architecture patterns using centralized components from flext-meltano to eliminate code duplication.

## Architecture & Design

### Consolidated Architecture
- **Centralized Components**: Uses `flext-meltano.extensions.oracle_oic` for core OIC functionality to prevent code duplication
- **Extension Pattern**: Implements Oracle OIC-specific extensions with enterprise integration patterns
- **Foundation**: Built on `flext-core` for FlextResult patterns, dependency injection, and base configurations
- **Zero Tolerance**: Strict consolidation policy - no duplicate implementations across the FLEXT ecosystem

### Key Components
- **OracleOICExtension**: Main extension class (consolidated from flext-meltano)
- **OIC Patterns**: Enterprise integration patterns (Message Router, Scatter-Gather, Content Filter, etc.)
- **OAuth2 Authentication**: IDCS OAuth2 client credentials flow with proper scope handling
- **REST API Clients**: OIC Tap and Target clients with pagination and retry logic
- **Configuration Management**: Environment-based configuration with validation

### Integration Patterns Supported
- **Message Router**: Route messages based on content and rules
- **Scatter-Gather**: Broadcast to multiple endpoints and aggregate responses
- **Content Filter**: Filter messages based on payload content
- **Message Translator**: Transform message formats and structures
- **Aggregator**: Combine multiple messages into single output
- **Splitter**: Split single message into multiple messages

## Development Commands

### Essential Commands
```bash
# Development setup
make setup                    # Complete development setup
make install                  # Install dependencies with Poetry
make dev-install             # Install in development mode with pre-commit hooks

# Quality Gates (run before committing)
make validate                # Full validation (lint + type + security + test + oic-test)
make check                   # Essential checks (lint + type + test)
make lint                    # Ruff linting with ALL rules enabled
make type-check              # MyPy strict type checking
make security                # Security scans (bandit + pip-audit)
make format                  # Format code with ruff

# Testing
make test                    # Run tests with 90% coverage requirement
make test-unit               # Run unit tests only
make test-integration        # Run integration tests only
make test-oic                # Run OIC-specific tests
make test-patterns           # Run integration pattern tests
make test-orchestration      # Run orchestration tests
make test-performance        # Run performance benchmarks
```

### OIC-Specific Operations
```bash
# Oracle OIC API Testing
make oic-test               # Test OIC API connectivity
make oic-auth               # Test OAuth2 authentication
make oic-deploy             # Test integration deployment
make oic-patterns           # Test enterprise integration patterns
make oic-orchestration      # Test workflow orchestration
make oic-monitoring         # Test monitoring capabilities

# Pattern Testing
make pattern-test           # Test all integration patterns
make message-router         # Test message router pattern
make scatter-gather         # Test scatter-gather pattern
make content-filter         # Test content filter pattern
make aggregator             # Test aggregator pattern

# Development Tools
make dev-oic-server         # Start development OIC mock server
make dev-pattern-playground # Integration pattern playground
make dev-orchestration-designer # Workflow designer
```

### Build & Deployment
```bash
make build                  # Build distribution packages
make package                # Create deployment package
make clean                  # Remove all artifacts
make deps-update            # Update dependencies
make deps-audit             # Security audit dependencies
```

## Testing Strategy

### Test Categories
- **Unit Tests**: Core functionality testing with mocks
- **Integration Tests**: Real OIC API integration testing
- **E2E Tests**: Complete workflow testing
- **OIC Tests**: Oracle OIC-specific functionality testing  
- **Pattern Tests**: Enterprise integration pattern validation
- **Performance Tests**: Benchmark critical operations

### Test Execution
```bash
# Run specific test types
pytest -m unit              # Unit tests only
pytest -m integration       # Integration tests only
pytest -m oic               # OIC-specific tests
pytest -m patterns          # Integration pattern tests
pytest -m orchestration     # Orchestration tests
pytest -m performance       # Performance tests

# Test single file
pytest tests/test_extension.py -v
pytest tests/unit/test_version.py -v

# Coverage reporting
make coverage               # Generate coverage report
make coverage-html          # Open HTML coverage report
```

## Configuration

### Environment Variables
Key environment variables for OIC extension operations:
```bash
# OIC Connection
export OIC_EXT_BASE_URL="https://your-instance.integration.ocp.oraclecloud.com"
export OIC_EXT_API_VERSION="v1"

# OAuth2 Authentication
export OIC_EXT_OAUTH_CLIENT_ID="your_client_id"
export OIC_EXT_OAUTH_CLIENT_SECRET="your_client_secret"  
export OIC_EXT_OAUTH_TOKEN_URL="https://idcs-tenant.identity.oraclecloud.com/oauth2/v1/token"
export OIC_EXT_OAUTH_SCOPE="https://integration.ocp.oraclecloud.com:443"

# Extension Features
export OIC_EXT_ENABLE_MONITORING="true"
export OIC_EXT_ENABLE_ENTERPRISE_PATTERNS="true"
export OIC_EXT_ENABLE_ORCHESTRATION="true"
export OIC_EXT_ENABLE_CUSTOM_ADAPTERS="true"
```

### Configuration Files
- `config.json`: Main configuration file (see `config.json.example`)
- `pyproject.toml`: Project dependencies and tool configuration
- `.env`: Environment variables (not tracked in git)

## Code Standards

### Quality Requirements
- **Coverage**: Minimum 90% test coverage enforced
- **Type Safety**: Strict MyPy configuration with no untyped code
- **Linting**: Ruff with ALL rule categories enabled
- **Security**: Bandit security scanning and pip-audit
- **Import Organization**: Consolidated imports from flext-meltano

### Architecture Constraints
1. **No Code Duplication**: All OIC functionality must use centralized components from flext-meltano
2. **FlextResult Pattern**: All operations must return FlextResult for consistent error handling
3. **Dependency Injection**: Use flext-core DI container for dependencies
4. **Configuration**: Use flext-core BaseSettings patterns
5. **Logging**: Use flext-core FlextLoggerFactory

## Integration with FLEXT Ecosystem

### Dependencies
- **flext-core**: Foundation patterns, FlextResult, DI container, logging
- **flext-meltano**: Centralized OIC extension implementation 
- **pydantic**: Data validation and settings management
- **requests/httpx**: HTTP client operations
- **tenacity**: Retry logic and resilience patterns

### Ecosystem Role
This project serves as the OIC extension library within the FLEXT ecosystem, providing:
- Oracle Integration Cloud REST API integration
- Enterprise integration patterns implementation
- Workflow orchestration capabilities
- Authentication and security patterns
- Monitoring and observability features

## Common Patterns

### FlextResult Usage
```python
from flext_core import FlextResult

def process_integration() -> FlextResult[IntegrationData]:
    try:
        result = perform_operation()
        return FlextResult.ok(result)
    except Exception as e:
        return FlextResult.fail(f"Operation failed: {e}")
```

### Configuration Pattern
```python
from flext_oracle_oic_ext.config import OracleOICExtensionSettings

settings = OracleOICExtensionSettings()
# Configuration automatically loaded from environment variables
```

### OIC Authentication
```python
from flext_oracle_oic_ext.oic_patterns import OICTapAuthenticator, OICConnectionConfig

auth = OICTapAuthenticator(auth_config)
token_result = auth.get_access_token()
if token_result.success:
    # Use token for API calls
    token = token_result.data
```

## Troubleshooting

### Common Issues
1. **Authentication Failures**: Check OAuth2 credentials and token URL
2. **API Timeouts**: Verify OIC instance accessibility and network connectivity  
3. **Import Errors**: Ensure flext-meltano dependency is properly installed
4. **Configuration Issues**: Validate config.json format and required fields

### Debug Commands
```bash
# Test OIC connectivity
make oic-test

# Validate configuration
poetry run python -c "from flext_oracle_oic_ext.config import OracleOICExtensionSettings; print(OracleOICExtensionSettings())"

# Check dependencies
poetry show --tree
make deps-audit
```