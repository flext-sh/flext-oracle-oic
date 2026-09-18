# from flext-oracle-oic_docs/configuration.md:132
import os
from flext_oracle_oic import FlextOracleOicSettings

# Manual environment variable loading (current approach)
settings = FlextOracleOicSettings(
    base_url=os.getenv(
        "ORACLE_OIC_BASE_URL", "https://your-instance.integration.ocp.oraclecloud.com"
    ),
    api_version=os.getenv("ORACLE_OIC_API_VERSION", "v1"),
    request_timeout=int(os.getenv("ORACLE_OIC_REQUEST_TIMEOUT", "30")),
    oauth_client_id=os.getenv("ORACLE_OIC_OAUTH_CLIENT_ID", "your_client_id"),
    oauth_client_secret=os.getenv(
        "ORACLE_OIC_OAUTH_CLIENT_SECRET", "your_client_secret"
    ),
    oauth_token_url=os.getenv(
        "ORACLE_OIC_OAUTH_TOKEN_URL",
        "https://your-idcs.identity.oraclecloud.com/oauth2/v1/token",
    ),
)
