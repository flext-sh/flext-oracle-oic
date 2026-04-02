"""Oracle OIC authentication validation utilities mixin."""

from __future__ import annotations

import re

from pydantic import SecretStr

from flext_core import r
from flext_oracle_oic import c


class FlextOracleOicUtilitiesAuthenticationValidation:
    """Oracle OIC authentication validation utilities."""

    @staticmethod
    def validate_oauth_client_id(client_id: str) -> r[str]:
        """Validate OAuth2 client ID.

        Args:
        client_id: OAuth2 client ID to validate

        Returns:
        r containing validated client ID or error

        """
        match client_id:
            case str():
                pass
            case _:
                return r[str].fail("OAuth client ID must be a string")
        client_id = client_id.strip()
        if len(client_id) < c.OracleOicValidation.MIN_CLIENT_ID_LENGTH:
            return r[str].fail("OAuth client ID cannot be empty")
        if not re.match(r"^[a-zA-Z0-9_\\-\\.]+$", client_id):
            return r[str].fail("OAuth client ID contains invalid characters")
        return r[str].ok(client_id)

    @staticmethod
    def validate_oauth_client_secret(client_secret: SecretStr) -> r[SecretStr]:
        """Validate OAuth2 client secret.

        Args:
        client_secret: OAuth2 client secret to validate

        Returns:
        r containing validated secret or error

        """
        secret_value = client_secret.get_secret_value()
        if not secret_value or not secret_value.strip():
            return r[SecretStr].fail("OAuth client secret cannot be empty")
        if len(secret_value) < c.OracleOicValidation.MIN_CLIENT_SECRET_LENGTH:
            return r[SecretStr].fail(
                "OAuth client secret must be at least 8 characters",
            )
        return r[SecretStr].ok(client_secret)
