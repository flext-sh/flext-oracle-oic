"""Oracle OIC integration validation utilities mixin."""

from __future__ import annotations

import re
from collections.abc import (
    Mapping,
    MutableSequence,
)

from flext_core import p, r

from flext_oracle_oic import c, t


class FlextOracleOicUtilitiesOracleOic:
    """Oracle OIC integration validation utilities."""

    @staticmethod
    def validate_integration_data(
        integration_data: Mapping[str, t.Container],
    ) -> p.Result[Mapping[str, t.Container]]:
        """Validate complete Oracle OIC integration data.

        Args:
        integration_data: Integration configuration data

        Returns:
        r containing validated data or validation errors

        """
        errors: MutableSequence[str] = []
        validated_data: t.MutableFlatContainerMapping = {
            str(key): value for key, value in integration_data.items()
        }
        if "name" not in integration_data:
            errors.append("Integration name is required")
        else:
            raw_name = integration_data["name"]
            match raw_name:
                case str():
                    name_result = (
                        FlextOracleOicUtilitiesOracleOic.validate_integration_name(
                            raw_name,
                        )
                    )
                    if name_result.failure:
                        errors.append(f"Name validation: {name_result.error}")
                    else:
                        validated_data["name"] = name_result.value
                case _:
                    errors.append(
                        "Name validation: Integration name must be a string",
                    )
        if "version" in integration_data:
            raw_version = integration_data["version"]
            match raw_version:
                case str():
                    version_result = (
                        FlextOracleOicUtilitiesOracleOic.validate_integration_version(
                            raw_version,
                        )
                    )
                    if version_result.failure:
                        errors.append(f"Version validation: {version_result.error}")
                    else:
                        validated_data["version"] = version_result.value
                case _:
                    errors.append(
                        "Version validation: Integration version must be a string",
                    )
        if "status" in integration_data:
            raw_status = integration_data["status"]
            match raw_status:
                case str():
                    status_result = (
                        FlextOracleOicUtilitiesOracleOic.validate_integration_status(
                            raw_status,
                        )
                    )
                    if status_result.failure:
                        errors.append(f"Status validation: {status_result.error}")
                    else:
                        validated_data["status"] = status_result.value
                case _:
                    errors.append(
                        "Status validation: Integration status must be a string",
                    )
        if errors:
            return r[Mapping[str, t.Container]].fail(
                f"Integration validation failed: {'; '.join(errors)}",
            )
        return r[Mapping[str, t.Container]].ok(validated_data)

    @staticmethod
    def validate_integration_name(name: str) -> p.Result[str]:
        """Validate Oracle OIC integration name.

        Args:
        name: Integration name to validate

        Returns:
        r containing validated name or validation error

        """
        match name:
            case str():
                pass
            case _:
                return r[str].fail("Integration name must be a string")
        name = name.strip()
        if not name:
            return r[str].fail("Integration name cannot be empty")
        if len(name) < c.OracleOicValidation.MIN_INTEGRATION_NAME_LENGTH:
            return r[str].fail("Integration name too short")
        if len(name) > c.OracleOicValidation.MAX_INTEGRATION_NAME_LENGTH:
            return r[str].fail("Integration name too long")
        if not re.match(r"^[a-zA-Z0-9_\\-\\s]+$", name):
            return r[str].fail("Integration name contains invalid characters")
        return r[str].ok(name)

    @staticmethod
    def validate_integration_status(status: str) -> p.Result[str]:
        """Validate Oracle OIC integration status.

        Args:
        status: Integration status to validate

        Returns:
        r containing validated status or error

        """
        match status:
            case str():
                pass
            case _:
                return r[str].fail("Integration status must be a string")
        status = status.upper().strip()
        if status not in c.OracleOicValidation.VALID_INTEGRATION_STATUSES:
            valid_statuses = ", ".join(
                sorted(c.OracleOicValidation.VALID_INTEGRATION_STATUSES),
            )
            return r[str].fail(
                f"Invalid integration status. Valid: {valid_statuses}",
            )
        return r[str].ok(status)

    @staticmethod
    def validate_integration_version(version: str) -> p.Result[str]:
        """Validate Oracle OIC integration version format.

        Args:
        version: Version string to validate (format: XX.XX.XXXX)

        Returns:
        r containing validated version or error

        """
        match version:
            case str():
                pass
            case _:
                return r[str].fail("Integration version must be a string")
        version = version.strip()
        if not c.OracleOicValidation.VERSION_PATTERN.match(version):
            return r[str].fail("Invalid version format. Expected: XX.XX.XXXX")
        return r[str].ok(version)
