# from flext-oracle-oic/docs/security/sonarqube-triage.md:274
       82              client_id="cid",
       83              client_value="secret",
       84              idcs_url="https://idcs.example.com/oauth2/v1/token",
       85          )
>>>    86          with pytest.raises(c.ValidationError):
       87              getattr(config, "__setattr__")("oauth_scope", "mutated")
       88
       89      def test_auth_config_equality_is_by_value(self) -> None:
       90          """Two auth configs with identical inputs compare equal."""
