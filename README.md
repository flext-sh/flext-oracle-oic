# flext-oracle-oic-ext

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![FLEXT Framework](https://img.shields.io/badge/FLEXT-Extension-green.svg)](https://github.com/flext)

**Oracle Integration Cloud extension for the FLEXT ecosystem** - Basic Oracle OIC HTTP client patterns with OAuth2 authentication framework.

> **⚠️ STATUS**: Early Development (v0.9.0) - Basic foundation with FLEXT compliance issues to resolve

---

## 🎯 Purpose and Role in FLEXT Ecosystem

### **For the FLEXT Ecosystem**

This extension provides basic Oracle Integration Cloud HTTP client patterns for FLEXT projects requiring Oracle OIC connectivity. Currently implements basic authentication and client structure with plans for full integration capabilities.

### **Key Responsibilities**

1. **Oracle OIC HTTP Client** - Basic HTTP client structure for Oracle Integration Cloud APIs
2. **OAuth2 Authentication Framework** - Foundation for Oracle IDCS authentication (partial implementation)
3. **FLEXT Integration Pattern** - Extension pattern following FLEXT ecosystem standards (with current violations to fix)

### **Integration Points**

- **flext-core** → Uses FlextResult, FlextLogger (needs dependency injection improvements)
- **flext-api** → Should use for HTTP clients (currently violates by using httpx directly)
- **flext-cli** → Should use for CLI functionality (currently violates by using typer directly)

---

## 🏗️ Architecture and Patterns

### **FLEXT-Core Integration Status**

| Pattern             | Status         | Description             |
| ------------------- | -------------- | ----------------------- |
| **FlextResult<T>**  | 🟡 75% | Basic usage implemented, needs completion     |
| **FlextService**    | 🔴 25% | Service structure exists, needs proper patterns    |
| **FlextContainer**  | 🔴 0% | Not implemented - needs dependency injection    |
| **Domain Patterns** | 🔴 10% | Basic models exist, no DDD implementation    |

> **Status**: 🔴 Critical | 🟡 Partial | 🟢 Complete

### **Current Implementation**

```
src/flext_oracle_oic_ext/
├── __init__.py              # Module exports
├── ext_config.py            # Pydantic configuration models
├── ext_exceptions.py        # Oracle OIC exception hierarchy
├── ext_client.py            # Basic HTTP client (needs FLEXT compliance)
├── ext_services.py          # Service layer (basic structure)
├── ext_models.py            # Data models using Pydantic
├── cli.py                   # CLI (needs flext-cli patterns)
├── extension.py             # Legacy extension pattern
└── factory.py               # Service factory patterns
```

---

## 🚀 Quick Start

### **Installation**

```bash
# From source (recommended for development)
cd flext-oracle-oic-ext
poetry install --with dev,test
```

### **Basic Usage**

```python
from flext_oracle_oic_ext import OracleOICExtensionService, OracleOICExtensionSettings

# Basic configuration
settings = OracleOICExtensionSettings(
    connection=OICExtensionConnectionConfig(
        base_url="https://your-oic-instance.integration.ocp.oraclecloud.com"
    ),
    auth=OICExtensionAuthConfig(
        oauth_client_id="your_client_id",
        oauth_client_secret="your_client_secret",
        oauth_token_url="https://your-idcs.identity.oraclecloud.com/oauth2/v1/token"
    )
)

# Create service instance
service = OracleOICExtensionService(settings)

# Note: Full functionality still in development
```

---

## 🔧 Development

### **Essential Commands**

```bash
# Setup development environment
make install-dev

# Quality gates
make validate      # Complete validation pipeline
make lint          # Code linting with ruff
make type-check    # MyPy type checking
make test          # Run test suite
make format        # Format code
```

### **Quality Gates**

Current quality status and requirements:

- **Coverage**: Target 90% (currently basic test suite exists)
- **Type Safety**: Partial implementation, needs completion
- **Security**: Basic structure, needs security audit
- **FLEXT-Core Compliance**: 25% - Major violations need fixing

---

## 🧪 Testing

### **Test Structure**

```
tests/
├── unit/                    # Unit tests for business logic
├── conftest.py             # Test configuration and fixtures
├── test_basic.py           # Basic functionality tests
├── test_config.py          # Configuration tests
├── test_models.py          # Model validation tests
└── test_extension.py       # Extension pattern tests
```

### **Testing Commands**

```bash
make test              # Run all tests
make test-unit         # Unit tests only
make coverage-html     # Generate coverage report
```

---

## 📊 Status and Metrics

### **Quality Standards**

- **Coverage**: 65% (needs improvement to 90%)
- **Type Safety**: Partial (MyPy strict mode compliance needed)
- **Security**: Basic (comprehensive security audit needed)
- **FLEXT-Core Compliance**: 25% (critical violations to fix)

### **Critical Issues to Address**

1. **FLEXT Compliance Violations**
   - Direct `httpx` import (should use flext-api)
   - Direct `typer` import (should use flext-cli)
   - Missing dependency injection patterns

2. **Language Inconsistency**
   - Portuguese comments mixed with English code
   - Needs standardization to English-only

3. **Architecture Gaps**
   - No Clean Architecture implementation
   - Missing Domain-Driven Design patterns
   - Basic service structure needs improvement

---

## 🗺️ Roadmap

### **Current Version (v0.9.0)**

Basic foundation with configuration, models, and service structure. FLEXT compliance violations need immediate attention.

### **Next Version (v0.10.0)**

- Fix all FLEXT compliance violations
- Implement proper dependency injection
- Complete OAuth2/IDCS authentication
- Achieve 90% test coverage

### **Future Versions**

- Real Oracle OIC API integration
- Enterprise integration patterns
- WMS integration (if business requirement confirmed)
- Production-ready deployment patterns

---

## 📚 Documentation

- **[Getting Started](docs/getting-started.md)** - Installation and basic setup
- **[Architecture](docs/architecture.md)** - Current architecture and improvement plans
- **[Development](docs/development.md)** - Development guidelines and standards
- **[TODO & Roadmap](TODO.md)** - Detailed development roadmap and priorities

---

## 🤝 Contributing

### **Immediate Priorities**

1. **Fix FLEXT compliance violations** - Replace direct httpx/typer usage
2. **Language standardization** - Convert Portuguese comments to English
3. **Implement proper patterns** - Add dependency injection and service patterns
4. **Improve test coverage** - Add comprehensive unit and integration tests

### **Quality Standards**

- **Type Safety**: 100% MyPy strict mode compliance required
- **Test Coverage**: 90% minimum for all new code
- **FLEXT Compliance**: Zero tolerance for ecosystem violations
- **Documentation**: English-only, clear and accurate

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🆘 Support

- **Documentation**: [docs/](docs/)
- **Issues**: [GitHub Issues](https://github.com/flext-sh/flext-oracle-oic-ext/issues)
- **Security**: Report security issues privately to maintainers

---

**flext-oracle-oic-ext v0.9.0** - Oracle Integration Cloud extension providing basic HTTP client patterns for FLEXT ecosystem integration projects.

**Mission**: Develop a reliable Oracle OIC integration library following FLEXT ecosystem standards and enabling Oracle Integration Cloud connectivity for enterprise Python applications.