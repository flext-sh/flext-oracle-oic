"""Behavioral tests for Oracle OIC unified models.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Asserts the OBSERVABLE PUBLIC CONTRACT of the model namespace only:
construction results, field values via the public API, value-object
immutability and equality, secret masking, entity identity surface,
and validation error paths. No private attributes, no internal spying.
"""

from __future__ import annotations

import pytest
from flext_tests import tm

from tests import c, m, t


class TestsFlextOracleOicModelsUnit:
    """Public-contract behavior of FlextOracleOicModels.OracleOic.*."""

    # ---- OICAuthConfig ---------------------------------------------------

    def test_auth_config_exposes_supplied_values(self) -> None:
        """A fully specified auth config returns the exact inputs."""
        config = m.OracleOic.OICAuthConfig(
            oauth_client_id="test_client_id",
            oauth_client_secret=t.SecretStr("test_client_secret"),
            oauth_token_url="https://idcs.example.com/oauth2/v1/token",
            oauth_client_aud="test_audience",
            oauth_scope="test_scope",
        )
        tm.that(config.oauth_client_id, eq="test_client_id")
        tm.that(config.oauth_client_secret.get_secret_value(), eq="test_client_secret")
        tm.that(config.oauth_token_url, eq="https://idcs.example.com/oauth2/v1/token")
        tm.that(config.oauth_client_aud, eq="test_audience")
        tm.that(config.oauth_scope, eq="test_scope")

    def test_auth_config_optional_fields_default(self) -> None:
        """Audience defaults to None and scope to an empty string."""
        config = m.OracleOic.OICAuthConfig(
            oauth_client_id="cid",
            oauth_client_secret=t.SecretStr("secret"),
            oauth_token_url="https://idcs.example.com/oauth2/v1/token",
        )
        tm.that(config.oauth_client_aud, none=True)
        tm.that(config.oauth_scope, eq="")

    def test_auth_config_masks_secret_in_repr_and_dump(self) -> None:
        """The client secret is never exposed via repr or model_dump."""
        config = m.OracleOic.OICAuthConfig(
            oauth_client_id="cid",
            oauth_client_secret=t.SecretStr("super_secret"),
            oauth_token_url="https://idcs.example.com/oauth2/v1/token",
        )
        tm.that(repr(config), lacks="super_secret")
        tm.that(config.model_dump()["oauth_client_secret"], ne="super_secret")
        # The real value stays retrievable through the explicit accessor.
        tm.that(config.oauth_client_secret.get_secret_value(), eq="super_secret")

    def test_auth_config_is_immutable(self) -> None:
        """Auth config is a frozen value object; mutation is rejected."""
        config = m.OracleOic.OICAuthConfig(
            oauth_client_id="cid",
            oauth_client_secret=t.SecretStr("secret"),
            oauth_token_url="https://idcs.example.com/oauth2/v1/token",
        )
        with pytest.raises(c.ValidationError):
            getattr(config, "__setattr__")("oauth_scope", "mutated")

    def test_auth_config_equality_is_by_value(self) -> None:
        """Two auth configs with identical inputs compare equal."""
        first = m.OracleOic.OICAuthConfig(
            oauth_client_id="cid",
            oauth_client_secret=t.SecretStr("secret"),
            oauth_token_url="https://idcs.example.com/oauth2/v1/token",
        )
        second = m.OracleOic.OICAuthConfig(
            oauth_client_id="cid",
            oauth_client_secret=t.SecretStr("secret"),
            oauth_token_url="https://idcs.example.com/oauth2/v1/token",
        )
        tm.that(first, eq=second)

    @pytest.mark.parametrize(
        "missing",
        ["oauth_client_id", "oauth_client_secret", "oauth_token_url"],
    )
    def test_auth_config_requires_mandatory_fields(self, missing: str) -> None:
        """Omitting any required field raises a validation error."""
        payload: t.MutableMappingKV[str, str] = {
            "oauth_client_id": "cid",
            "oauth_client_secret": "secret",
            "oauth_token_url": "https://idcs.example.com/oauth2/v1/token",
        }
        del payload[missing]
        with pytest.raises(c.ValidationError):
            m.OracleOic.OICAuthConfig.model_validate(payload)

    # ---- OICConnectionConfig --------------------------------------------

    def test_connection_config_exposes_supplied_values(self) -> None:
        """A fully specified connection config returns the exact inputs."""
        config = m.OracleOic.OICConnectionConfig(
            base_url="https://oic.example.com",
            api_version="v2",
            request_timeout=45,
            max_retries=5,
            verify_ssl=False,
        )
        tm.that(config.base_url, eq="https://oic.example.com")
        tm.that(config.api_version, eq="v2")
        tm.that(config.request_timeout, eq=45)
        tm.that(config.max_retries, eq=5)
        tm.that(config.verify_ssl, eq=False)

    def test_connection_config_applies_documented_defaults(self) -> None:
        """Only base_url is required; the rest fall back to catalog defaults."""
        config = m.OracleOic.OICConnectionConfig(base_url="https://oic.example.com")
        tm.that(config.api_version, eq=c.OracleOic.DEFAULT_API_VERSION)
        tm.that(config.request_timeout, eq=c.DEFAULT_TIMEOUT_SECONDS)
        tm.that(config.max_retries, eq=c.MAX_RETRY_ATTEMPTS)
        assert config.verify_ssl is c.OracleOic.DEFAULT_VERIFY_SSL

    def test_connection_config_is_immutable(self) -> None:
        """Connection config is a frozen value object."""
        config = m.OracleOic.OICConnectionConfig(base_url="https://oic.example.com")
        with pytest.raises(c.ValidationError):
            getattr(config, "__setattr__")("verify_ssl", False)

    @pytest.mark.parametrize("timeout", [0, -1, -30])
    def test_connection_config_rejects_non_positive_timeout(self, timeout: int) -> None:
        """request_timeout must be strictly positive."""
        with pytest.raises(c.ValidationError):
            m.OracleOic.OICConnectionConfig(
                base_url="https://oic.example.com",
                request_timeout=timeout,
            )

    def test_connection_config_rejects_negative_retries(self) -> None:
        """max_retries cannot be negative."""
        with pytest.raises(c.ValidationError):
            m.OracleOic.OICConnectionConfig(
                base_url="https://oic.example.com",
                max_retries=-1,
            )

    # ---- OICIntegrationInfo (entity) ------------------------------------

    def test_integration_info_roundtrips_public_state(self) -> None:
        """Supplied domain fields survive a model_dump roundtrip."""
        info = m.OracleOic.OICIntegrationInfo(
            integration_id="int-1",
            name="Test Integration",
            status="ACTIVE",
            integration_version="1.0.0",
            description="desc",
            created_by="user",
            last_updated="2025-01-08T10:00:00Z",
        )
        dumped = info.model_dump()
        tm.that(dumped["integration_id"], eq="int-1")
        tm.that(dumped["name"], eq="Test Integration")
        tm.that(dumped["status"], eq="ACTIVE")
        tm.that(dumped["integration_version"], eq="1.0.0")
        tm.that(dumped["description"], eq="desc")
        tm.that(dumped["created_by"], eq="user")
        tm.that(dumped["last_updated"], eq="2025-01-08T10:00:00Z")

    def test_integration_info_optional_fields_default_empty(self) -> None:
        """Description, creator, and timestamp default to empty strings."""
        info = m.OracleOic.OICIntegrationInfo(
            integration_id="int-1",
            name="Test Integration",
            status="ACTIVE",
            integration_version="1.0.0",
        )
        tm.that(info.description, eq="")
        tm.that(info.created_by, eq="")
        tm.that(info.last_updated, eq="")

    def test_integration_info_carries_entity_identity(self) -> None:
        """As an entity it exposes a stable non-empty identity surface."""
        info = m.OracleOic.OICIntegrationInfo(
            integration_id="int-1",
            name="Test Integration",
            status="ACTIVE",
            integration_version="1.0.0",
        )
        dumped = info.model_dump()
        tm.that(dumped["unique_id"], is_=str)
        assert dumped["unique_id"]

    def test_integration_info_requires_core_fields(self) -> None:
        """The domain identifier and descriptors are mandatory."""
        with pytest.raises(c.ValidationError):
            m.OracleOic.OICIntegrationInfo.model_validate({"name": "only name"})

    # ---- OICConnectionInfo (entity) -------------------------------------

    def test_connection_info_roundtrips_public_state(self) -> None:
        """Supplied connection fields survive a model_dump roundtrip."""
        info = m.OracleOic.OICConnectionInfo(
            connection_id="conn-1",
            name="Test Connection",
            adapter_type="REST",
            status="ACTIVE",
            connection_type="HTTP",
            description="desc",
        )
        dumped = info.model_dump()
        tm.that(dumped["connection_id"], eq="conn-1")
        tm.that(dumped["name"], eq="Test Connection")
        tm.that(dumped["adapter_type"], eq="REST")
        tm.that(dumped["status"], eq="ACTIVE")
        tm.that(dumped["connection_type"], eq="HTTP")
        tm.that(dumped["description"], eq="desc")

    def test_connection_info_description_defaults_empty(self) -> None:
        """Description defaults to an empty string when omitted."""
        info = m.OracleOic.OICConnectionInfo(
            connection_id="conn-1",
            name="Test Connection",
            adapter_type="REST",
            status="ACTIVE",
            connection_type="HTTP",
        )
        tm.that(info.description, eq="")

    def test_connection_info_requires_core_fields(self) -> None:
        """Connection identifier and descriptors are mandatory."""
        with pytest.raises(c.ValidationError):
            m.OracleOic.OICConnectionInfo.model_validate({"name": "only name"})

    # ---- IntegrationStatus (entity) -------------------------------------

    def test_integration_status_roundtrips_public_state(self) -> None:
        """Status fields survive a model_dump roundtrip with defaults."""
        status = m.OracleOic.IntegrationStatus(
            integration_id="int-1",
            integration_version="1.0.0",
            status="ACTIVATED",
        )
        dumped = status.model_dump()
        tm.that(dumped["integration_id"], eq="int-1")
        tm.that(dumped["integration_version"], eq="1.0.0")
        tm.that(dumped["status"], eq="ACTIVATED")
        tm.that(dumped["last_updated"], eq="")
        tm.that(dumped["activated_by"], eq="")


__all__: list[str] = ["TestsFlextOracleOicModelsUnit"]
