"""Oracle OIC integration validation utilities mixin."""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated, ClassVar

from flext_auth import m

from flext_oracle_oic import c, p, r, t

if TYPE_CHECKING:
    from collections.abc import (
        Callable,
        MutableSequence,
    )


class FlextOracleOicUtilitiesOracleOic:
    """Oracle OIC integration validation utilities."""

    class FieldValidationPlan(m.Value):
        """Validated plan for one integration string field."""

        model_config: ClassVar[t.ConfigDict] = m.ConfigDict(
            arbitrary_types_allowed=True,
            frozen=True,
        )

        field_name: Annotated[str, m.Field(description="Name of the field to validate")]
        label: Annotated[str, m.Field(description="Human-readable label for the field")]
        required: Annotated[
            bool,
            m.Field(description="Whether the field is required"),
        ] = False
        required_message: Annotated[
            str,
            m.Field(description="Error message when required field is missing"),
        ] = ""
        validator: Annotated[
            Callable[[str], p.Result[str]],
            m.Field(description="Validation function for the field value"),
        ]

    @staticmethod
    def validate_integration_data(
        integration_data: t.JsonMapping,
    ) -> p.Result[t.JsonMapping]:
        """Validate complete Oracle OIC integration data.

        Args:
        integration_data: Integration configuration data

        Returns:
        r containing validated data or validation errors

        """
        errors: MutableSequence[str] = []
        validated_data = t.json_dict_adapter().validate_python(integration_data)
        field_specs: tuple[
            FlextOracleOicUtilitiesOracleOic.FieldValidationPlan,
            ...,
        ] = (
            FlextOracleOicUtilitiesOracleOic.FieldValidationPlan(
                field_name="name",
                label="Name",
                required=True,
                required_message="Integration name is required",
                validator=FlextOracleOicUtilitiesOracleOic.validate_integration_name,
            ),
            FlextOracleOicUtilitiesOracleOic.FieldValidationPlan(
                field_name="version",
                label="Version",
                validator=FlextOracleOicUtilitiesOracleOic.validate_integration_version,
            ),
            FlextOracleOicUtilitiesOracleOic.FieldValidationPlan(
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
        plan: FieldValidationPlan,
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
                    f"{plan.label} validation: Integration {plan.field_name} must be a string",
                )

    @staticmethod
    def validate_integration_name(name: str) -> p.Result[str]:
        """Validate Oracle OIC integration name.

        Args:
        name: Integration name to validate

        Returns:
        r containing validated name or validation error

        """
        name = name.strip()
        if not name:
            return r[str].fail("Integration name cannot be empty")
        if len(name) < c.OracleOicValidation.MIN_INTEGRATION_NAME_LENGTH:
            return r[str].fail("Integration name too short")
        if len(name) > c.OracleOicValidation.MAX_INTEGRATION_NAME_LENGTH:
            return r[str].fail("Integration name too long")
        if not c.OracleOicValidation.INTEGRATION_NAME_RE.match(name):
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
        version = version.strip()
        if not c.OracleOicValidation.VERSION_PATTERN.match(version):
            return r[str].fail("Invalid version format. Expected: XX.XX.XXXX")
        return r[str].ok(version)
