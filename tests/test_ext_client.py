"""Tests for ext_client.py module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import base64
from unittest.mock import Mock, patch

import httpx
import pytest
from pydantic import SecretStr

from flext_core import FlextResult
from flext_oracle_oic_ext.ext_client import (
    BaseOICAuthenticator,
    OICExtensionAuthenticator,
    OracleOICExtensionClient,
)
from flext_oracle_oic_ext.ext_models import OICAuthConfig, OICConnectionConfig


class TestBaseOICAuthenticator:
    """Test BaseOICAuthenticator abstract base class."""

    def test_base_authenticator_is_abstract(self) -> None:
        """Test BaseOICAuthenticator cannot be instantiated directly."""
        auth_config = OICAuthConfig(
            oauth_client_id="test_id",
            oauth_client_secret=SecretStr("test_secret"),
            oauth_token_url="https://test.com/token",
            oauth_client_aud=None,
            oauth_scope="",
        )

        with pytest.raises(TypeError, match="Cannot instantiate abstract class"):
            BaseOICAuthenticator(auth_config)

    def test_base_authenticator_abstract_methods(self) -> None:
        """Test BaseOICAuthenticator has required abstract methods."""
        assert hasattr(BaseOICAuthenticator, "get_oauth_scopes")
        # get_oauth_scopes is the only abstract method


class TestOICExtensionAuthenticator:
    """Test OICExtensionAuthenticator implementation."""

    @pytest.fixture
    def auth_config(self) -> OICAuthConfig:
        """Create test auth config."""
        return OICAuthConfig(
            oauth_client_id="test_client_id",
            oauth_client_secret=SecretStr("test_secret"),
            oauth_token_url="https://test.identity.oraclecloud.com/oauth2/v1/token",
            oauth_client_aud="test_audience",
            oauth_scope="test_scope",
        )

    @pytest.fixture
    def authenticator(self, auth_config: OICAuthConfig) -> OICExtensionAuthenticator:
        """Create authenticator instance."""
        return OICExtensionAuthenticator(auth_config)

    def test_authenticator_initialization(
        self, authenticator: OICExtensionAuthenticator, auth_config: OICAuthConfig,
    ) -> None:
        """Test authenticator initializes properly."""
        assert authenticator.auth_config == auth_config
        assert authenticator._access_token is None
        assert hasattr(authenticator, "logger")

    def test_get_oauth_scopes(self, authenticator: OICExtensionAuthenticator) -> None:
        """Test get_oauth_scopes returns built scope based on audience."""
        scopes = authenticator.get_oauth_scopes()
        expected = (
            "test_audience:443urn:opc:resource:consumer:all test_audience:443/ic/api/"
        )
        assert scopes == expected

    def test_get_oauth_scopes_default(self) -> None:
        """Test get_oauth_scopes returns default when no audience configured."""
        auth_config = OICAuthConfig(
            oauth_client_id="test_id",
            oauth_client_secret=SecretStr("test_secret"),
            oauth_token_url="https://test.com/token",
            oauth_client_aud=None,
            oauth_scope="",
        )
        authenticator = OICExtensionAuthenticator(auth_config)

        scopes = authenticator.get_oauth_scopes()
        assert scopes == "urn:opc:resource:consumer:all"

    @patch("httpx.Client.post")
    def test_get_access_token_success(
        self, mock_post: Mock, authenticator: OICExtensionAuthenticator,
    ) -> None:
        """Test successful access token retrieval."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "access_token": "test_access_token",
            "token_type": "Bearer",
            "expires_in": 3600,
        }
        mock_post.return_value = mock_response

        result = authenticator.get_access_token()

        assert result.is_success
        assert result.value == "test_access_token"
        assert authenticator._access_token == "test_access_token"

    @patch("httpx.Client.post")
    def test_get_access_token_http_error(
        self, mock_post: Mock, authenticator: OICExtensionAuthenticator,
    ) -> None:
        """Test access token retrieval with HTTP error."""
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        # Configure raise_for_status to raise HTTPStatusError
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "HTTP Error", request=Mock(), response=mock_response,
        )
        mock_post.return_value = mock_response

        result = authenticator.get_access_token()

        assert result.is_failure
        assert "OIC OAuth2 authentication HTTP error" in str(result.error)

    @patch("httpx.Client.post")
    def test_get_access_token_missing_token(
        self, mock_post: Mock, authenticator: OICExtensionAuthenticator,
    ) -> None:
        """Test access token retrieval with missing token in response."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"token_type": "Bearer"}
        mock_post.return_value = mock_response

        result = authenticator.get_access_token()

        assert result.is_failure
        assert "No access token" in str(result.error)

    @patch("httpx.Client.post")
    def test_get_access_token_exception(
        self, mock_post: Mock, authenticator: OICExtensionAuthenticator,
    ) -> None:
        """Test access token retrieval with exception."""
        mock_post.side_effect = httpx.ConnectError("Network error")

        result = authenticator.get_access_token()

        assert result.is_failure
        assert "OIC OAuth2 authentication request failed" in str(result.error)

    def test_build_oauth_scopes_with_audience(
        self, authenticator: OICExtensionAuthenticator,
    ) -> None:
        """Test build_oauth_scopes with custom audience."""
        scopes = authenticator.build_oauth_scopes("custom_audience")
        expected = "custom_audience:443urn:opc:resource:consumer:all custom_audience:443/ic/api/"
        assert scopes == expected

    def test_get_oauth_request_body(
        self, authenticator: OICExtensionAuthenticator,
    ) -> None:
        """Test OAuth request body generation."""
        body = authenticator.get_oauth_request_body()

        assert body["grant_type"] == "client_credentials"
        assert "scope" in body
        # The scope should be the built OAuth scope
        expected_scope = (
            "test_audience:443urn:opc:resource:consumer:all test_audience:443/ic/api/"
        )
        assert body["scope"] == expected_scope

    def test_encode_client_credentials(
        self, authenticator: OICExtensionAuthenticator,
    ) -> None:
        """Test client credentials encoding."""
        encoded = authenticator.encode_client_credentials()

        # Should be base64 encoded "test_client_id:test_secret"
        expected = base64.b64encode(b"test_client_id:test_secret").decode()
        assert encoded == expected


class TestOracleOICExtensionClient:
    """Test OracleOICExtensionClient main client class."""

    @pytest.fixture
    def connection_config(self) -> OICConnectionConfig:
        """Create test connection config."""
        return OICConnectionConfig(
            base_url="https://test.integration.ocp.oraclecloud.com",
            api_version="v1",
            request_timeout=30,
            max_retries=3,
            verify_ssl=True,
        )

    @pytest.fixture
    def auth_config(self) -> OICAuthConfig:
        """Create test auth config."""
        return OICAuthConfig(
            oauth_client_id="test_client_id",
            oauth_client_secret=SecretStr("test_secret"),
            oauth_token_url="https://test.identity.oraclecloud.com/oauth2/v1/token",
            oauth_client_aud=None,
            oauth_scope="",
        )

    @pytest.fixture
    def authenticator(self, auth_config: OICAuthConfig) -> OICExtensionAuthenticator:
        """Create authenticator."""
        return OICExtensionAuthenticator(auth_config)

    @pytest.fixture
    def client(
        self,
        connection_config: OICConnectionConfig,
        authenticator: OICExtensionAuthenticator,
    ) -> OracleOICExtensionClient:
        """Create client instance."""
        return OracleOICExtensionClient(connection_config, authenticator)

    def test_client_initialization(
        self,
        client: OracleOICExtensionClient,
        connection_config: OICConnectionConfig,
        authenticator: OICExtensionAuthenticator,
    ) -> None:
        """Test client initializes properly."""
        assert client.connection_config == connection_config
        assert client.authenticator == authenticator
        assert client._client is None
        assert hasattr(client, "logger")

    @patch.object(OICExtensionAuthenticator, "get_access_token")
    def test_get_authenticated_client_success(
        self, mock_get_token: Mock, client: OracleOICExtensionClient,
    ) -> None:
        """Test successful authenticated client creation."""
        mock_get_token.return_value.is_success = True
        mock_get_token.return_value.value = "test_token"

        result = client.get_authenticated_client()

        assert result.is_success
        assert result.value is not None
        mock_get_token.assert_called_once()

    @patch.object(OICExtensionAuthenticator, "get_access_token")
    def test_get_authenticated_client_auth_failure(
        self, mock_get_token: Mock, client: OracleOICExtensionClient,
    ) -> None:
        """Test authenticated client creation with auth failure."""
        # Mock the authenticator to return a failed result
        mock_get_token.return_value = FlextResult[str].fail("Auth failed")

        result = client.get_authenticated_client()

        assert result.is_failure
        assert "Authentication failed" in str(result.error)

    def test_get_base_url(self, client: OracleOICExtensionClient) -> None:
        """Test base URL generation."""
        base_url = client.get_base_url()
        expected = "https://test.integration.ocp.oraclecloud.com/ic/api/v1"
        assert base_url == expected

    @patch.object(OracleOICExtensionClient, "get_authenticated_client")
    def test_get_integrations_success(
        self, mock_get_client: Mock, client: OracleOICExtensionClient,
    ) -> None:
        """Test successful integration retrieval."""
        mock_http_client = Mock()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.raise_for_status.return_value = None
        mock_headers = Mock()
        mock_headers.get.side_effect = (
            lambda key, default="": "application/json"
            if key == "content-type"
            else default
        )
        mock_response.headers = mock_headers
        mock_response.json.return_value = {
            "items": [{"id": "int1", "name": "Integration 1"}],
        }
        mock_response.text = "{}"
        mock_response.url = "https://test.com"
        mock_response.request = Mock()
        mock_http_client.request.return_value = mock_response

        mock_get_client.return_value.is_success = True
        mock_get_client.return_value.value = mock_http_client

        result = client.get_integrations()

        assert result.is_success
        assert len(result.value) == 1
        assert result.value[0]["id"] == "int1"

    @patch.object(OracleOICExtensionClient, "get_authenticated_client")
    def test_get_integrations_client_failure(
        self, mock_get_client: Mock, client: OracleOICExtensionClient,
    ) -> None:
        """Test integration retrieval with client failure."""
        mock_get_client.return_value.is_success = False
        mock_get_client.return_value.error = "Client error"

        result = client.get_integrations()

        assert result.is_failure
        assert "Client error" in str(result.error)

    @patch.object(OracleOICExtensionClient, "get_authenticated_client")
    def test_get_integrations_http_error(
        self, mock_get_client: Mock, client: OracleOICExtensionClient,
    ) -> None:
        """Test integration retrieval with HTTP error."""
        mock_http_client = Mock()
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_http_client.request.return_value = mock_response

        mock_get_client.return_value.is_success = True
        mock_get_client.return_value.value = mock_http_client

        result = client.get_integrations()

        assert result.is_failure
        assert "HTTP 500" in str(result.error)

    @patch.object(OracleOICExtensionClient, "get_authenticated_client")
    def test_get_connections_success(
        self, mock_get_client: Mock, client: OracleOICExtensionClient,
    ) -> None:
        """Test successful connection retrieval."""
        mock_http_client = Mock()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.raise_for_status.return_value = None
        mock_headers = Mock()
        mock_headers.get.side_effect = (
            lambda key, default="": "application/json"
            if key == "content-type"
            else default
        )
        mock_response.headers = mock_headers
        mock_response.json.return_value = {
            "items": [{"id": "conn1", "name": "Connection 1"}],
        }
        mock_response.text = "{}"
        mock_response.url = "https://test.com"
        mock_response.request = Mock()
        mock_http_client.request.return_value = mock_response

        mock_get_client.return_value.is_success = True
        mock_get_client.return_value.value = mock_http_client

        result = client.get_connections()

        assert result.is_success
        assert len(result.value) == 1
        assert result.value[0]["id"] == "conn1"

    def test_context_manager_enter(self, client: OracleOICExtensionClient) -> None:
        """Test context manager __enter__ method."""
        with client as result:
            assert result is client

    def test_client_authenticator_attribute(
        self, client: OracleOICExtensionClient,
    ) -> None:
        """Test client has authenticator attribute."""
        assert client.authenticator is not None
        assert hasattr(client.authenticator, "auth_config")

    def test_client_has_connection_config(
        self, client: OracleOICExtensionClient,
    ) -> None:
        """Test client has proper connection configuration."""
        assert client.connection_config is not None
        assert hasattr(client.connection_config, "base_url")
        assert hasattr(client.connection_config, "api_version")
