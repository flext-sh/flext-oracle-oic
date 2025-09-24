# Task Completion Checklist for flext-oracle-oic-ext

## Pre-Commit Validation (MANDATORY)

```bash
# 1. Check for prohibited scripts
find . -name "fix_*.py" -o -name "temp_*.py" -o -name "migrate_*.py" | grep -v tests/
# Should return empty - if not, STOP IMMEDIATELY

# 2. Run linting
make lint
# Must pass with zero errors

# 3. Run type checking
make type-check
# Must pass with zero errors

# 4. Run tests
make test
# Must pass with minimum 75% coverage

# 5. Check for unauthorized file modifications
git status | grep -E "(pyproject\.toml|Makefile|\.gitignore|go\.mod|package\.json|\.env)"
# Should not show any critical files modified
```

## Quality Gates Checklist

- [ ] **No Prohibited Scripts**: No fix*\*.py, temp*_.py, migrate\__.py files created
- [ ] **Linting Passes**: `make lint` returns zero errors
- [ ] **Type Checking Passes**: `make type-check` returns zero errors
- [ ] **Tests Pass**: `make test` passes with minimum 75% coverage
- [ ] **No Critical Files Modified**: pyproject.toml, Makefile, .gitignore unchanged
- [ ] **FlextResult Pattern**: All operations use FlextResult[T] for error handling
- [ ] **Unified Class Pattern**: Single class per module with nested helpers
- [ ] **Constants Standardized**: All constants in dedicated constants.py file
- [ ] **No Duplication**: Single source of truth for all constants
- [ ] **Proper Imports**: Use flext-core imports, no direct third-party imports

## Constants Standardization Checklist

- [ ] **FlextOracleOicExtConstants Created**: Inherits from FlextConstants
- [ ] **Flat Structure**: All constants as flat class attributes
- [ ] **No Duplication**: Removed duplicate constants from other files
- [ ] **References Updated**: All code references updated to use new constants
- [ ] **Enums/Literals**: Converted to use FlextConstants patterns
- [ ] **Documentation**: Constants properly documented with usage examples
- [ ] **Type Safety**: All constants properly typed with Final annotations

## Code Quality Checklist

- [ ] **Type Annotations**: 100% type coverage
- [ ] **Docstrings**: Complete documentation for all public methods
- [ ] **Error Handling**: Explicit FlextResult error handling
- [ ] **Logging**: Structured logging with FlextLogger
- [ ] **Configuration**: Pydantic models for all configuration
- [ ] **Testing**: Comprehensive test coverage
- [ ] **Performance**: No performance regressions
- [ ] **Security**: No security vulnerabilities

## Final Validation

```bash
# Run complete validation pipeline
make validate

# Check for any remaining issues
poetry run ruff check src/ --fix
poetry run mypy src/
poetry run pytest --cov=src --cov-report=term-missing

# Verify constants are properly used
grep -r "FlextOracleOicExtConstants" src/
grep -r "100\|200\|30\|60\|300\|1000" src/ | grep -v constants.py
```

## Success Criteria

- All quality gates pass
- Constants properly standardized
- No duplication of constants
- All references updated
- Code follows FLEXT patterns
- Documentation complete
- Tests pass with good coverage
