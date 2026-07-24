"""flext-oracle-oic config models — typed business-rule shapes.

Frozen Pydantic shapes for the ``config/oracle_oic.yaml`` business-rule SSOT.
The ``_config.py`` facade validates the model-less YAML slice into these
classes and exposes the ready objects under ``config.OracleOic``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class FlextOracleOicConfigModels:
    """Namespace of typed flext-oracle-oic config models."""

    class Api(BaseModel):
        """Oracle OIC API defaults and connection policy."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        base_url: str = Field(description="Default Oracle Integration Cloud base URL.")
        api_version: str = Field(description="Default OIC REST API version.")
        request_timeout: int = Field(
            ge=1, description="Default request timeout in seconds."
        )
        max_retries: int = Field(
            ge=0, description="Maximum retry attempts for idempotent requests."
        )
        page_size: int = Field(
            ge=1, description="Default page size for paginated list endpoints."
        )
        verify_ssl: bool = Field(
            description="Whether to verify TLS certificates by default."
        )
        http_error_status_threshold: int = Field(
            ge=100,
            le=599,
            description="HTTP status codes at or above this value are treated as errors.",
        )

    class Integration(BaseModel):
        """Oracle OIC integration defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        default_version: str = Field(description="Default integration version string.")

    class Validation(BaseModel):
        """Oracle OIC validation rule defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        class IntegrationName(BaseModel):
            """Integration name validation thresholds."""

            model_config = ConfigDict(frozen=True, extra="forbid")

            min_length: int = Field(
                ge=1, description="Minimum integration name length."
            )
            max_length: int = Field(
                ge=1, description="Maximum integration name length."
            )
            pattern: str = Field(description="Regex validating an integration name.")

        class Version(BaseModel):
            """Integration version validation rules."""

            model_config = ConfigDict(frozen=True, extra="forbid")

            pattern: str = Field(description="Regex validating an integration version.")

        class Performance(BaseModel):
            """Monitoring performance thresholds."""

            model_config = ConfigDict(frozen=True, extra="forbid")

            response_time_ms: float = Field(
                ge=0, description="Maximum acceptable response time in milliseconds."
            )
            success_rate: float = Field(
                ge=0, le=1, description="Minimum acceptable success rate."
            )
            error_rate: float = Field(
                ge=0, le=1, description="Maximum acceptable error rate."
            )

        integration_name: FlextOracleOicConfigModels.Validation.IntegrationName = Field(
            description="Integration name validation thresholds."
        )
        version: FlextOracleOicConfigModels.Validation.Version = Field(
            description="Integration version validation rules."
        )
        performance: FlextOracleOicConfigModels.Validation.Performance = Field(
            description="Monitoring performance thresholds."
        )

    class Monitoring(BaseModel):
        """Oracle OIC monitoring component defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        component_database: str = Field(
            description="Display name for the database component."
        )
        component_messaging: str = Field(
            description="Display name for the messaging component."
        )
        component_integration_engine: str = Field(
            description="Display name for the integration engine component."
        )

    class OracleOic(BaseModel):
        """Root Oracle OIC business-rule namespace."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        api: FlextOracleOicConfigModels.Api = Field(
            description="Oracle OIC API defaults and connection policy."
        )
        integration: FlextOracleOicConfigModels.Integration = Field(
            description="Oracle OIC integration defaults."
        )
        validation: FlextOracleOicConfigModels.Validation = Field(
            description="Oracle OIC validation rule defaults."
        )
        monitoring: FlextOracleOicConfigModels.Monitoring = Field(
            description="Oracle OIC monitoring component defaults."
        )

    class Root(BaseModel):
        """Root flext-oracle-oic config validated from ``config/*.yaml``."""

        model_config = ConfigDict(frozen=True, extra="ignore")

        OracleOic: FlextOracleOicConfigModels.OracleOic = Field(
            description="Oracle OIC business-rule config namespace."
        )


__all__: list[str] = ["FlextOracleOicConfigModels"]
