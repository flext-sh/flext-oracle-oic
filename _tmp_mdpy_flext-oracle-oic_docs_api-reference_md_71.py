# from flext-oracle-oic_docs/api-reference.md:71
from flext_oracle_oic import FlextOracleOicSettings

# Basic connection configuration
settings = FlextOracleOicSettings(
    base_url="https://your-instance.integration.ocp.oraclecloud.com",
    api_version="v1",
    request_timeout=30,
)
