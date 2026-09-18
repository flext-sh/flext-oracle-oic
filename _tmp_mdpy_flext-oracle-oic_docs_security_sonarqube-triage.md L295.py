# from flext-oracle-oic/docs/security/sonarqube-triage.md:295
      141
      142      def test_connection_config_is_immutable(self) -> None:
      143          """Connection config is a frozen value object."""
      144          config = m.OracleOic.OICConnectionConfig(base_url="https://oic.example.com")
>>>   145          with pytest.raises(c.ValidationError):
      146              getattr(config, "__setattr__")("verify_ssl", False)
      147
      148      @pytest.mark.parametrize("timeout", [0, -1, -30])
      149      def test_connection_config_rejects_non_positive_timeout(self, timeout: int) -> None:
