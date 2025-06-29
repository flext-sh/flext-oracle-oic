# internal.invalid.md - ORACLE-OIC-EXT PROJECT SPECIFICS

**Hierarchy**: PROJECT-SPECIFIC  
**Project**: Oracle OIC Extension - Meltano extension for Oracle Integration Cloud lifecycle management  
**Framework**: Meltano Extension (EDK-based)  
**Status**: ALPHA  
**Last Updated**: 2025-06-26

**Reference**: `/home/marlonsc/CLAUDE.md` → Universal Development Principles  
**Reference**: `/home/marlonsc/internal.invalid.md` → Cross-workspace temporary issues  
**Reference**: `../CLAUDE.md` → PyAuto workspace patterns

---

## 🎯 PROJECT-SPECIFIC CONFIGURATION

### Virtual Environment Usage

```bash
# MANDATORY: Use workspace venv
source /home/marlonsc/pyauto/.venv/bin/activate
# Verify Meltano: python -c "import meltano; print('✅ Meltano available')"
# Verify OIC modules: python -c "import oracle_oic_ext; print('✅ OIC extension available')"
```

### Agent Coordination

```bash
# Read workspace coordination first
cat /home/marlonsc/pyauto/.token | tail -5
# Project context
echo "PROJECT_CONTEXT=oracle-oic-ext" > .token
echo "STATUS=alpha-meltano-extension" >> .token
echo "ORACLE_OIC_INTEGRATION=active" >> .token
```

---

## 🚨 PROJECT-SPECIFIC ISSUES

### **1. Meltano Extension Development Status**

**Status**: **ALPHA** - Built with Meltano Extension Developer Kit (EDK)

**Current Implementation**:

- ✅ Lifecycle management commands (activate, deactivate, status)
- ✅ Monitoring capabilities (health, performance, errors)
- ✅ Advanced extraction features
- ✅ Bulk operations support
- ⚠️ Usage analytics in development

### **2. Oracle Integration Cloud Dependencies**

**Critical**: Requires OIC instance connection and authentication

**OIC Connection Requirements**:

```bash
# Required environment variables for OIC connection
export OIC_HOST="your-oic-instance.oraclecloud.com"
export OIC_USERNAME="your-username"
export OIC_PASSWORD="your-password"
export OIC_VERSION="3"  # OIC API version
```

---

## 🔧 MELTANO EXTENSION SPECIFICS

### Extension Commands Available

```bash
# Lifecycle Management
meltano invoke oracle-oic-ext lifecycle:activate INTEGRATION_ID [VERSION]
meltano invoke oracle-oic-ext lifecycle:deactivate INTEGRATION_ID [VERSION]
meltano invoke oracle-oic-ext lifecycle:status INTEGRATION_ID [VERSION]
meltano invoke oracle-oic-ext lifecycle:bulk-activate --file integrations.json

# Monitoring
meltano invoke oracle-oic-ext monitor:health [--detailed]
meltano invoke oracle-oic-ext monitor:performance [--window HOURS]
meltano invoke oracle-oic-ext monitor:errors [--window HOURS] [--integration INTEGRATION_ID]
meltano invoke oracle-oic-ext monitor:usage [--window DAYS]

# Advanced Extraction
meltano invoke oracle-oic-ext extract:artifacts INTEGRATION_ID [--version VERSION]
meltano invoke oracle-oic-ext extract:logs [--window HOURS] [--level ERROR]
meltano invoke oracle-oic-ext extract:metadata [--detailed]
```

### Meltano Configuration

```yaml
# meltano.yml configuration for this extension
plugins:
  utilities:
    - name: oracle-oic-ext
      namespace: oracle_oic_ext
      pip_url: -e .
      executable: oracle-oic-ext
      commands:
        lifecycle:activate:
          args: activate
          description: Activate OIC integration
        monitor:health:
          args: health
          description: Check OIC instance health
```

---

## 📋 ENVIRONMENT VARIABLES (PROJECT-SPECIFIC)

### Required Variables

```bash
# Oracle Integration Cloud connection
OIC_HOST=your-oic-instance.oraclecloud.com     # OIC instance hostname
OIC_USERNAME=your-username                      # OIC username
OIC_PASSWORD=your-password                      # OIC password
OIC_VERSION=3                                   # OIC API version
OIC_TIMEOUT=30                                  # Connection timeout in seconds
```

### Optional Variables

```bash
# Extension behavior configuration
OIC_DEBUG_MODE=true                             # Enable debug logging
OIC_RETRY_COUNT=3                               # Number of retry attempts
OIC_BATCH_SIZE=10                               # Batch size for bulk operations
OIC_CACHE_TTL=300                               # Cache TTL in seconds
```

---

## 🔍 CLI COMMANDS (PROJECT-SPECIFIC)

### Direct Extension Usage

```bash
# Generate configuration from template
python generate_config.py --output config.json

# Run extension directly (development)
python -m oracle_oic_ext.main --help

# Test extension integration
python -m oracle_oic_ext.main lifecycle:status --integration TEST_INTEGRATION
```

### Meltano Integration Testing

```bash
# Install extension in Meltano
meltano install utility oracle-oic-ext

# Test extension commands
meltano invoke oracle-oic-ext monitor:health --detailed

# Run with debug logging
meltano --log-level debug invoke oracle-oic-ext lifecycle:status INTEGRATION_ID
```

---

## 🧪 TESTING NOTES (PROJECT-SPECIFIC)

### Extension Testing Strategy

```bash
# Unit tests for extension components
pytest tests/test_extension.py --verbose

# End-to-end testing with OIC instance
pytest tests/test_e2e_complete.py --verbose

# Test configuration generation
python generate_config.py --test-mode
```

### Testing Requirements

- **OIC Instance Access**: Requires valid OIC connection for integration tests
- **Mock Testing**: Unit tests use mocked OIC responses
- **Configuration Testing**: Validates config.json generation and parsing

---

## 📈 ORACLE OIC INTEGRATION SPECIFICS

### OIC API Integration

- **REST API**: Uses OIC REST API for lifecycle management
- **Authentication**: Basic authentication with OIC credentials
- **Error Handling**: Comprehensive error handling for OIC API responses
- **Rate Limiting**: Respects OIC API rate limits

### Integration Lifecycle Management

```python
# Example integration activation
from oracle_oic_ext.lifecycle.manager import LifecycleManager

manager = LifecycleManager(config)
result = manager.activate_integration("INTEGRATION_ID", version="01.00.0000")
```

### Monitoring Capabilities

- **Health Checks**: OIC instance availability and status
- **Performance Metrics**: Integration execution times and throughput
- **Error Analysis**: Error pattern analysis and reporting
- **Usage Analytics**: Integration usage patterns and statistics

---

## 🔄 MELTANO EDK INTEGRATION

### Extension Development Kit Features

- **Command Framework**: EDK command structure for lifecycle and monitoring
- **Configuration Management**: EDK configuration handling
- **Logging Integration**: EDK logging framework integration
- **Error Handling**: EDK error handling patterns

### Extension Deployment

```bash
# Package extension for distribution
python setup.py sdist bdist_wheel

# Install in development mode
pip install -e .

# Install from package
pip install oracle-oic-ext
```

---

## 🚀 DEPLOYMENT NOTES

### Meltano Project Integration

1. Add extension to meltano.yml
2. Configure OIC connection parameters
3. Install extension via Meltano CLI
4. Test extension commands
5. Integrate with Meltano pipelines

### Production Considerations

- **Security**: Store OIC credentials securely
- **Monitoring**: Set up monitoring for extension operations
- **Logging**: Configure appropriate log levels
- **Error Handling**: Implement retry logic for transient failures

---

**Authority**: This file contains project-specific information for oracle-oic-ext  
**Escalation**: Issues affecting Meltano extension patterns should be documented in workspace CLAUDE.md  
**Reference**: For Meltano extension patterns → `../CLAUDE.md`
