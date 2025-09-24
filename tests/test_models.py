"""Tests for ext_models.py.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import pytest
from pydantic import SecretStr, ValidationError

from flext_oracle_oic_ext import (
    OICAuthConfig,
    OICConnectionConfig,
    OICConnectionInfo,
    OICIntegrationInfo,
)


class TestOICAuthConfig:
    """Test OICAuthConfig model."""

    def test_valid_auth_config(self) -> None:
        """Test valid auth config creation."""
        config = OICAuthConfig(
            oauth_client_id="test_client_id",
            oauth_client_secret=SecretStr("test_client_secret"),
            oauth_token_url="https://test.identity.oraclecloud.com/oauth2/v1/token",
            oauth_client_aud="test_audience",
            oauth_scope="test_scope",
        )

        assert config.oauth_client_id == "test_client_id"
        assert config.oauth_client_secret.get_secret_value() == "test_client_secret"
        assert (
            config.oauth_token_url
            == "https://test.identity.oraclecloud.com/oauth2/v1/token"
        )
        assert config.oauth_client_aud == "test_audience"
        assert config.oauth_scope == "test_scope"

    def test_auth_config_with_none_audience(self) -> None:
        """Test auth config with None audience."""
        config = OICAuthConfig(
            oauth_client_id="test_client_id",
            oauth_client_secret=SecretStr("test_client_secret"),
            oauth_token_url="https://test.identity.oraclecloud.com/oauth2/v1/token",
            oauth_client_aud=None,
            oauth_scope="",
        )

        assert config.oauth_client_aud is None
        assert config.oauth_scope is not None

    def test_auth_config_validation_error(self) -> None:
        """Test auth config validation error."""
        # Test validation with invalid data using dict construction
        invalid_data = {
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": 123,  # Invalid type - will fail at runtime validation
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "oauth_client_aud": None,
            "oauth_scope": "",
        }
        with pytest.raises(ValidationError):
            OICAuthConfig.model_validate(invalid_data)


class TestOICConnectionConfig:
    """Test OICConnectionConfig model."""

    def test_valid_connection_config(self) -> None:
        """Test valid connection config creation."""
        config = OICConnectionConfig(
            base_url="https://test.integration.ocp.oraclecloud.com",
            api_version="v1",
            request_timeout=30,
            max_retries=3,
            verify_ssl=True,
        )

        assert config.base_url == "https://test.integration.ocp.oraclecloud.com"
        assert config.api_version == "v1"
        assert config.request_timeout == 30
        assert config.max_retries == 3
        assert config.verify_ssl is True

    def test_connection_config_defaults(self) -> None:
        """Test connection config with defaults."""
        config = OICConnectionConfig(
            base_url="https://test.integration.ocp.oraclecloud.com",
            api_version="v1",
            request_timeout=30,
            max_retries=3,
        )

        assert config.api_version == "v1"
        assert config.request_timeout == 30
        assert config.max_retries == 3
        assert config.verify_ssl is True

    def test_connection_config_validation_error(self) -> None:
        """Test connection config validation error."""
        with pytest.raises(ValidationError):
            OICConnectionConfig(
                base_url="https://test.integration.ocp.oraclecloud.com",
                api_version="v1",
                request_timeout=0,  # Should be >= 1
                max_retries=3,
            )


class TestOICIntegrationInfo:
    """Test OICIntegrationInfo model."""

    def test_valid_integration_info(self) -> None:
        """Test valid integration info creation."""
        info = OICIntegrationInfo(
            integration_id="test_integration_id",
            name="Test Integration",
            status="ACTIVE",
            version="1.0.0",
            description="Test integration description",
            created_by="test_user",
            last_updated="2025-01-08T10:00:00Z",
        )

        assert info.integration_id == "test_integration_id"
        assert info.name == "Test Integration"
        assert info.status == "ACTIVE"
        assert info.version == "1.0.0"
        assert info.description == "Test integration description"
        assert info.created_by == "test_user"
        assert info.last_updated == "2025-01-08T10:00:00Z"

    def test_integration_info_defaults(self) -> None:
        """Test integration info with defaults."""
        info = OICIntegrationInfo(
            integration_id="test_integration_id",
            name="Test Integration",
            status="ACTIVE",
            version="1.0.0",
            description="",
            created_by="",
            last_updated="",
        )

        assert info.description is not None
        assert info.created_by is not None
        assert info.last_updated is not None


class TestOICConnectionInfo:
    """Test OICConnectionInfo model."""

    def test_valid_connection_info(self) -> None:
        """Test valid connection info creation."""
        info = OICConnectionInfo(
            connection_id="test_connection_id",
            name="Test Connection",
            adapter_type="REST",
            status="ACTIVE",
            connection_type="HTTP",
            description="Test connection description",
        )

        assert info.connection_id == "test_connection_id"
        assert info.name == "Test Connection"
        assert info.adapter_type == "REST"
        assert info.status == "ACTIVE"
        assert info.connection_type == "HTTP"
        assert info.description == "Test connection description"

    def test_connection_info_defaults(self) -> None:
        """Test connection info with defaults."""
        info = OICConnectionInfo(
            connection_id="test_connection_id",
            name="Test Connection",
            adapter_type="REST",
            status="ACTIVE",
            connection_type="HTTP",
            description="",
        )

        assert info.description is not None
