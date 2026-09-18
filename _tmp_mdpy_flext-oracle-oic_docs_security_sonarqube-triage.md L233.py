# from flext-oracle-oic/docs/security/sonarqube-triage.md:233
       67          match value:
       68              case str():
       69                  return value
       70              case _:
>>>    71                  pass
       72          if value is None:
       73              return default
       74          return str(value)
       75
