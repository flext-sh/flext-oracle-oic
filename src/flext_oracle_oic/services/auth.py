"""FLEXT Oracle OIC Auth - Token refresh and validation operations.

Mixin providing authentication operations for the FlextOracleOicService facade.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import p, r
from flext_oracle_oic.services.base import FlextOracleOicServiceBase


class FlextOracleOicAuthMixin(FlextOracleOicServiceBase):
    """Mixin providing authentication operations for FlextOracleOicService facade."""

    def refresh_auth_token(self) -> p.Result[str]:
        """Refresh OAuth2 authentication token.

        Returns:
        r containing new access token.

        """
        try:
            if not self._authenticator:
                return r[str].fail("Authenticator not initialized")
            refresh_fn = getattr(self._authenticator, "refresh_token", None)
            if not callable(refresh_fn):
                return r[str].fail("Authenticator has no refresh_token")
            token = refresh_fn()
            return r[str].ok(str(token))
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Token refresh failed")
            return r[str].fail_op("Token refresh", e)

    def validate_auth_token(self, token: str) -> p.Result[bool]:
        """Validate OAuth2 authentication token.

        Args:
        token: Token to validate.

        Returns:
        r containing validation result.

        """
        try:
            if not self._authenticator:
                return r[bool].fail("Authenticator not initialized")
            validate_fn = getattr(self._authenticator, "validate_token", None)
            if not callable(validate_fn):
                return r[bool].fail("Authenticator has no validate_token")
            valid = validate_fn(token)
            return r[bool].ok(bool(valid))
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Token validation failed")
            return r[bool].fail_op("Token validation", e)


__all__: list[str] = ["FlextOracleOicAuthMixin"]
