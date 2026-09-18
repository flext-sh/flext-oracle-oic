# from flext-oracle-oic_docs/configuration.md:93
from flext_oracle_oic import FlextOracleOicSettings

# Complete configuration (connection + auth fields are flat on a single model)
settings = FlextOracleOicSettings(
    base_url="https://your-instance.integration.ocp.oraclecloud.com",
    oauth_client_id="your_client_id",
    oauth_client_secret="your_client_secret",
    oauth_token_url="https://your-idcs.identity.oraclecloud.com/oauth2/v1/token",
)
