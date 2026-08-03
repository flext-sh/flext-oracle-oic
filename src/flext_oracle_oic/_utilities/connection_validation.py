"""Oracle OIC connection validation utilities mixin."""

from __future__ import annotations

from flext_oracle_oic import c, p, r


class FlextOracleOicUtilitiesConnectionValidation:
    """Oracle OIC connection validation utilities."""

    @staticmethod
    def _validate_closed_string(
        value: p.AttributeProbe, *, field_label: str, valid_values: frozenset[str]
    ) -> p.Result[str]:
        """Validate one upper-cased string against a closed canonical set."""
        match value:
            case str():
                pass
            case _:
                return r[str].fail(f"{field_label} must be a string")
        normalized_value = value.upper().strip()
        if normalized_value not in valid_values:
            formatted_values = ", ".join(sorted(valid_values))
            return r[str].fail(
                f"Invalid {field_label.lower()}. Valid: {formatted_values}"
            )
        return r[str].ok(normalized_value)

    @staticmethod
    def validate_base_url(base_url: p.AttributeProbe) -> p.Result[str]:
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
    def validate_connection_status(status: p.AttributeProbe) -> p.Result[str]:
        """Validate Oracle OIC connection status.

        Args:
        status: Connection status to validate

        Returns:
        r containing validated status or error

        """
        return FlextOracleOicUtilitiesConnectionValidation._validate_closed_string(
            status,
            field_label="Connection status",
            valid_values=c.OracleOicValidation.VALID_CONNECTION_STATUSES,
        )

    @staticmethod
    def validate_connection_type(connection_type: p.AttributeProbe) -> p.Result[str]:
        """Validate Oracle OIC connection type.

        Args:
        connection_type: Connection type to validate

        Returns:
        r containing validated type or error

        """
        return FlextOracleOicUtilitiesConnectionValidation._validate_closed_string(
            connection_type,
            field_label="Connection type",
            valid_values=c.OracleOicValidation.VALID_CONNECTION_TYPES,
        )
