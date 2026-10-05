# Getting Started

<!-- TOC START -->

- [Prerequisites](#prerequisites)
  - [Required Software](#required-software)
  - [Optional for Testing](#optional-for-testing)
  - [Knowledge Requirements](#knowledge-requirements)
- [Installation](#installation)
  - [Development Installation (Recommended)](#development-installation-recommended)
  - [Environment Setup](#environment-setup)
- [Basic Usage](#basic-usage)
  - [Configuration Management](#configuration-management)
  - [Current Capabilities](#current-capabilities)
- [Development Commands](#development-commands)
  - [Essential Commands](#essential-commands)
  - [Testing Commands](#testing-commands)
- [Current Implementation Status](#current-implementation-status)
  - [Available Features ✅](#available-features)
  - [Planned Features 🚧](#planned-features)
  - [Known Limitations ⚠️](#known-limitations)
- [Troubleshooting](#troubleshooting)
  - [Common Installation Issues](#common-installation-issues)
  - [Development Issues](#development-issues)
- [Next Steps](#next-steps)
- [Getting Help](#getting-help)
  - [Resources](#resources)
  - [Support Channels](#support-channels)
- [Related Documentation](#related-documentation)

<!-- TOC END -->

**flext-oracle-oic v0.12.0-dev** - Oracle Integration Cloud client library for the FLEXT
ecosystem

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)

## Prerequisites

### Required Software

- **Managed Python toolchain** provisioned by `make setup` through Mise and uv
- **FLEXT workspace** setup with access to
  [flext-core](https://github.com/flext-sh/flext/tree/0.12.0-dev/flext-core/README.md)
- **Git** for version control

### Optional for Testing

- Oracle Integration Cloud instance access
- OAuth2/IDCS credentials for Oracle cloud

### Knowledge Requirements

- Basic understanding of Oracle Integration Cloud concepts
- Familiarity with FLEXT ecosystem patterns (r, s)
- Python experience with Pydantic and type annotations

## Installation

### Development Installation (Recommended)

```bash
# Standalone checkout on the configured integration line
git clone --branch 0.12.0-dev https://github.com/flext-sh/flext-oracle-oic.git
cd flext-oracle-oic

# Provision and validate through this checkout's canonical Make interface
make setup
make check
```

### Environment Setup

```bash
# Before selecting network operations, provision the declared deployment inputs.
# These checks do not print credentials or invent defaults.
: "${FLEXT_ORACLE_OIC_ORACLEOIC__BASE_URL:?Set the OIC instance URL}"
: "${FLEXT_ORACLE_OIC_ORACLEOIC__OAUTH_CLIENT_ID:?Set the OAuth client ID}"
: "${FLEXT_ORACLE_OIC_ORACLEOIC__OAUTH_CLIENT_SECRET:?Set the OAuth secret}"
: "${FLEXT_ORACLE_OIC_ORACLEOIC__OAUTH_TOKEN_URL:?Set the OAuth token endpoint}"
```

## Basic Usage

### Configuration Management

The library provides Pydantic-based configuration following FLEXT patterns:

```python
from flext_oracle_oic import FlextOracleOicSettings, settings

runtime_settings = FlextOracleOicSettings.model_validate(settings.model_dump())
if runtime_settings.OracleOic.base_url != settings.OracleOic.base_url:
    message = "Settings validation did not preserve the configured URL"
    raise ValueError(message)
```

### Current Capabilities

> **Important**: Version 0.9.9 provides foundation configuration and basic service
> structure:

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

## Development Commands

### Essential Commands

```bash
# Setup development environment
make setup
make gen
make mod
make gen
make gen
make fix
make fmt
make check
make test
make build

```

### Testing Commands

```bash
# Preserve the canonical persistent testmon database and runner budgets.
make test
make test-full
make test-file FILE=tests/unit/test_models.py

# Execute the existing authored Markdown examples through the public consumer.
make test-file FILE=docs/configuration.md
```

## Current Implementation Status

### Available Features ✅

- **Configuration Management**: Pydantic models for Oracle OIC settings
- **Basic Service Structure**: Foundation classes and module organization
- **FLEXT Integration**: Imports and basic patterns (needs completion)

### Planned Features 🚧

- **s Implementation**: Complete FLEXT compliance (critical requirement)
- **OAuth2/IDCS Authentication**: Full Oracle cloud authentication
- **Integration Patterns**: App-driven orchestration, scheduled orchestration
- **Enterprise Features**: Circuit breaker, retry patterns, monitoring

### Known Limitations ⚠️

1. **FLEXT Compliance Violations**:

   - Direct `httpx` import in `ext_client.py:12` (should use flext-api)
   - Direct `typer` import in `main.py:15` (should use flext-cli)
   - Missing s inheritance

1. **Type Safety Issues**:

   - 2 MyPy errors in `exceptions.py:283` and `test_models.py:61`

1. **Test Coverage**:

   - Current: 21% coverage (measured)
   - Target: 70%+ with integration tests

## Troubleshooting

### Common Installation Issues

**Import Errors from FLEXT-Core**

```bash
# Reconcile this checkout's managed environment, then inspect native import gates.
make setup
make check
```

**Quality Gate Failures**

```bash
# Preserve full native diagnostics; do not truncate the first failure.
make check
make fix
make fmt
make check
```

**Dependency Reset**

```bash
# Reset environment
make setup
```

### Development Issues

**FLEXT Pattern Violations**

```bash
# Use the canonical modernization owner and then verify its findings.
make mod
make check
```

## Next Steps

1. **Review Current Implementation**: See [architecture.md](architecture.md) for
   detailed analysis
1. **Check Development Workflow**: See [guides/development.md](guides/development.md)
   for the evidence-based development plan
1. **Understand FLEXT Patterns**: Review
   [flext-core documentation](https://github.com/flext-sh/flext/tree/0.12.0-dev/flext-core/README.md)
1. **Review Configuration**: See [configuration.md](configuration.md) for detailed
   settings

## Getting Help

### Resources

- **Documentation**: Complete docs in the [documentation index](index.md)
- **FLEXT Ecosystem**: See the
  [workspace README](https://github.com/flext-sh/flext/blob/0.12.0-dev/README.md) for
  context
- **API Reference**: See [api-reference.md](api-reference.md) for available APIs

### Support Channels

- **Issues**: Create GitHub issue with detailed error information
- **Questions**: Check existing documentation and README files first
- **Contributing**: Follow development guidelines in
  [guides/development.md](guides/development.md)

---

This guide reflects the actual current implementation status as of April 14, 2026. The
library is in early development (v0.12.0-dev) with foundation configuration and basic
service structure implemented. Full Oracle OIC integration capabilities are planned for
future releases following the evidence-based roadmap in the development guide.

## Related Documentation

**Within Project**:

- [Architecture](architecture.md) - Architecture and design patterns
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
