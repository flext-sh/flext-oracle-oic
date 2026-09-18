# from flext-oracle-oic_docs/api-reference.md:252
# Safe to use for configuration and basic setup
from flext_oracle_oic import FlextOracleOicSettings

# Configuration validation and type safety works correctly
try:
    settings = FlextOracleOicSettings(
        base_url="https://test-instance.integration.ocp.oraclecloud.com"
    )
    print("✅ Configuration valid")
except ValueError as e:
    print(f"❌ Configuration error: {e}")
