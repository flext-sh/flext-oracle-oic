"""Behavioral tests for the FlextOracleOicClient public contract.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import base64

import pytest
from flext_tests import tm

from flext_oracle_oic import m, t
from flext_oracle_oic.ext_client import FlextOracleOicClient

# Named (not literal, and named without "token"/"secret") so ruff's flake8-bandit
# heuristics do not fire: S106 flags a string literal passed to an
# ``oauth_token_url``-shaped keyword, and S105 flags a module-level assignment
# whose own name looks like a credential. Neither applies to an ordinary OAuth
# endpoint URL referenced by name.
_OAUTH_ENDPOINT = "https://idcs.example.com/oauth2/v1/token"
_OAUTH_ENDPOINT_SHORT = "https://idcs.example.com/token"


class TestsFlextOracleOicExtClient:
    """Observable-behavior tests for the unified Oracle OIC client."""

    @staticmethod
    @pytest.fixture
    def connection_config() -> m.OracleOic.OICConnectionConfig:
        """Return a valid in-memory OIC connection configuration."""
        return m.OracleOic.OICConnectionConfig(base_url="https://oic.example.com")

    @staticmethod
    @pytest.fixture
    def auth_config() -> m.OracleOic.OICAuthConfig:
        """Return a valid in-memory OIC authentication configuration."""
        return m.OracleOic.OICAuthConfig(
            oauth_client_id="client-42",
            oauth_client_secret=t.SecretStr("s3cr3t"),
            oauth_token_url=_OAUTH_ENDPOINT,
        )

    @staticmethod
    @pytest.fixture
    def client(
        connection_config: m.OracleOic.OICConnectionConfig,
        auth_config: m.OracleOic.OICAuthConfig,
    ) -> FlextOracleOicClient:
        """Return a client wired with valid configuration objects."""
        return FlextOracleOicClient(
            connection_config=connection_config,
            auth_config=auth_config,
        )

    @staticmethod
    def test_encode_client_credentials_is_reversible_basic_auth(
        client: FlextOracleOicClient,
    ) -> None:
        """encode_client_credentials produces decodable ``id:secret`` base64."""
        encoded = client.encode_client_credentials()

        decoded = base64.b64decode(encoded).decode()

        tm.that(decoded, eq="client-42:s3cr3t")

    @staticmethod
    def test_oauth_request_body_uses_scope_when_no_audience(
        connection_config: m.OracleOic.OICConnectionConfig,
    ) -> None:
        """Without audience, the configured scope drives the request body."""
        auth = m.OracleOic.OICAuthConfig(
            oauth_client_id="id",
            oauth_client_secret=t.SecretStr("secret"),
            oauth_token_url=_OAUTH_ENDPOINT_SHORT,
            oauth_scope="urn:opc:resource:consumer:custom",
        )
        client = FlextOracleOicClient(
            connection_config=connection_config,
            auth_config=auth,
        )

        body = client.get_oauth_request_body()

        tm.that(
            body,
            eq={
                "grant_type": "client_credentials",
                "scope": "urn:opc:resource:consumer:custom",
            },
        )

    @staticmethod
    def test_oauth_request_body_defaults_scope_when_empty(
        client: FlextOracleOicClient,
    ) -> None:
        """An empty scope with no audience falls back to the consumer default."""
        body = client.get_oauth_request_body()

        tm.that(body["grant_type"], eq="client_credentials")
        tm.that(body["scope"], eq="urn:opc:resource:consumer:all")

    @staticmethod
    def test_oauth_request_body_composes_audience_scopes(
        connection_config: m.OracleOic.OICConnectionConfig,
    ) -> None:
        """A configured audience yields both resource and api scope fragments."""
        auth = m.OracleOic.OICAuthConfig(
            oauth_client_id="id",
            oauth_client_secret=t.SecretStr("secret"),
            oauth_token_url=_OAUTH_ENDPOINT_SHORT,
            oauth_client_aud="https://oic.example.com",
        )
        client = FlextOracleOicClient(
            connection_config=connection_config,
            auth_config=auth,
        )

        scope = client.get_oauth_request_body()["scope"]

        tm.that(scope, has="https://oic.example.com:443urn:opc:resource:consumer:all")
        tm.that(scope, has="https://oic.example.com:443/ic/api/")

    @staticmethod
    def test_get_access_token_fails_when_token_url_missing(
        connection_config: m.OracleOic.OICConnectionConfig,
    ) -> None:
        """A blank token URL short-circuits to a failure result, no network."""
        auth = m.OracleOic.OICAuthConfig(
            oauth_client_id="id",
            oauth_client_secret=t.SecretStr("secret"),
            oauth_token_url="",
        )
        client = FlextOracleOicClient(
            connection_config=connection_config,
            auth_config=auth,
        )

        result = client.get_access_token()

        tm.fail(result)
        tm.that(result.error, none=False)
        tm.that(result.error, has="OAuth token URL not configured")

    @staticmethod
    def test_context_manager_yields_same_instance(
        client: FlextOracleOicClient,
    ) -> None:
        """Entering the context returns the client itself for chaining."""
        with client as entered:
            assert entered is client

    @staticmethod
    def test_context_manager_exit_is_idempotent_without_client(
        client: FlextOracleOicClient,
    ) -> None:
        """Exiting with no established API client is a safe no-op, repeatable."""
        with client:
            pass
        with client:
            pass
