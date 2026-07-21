# Private project handlers for flext-oracle-oic.
# Strict extension: only `_custom_<verb>_<what>` handlers and `(pre|post)-<verb>[-<what>]`
# hooks. Public targets, toolchain vars, .DEFAULT_GOAL, includes, and help are
# invalid (base.mk owns those). Each handler maps to `make <verb> WHAT=<what>`.
.PHONY: _custom_run_oic-test _custom_run_oic-auth _custom_run_oic-patterns _custom_run_oic-deploy _custom_test_oic _custom_test_patterns
_custom_run_oic-test: ## make run WHAT=oic-test — test OIC API connectivity
	$(Q)PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_oracle_oic import test_oic_connectivity; test_oic_connectivity()"
_custom_run_oic-auth: ## make run WHAT=oic-auth — test OIC OAuth2 auth
	$(Q)PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_oracle_oic import test_oic_auth; test_oic_auth()"
_custom_run_oic-patterns: ## make run WHAT=oic-patterns — test integration patterns
	$(Q)PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_oracle_oic import test_integration_patterns; test_integration_patterns()"
_custom_run_oic-deploy: ## make run WHAT=oic-deploy — test OIC deployment
	$(Q)PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_oracle_oic import test_oic_deployment; test_oic_deployment()"
_custom_test_oic: ## make test WHAT=oic — OIC-specific tests
	$(Q)$(POETRY) run pytest $(TESTS_DIR) -m oic -v
_custom_test_patterns: ## make test WHAT=patterns — integration pattern tests
	$(Q)$(POETRY) run pytest $(TESTS_DIR) -m patterns -v
