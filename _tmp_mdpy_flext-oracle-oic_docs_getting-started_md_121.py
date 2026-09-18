# from flext-oracle-oic_docs/getting-started.md:121
# Import available components
from flext_oracle_oic import FlextOracleOicSettings

# Basic configuration validation
try:
    settings = FlextOracleOicSettings(
        base_url="https://test.integration.ocp.oraclecloud.com", api_version="v1"
    )
    print("✅ Configuration valid")
except Exception as e:
    print(f"❌ Configuration error: {e}")
