# from flext-oracle-oic_docs/security/sonarqube-triage.md:253
       88          match value:
       89              case list() | tuple():
       90                  return [FlextOracleOicServiceBase._to_general_value(v) for v in value]
       91              case _:
>>>    92                  pass
       93          return str(value)
       94
       95      def _build_integration_info(
       96          self, data: t.JsonMapping, *, fallback_id: str, default_status: str
