# FLEXT-ORACLE-OIC Makefile
# Migrated to use base.mk - 2026-01-03

PROJECT_NAME := flext-oracle-oic
MIN_COVERAGE := 100

# Include shared base.mk for standard targets
include ../base.mk

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
