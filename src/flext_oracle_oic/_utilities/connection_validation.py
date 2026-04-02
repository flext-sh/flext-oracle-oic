"""Oracle OIC connection validation utilities mixin."""

from __future__ import annotations

from flext_core import r
from flext_oracle_oic import c


class FlextOracleOicUtilitiesConnectionValidation:
    """Oracle OIC connection validation utilities."""

    @staticmethod
    def validate_base_url(base_url: str) -> r[str]:
        """Validate Oracle OIC base URL.

        Args:
        base_url: Base URL to validate

        Returns:
        r containing validated URL or error

        """
        match base_url:
            case str():
                pass
            case _:
                return r[str].fail("Base URL must be a string")
        base_url = base_url.strip()
        if not base_url:
            return r[str].fail("Base URL cannot be empty")
        if not base_url.startswith(("http://", "https://")):
            return r[str].fail("Base URL must start with http:// or https://")
        return r[str].ok(base_url)

    @staticmethod
    def validate_connection_status(status: str) -> r[str]:
        """Validate Oracle OIC connection status.

        Args:
        status: Connection status to validate

        Returns:
        r containing validated status or error

        """
        match status:
            case str():
                pass
            case _:
                return r[str].fail("Connection status must be a string")
        status = status.upper().strip()
        if status not in c.OracleOicValidation.VALID_CONNECTION_STATUSES:
            valid_statuses = ", ".join(
                sorted(c.OracleOicValidation.VALID_CONNECTION_STATUSES),
            )
            return r[str].fail(
                f"Invalid connection status. Valid: {valid_statuses}",
            )
        return r[str].ok(status)

    @staticmethod
    def validate_connection_type(connection_type: str) -> r[str]:
        """Validate Oracle OIC connection type.

        Args:
        connection_type: Connection type to validate

        Returns:
        r containing validated type or error

        """
        match connection_type:
            case str():
                pass
            case _:
                return r[str].fail("Connection type must be a string")
        connection_type = connection_type.upper().strip()
        if connection_type not in c.OracleOicValidation.VALID_CONNECTION_TYPES:
            valid_types = ", ".join(
                sorted(c.OracleOicValidation.VALID_CONNECTION_TYPES),
            )
            return r[str].fail(f"Invalid connection type. Valid: {valid_types}")
        return r[str].ok(connection_type)
