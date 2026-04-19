"""Oracle OIC integration pattern analysis utilities mixin."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from flext_core import p, r
from flext_oracle_oic import c, t


class FlextOracleOicUtilitiesPatternAnalysis:
    """Oracle OIC integration pattern analysis utilities."""

    @staticmethod
    def analyze_integration_pattern(
        integration_data: Mapping[str, t.Container],
    ) -> p.Result[str]:
        """Analyze Oracle OIC integration to determine pattern type.

        Args:
        integration_data: Integration configuration data

        Returns:
        r containing detected pattern or analysis error

        """
        endpoints_raw = integration_data.get("endpoints", [])
        connections_raw = integration_data.get("connections", [])
        mappings_raw = integration_data.get("mappings", [])
        endpoints: Sequence[Mapping[str, t.Container]] = (
            [dict(endpoint) for endpoint in endpoints_raw if isinstance(endpoint, dict)]
            if isinstance(endpoints_raw, list)
            else []
        )
        connections: t.RecursiveContainerList = (
            list(connections_raw) if isinstance(connections_raw, list) else []
        )
        mappings: t.RecursiveContainerList = (
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
        configuration: t.ValueOrModel,
    ) -> p.Result[Mapping[str, t.Container]]:
        """Validate Oracle OIC integration pattern configuration.

        Args:
        pattern_type: Integration pattern type
        configuration: Pattern-specific configuration

        Returns:
        r containing validated configuration or error

        """
        if pattern_type not in c.OracleOicValidation.SUPPORTED_PATTERNS:
            supported = ", ".join(sorted(c.OracleOicValidation.SUPPORTED_PATTERNS))
            return r[Mapping[str, t.Container]].fail(
                f"Unsupported pattern type. Supported: {supported}",
            )
        if configuration is None:
            return r[Mapping[str, t.Container]].fail(
                "Pattern configuration must be a mapping or model",
            )
        if isinstance(configuration, Mapping):
            normalized_configuration: Mapping[str, t.Container] = dict(configuration)
        elif hasattr(configuration, "model_dump"):
            dumped = configuration.model_dump(mode="python")
            if not isinstance(dumped, Mapping):
                return r[Mapping[str, t.Container]].fail(
                    "Pattern configuration dump must be a mapping",
                )
            normalized_configuration = dict(dumped)
        else:
            return r[Mapping[str, t.Container]].fail(
                "Pattern configuration must be a mapping or model",
            )
        if pattern_type == "message_router":
            if "routing_rules" not in normalized_configuration:
                return r[Mapping[str, t.Container]].fail(
                    "Message router pattern requires MessageRouterPatternConfig",
                )
        elif pattern_type == "scatter_gather":
            if "parallel_routes" not in normalized_configuration:
                return r[Mapping[str, t.Container]].fail(
                    "Scatter-gather pattern requires ScatterGatherPatternConfig",
                )
        elif (
            pattern_type == "publish_subscribe"
            and "event_types" not in normalized_configuration
        ):
            return r[Mapping[str, t.Container]].fail(
                "Publish-subscribe pattern requires event_types",
            )
        return r[Mapping[str, t.Container]].ok(normalized_configuration)
