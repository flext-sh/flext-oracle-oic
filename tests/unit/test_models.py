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

from tests.constants import c
from tests.models import m
from tests.typings import t


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
        assert config.oauth_client_id == "test_client_id"
        assert config.oauth_client_secret.get_secret_value() == "test_client_secret"
        assert config.oauth_token_url == "https://idcs.example.com/oauth2/v1/token"
        assert config.oauth_client_aud == "test_audience"
        assert config.oauth_scope == "test_scope"

    def test_auth_config_optional_fields_default(self) -> None:
        """Audience defaults to None and scope to an empty string."""
        config = m.OracleOic.OICAuthConfig(
            oauth_client_id="cid",
            oauth_client_secret=t.SecretStr("secret"),
            oauth_token_url="https://idcs.example.com/oauth2/v1/token",
        )
        assert config.oauth_client_aud is None
        assert config.oauth_scope == ""

    def test_auth_config_masks_secret_in_repr_and_dump(self) -> None:
        """The client secret is never exposed via repr or model_dump."""
        config = m.OracleOic.OICAuthConfig(
            oauth_client_id="cid",
            oauth_client_secret=t.SecretStr("super_secret"),
            oauth_token_url="https://idcs.example.com/oauth2/v1/token",
        )
        assert "super_secret" not in repr(config)
        assert config.model_dump()["oauth_client_secret"] != "super_secret"
        # The real value stays retrievable through the explicit accessor.
        assert config.oauth_client_secret.get_secret_value() == "super_secret"

    def test_auth_config_is_immutable(self) -> None:
        """Auth config is a frozen value object; mutation is rejected."""
        config = m.OracleOic.OICAuthConfig(
            oauth_client_id="cid",
            oauth_client_secret=t.SecretStr("secret"),
            oauth_token_url="https://idcs.example.com/oauth2/v1/token",
        )
        with pytest.raises(c.ValidationError):
            config.oauth_scope = "mutated"

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
        assert first == second

    @pytest.mark.parametrize(
        "missing",
        ["oauth_client_id", "oauth_client_secret", "oauth_token_url"],
    )
    def test_auth_config_requires_mandatory_fields(self, missing: str) -> None:
        """Omitting any required field raises a validation error."""
        payload: dict[str, str] = {
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
        assert config.base_url == "https://oic.example.com"
        assert config.api_version == "v2"
        assert config.request_timeout == 45
        assert config.max_retries == 5
        assert config.verify_ssl is False

    def test_connection_config_applies_documented_defaults(self) -> None:
        """Only base_url is required; the rest fall back to catalog defaults."""
        config = m.OracleOic.OICConnectionConfig(base_url="https://oic.example.com")
        assert config.api_version == c.OracleOic.DEFAULT_API_VERSION
        assert config.request_timeout == c.DEFAULT_TIMEOUT_SECONDS
        assert config.max_retries == c.MAX_RETRY_ATTEMPTS
        assert config.verify_ssl is c.OracleOic.DEFAULT_VERIFY_SSL

    def test_connection_config_is_immutable(self) -> None:
        """Connection config is a frozen value object."""
        config = m.OracleOic.OICConnectionConfig(base_url="https://oic.example.com")
        with pytest.raises(c.ValidationError):
            config.verify_ssl = False

    @pytest.mark.parametrize("timeout", [0, -1, -30])
    def test_connection_config_rejects_non_positive_timeout(
        self, timeout: int
    ) -> None:
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
        assert dumped["integration_id"] == "int-1"
        assert dumped["name"] == "Test Integration"
        assert dumped["status"] == "ACTIVE"
        assert dumped["integration_version"] == "1.0.0"
        assert dumped["description"] == "desc"
        assert dumped["created_by"] == "user"
        assert dumped["last_updated"] == "2025-01-08T10:00:00Z"

    def test_integration_info_optional_fields_default_empty(self) -> None:
        """Description, creator, and timestamp default to empty strings."""
        info = m.OracleOic.OICIntegrationInfo(
            integration_id="int-1",
            name="Test Integration",
            status="ACTIVE",
            integration_version="1.0.0",
        )
        assert info.description == ""
        assert info.created_by == ""
        assert info.last_updated == ""

    def test_integration_info_carries_entity_identity(self) -> None:
        """As an entity it exposes a stable non-empty identity surface."""
        info = m.OracleOic.OICIntegrationInfo(
            integration_id="int-1",
            name="Test Integration",
            status="ACTIVE",
            integration_version="1.0.0",
        )
        dumped = info.model_dump()
        assert isinstance(dumped["unique_id"], str)
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
        assert dumped["connection_id"] == "conn-1"
        assert dumped["name"] == "Test Connection"
        assert dumped["adapter_type"] == "REST"
        assert dumped["status"] == "ACTIVE"
        assert dumped["connection_type"] == "HTTP"
        assert dumped["description"] == "desc"

    def test_connection_info_description_defaults_empty(self) -> None:
        """Description defaults to an empty string when omitted."""
        info = m.OracleOic.OICConnectionInfo(
            connection_id="conn-1",
            name="Test Connection",
            adapter_type="REST",
            status="ACTIVE",
            connection_type="HTTP",
        )
        assert info.description == ""

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
        assert dumped["integration_id"] == "int-1"
        assert dumped["integration_version"] == "1.0.0"
        assert dumped["status"] == "ACTIVATED"
        assert dumped["last_updated"] == ""
        assert dumped["activated_by"] == ""


__all__: list[str] = ["TestsFlextOracleOicModelsUnit"]
