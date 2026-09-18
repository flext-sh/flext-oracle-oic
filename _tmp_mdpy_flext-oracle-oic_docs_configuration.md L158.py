# from flext-oracle-oic/docs/configuration.md:158
from flext_oracle_oic import FlextOracleOicSettings

try:
    # Invalid configuration - empty base_url is rejected
    connection_config = FlextOracleOicSettings(base_url="")
except ValueError as e:
    print(f"Configuration validation error: {e}")

try:
    # Valid configuration
    connection_config = FlextOracleOicSettings(
        base_url="https://valid-oic-instance.integration.ocp.oraclecloud.com"
    )
    print("✅ Configuration valid")
except ValueError as e:
    print(f"❌ Configuration error: {e}")
