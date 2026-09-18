# from flext-oracle-oic_docs/security/sonarqube-triage.md:172
       14      ) -> p.Result[str]:
       15          """Validate one upper-cased string against a closed canonical set."""
       16          match value:
       17              case str():
>>>    18                  pass
       19              case _:
       20                  return r[str].fail(f"{field_label} must be a string")
       21          normalized_value = value.upper().strip()
       22          if normalized_value not in valid_values:
