"""Oracle OIC integration pattern analysis utilities mixin."""

from __future__ import annotations

from collections.abc import Sequence

from flext_core import r
from flext_oracle_oic import c, m, t


class FlextOracleOicUtilitiesPatternAnalysis:
    """Oracle OIC integration pattern analysis utilities."""

    @staticmethod
    def analyze_integration_pattern(
        integration_data: t.ContainerMapping,
    ) -> r[str]:
        """Analyze Oracle OIC integration to determine pattern type.

        Args:
        integration_data: Integration configuration data

        Returns:
        r containing detected pattern or analysis error

        """
        endpoints_raw = integration_data.get("endpoints", [])
        connections_raw = integration_data.get("connections", [])
        mappings_raw = integration_data.get("mappings", [])
        endpoints: Sequence[t.ContainerMapping] = (
            [dict(endpoint) for endpoint in endpoints_raw if isinstance(endpoint, dict)]
            if isinstance(endpoints_raw, list)
            else []
        )
        connections: t.ContainerList = (
            list(connections_raw) if isinstance(connections_raw, list) else []
        )
        mappings: t.ContainerList = (
            list(mappings_raw) if isinstance(mappings_raw, list) else []
        )
        if len(endpoints) > c.OracleOicValidation.MIN_ENDPOINTS_FOR_ROUTER and any(
            endpoint.get("direction") == "outbound" for endpoint in endpoints
        ):
            return r[str].ok("message_router")
        if len(connections) > 1 and any(
            "aggregate" in str(mapping).lower() for mapping in mappings
        ):
            return r[str].ok("scatter_gather")
        if any(
            "event" in str(endpoint).lower() or "publish" in str(endpoint).lower()
            for endpoint in endpoints
        ):
            return r[str].ok("publish_subscribe")
        return r[str].ok("request_reply")

    @staticmethod
    def validate_pattern_configuration(
        pattern_type: str,
        configuration: m.OracleOic.MessageRouterPatternConfig
        | m.OracleOic.ScatterGatherPatternConfig,
    ) -> r[
        m.OracleOic.MessageRouterPatternConfig | m.OracleOic.ScatterGatherPatternConfig
    ]:
        """Validate Oracle OIC integration pattern configuration.

        Args:
        pattern_type: Integration pattern type
        configuration: Pattern-specific configuration

        Returns:
        r containing validated configuration or error

        """
        if pattern_type not in c.OracleOicValidation.SUPPORTED_PATTERNS:
            supported = ", ".join(sorted(c.OracleOicValidation.SUPPORTED_PATTERNS))
            return r[
                m.OracleOic.MessageRouterPatternConfig
                | m.OracleOic.ScatterGatherPatternConfig
            ].fail(
                f"Unsupported pattern type. Supported: {supported}",
            )
        if pattern_type == "message_router":
            if not isinstance(
                configuration,
                m.OracleOic.MessageRouterPatternConfig,
            ):
                return r[
                    m.OracleOic.MessageRouterPatternConfig
                    | m.OracleOic.ScatterGatherPatternConfig
                ].fail(
                    "Message router pattern requires MessageRouterPatternConfig",
                )
        elif pattern_type == "scatter_gather":
            if not isinstance(
                configuration,
                m.OracleOic.ScatterGatherPatternConfig,
            ):
                return r[
                    m.OracleOic.MessageRouterPatternConfig
                    | m.OracleOic.ScatterGatherPatternConfig
                ].fail(
                    "Scatter-gather pattern requires ScatterGatherPatternConfig",
                )
        elif pattern_type == "publish_subscribe":
            configuration_data = configuration.model_dump(mode="python")
            if "event_types" not in configuration_data:
                return r[
                    m.OracleOic.MessageRouterPatternConfig
                    | m.OracleOic.ScatterGatherPatternConfig
                ].fail(
                    "Publish-subscribe pattern requires event_types",
                )
        return r[
            m.OracleOic.MessageRouterPatternConfig
            | m.OracleOic.ScatterGatherPatternConfig
        ].ok(configuration)
