"""Tests for unified models.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest

from tests import c, m, t


class TestsFlextOracleOicModelsUnit:
    """Test OICAuthConfig model."""

    def test_valid_auth_config(self) -> None:
        """Test valid auth settings creation."""
        settings = m.OracleOic.OICAuthConfig(
            oauth_client_id="test_client_id",
            oauth_client_secret=t.SecretStr("test_client_secret"),
            oauth_token_url="https://test.identity.oraclecloud.com/oauth2/v1/token",
            oauth_client_aud="test_audience",
            oauth_scope="test_scope",
        )
        assert settings.oauth_client_id == "test_client_id"
        assert settings.oauth_client_secret.get_secret_value() == "test_client_secret"
        assert (
            settings.oauth_token_url
            == "https://test.identity.oraclecloud.com/oauth2/v1/token"
        )
        assert settings.oauth_client_aud == "test_audience"
        assert settings.oauth_scope == "test_scope"

    def test_auth_config_with_none_audience(self) -> None:
        """Test auth settings with None audience."""
        settings = m.OracleOic.OICAuthConfig(
            oauth_client_id="test_client_id",
            oauth_client_secret=t.SecretStr("test_client_secret"),
            oauth_token_url="https://test.identity.oraclecloud.com/oauth2/v1/token",
            oauth_client_aud=None,
            oauth_scope="",
        )
        assert settings.oauth_client_aud is None
        assert settings.oauth_scope is not None

    def test_auth_config_validation_error(self) -> None:
        """Test auth settings validation error."""
        invalid_data: t.MappingKV[str, str | int | None] = {
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": 123,
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "oauth_client_aud": None,
            "oauth_scope": "",
        }
        with pytest.raises(c.ValidationError):
            m.OracleOic.OICAuthConfig.model_validate(invalid_data)

    def test_valid_connection_config(self) -> None:
        """Test valid connection settings creation."""
        settings = m.OracleOic.OICConnectionConfig(
            base_url="https://test.integration.ocp.oraclecloud.com",
            api_version="v1",
            request_timeout=30,
            max_retries=3,
            verify_ssl=True,
        )
        assert settings.base_url == "https://test.integration.ocp.oraclecloud.com"
        assert settings.api_version == "v1"
        assert settings.request_timeout == 30
        assert settings.max_retries == 3
        assert settings.verify_ssl is True

    def test_connection_config_defaults(self) -> None:
        """Test connection settings with defaults."""
        settings = m.OracleOic.OICConnectionConfig.model_validate({
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "api_version": "v1",
            "request_timeout": 30,
            "max_retries": 3,
        })
        assert settings.api_version == "v1"
        assert settings.request_timeout == 30
        assert settings.max_retries == 3
        assert settings.verify_ssl is True

    def test_connection_config_validation_error(self) -> None:
        """Test connection settings validation error."""
        with pytest.raises(c.ValidationError):
            m.OracleOic.OICConnectionConfig.model_validate({
                "base_url": "https://test.integration.ocp.oraclecloud.com",
                "api_version": "v1",
                "request_timeout": 0,
                "max_retries": 3,
            })

    def test_valid_integration_info(self) -> None:
        """Test valid integration info creation."""
        info = m.OracleOic.OICIntegrationInfo(
            integration_id="test_integration_id",
            name="Test Integration",
            status="ACTIVE",
            integration_version="1.0.0",
            description="Test integration description",
            created_by="test_user",
            last_updated="2025-01-08T10:00:00Z",
        )
        assert info.integration_id == "test_integration_id"
        assert info.name == "Test Integration"
        assert info.status == "ACTIVE"
        assert info.integration_version == "1.0.0"
        assert info.description == "Test integration description"
        assert info.created_by == "test_user"
        assert info.last_updated == "2025-01-08T10:00:00Z"

    def test_integration_info_defaults(self) -> None:
        """Test integration info with defaults."""
        info = m.OracleOic.OICIntegrationInfo(
            integration_id="test_integration_id",
            name="Test Integration",
            status="ACTIVE",
            integration_version="1.0.0",
            description="",
            created_by="",
            last_updated="",
        )
        assert info.description is not None
        assert info.created_by is not None
        assert info.last_updated is not None

    def test_valid_connection_info(self) -> None:
        """Test valid connection info creation."""
        info = m.OracleOic.OICConnectionInfo(
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
        info = m.OracleOic.OICConnectionInfo(
            connection_id="test_connection_id",
            name="Test Connection",
            adapter_type="REST",
            status="ACTIVE",
            connection_type="HTTP",
            description="",
        )
        assert info.description is not None
