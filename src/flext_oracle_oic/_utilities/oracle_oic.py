"""Oracle OIC integration validation utilities mixin.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import MutableSequence

from flext_api import u
from flext_core import r

from flext_oracle_oic import c, m, p, t


class FlextOracleOicUtilitiesOracleOic:
    """Oracle OIC integration validation utilities."""

    @staticmethod
    def validate_integration_data(
        integration_data: t.JsonMapping,
    ) -> p.Result[t.JsonMapping]:
        """Validate complete Oracle OIC integration data.

        Args:
            integration_data: Integration configuration data.

        Returns:
            Result wrapping the validated data.

        """
        errors: MutableSequence[str] = []
        validated_data = u.json_dict_adapter().validate_python(integration_data)
        field_specs: tuple[
            m.OracleOic.FieldValidationPlan,
            ...,
        ] = (
            m.OracleOic.FieldValidationPlan(
                field_name="name",
                label="Name",
                required=True,
                required_message="Integration name is required",
                validator=FlextOracleOicUtilitiesOracleOic.validate_integration_name,
            ),
            m.OracleOic.FieldValidationPlan(
                field_name="version",
                label="Version",
                validator=FlextOracleOicUtilitiesOracleOic.validate_integration_version,
            ),
            m.OracleOic.FieldValidationPlan(
                field_name="status",
                label="Status",
                validator=FlextOracleOicUtilitiesOracleOic.validate_integration_status,
            ),
        )
        for field_plan in field_specs:
            FlextOracleOicUtilitiesOracleOic.validate_string_field(
                integration_data=integration_data,
                validated_data=validated_data,
                errors=errors,
                plan=field_plan,
            )
        if errors:
            return r[t.JsonMapping].fail_op("Integration validation", "; ".join(errors))
        return r[t.JsonMapping].ok(validated_data)

    @staticmethod
    def validate_string_field(
        *,
        integration_data: t.JsonMapping,
        validated_data: t.MutableJsonMapping,
        errors: MutableSequence[str],
        plan: m.OracleOic.FieldValidationPlan,
    ) -> None:
        """Validate one string field and update normalized payload or errors."""
        if plan.field_name not in integration_data:
            if plan.required:
                errors.append(plan.required_message)
            return
        field_value = integration_data[plan.field_name]
        match field_value:
            case str():
                field_result = plan.validator(field_value)
                if field_result.failure:
                    errors.append(f"{plan.label} validation: {field_result.error}")
                else:
                    validated_data[plan.field_name] = field_result.value
            case _:
                errors.append(
                    f"{plan.label} validation: "
                    f"Integration {plan.field_name} must be a string",
                )

    @staticmethod
    def validate_integration_name(name: str) -> p.Result[str]:
        """Validate an Oracle OIC integration name.

        Args:
            name: Integration name to validate.

        Returns:
            Result wrapping the validated name.

        """
        name = name.strip()
        if not name:
            return r[str].fail("Integration name cannot be empty")
        if len(name) < c.OracleOic.OracleOicValidation.MIN_INTEGRATION_NAME_LENGTH:
            return r[str].fail("Integration name too short")
        if len(name) > c.OracleOic.OracleOicValidation.MAX_INTEGRATION_NAME_LENGTH:
            return r[str].fail("Integration name too long")
        if not c.OracleOic.OracleOicValidation.INTEGRATION_NAME_RE.match(name):
            return r[str].fail("Integration name contains invalid characters")
        return r[str].ok(name)

    @staticmethod
    def validate_integration_status(status: str) -> p.Result[str]:
        """Validate an Oracle OIC integration status.

        Args:
            status: Integration status to validate.

        Returns:
            Result wrapping the validated status.

        """
        status = status.upper().strip()
        if status not in c.OracleOic.OracleOicValidation.VALID_INTEGRATION_STATUSES:
            valid_statuses = ", ".join(
                sorted(c.OracleOic.OracleOicValidation.VALID_INTEGRATION_STATUSES),
            )
            return r[str].fail(f"Invalid integration status. Valid: {valid_statuses}")
        return r[str].ok(status)

    @staticmethod
    def validate_integration_version(version: str) -> p.Result[str]:
        """Validate an Oracle OIC integration version format.

        Args:
            version: Version string to validate (format: XX.XX.XXXX).

        Returns:
            Result wrapping the validated version.

        """
        version = version.strip()
        if not c.OracleOic.OracleOicValidation.VERSION_PATTERN.match(version):
            return r[str].fail("Invalid version format. Expected: XX.XX.XXXX")
        return r[str].ok(version)


__all__: list[str] = ["FlextOracleOicUtilitiesOracleOic"]
