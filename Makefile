# =============================================================================
# FLEXT ORACLE OIC EXTENSIONS - MAKEFILE
# PEP Strict Compliance with Poetry Build System - Oracle Extensions
# =============================================================================

.DEFAULT_GOAL := help
SHELL := /bin/bash

# Project Configuration
PROJECT_NAME := flext-oracle-oic-ext
PYTHON_VERSION := 3.13
SOURCE_DIR := src
TESTS_DIR := tests
REPORTS_DIR := reports
MODULE_NAME := oracle_oic_ext

# Colors for output
CYAN := \\033[0;36m
GREEN := \\033[0;32m
YELLOW := \\033[1;33m
RED := \\033[0;31m
NC := \\033[0m # No Color

# =============================================================================
# HELP SYSTEM
# =============================================================================

.PHONY: help
help: ## Show this help message
	@echo -e "$(CYAN)$(PROJECT_NAME) - Oracle OIC Extensions Development Commands$(NC)"
	@echo -e "$(CYAN)=========================================================$(NC)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "$(GREEN)%-20s$(NC) %s\\n", $$1, $$2}' $(MAKEFILE_LIST)

# =============================================================================
# ENVIRONMENT SETUP
# =============================================================================

.PHONY: install
install: ## Install project dependencies with Poetry
	@echo -e "$(CYAN)Installing project dependencies...$(NC)"
	poetry install --all-extras
	poetry run pre-commit install
	@echo -e "$(GREEN)✓ Installation complete$(NC)"

.PHONY: install-dev
install-dev: ## Install development dependencies
	@echo -e "$(CYAN)Installing development dependencies...$(NC)"
	poetry install --with dev,security,build,test
	poetry run pre-commit install
	@echo -e "$(GREEN)✓ Development installation complete$(NC)"

.PHONY: update
update: ## Update all dependencies
	@echo -e "$(CYAN)Updating dependencies...$(NC)"
	poetry update
	@echo -e "$(GREEN)✓ Dependencies updated$(NC)"

.PHONY: lock
lock: ## Generate poetry.lock file
	@echo -e "$(CYAN)Generating lock file...$(NC)"
	poetry lock --no-update
	@echo -e "$(GREEN)✓ Lock file generated$(NC)"

# =============================================================================
# CODE QUALITY - PEP STRICT COMPLIANCE
# =============================================================================

.PHONY: format
format: ## Format code with black and isort
	@echo -e "$(CYAN)Formatting code...$(NC)"
	poetry run black $(SOURCE_DIR) $(TESTS_DIR)
	poetry run isort $(SOURCE_DIR) $(TESTS_DIR)
	@echo -e "$(GREEN)✓ Code formatted$(NC)"

.PHONY: lint
lint: ## Run all linters (ruff, mypy, bandit)
	@echo -e "$(CYAN)Running linters...$(NC)"
	poetry run ruff check $(SOURCE_DIR) $(TESTS_DIR)
	poetry run mypy $(SOURCE_DIR)
	poetry run bandit -r $(SOURCE_DIR)
	@echo -e "$(GREEN)✓ Linting complete$(NC)"

.PHONY: lint-fix
lint-fix: ## Run linters with auto-fix
	@echo -e "$(CYAN)Running linters with auto-fix...$(NC)"
	poetry run ruff check --fix $(SOURCE_DIR) $(TESTS_DIR)
	poetry run black $(SOURCE_DIR) $(TESTS_DIR)
	poetry run isort $(SOURCE_DIR) $(TESTS_DIR)
	@echo -e "$(GREEN)✓ Linting and formatting complete$(NC)"

.PHONY: type-check
type-check: ## Run type checking with mypy
	@echo -e "$(CYAN)Running type checks...$(NC)"
	poetry run mypy $(SOURCE_DIR)
	@echo -e "$(GREEN)✓ Type checking complete$(NC)"

.PHONY: security
security: ## Run security checks
	@echo -e "$(CYAN)Running security checks...$(NC)"
	poetry run bandit -r $(SOURCE_DIR)
	poetry run safety check
	@echo -e "$(GREEN)✓ Security checks complete$(NC)"

# =============================================================================
# TESTING
# =============================================================================

.PHONY: test
test: ## Run all tests with coverage
	@echo -e "$(CYAN)Running tests...$(NC)"
	mkdir -p $(REPORTS_DIR)
	poetry run pytest
	@echo -e "$(GREEN)✓ Tests complete$(NC)"

.PHONY: test-unit
test-unit: ## Run unit tests only
	@echo -e "$(CYAN)Running unit tests...$(NC)"
	poetry run pytest -m "unit" -v
	@echo -e "$(GREEN)✓ Unit tests complete$(NC)"

.PHONY: test-integration
test-integration: ## Run integration tests only
	@echo -e "$(CYAN)Running integration tests...$(NC)"
	poetry run pytest -m "integration" -v
	@echo -e "$(GREEN)✓ Integration tests complete$(NC)"

.PHONY: test-oracle
test-oracle: ## Run Oracle tests only
	@echo -e "$(CYAN)Running Oracle tests...$(NC)"
	poetry run pytest -m "oracle" -v
	@echo -e "$(GREEN)✓ Oracle tests complete$(NC)"

.PHONY: test-oic
test-oic: ## Run OIC tests only
	@echo -e "$(CYAN)Running OIC tests...$(NC)"
	poetry run pytest -m "oic" -v
	@echo -e "$(GREEN)✓ OIC tests complete$(NC)"

.PHONY: test-extensions
test-extensions: ## Run extension tests only
	@echo -e "$(CYAN)Running extension tests...$(NC)"
	poetry run pytest -m "extensions" -v
	@echo -e "$(GREEN)✓ Extension tests complete$(NC)"

.PHONY: test-performance
test-performance: ## Run performance tests only
	@echo -e "$(CYAN)Running performance tests...$(NC)"
	poetry run pytest -m "performance" -v
	@echo -e "$(GREEN)✓ Performance tests complete$(NC)"

.PHONY: test-e2e
test-e2e: ## Run end-to-end tests only
	@echo -e "$(CYAN)Running E2E tests...$(NC)"
	poetry run pytest -m "e2e" -v
	@echo -e "$(GREEN)✓ E2E tests complete$(NC)"

.PHONY: test-watch
test-watch: ## Run tests in watch mode
	@echo -e "$(CYAN)Running tests in watch mode...$(NC)"
	poetry run pytest-watch

.PHONY: coverage
coverage: ## Generate coverage report
	@echo -e "$(CYAN)Generating coverage report...$(NC)"
	mkdir -p $(REPORTS_DIR)
	poetry run pytest --cov=$(SOURCE_DIR) --cov-report=html:$(REPORTS_DIR)/coverage --cov-report=term-missing
	@echo -e "$(GREEN)✓ Coverage report generated: $(REPORTS_DIR)/coverage/index.html$(NC)"

# =============================================================================
# ORACLE OIC OPERATIONS
# =============================================================================

.PHONY: oic-check
oic-check: ## Check Oracle OIC connectivity
	@echo -e "$(CYAN)Checking Oracle OIC connectivity...$(NC)"
	poetry run python -m $(MODULE_NAME).cli check-connectivity
	@echo -e "$(GREEN)✓ OIC connectivity check complete$(NC)"

.PHONY: oic-list-integrations
oic-list-integrations: ## List available OIC integrations
	@echo -e "$(CYAN)Listing Oracle OIC integrations...$(NC)"
	poetry run python -m $(MODULE_NAME).cli list-integrations
	@echo -e "$(GREEN)✓ Integration listing complete$(NC)"

.PHONY: oic-list-connections
oic-list-connections: ## List available OIC connections
	@echo -e "$(CYAN)Listing Oracle OIC connections...$(NC)"
	poetry run python -m $(MODULE_NAME).cli list-connections
	@echo -e "$(GREEN)✓ Connection listing complete$(NC)"

.PHONY: oic-validate
oic-validate: ## Validate OIC configuration
	@echo -e "$(CYAN)Validating OIC configuration...$(NC)"
	poetry run python -m $(MODULE_NAME).cli validate-config
	@echo -e "$(GREEN)✓ OIC configuration validation complete$(NC)"

.PHONY: oic-test-connection
oic-test-connection: ## Test OIC connection
	@echo -e "$(CYAN)Testing OIC connection...$(NC)"
	poetry run python -m $(MODULE_NAME).cli test-connection
	@echo -e "$(GREEN)✓ OIC connection test complete$(NC)"

.PHONY: oic-deploy
oic-deploy: ## Deploy OIC integration
	@echo -e "$(CYAN)Deploying OIC integration...$(NC)"
	poetry run python -m $(MODULE_NAME).cli deploy-integration
	@echo -e "$(GREEN)✓ OIC integration deployment complete$(NC)"

.PHONY: oic-monitor
oic-monitor: ## Monitor OIC integration status
	@echo -e "$(CYAN)Monitoring OIC integration status...$(NC)"
	poetry run python -m $(MODULE_NAME).cli monitor-status
	@echo -e "$(GREEN)✓ OIC monitoring complete$(NC)"

# =============================================================================
# ORACLE DATABASE OPERATIONS
# =============================================================================

.PHONY: oracle-check
oracle-check: ## Check Oracle database connectivity
	@echo -e "$(CYAN)Checking Oracle database connectivity...$(NC)"
	poetry run python -m $(MODULE_NAME).cli check-oracle-db
	@echo -e "$(GREEN)✓ Oracle DB connectivity check complete$(NC)"

.PHONY: oracle-schema
oracle-schema: ## Get Oracle schema information
	@echo -e "$(CYAN)Getting Oracle schema information...$(NC)"
	poetry run python -m $(MODULE_NAME).cli get-schema-info
	@echo -e "$(GREEN)✓ Oracle schema information complete$(NC)"

.PHONY: oracle-tables
oracle-tables: ## List Oracle tables
	@echo -e "$(CYAN)Listing Oracle tables...$(NC)"
	poetry run python -m $(MODULE_NAME).cli list-tables
	@echo -e "$(GREEN)✓ Oracle tables listing complete$(NC)"

.PHONY: oracle-sync
oracle-sync: ## Sync Oracle metadata
	@echo -e "$(CYAN)Syncing Oracle metadata...$(NC)"
	poetry run python -m $(MODULE_NAME).cli sync-metadata
	@echo -e "$(GREEN)✓ Oracle metadata sync complete$(NC)"

# =============================================================================
# MELTANO EDK OPERATIONS
# =============================================================================

.PHONY: meltano-validate
meltano-validate: ## Validate Meltano EDK configuration
	@echo -e "$(CYAN)Validating Meltano EDK configuration...$(NC)"
	poetry run python -m $(MODULE_NAME).cli validate-meltano
	@echo -e "$(GREEN)✓ Meltano EDK validation complete$(NC)"

.PHONY: meltano-test
meltano-test: ## Test Meltano EDK integration
	@echo -e "$(CYAN)Testing Meltano EDK integration...$(NC)"
	poetry run python -m $(MODULE_NAME).cli test-meltano
	@echo -e "$(GREEN)✓ Meltano EDK test complete$(NC)"

.PHONY: meltano-deploy
meltano-deploy: ## Deploy Meltano EDK extension
	@echo -e "$(CYAN)Deploying Meltano EDK extension...$(NC)"
	poetry run python -m $(MODULE_NAME).cli deploy-meltano
	@echo -e "$(GREEN)✓ Meltano EDK deployment complete$(NC)"

# =============================================================================
# BUILD AND DISTRIBUTION
# =============================================================================

.PHONY: build
build: clean ## Build the package
	@echo -e "$(CYAN)Building package...$(NC)"
	poetry build
	@echo -e "$(GREEN)✓ Package built$(NC)"

.PHONY: publish-test
publish-test: build ## Publish to TestPyPI
	@echo -e "$(CYAN)Publishing to TestPyPI...$(NC)"
	poetry publish --repository testpypi
	@echo -e "$(GREEN)✓ Published to TestPyPI$(NC)"

.PHONY: publish
publish: build ## Publish to PyPI
	@echo -e "$(CYAN)Publishing to PyPI...$(NC)"
	poetry publish
	@echo -e "$(GREEN)✓ Published to PyPI$(NC)"

# =============================================================================
# CI/CD PIPELINE COMMANDS
# =============================================================================

.PHONY: ci-check
ci-check: install-dev lint security test oic-check ## Run all CI checks
	@echo -e "$(GREEN)✓ All CI checks passed$(NC)"

.PHONY: pre-commit
pre-commit: ## Run pre-commit hooks
	@echo -e "$(CYAN)Running pre-commit hooks...$(NC)"
	poetry run pre-commit run --all-files
	@echo -e "$(GREEN)✓ Pre-commit hooks complete$(NC)"

# =============================================================================
# CLEANUP
# =============================================================================

.PHONY: clean
clean: ## Clean build artifacts and cache files
	@echo -e "$(CYAN)Cleaning build artifacts...$(NC)"
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf $(REPORTS_DIR)/
	rm -f config.json
	rm -f connection-config.json
	rm -f integration-config.json
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type f -name "coverage.xml" -delete
	@echo -e "$(GREEN)✓ Cleanup complete$(NC)"

# =============================================================================
# QUALITY GATES FOR CI/CD
# =============================================================================

.PHONY: quality-gate
quality-gate: ## Quality gate for CI/CD (strict)
	@echo -e "$(CYAN)Running quality gate...$(NC)"
	$(MAKE) format
	$(MAKE) lint
	$(MAKE) type-check
	$(MAKE) security
	$(MAKE) test
	$(MAKE) oic-validate
	@echo -e "$(GREEN)✓ Quality gate passed$(NC)"

# =============================================================================
# INFORMATION
# =============================================================================

.PHONY: info
info: ## Show project information
	@echo -e "$(CYAN)Project Information$(NC)"
	@echo -e "$(CYAN)==================$(NC)"
	@echo -e "Project: $(PROJECT_NAME)"
	@echo -e "Python Version: $(PYTHON_VERSION)"
	@echo -e "Source Directory: $(SOURCE_DIR)"
	@echo -e "Tests Directory: $(TESTS_DIR)"
	@echo -e "Reports Directory: $(REPORTS_DIR)"
	@echo -e "Module Name: $(MODULE_NAME)"
	@echo ""
	@poetry env info
	@echo ""
	@poetry show --tree
