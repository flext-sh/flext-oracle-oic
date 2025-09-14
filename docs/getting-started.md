# Getting Started

**flext-oracle-oic-ext v0.9.0** - Oracle Integration Cloud extension for the FLEXT ecosystem

## Prerequisites

- **Python 3.13+** with Poetry for dependency management
- **FLEXT workspace** setup and access to flext-core
- Basic understanding of Oracle Integration Cloud concepts
- (Optional) Oracle OIC instance for testing real integrations

## Installation

### Development Installation

```bash
# Clone and setup within FLEXT workspace
cd /path/to/flext/workspace
git clone <repository-url> flext-oracle-oic-ext
cd flext-oracle-oic-ext

# Install dependencies
poetry install --with dev,test

# Run basic validation
make validate
```

### Environment Setup

```bash
# Set Python path for FLEXT workspace
export PYTHONPATH="/path/to/flext/workspace/src:$PYTHONPATH"

# Optional: Oracle OIC environment variables for testing
export ORACLE_OIC_BASE_URL="https://your-instance.integration.ocp.oraclecloud.com"
export ORACLE_OIC_CLIENT_ID="your_client_id"
export ORACLE_OIC_CLIENT_SECRET="your_client_secret"
```

## Basic Usage

### Configuration

```python
from flext_oracle_oic_ext import (
    OracleOICExtensionSettings,
    OICExtensionConnectionConfig,
    OICExtensionAuthConfig
)

# Create basic configuration
settings = OracleOICExtensionSettings(
    connection=OICExtensionConnectionConfig(
        base_url="https://test.integration.ocp.oraclecloud.com",
        api_version="v1",
        request_timeout=30
    ),
    auth=OICExtensionAuthConfig(
        oauth_client_id="test_client",
        oauth_client_secret="test_secret",
        oauth_token_url="https://test.identity.oraclecloud.com/oauth2/v1/token"
    )
)
```

### Service Creation

```python
from flext_oracle_oic_ext import OracleOICExtensionService

# Create service instance
service = OracleOICExtensionService(settings)

# Note: Full Oracle OIC integration still in development
# Current implementation provides basic structure and configuration
```

## Development Commands

```bash
# Essential development commands
make install-dev    # Install development dependencies
make validate       # Run all quality gates
make test           # Run test suite
make lint           # Code linting
make type-check     # Type checking
make format         # Code formatting
```

## Current Limitations

> **Important**: This is an early development version (v0.9.0) with several limitations:

- **FLEXT Compliance**: Has violations that need fixing (direct httpx usage)
- **Oracle OIC Integration**: Basic structure only, no real OIC API calls yet
- **Authentication**: Framework exists but needs complete OAuth2/IDCS implementation
- **WMS Integration**: Not implemented
- **Enterprise Patterns**: Not implemented

## Next Steps

1. **Review Architecture** - See [architecture.md](architecture.md) for current implementation
2. **Check Development Guide** - See [development.md](development.md) for contribution guidelines
3. **Review Roadmap** - See [../TODO.md](../TODO.md) for development priorities

## Troubleshooting

### Common Issues

**Import Errors**
```bash
# Ensure FLEXT workspace is properly configured
export PYTHONPATH="/path/to/flext/workspace/src:$PYTHONPATH"
cd /path/to/flext/workspace
poetry shell
```

**Quality Gate Failures**
```bash
# Check specific quality gates
make lint           # Fix linting issues
make type-check     # Fix type annotations
make test           # Fix failing tests
```

### Getting Help

- **Issues**: Create GitHub issue with detailed description
- **Questions**: Check existing documentation first
- **Contributing**: See development guide for contribution process

---

This guide reflects the current early development status of the project. Full Oracle OIC integration capabilities are planned for future releases.