# from flext-oracle-oic_docs/api-reference.md:93
from flext_oracle_oic import FlextOracleOicSettings

# OAuth2 authentication setup
auth_config = FlextOracleOicSettings(
    base_url="https://your-instance.integration.ocp.oraclecloud.com",
    oauth_client_id="your_client_id",
    oauth_client_secret="your_client_secret",
    oauth_token_url="https://your-idcs.identity.oraclecloud.com/oauth2/v1/token",
)
