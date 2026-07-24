"""Behavioral tests for the FlextOracleOicClient public contract.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import base64

import pytest
from flext_tests import tm

from flext_oracle_oic import m, p
from flext_oracle_oic.ext_client import FlextOracleOicClient


class TestsFlextOracleOicExtClient:
    """Observable-behavior tests for the unified Oracle OIC client."""

    @pytest.fixture
    def connection_config(self) -> p.OracleOic.OICConnectionConfig:
        """Return a valid in-memory OIC connection configuration."""
        return m.OracleOic.OICConnectionConfig(base_url="https://oic.example.com")

    @pytest.fixture
    def auth_config(self) -> p.OracleOic.OICAuthConfig:
        """Return a valid in-memory OIC authentication configuration."""
        return m.OracleOic.OICAuthConfig(
            oauth_client_id="client-42",
            oauth_client_secret="s3cr3t",
            oauth_token_url="https://idcs.example.com/oauth2/v1/token",
        )

    @pytest.fixture
    def client(
        self,
        connection_config: p.OracleOic.OICConnectionConfig,
        auth_config: p.OracleOic.OICAuthConfig,
    ) -> FlextOracleOicClient:
        """Return a client wired with valid configuration objects."""
        return FlextOracleOicClient(
            connection_config=connection_config, auth_config=auth_config
        )

    def test_encode_client_credentials_is_reversible_basic_auth(
        self, client: FlextOracleOicClient
    ) -> None:
        """encode_client_credentials produces decodable ``id:secret`` base64."""
        encoded = client.encode_client_credentials()

        decoded = base64.b64decode(encoded).decode()

        tm.that(decoded, eq="client-42:s3cr3t")

    def test_oauth_request_body_uses_scope_when_no_audience(
        self, connection_config: p.OracleOic.OICConnectionConfig
    ) -> None:
        """Without audience, the configured scope drives the request body."""
        auth = m.OracleOic.OICAuthConfig(
            oauth_client_id="id",
            oauth_client_secret="secret",
            oauth_token_url="https://idcs.example.com/token",
            oauth_scope="urn:opc:resource:consumer:custom",
        )
        client = FlextOracleOicClient(
            connection_config=connection_config, auth_config=auth
        )

        body = client.get_oauth_request_body()

        tm.that(
            body,
            eq={
                "grant_type": "client_credentials",
                "scope": "urn:opc:resource:consumer:custom",
            },
        )

    def test_oauth_request_body_defaults_scope_when_empty(
        self, client: FlextOracleOicClient
    ) -> None:
        """An empty scope with no audience falls back to the consumer default."""
        body = client.get_oauth_request_body()

        tm.that(body["grant_type"], eq="client_credentials")
        tm.that(body["scope"], eq="urn:opc:resource:consumer:all")

    def test_oauth_request_body_composes_audience_scopes(
        self, connection_config: p.OracleOic.OICConnectionConfig
    ) -> None:
        """A configured audience yields both resource and api scope fragments."""
        auth = m.OracleOic.OICAuthConfig(
            oauth_client_id="id",
            oauth_client_secret="secret",
            oauth_token_url="https://idcs.example.com/token",
            oauth_client_aud="https://oic.example.com",
        )
        client = FlextOracleOicClient(
            connection_config=connection_config, auth_config=auth
        )

        scope = client.get_oauth_request_body()["scope"]

        tm.that(scope, has="https://oic.example.com:443urn:opc:resource:consumer:all")
        tm.that(scope, has="https://oic.example.com:443/ic/api/")

    def test_get_access_token_fails_when_token_url_missing(
        self, connection_config: p.OracleOic.OICConnectionConfig
    ) -> None:
        """A blank token URL short-circuits to a failure result, no network."""
        auth = m.OracleOic.OICAuthConfig(
            oauth_client_id="id", oauth_client_secret="secret", oauth_token_url=""
        )
        client = FlextOracleOicClient(
            connection_config=connection_config, auth_config=auth
        )

        result = client.get_access_token()

        tm.fail(result)
        tm.that(result.error, none=False)
        tm.that(result.error, has="OAuth token URL not configured")

    def test_context_manager_yields_same_instance(
        self, client: FlextOracleOicClient
    ) -> None:
        """Entering the context returns the client itself for chaining."""
        with client as entered:
            assert entered is client

    def test_context_manager_exit_is_idempotent_without_client(
        self, client: FlextOracleOicClient
    ) -> None:
        """Exiting with no established API client is a safe no-op, repeatable."""
        client.__exit__(None, None, None)
        client.__exit__(None, None, None)


# Registry alias: tests/unit/__init__.py lazily re-exports this module symbol.
test_ext_client = TestsFlextOracleOicExtClient

__all__: list[str] = ["TestsFlextOracleOicExtClient", "test_ext_client"]
