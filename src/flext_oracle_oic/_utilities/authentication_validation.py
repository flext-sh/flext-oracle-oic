"""Oracle OIC authentication validation utilities mixin."""

from __future__ import annotations

from flext_oracle_oic import c, p, r, t


class FlextOracleOicUtilitiesAuthenticationValidation:
    """Oracle OIC authentication validation utilities."""

    @staticmethod
    def validate_oauth_client_id(client_id: str) -> p.Result[str]:
        """Validate OAuth2 client ID.

        Args:
        client_id: OAuth2 client ID to validate

        Returns:
        r containing validated client ID or error

        """
        client_id = client_id.strip()
        if len(client_id) < c.OracleOicValidation.MIN_CLIENT_ID_LENGTH:
            return r[str].fail("OAuth client ID cannot be empty")
        if not c.OracleOicValidation.CLIENT_ID_RE.match(client_id):
            return r[str].fail("OAuth client ID contains invalid characters")
        return r[str].ok(client_id)

    @staticmethod
    def validate_oauth_client_secret(
        client_secret: t.SecretStr,
    ) -> p.Result[t.SecretStr]:
        """Validate OAuth2 client secret.

        Args:
        client_secret: OAuth2 client secret to validate

        Returns:
        r containing validated secret or error

        """
        secret_value = client_secret.get_secret_value()
        if not secret_value or not secret_value.strip():
            return r[t.SecretStr].fail("OAuth client secret cannot be empty")
        if len(secret_value) < c.OracleOicValidation.MIN_CLIENT_SECRET_LENGTH:
            return r[t.SecretStr].fail(
                "OAuth client secret must be at least 8 characters",
            )
        return r[t.SecretStr].ok(client_secret)
