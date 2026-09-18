# from flext-oracle-oic/docs/configuration.md:49
from flext_oracle_oic import FlextOracleOicSettings

# Basic connection configuration
connection_config = FlextOracleOicSettings(
    base_url="https://your-instance.integration.ocp.oraclecloud.com",
    api_version="v1",
    request_timeout=30,
)
