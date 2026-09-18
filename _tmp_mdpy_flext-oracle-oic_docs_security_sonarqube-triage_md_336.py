# from flext-oracle-oic_docs/security/sonarqube-triage.md:336
       44                  return r[str].fail("Base URL must be a string")
       45          base_url = base_url.strip()
       46          if not base_url:
       47              return r[str].fail("Base URL cannot be empty")
>>>    48          if not base_url.startswith(("http://", "https://")):
       49              return r[str].fail("Base URL must start with http:// or https://")
       50          return r[str].ok(base_url)
       51
       52      @staticmethod
