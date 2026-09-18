# from flext-oracle-oic/docs/configuration.md:235
from __future__ import annotations

import os
from flext_oracle_oic import FlextOracleOicSettings


# Development configuration with environment variables
def create_dev_config():
    return FlextOracleOicSettings(
        base_url=os.getenv("DEV_ORACLE_OIC_BASE_URL", "https://dev-instance.com"),
        api_version="v1",
        request_timeout=60,  # Longer timeout for development
        oauth_client_id=os.getenv("DEV_OIC_CLIENT_ID", "dev_client_id"),
        oauth_client_secret=os.getenv("DEV_OIC_CLIENT_SECRET", "dev_client_secret"),
        oauth_token_url=os.getenv(
            "DEV_OIC_TOKEN_URL", "https://dev-idcs.example.com/oauth2/v1/token"
        ),
    )


# Create development configuration
dev_settings = create_dev_config()
