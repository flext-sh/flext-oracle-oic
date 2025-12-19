# flext-oracle-oic - Oracle OIC Integration
PROJECT_NAME := flext-oracle-oic
COV_DIR := flext_oracle_oic
MIN_COVERAGE := 90

include ../base.mk

# === PROJECT-SPECIFIC TARGETS ===
.PHONY: test-unit test-integration build shell

.DEFAULT_GOAL := help
