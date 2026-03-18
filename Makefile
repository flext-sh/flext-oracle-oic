# FLEXT-ORACLE-OIC Makefile
# Migrated to use base.mk - 2026-01-03

PROJECT_NAME := flext-oracle-oic
# Include shared base.mk for standard targets
ifneq ("$(wildcard ../base.mk)", "")
include ../base.mk
else
# =============================================================================
# STANDALONE BOOTSTRAP — auto-generates base.mk via flext-infra
# =============================================================================
# GNU Make auto-rebuild: if base.mk is missing, Make builds this target first,
# then restarts with base.mk loaded. All standard verbs become available.
# =============================================================================

PYTHON_VERSION ?= 3.13
PYTHON_CMD := $(firstword $(shell command -v python$(PYTHON_VERSION) python3 python 2>/dev/null))
BOOTSTRAP_VENV := .venv
BOOTSTRAP_PIP := $(BOOTSTRAP_VENV)/bin/pip
BOOTSTRAP_PYTHON := $(BOOTSTRAP_VENV)/bin/python

-include base.mk

base.mk: Makefile
	@echo "==> Resolving base.mk for $(PROJECT_NAME)..."
	@if [ -d "$(BOOTSTRAP_VENV)" ] && $(BOOTSTRAP_PYTHON) -c 'import flext_infra' 2>/dev/null; then \
		$(BOOTSTRAP_PYTHON) -m flext_infra basemk generate \
			--project-name $(PROJECT_NAME) --output $@; \
	elif $(PYTHON_CMD) -c 'import flext_infra' 2>/dev/null; then \
		$(PYTHON_CMD) -m flext_infra basemk generate \
			--project-name $(PROJECT_NAME) --output $@; \
	else \
		echo "==> flext-infra not found. Bootstrapping standalone environment..."; \
		$(MAKE) _bootstrap-venv; \
		$(BOOTSTRAP_PIP) install -q flext-infra; \
		$(BOOTSTRAP_PYTHON) -m flext_infra basemk generate \
			--project-name $(PROJECT_NAME) --output $@; \
	fi
	@test -s $@ || { echo "ERROR: base.mk generation failed"; rm -f $@; exit 1; }
	@echo "==> base.mk generated. Restarting make..."

.PHONY: _bootstrap-venv venv setup help

_bootstrap-venv:
	@if [ ! -d "$(BOOTSTRAP_VENV)" ]; then \
		echo "==> Creating virtual environment with $(PYTHON_CMD)..."; \
		if [ -z "$(PYTHON_CMD)" ]; then \
			echo "ERROR: Python $(PYTHON_VERSION) not found. Install it first."; \
			exit 1; \
		fi; \
		$(PYTHON_CMD) -m venv $(BOOTSTRAP_VENV); \
		$(BOOTSTRAP_PIP) install -q -U pip; \
	fi

venv: _bootstrap-venv ## Create standalone virtual environment
	@$(BOOTSTRAP_PIP) install -q -U pip poetry
	@echo "Virtual environment ready at $(BOOTSTRAP_VENV)"

setup: venv ## Full standalone setup (venv + dependencies + base.mk)
	@echo "==> Installing project dependencies..."
	@$(BOOTSTRAP_PIP) install -q flext-infra
	@$(BOOTSTRAP_PYTHON) -m flext_infra deps internal-sync \
		--project-root "$(CURDIR)" 2>/dev/null || true
	@$(BOOTSTRAP_VENV)/bin/poetry lock
	@$(BOOTSTRAP_VENV)/bin/poetry install --all-extras --all-groups
	@if git rev-parse --git-dir >/dev/null 2>&1; then \
		$(BOOTSTRAP_VENV)/bin/poetry run pre-commit install 2>/dev/null || true; \
	fi
	@$(BOOTSTRAP_PYTHON) -m flext_infra basemk generate \
		--project-name $(PROJECT_NAME) --output base.mk
	@echo "==> Setup complete. All 'make' verbs now available."

help: ## Show available commands
	@echo "================================================"
	@echo "  $(PROJECT_NAME) (standalone bootstrap)"
	@echo "================================================"
	@echo ""
	@echo "Bootstrap targets (no base.mk required):"
	@printf "  %-14s %s\n" "venv"   "Create virtual environment"
	@printf "  %-14s %s\n" "setup"  "Full standalone setup"
	@printf "  %-14s %s\n" "help"   "Show this help"
	@echo ""
	@echo "After 'make setup', all standard verbs become available:"
	@echo "  check, test, format, build, validate, clean, docs, pr"
	@echo ""
	@echo "Run 'make setup' first, then 'make help' for full verb list."
endif

# =============================================================================
# PROJECT-SPECIFIC CONFIGURATION
# =============================================================================

# OIC configuration
OIC_EXT_BASE_URL ?= https://oic-prod.integration.ocp.oraclecloud.com
OIC_EXT_API_VERSION ?= v1

# =============================================================================
# OIC-SPECIFIC TARGETS
# =============================================================================

.PHONY: oic-test oic-auth oic-patterns oic-deploy test-oic test-patterns

oic-test: ## Test OIC API connectivity
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_oracle_oic import test_oic_connectivity; test_oic_connectivity()"

oic-auth: ## Test OIC OAuth2 authentication
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_oracle_oic import test_oic_auth; test_oic_auth()"

oic-patterns: ## Test integration patterns
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_oracle_oic import test_integration_patterns; test_integration_patterns()"

oic-deploy: ## Test OIC deployment
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_oracle_oic import test_oic_deployment; test_oic_deployment()"

# =============================================================================
# PROJECT-SPECIFIC TEST TARGETS
# =============================================================================

test-oic: ## Run OIC specific tests
	$(POETRY) run pytest $(TESTS_DIR) -m oic -v

test-patterns: ## Run integration patterns tests
	$(POETRY) run pytest $(TESTS_DIR) -m patterns -v
