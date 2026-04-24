"""FLEXT Oracle OIC Integration Patterns - Message Router and Scatter-Gather.

Mixin providing enterprise integration pattern operations for the
FlextOracleOicService facade.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import (
    Sequence,
)

from flext_core import p, r

from flext_oracle_oic.constants import c
from flext_oracle_oic.models import m
from flext_oracle_oic.services.base import FlextOracleOicServiceBase
from flext_oracle_oic.typings import t
from flext_oracle_oic.utilities import u


class FlextOracleOicIntegrationPatternsMixin(FlextOracleOicServiceBase):
    """Mixin providing enterprise integration patterns for FlextOracleOicService facade."""

    def apply_message_router_pattern(
        self,
        message_data: t.JsonMapping,
        routing_rules: Sequence[t.JsonMapping],
    ) -> p.Result[t.JsonMapping]:
        """Apply message router pattern to OIC integration using u.

        Args:
        message_data: Message to route
        routing_rules: Routing rules configuration

        Returns:
        r containing routing result or error

        """
        try:
            self.logger.info("Applying message router pattern")
            pattern_config = m.OracleOic.MessageRouterPatternConfig(
                routing_rules=routing_rules,
                message_data=message_data,
            )
            validation_result = u.PatternAnalysis.validate_pattern_configuration(
                "message_router",
                pattern_config,
            )
            if validation_result.failure:
                return r[t.JsonMapping].fail(
                    f"Pattern validation failed: {validation_result.error}",
                )
            routing_result = {
                "pattern": c.OICPatterns.PATTERN_MESSAGE_ROUTER,
                "message_id": message_data.get(
                    "id",
                    c.OICPatterns.PATTERN_MESSAGE_ID_UNKNOWN,
                ),
                "applied_rules": len(routing_rules),
                "status": c.OICPatterns.PatternStatus.PROCESSED,
            }
            return r[t.JsonMapping].ok(routing_result)
        except (ConnectionError, TimeoutError, ValueError) as e:
            error_msg = f"Message router pattern failed: {e}"
            self.logger.exception(error_msg)
            return r[t.JsonMapping].fail(error_msg)

    def apply_scatter_gather_pattern(
        self,
        request_data: t.JsonMapping,
        target_endpoints: t.StrSequence,
    ) -> p.Result[t.JsonMapping]:
        """Apply scatter-gather pattern to OIC integration using u.

        Args:
        request_data: Request to scatter
        target_endpoints: Target endpoints for scatter

        Returns:
        r containing scatter-gather result or error

        """
        try:
            self.logger.info("Applying scatter-gather pattern")
            pattern_config = m.OracleOic.ScatterGatherPatternConfig(
                target_services=target_endpoints,
                request_data=request_data,
            )
            validation_result = u.PatternAnalysis.validate_pattern_configuration(
                "scatter_gather",
                pattern_config,
            )
            if validation_result.failure:
                return r[t.JsonMapping].fail(
                    f"Pattern validation failed: {validation_result.error}",
                )
            scatter_result = {
                "pattern": c.OICPatterns.PATTERN_SCATTER_GATHER,
                "request_id": request_data.get(
                    "id",
                    c.OICPatterns.PATTERN_REQUEST_ID_UNKNOWN,
                ),
                "target_count": len(target_endpoints),
                "status": c.OICPatterns.PatternStatus.PROCESSED,
            }
            return r[t.JsonMapping].ok(scatter_result)
        except (ConnectionError, TimeoutError, ValueError) as e:
            error_msg = f"Scatter-gather pattern failed: {e}"
            self.logger.exception(error_msg)
            return r[t.JsonMapping].fail(error_msg)


__all__: list[str] = ["FlextOracleOicIntegrationPatternsMixin"]
