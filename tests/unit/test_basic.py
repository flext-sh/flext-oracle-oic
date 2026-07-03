"""Basic tests for flext-oracle-oic.

Tests the actual functionality that exists in the current implementation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_oracle_oic import FlextOracleOicSettings
from tests.models import m
from tests.typings import t


class TestsFlextOracleOicBasic:
    """Test basic functionality that actually exists."""

    def test_flext_oracle_oic_basic(self) -> None:
        """Test basic FlextOracleOic functionality."""
        settings = FlextOracleOicSettings.model_validate({})
        assert settings.base_url is not None

    def test_flext_oracle_oic_config(self) -> None:
        """Test FlextOracleOicSettings creation."""
        settings = FlextOracleOicSettings.model_validate({
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        })
        assert settings.base_url == "https://test.integration.ocp.oraclecloud.com"
        assert settings.oauth_client_id == "test_client_id"

    def test_models(self) -> None:
        """Test model classes."""
        auth_config = m.OracleOic.OICAuthConfig.model_validate({
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": t.SecretStr("test_secret"),
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        })
        assert auth_config.oauth_client_id == "test_client_id"
        connection_config = m.OracleOic.OICConnectionConfig.model_validate({
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "api_version": "v1",
            "request_timeout": 30,
        })
        assert (
            connection_config.base_url == "https://test.integration.ocp.oraclecloud.com"
        )
