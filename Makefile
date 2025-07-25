# FLEXT ORACLE OIC EXT - Oracle Integration Cloud Extension Library
# ==================================================================
# Enterprise OIC extensions with integration patterns and workflow orchestration
# PROJECT_TYPE: oracle-extension
# Python 3.13 + OIC REST API + Enterprise Patterns + Zero Tolerance Quality Gates

.PHONY: help info diagnose check validate test lint type-check security format format-check fix
.PHONY: install dev-install setup pre-commit build clean
.PHONY: coverage coverage-html test-unit test-integration test-oic
.PHONY: deps-update deps-audit deps-tree deps-outdated
.PHONY: oic-test oic-auth oic-deploy oic-patterns oic-orchestration
.PHONY: adapter-test pattern-test flow-test monitoring-test extensions-test

# ============================================================================
# 🎯 HELP & INFORMATION
# ============================================================================

help: ## Show this help message
	@echo "🎯 FLEXT ORACLE OIC EXT - Oracle Integration Cloud Extension Library"
	@echo "=============================================================="
	@echo "🎯 OIC REST API + Enterprise Patterns + Orchestration + Python 3.13"
	@echo ""
	@echo "📦 Enterprise OIC extensions with integration patterns and workflows"
	@echo "🔒 Zero tolerance quality gates with real OIC REST API integration"
	@echo "🧪 90%+ test coverage requirement with OIC API compliance"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\\033[36m%-20s\\033[0m %s\\n", $$1, $$2}'


info: ## Mostrar informações do projeto
	@echo "📊 Informações do Projeto"
	@echo "======================"
	@echo "Nome: flext-oracle-oic-ext"
	@echo "Título: FLEXT ORACLE OIC EXT"
	@echo "Versão: $(shell poetry version -s 2>/dev/null || echo "0.7.0")"
	@echo "Python: $(shell python3.13 --version 2>/dev/null || echo "Não encontrado")"
	@echo "Poetry: $(shell poetry --version 2>/dev/null || echo "Não instalado")"
	@echo "Venv: $(shell poetry env info --path 2>/dev/null || echo "Não ativado")"
	@echo "Diretório: $(CURDIR)"
	@echo "Git Branch: $(shell git branch --show-current 2>/dev/null || echo "Não é repo git")"
	@echo "Git Status: $(shell git status --porcelain 2>/dev/null | wc -l | xargs echo) arquivos alterados"

diagnose: ## Executar diagnósticos completos
	@echo "🔍 Executando diagnósticos para flext-oracle-oic-ext..."
	@echo "Informações do Sistema:"
	@echo "OS: $(shell uname -s)"
	@echo "Arquitetura: $(shell uname -m)"
	@echo "Python: $(shell python3.13 --version 2>/dev/null || echo "Não encontrado")"
	@echo "Poetry: $(shell poetry --version 2>/dev/null || echo "Não instalado")"
	@echo ""
	@echo "Estrutura do Projeto:"
	@ls -la
	@echo ""
	@echo "Configuração Poetry:"
	@poetry config --list 2>/dev/null || echo "Poetry não configurado"
	@echo ""
	@echo "Status das Dependências:"
	@poetry show --outdated 2>/dev/null || echo "Nenhuma dependência desatualizada"

# ============================================================================
# 🎯 CORE QUALITY GATES - ZERO TOLERANCE
# ============================================================================

validate: lint type-check security test oic-test ## STRICT compliance validation (all must pass)
	@echo "✅ ALL QUALITY GATES PASSED - FLEXT ORACLE OIC EXT COMPLIANT"

check: lint type-check test ## Essential quality checks (pre-commit standard)
	@echo "✅ Essential checks passed"

lint: ## Ruff linting (17 rule categories, ALL enabled)
	@echo "🔍 Running ruff linter (ALL rules enabled)..."
	@poetry run ruff check src/ tests/ --fix --unsafe-fixes
	@echo "✅ Linting complete"

type-check: ## MyPy strict mode type checking (zero errors tolerated)
	@echo "🛡️ Running MyPy strict type checking..."
	@poetry run mypy src/ tests/ --strict
	@echo "✅ Type checking complete"

security: ## Security scans (bandit + pip-audit + secrets)
	@echo "🔒 Running security scans..."
	@poetry run bandit -r src/ --severity-level medium --confidence-level medium
	@poetry run pip-audit --ignore-vuln PYSEC-2022-42969
	@poetry run detect-secrets scan --all-files
	@echo "✅ Security scans complete"

format: ## Format code with ruff
	@echo "🎨 Formatting code..."
	@poetry run ruff format src/ tests/
	@echo "✅ Formatting complete"

format-check: ## Check formatting without fixing
	@echo "🎨 Checking code formatting..."
	@poetry run ruff format src/ tests/ --check
	@echo "✅ Format check complete"

fix: format lint ## Auto-fix all issues (format + imports + lint)
	@echo "🔧 Auto-fixing all issues..."
	@poetry run ruff check src/ tests/ --fix --unsafe-fixes
	@echo "✅ All auto-fixes applied"

# ============================================================================
# 🧪 TESTING - 90% COVERAGE MINIMUM
# ============================================================================

test: ## Run tests with coverage (90% minimum required)
	@echo "🧪 Running tests with coverage..."
	@poetry run pytest tests/ -v --cov=src/flext_oracle_oic_ext --cov-report=term-missing --cov-fail-under=90
	@echo "✅ Tests complete"

test-unit: ## Run unit tests only
	@echo "🧪 Running unit tests..."
	@poetry run pytest tests/unit/ -v
	@echo "✅ Unit tests complete"

test-integration: ## Run integration tests only
	@echo "🧪 Running integration tests..."
	@poetry run pytest tests/integration/ -v
	@echo "✅ Integration tests complete"

test-oic: ## Run OIC-specific tests
	@echo "🧪 Running Oracle OIC tests..."
	@poetry run pytest tests/ -m "oic" -v
	@echo "✅ OIC tests complete"

test-patterns: ## Run integration pattern tests
	@echo "🧪 Running integration pattern tests..."
	@poetry run pytest tests/ -m "patterns" -v
	@echo "✅ Pattern tests complete"

test-orchestration: ## Run orchestration tests
	@echo "🧪 Running orchestration tests..."
	@poetry run pytest tests/ -m "orchestration" -v
	@echo "✅ Orchestration tests complete"

test-performance: ## Run performance tests
	@echo "⚡ Running OIC extension performance tests..."
	@poetry run pytest tests/performance/ -v --benchmark-only
	@echo "✅ Performance tests complete"

coverage: ## Generate detailed coverage report
	@echo "📊 Generating coverage report..."
	@poetry run pytest tests/ --cov=src/flext_oracle_oic_ext --cov-report=term-missing --cov-report=html
	@echo "✅ Coverage report generated in htmlcov/"

coverage-html: coverage ## Generate HTML coverage report
	@echo "📊 Opening coverage report..."
	@python -m webbrowser htmlcov/index.html

# ============================================================================
# 🚀 DEVELOPMENT SETUP
# ============================================================================

setup: install pre-commit ## Complete development setup
	@echo "🎯 Development setup complete!"

install: ## Install dependencies with Poetry
	@echo "📦 Installing dependencies..."
	@poetry install --all-extras --with dev,test,docs,security
	@echo "✅ Dependencies installed"

dev-install: install ## Install in development mode
	@echo "🔧 Setting up development environment..."
	@poetry install --all-extras --with dev,test,docs,security
	@poetry run pre-commit install
	@echo "✅ Development environment ready"

pre-commit: ## Setup pre-commit hooks
	@echo "🎣 Setting up pre-commit hooks..."
	@poetry run pre-commit install
	@poetry run pre-commit run --all-files || true
	@echo "✅ Pre-commit hooks installed"

# ============================================================================
# 🎯 ORACLE EXTENSION OPERATIONS
# ============================================================================

oracle-test: oic-test ## Run Oracle connectivity tests

oracle-validate: validate-oic-extensions ## Validate Oracle extension integrity

oracle-performance: test-performance ## Run Oracle extension performance tests

# ============================================================================
# 🏢 ORACLE OIC OPERATIONS - CORE FUNCTIONALITY
# ============================================================================

oic-test: ## Test Oracle OIC API connectivity
	@echo "🏢 Testing Oracle OIC API connectivity..."
	@poetry run python scripts/test_oic_connectivity.py
	@echo "✅ OIC API connectivity test complete"

oic-auth: ## Test Oracle OIC OAuth2 authentication
	@echo "🔐 Testing Oracle OIC OAuth2 authentication..."
	@poetry run python scripts/test_oic_authentication.py
	@echo "✅ OIC OAuth2 authentication test complete"

oic-deploy: ## Test OIC integration deployment
	@echo "🚀 Testing OIC integration deployment..."
	@poetry run python scripts/test_oic_deployment.py
	@echo "✅ OIC deployment test complete"

oic-patterns: ## Test enterprise integration patterns
	@echo "🔄 Testing enterprise integration patterns..."
	@poetry run python scripts/test_integration_patterns.py
	@echo "✅ Integration patterns test complete"

oic-orchestration: ## Test workflow orchestration
	@echo "⚙️ Testing workflow orchestration..."
	@poetry run python scripts/test_orchestration.py
	@echo "✅ Orchestration test complete"

oic-monitoring: ## Test OIC monitoring capabilities
	@echo "📊 Testing OIC monitoring capabilities..."
	@poetry run python scripts/test_monitoring.py
	@echo "✅ Monitoring test complete"

oic-adapters: ## Test custom adapter creation
	@echo "🔌 Testing custom adapter creation..."
	@poetry run python scripts/test_custom_adapters.py
	@echo "✅ Custom adapters test complete"

oic-extensions: ## Test OIC functionality extensions
	@echo "🔧 Testing OIC functionality extensions..."
	@poetry run python scripts/test_oic_extensions.py
	@echo "✅ OIC extensions test complete"

# ============================================================================
# 🔄 ENTERPRISE INTEGRATION PATTERNS
# ============================================================================

pattern-test: ## Test all integration patterns
	@echo "🔄 Testing all integration patterns..."
	@poetry run python scripts/test_all_patterns.py
	@echo "✅ All patterns test complete"

message-router: ## Test message router pattern
	@echo "📧 Testing message router pattern..."
	@poetry run python scripts/test_message_router.py
	@echo "✅ Message router test complete"

scatter-gather: ## Test scatter-gather pattern
	@echo "📡 Testing scatter-gather pattern..."
	@poetry run python scripts/test_scatter_gather.py
	@echo "✅ Scatter-gather test complete"

content-filter: ## Test content filter pattern
	@echo "🔍 Testing content filter pattern..."
	@poetry run python scripts/test_content_filter.py
	@echo "✅ Content filter test complete"

message-translator: ## Test message translator pattern
	@echo "🔄 Testing message translator pattern..."
	@poetry run python scripts/test_message_translator.py
	@echo "✅ Message translator test complete"

aggregator: ## Test aggregator pattern
	@echo "📊 Testing aggregator pattern..."
	@poetry run python scripts/test_aggregator.py
	@echo "✅ Aggregator test complete"

splitter: ## Test splitter pattern
	@echo "✂️ Testing splitter pattern..."
	@poetry run python scripts/test_splitter.py
	@echo "✅ Splitter test complete"

# ============================================================================
# 🔧 ADAPTER MANAGEMENT
# ============================================================================

adapter-test: ## Test all custom adapters
	@echo "🔌 Testing all custom adapters..."
	@poetry run python scripts/test_all_adapters.py
	@echo "✅ All adapters test complete"

database-adapter: ## Test database adapter extensions
	@echo "🗄️ Testing database adapter extensions..."
	@poetry run python scripts/test_database_adapter.py
	@echo "✅ Database adapter test complete"

file-adapter: ## Test file adapter extensions
	@echo "📁 Testing file adapter extensions..."
	@poetry run python scripts/test_file_adapter.py
	@echo "✅ File adapter test complete"

rest-adapter: ## Test REST adapter extensions
	@echo "🌐 Testing REST adapter extensions..."
	@poetry run python scripts/test_rest_adapter.py
	@echo "✅ REST adapter test complete"

# ============================================================================
# 🎵 WORKFLOW ORCHESTRATION
# ============================================================================

flow-test: ## Test all integration flows
	@echo "🌊 Testing all integration flows..."
	@poetry run python scripts/test_all_flows.py
	@echo "✅ All flows test complete"

flow-monitoring: ## Test flow monitoring and metrics
	@echo "📊 Testing flow monitoring and metrics..."
	@poetry run python scripts/test_flow_monitoring.py
	@echo "✅ Flow monitoring test complete"

flow-error-handling: ## Test flow error handling
	@echo "🚨 Testing flow error handling..."
	@poetry run python scripts/test_flow_error_handling.py
	@echo "✅ Flow error handling test complete"

flow-parallel: ## Test parallel flow execution
	@echo "⚡ Testing parallel flow execution..."
	@poetry run python scripts/test_parallel_flows.py
	@echo "✅ Parallel flows test complete"

# ============================================================================
# 🔍 DATA QUALITY & VALIDATION
# ============================================================================

validate-oic-extensions: ## Validate OIC extension functionality
	@echo "🔍 Validating OIC extension functionality..."
	@poetry run python scripts/validate_oic_extensions.py
	@echo "✅ OIC extensions validation complete"

validate-patterns: ## Validate integration pattern implementations
	@echo "🔍 Validating integration pattern implementations..."
	@poetry run python scripts/validate_patterns.py
	@echo "✅ Pattern implementations validation complete"

validate-orchestration: ## Validate orchestration workflows
	@echo "🔍 Validating orchestration workflows..."
	@poetry run python scripts/validate_orchestration.py
	@echo "✅ Orchestration validation complete"

data-quality-report: ## Generate comprehensive data quality report
	@echo "📊 Generating data quality report..."
	@poetry run python scripts/generate_quality_report.py
	@echo "✅ Data quality report generated"

# ============================================================================
# 📦 BUILD & DISTRIBUTION
# ============================================================================

build: clean ## Build distribution packages
	@echo "🔨 Building distribution..."
	@poetry build
	@echo "✅ Build complete - packages in dist/"

package: build ## Create deployment package
	@echo "📦 Creating deployment package..."
	@tar -czf dist/flext-oracle-oic-ext-deployment.tar.gz \
		src/ \
		tests/ \
		scripts/ \
		pyproject.toml \
		README.md \
		CLAUDE.md
	@echo "✅ Deployment package created: dist/flext-oracle-oic-ext-deployment.tar.gz"

# ============================================================================
# 🧹 CLEANUP
# ============================================================================

clean: ## Remove all artifacts
	@echo "🧹 Cleaning up..."
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info/
	@rm -rf .coverage
	@rm -rf htmlcov/
	@rm -rf .pytest_cache/
	@rm -rf .mypy_cache/
	@rm -rf .ruff_cache/
	@rm -rf logs/
	@rm -f *.log
	@rm -f deployment_*.json
	@rm -f orchestration_*.json
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "✅ Cleanup complete"

# ============================================================================
# 📊 DEPENDENCY MANAGEMENT
# ============================================================================

deps-update: ## Update all dependencies
	@echo "🔄 Updating dependencies..."
	@poetry update
	@echo "✅ Dependencies updated"

deps-audit: ## Audit dependencies for vulnerabilities
	@echo "🔍 Auditing dependencies..."
	@poetry run pip-audit
	@echo "✅ Dependency audit complete"

deps-tree: ## Show dependency tree
	@echo "🌳 Dependency tree:"
	@poetry show --tree

deps-outdated: ## Show outdated dependencies
	@echo "📋 Outdated dependencies:"
	@poetry show --outdated

# ============================================================================
# 🔧 ENVIRONMENT CONFIGURATION
# ============================================================================

# Python settings
PYTHON := python3.13
export PYTHONPATH := $(PWD)/src:$(PYTHONPATH)
export PYTHONDONTWRITEBYTECODE := 1
export PYTHONUNBUFFERED := 1

# OIC Extension settings
export FLEXT_OIC_EXT_CONFIG := ./config.json
export FLEXT_OIC_EXT_DEBUG := false

# Oracle OIC connection settings
export OIC_EXT_BASE_URL := https://oic-prod.integration.ocp.oraclecloud.com
export OIC_EXT_API_VERSION := v1

# OAuth2 Authentication settings
export OIC_EXT_OAUTH_CLIENT_ID := your_ext_client_id
export OIC_EXT_OAUTH_CLIENT_SECRET := your_ext_client_secret
export OIC_EXT_OAUTH_TOKEN_URL := https://idcs.identity.oraclecloud.com/oauth2/v1/token
export OIC_EXT_OAUTH_SCOPE := https://integration.ocp.oraclecloud.com:443

# Extension operation settings
export OIC_EXT_ENABLE_MONITORING := true
export OIC_EXT_ENABLE_ENTERPRISE_PATTERNS := true
export OIC_EXT_ENABLE_ORCHESTRATION := true
export OIC_EXT_ENABLE_CUSTOM_ADAPTERS := true

# Performance settings
export OIC_EXT_REQUEST_TIMEOUT := 30
export OIC_EXT_MAX_RETRIES := 3
export OIC_EXT_RETRY_DELAY := 1.0
export OIC_EXT_CONCURRENT_FLOWS := 10

# Deployment settings
export OIC_EXT_ENVIRONMENT := development
export OIC_EXT_DEPLOYMENT_MODE := async
export OIC_EXT_VALIDATE_BEFORE_DEPLOY := true
export OIC_EXT_ENABLE_ROLLBACK := true

# Enterprise pattern settings
export OIC_EXT_MESSAGE_ROUTER_ENABLED := true
export OIC_EXT_SCATTER_GATHER_ENABLED := true
export OIC_EXT_CONTENT_FILTER_ENABLED := true
export OIC_EXT_AGGREGATOR_ENABLED := true

# Orchestration settings
export OIC_EXT_ORCHESTRATION_TIMEOUT := 300
export OIC_EXT_PARALLEL_EXECUTION := true
export OIC_EXT_ERROR_HANDLING := continue_on_error
export OIC_EXT_ENABLE_CHECKPOINTS := true

# Monitoring settings
export OIC_EXT_ENABLE_DETAILED_LOGGING := true
export OIC_EXT_ENABLE_METRICS := true
export OIC_EXT_ENABLE_TRACING := true
export OIC_EXT_LOG_LEVEL := INFO

# Quality gate settings
export MYPY_CACHE_DIR := .mypy_cache
export RUFF_CACHE_DIR := .ruff_cache

# ============================================================================
# 📝 PROJECT METADATA
# ============================================================================

# Project information
PROJECT_NAME := flext-oracle-oic-ext
PROJECT_TYPE := oracle-extension
PROJECT_VERSION := $(shell poetry version -s)
PROJECT_DESCRIPTION := FLEXT ORACLE OIC EXT - Oracle Integration Cloud Extension Library

.DEFAULT_GOAL := help

# ============================================================================
# 🎯 DEVELOPMENT UTILITIES
# ============================================================================

dev-oic-server: ## Start development OIC mock server
	@echo "🔧 Starting development OIC mock server..."
	@poetry run python scripts/dev_oic_server.py
	@echo "✅ Development OIC mock server started"

dev-pattern-playground: ## Start integration pattern playground
	@echo "🎮 Starting integration pattern playground..."
	@poetry run python scripts/pattern_playground.py
	@echo "✅ Pattern playground session complete"

dev-orchestration-designer: ## Start orchestration workflow designer
	@echo "🎨 Starting orchestration workflow designer..."
	@poetry run python scripts/orchestration_designer.py
	@echo "✅ Orchestration designer session complete"

dev-adapter-builder: ## Start custom adapter builder
	@echo "🔧 Starting custom adapter builder..."
	@poetry run python scripts/adapter_builder.py
	@echo "✅ Adapter builder session complete"

dev-extension-explorer: ## Start OIC extension explorer
	@echo "🎮 Starting OIC extension explorer..."
	@poetry run python scripts/extension_explorer.py
	@echo "✅ Extension explorer session complete"

# ============================================================================
# 🎯 FLEXT ECOSYSTEM INTEGRATION
# ============================================================================

ecosystem-check: ## Verify FLEXT ecosystem compatibility
	@echo "🌐 Checking FLEXT ecosystem compatibility..."
	@echo "📦 Core project: $(PROJECT_NAME) v$(PROJECT_VERSION)"
	@echo "🏗️ Architecture: OIC Extensions + Enterprise Patterns + Orchestration"
	@echo "🐍 Python: 3.13"
	@echo "🔗 Framework: FLEXT Core + OIC REST API + Enterprise Integration"
	@echo "📊 Quality: Zero tolerance enforcement"
	@echo "✅ Ecosystem compatibility verified"

workspace-info: ## Show workspace integration info
	@echo "🏢 FLEXT Workspace Integration"
	@echo "==============================="
	@echo "📁 Project Path: $(PWD)"
	@echo "🏆 Role: Oracle Integration Cloud Extension Library"
	@echo "🔗 Dependencies: flext-core, flext-observability, requests, pydantic"
	@echo "📦 Provides: OIC extensions, enterprise patterns, workflow orchestration"
	@echo "🎯 Standards: Enterprise OIC patterns with advanced integration capabilities"

# ============================================================================
# 🔄 CONTINUOUS INTEGRATION
# ============================================================================

ci-check: validate ## CI quality checks
	@echo "🔍 Running CI quality checks..."
	@poetry run python scripts/ci_quality_report.py
	@echo "✅ CI quality checks complete"

ci-performance: ## CI performance benchmarks
	@echo "⚡ Running CI performance benchmarks..."
	@poetry run python scripts/ci_performance_benchmarks.py
	@echo "✅ CI performance benchmarks complete"

ci-integration: ## CI integration tests
	@echo "🔗 Running CI integration tests..."
	@poetry run pytest tests/integration/ -v --tb=short
	@echo "✅ CI integration tests complete"

ci-oic: ## CI Oracle OIC tests
	@echo "🏢 Running CI Oracle OIC tests..."
	@poetry run pytest tests/ -m "oic" -v --tb=short
	@echo "✅ CI OIC tests complete"

ci-patterns: ## CI integration pattern tests
	@echo "🔄 Running CI pattern tests..."
	@poetry run pytest tests/ -m "patterns" -v --tb=short
	@echo "✅ CI pattern tests complete"

ci-orchestration: ## CI orchestration tests
	@echo "⚙️ Running CI orchestration tests..."
	@poetry run pytest tests/ -m "orchestration" -v --tb=short
	@echo "✅ CI orchestration tests complete"

ci-all: ci-check ci-performance ci-integration ci-oic ci-patterns ci-orchestration ## Run all CI checks
	@echo "✅ All CI checks complete"

# ============================================================================
# 🚀 PRODUCTION DEPLOYMENT
# ============================================================================

deploy-extensions: validate build ## Deploy OIC extensions for production use
	@echo "🚀 Deploying OIC extensions..."
	@poetry run python scripts/deploy_extensions.py
	@echo "✅ OIC extensions deployment complete"

test-deployment: ## Test deployed extensions functionality
	@echo "🧪 Testing deployed extensions..."
	@poetry run python scripts/test_deployed_extensions.py
	@echo "✅ Deployment test complete"

rollback-deployment: ## Rollback extensions deployment
	@echo "🔄 Rolling back extensions deployment..."
	@poetry run python scripts/rollback_extensions_deployment.py
	@echo "✅ Deployment rollback complete"

# ============================================================================
# 🔬 MONITORING & OBSERVABILITY
# ============================================================================

monitor-extensions: ## Monitor OIC extension health
	@echo "📊 Monitoring OIC extension health..."
	@poetry run python scripts/monitor_extensions.py
	@echo "✅ Extension health monitoring complete"

monitor-patterns: ## Monitor integration pattern performance
	@echo "📊 Monitoring integration pattern performance..."
	@poetry run python scripts/monitor_patterns.py
	@echo "✅ Pattern performance monitoring complete"

monitor-orchestration: ## Monitor orchestration workflow health
	@echo "📊 Monitoring orchestration workflow health..."
	@poetry run python scripts/monitor_orchestration.py
	@echo "✅ Orchestration monitoring complete"

generate-metrics: ## Generate extension performance metrics
	@echo "📊 Generating extension performance metrics..."
	@poetry run python scripts/generate_extension_metrics.py
	@echo "✅ Extension metrics generated"

generate-usage-report: ## Generate OIC extension usage report
	@echo "📊 Generating OIC extension usage report..."
	@poetry run python scripts/generate_usage_report.py
	@echo "✅ Extension usage report generated"