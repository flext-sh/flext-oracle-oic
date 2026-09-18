# from flext-oracle-oic/docs/security/sonarqube-triage.md:39
      251                  "base_url": base_url,
      252                  "timeout": self.connection_config.request_timeout,
      253                  "headers": {
      254                      "Authorization": f"Bearer {token}",
>>>   255                      "Content-Type": "application/json",
      256                      "Accept": "application/json",
      257                  },
      258              })
      259              client = FlextApi(settings=api_config)
