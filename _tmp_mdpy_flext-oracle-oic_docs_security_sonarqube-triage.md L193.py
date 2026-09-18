# from flext-oracle-oic/docs/security/sonarqube-triage.md:193
       38
       39          """
       40          match base_url:
       41              case str():
>>>    42                  pass
       43              case _:
       44                  return r[str].fail("Base URL must be a string")
       45          base_url = base_url.strip()
       46          if not base_url:
