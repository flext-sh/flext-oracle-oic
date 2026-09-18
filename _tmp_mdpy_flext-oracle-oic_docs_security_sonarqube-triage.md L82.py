# from flext-oracle-oic/docs/security/sonarqube-triage.md:82
       36      def _activate_integration(self, integration_id: str) -> p.Result[bool]:
       37          """Activate Oracle OIC integration without exception translation."""
       38          client_result = self._get_client()
       39          if client_result.failure:
>>>    40              error_msg = client_result.error or "Client initialization failed"
       41              return r[bool].fail(error_msg)
       42          client = client_result.value
       43          activate_result = client.make_request(
       44              "POST", f"/integrations/{integration_id}/activate"
