# from flext-oracle-oic_docs/configuration.md:266
from flext_oracle_oic import FlextOracleOicSettings

# ❌ This will fail - empty base_url is rejected
try:
    settings = FlextOracleOicSettings(base_url="", api_version="v1")
except ValueError as e:
    print(f"Error: {e}")  # field validation error

# ✅ This will work - base_url provided
settings = FlextOracleOicSettings(
    base_url="https://your-instance.integration.ocp.oraclecloud.com"
)
