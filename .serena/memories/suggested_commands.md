# Suggested Commands for flext-oracle-oic-ext Development

## Quality Gates (MANDATORY)

```bash
# Complete validation pipeline
make validate

# Quick health check
make check

# Individual quality checks
make lint          # Ruff linting
make type-check    # MyPy type checking
make test          # Run tests with coverage
make format        # Auto-format code
```

## Development Workflow

```bash
# Setup development environment
make setup

# Install dependencies
poetry install

# Run specific tests
poetry run pytest tests/test_ext_services.py -v
poetry run pytest tests/test_ext_client.py -v

# Type checking
poetry run mypy src/

# Linting
poetry run ruff check src/
poetry run ruff format src/
```

## Testing

```bash
# Run all tests
make test

# Run with coverage
poetry run pytest --cov=src --cov-report=term-missing

# Run specific test file
poetry run pytest tests/test_ext_services.py::test_oracle_oic_extension_service -v

# Run with verbose output
poetry run pytest -v -s
```

## CLI Usage

```bash
# Run the extension
flext-oracle-oic-ext

# Run as module
python -m flext_oracle_oic_ext

# Help
flext-oracle-oic-ext --help
```

## Configuration

```bash
# Check configuration
python -c "from flext_oracle_oic_ext.ext_config import OracleOICExtensionConfig; print(OracleOICExtensionConfig())"

# Validate settings
python -c "from flext_oracle_oic_ext.ext_config import OracleOICExtensionSettings; print(OracleOICExtensionSettings())"
```

## Debugging

```bash
# Run with debug logging
PYTHONPATH=src python -m flext_oracle_oic_ext --debug

# Interactive debugging
python -c "from flext_oracle_oic_ext.ext_services import OracleOICExtensionService; help(OracleOICExtensionService)"

# Check imports
python -c "from flext_oracle_oic_ext import *; print('All imports successful')"
```

## Build & Distribution

```bash
# Build package
poetry build

# Install in development mode
poetry install --editable

# Check package
poetry check
```
