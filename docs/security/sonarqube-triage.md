# Triagem SonarCloud — flext-sh/flext-oracle-oic

Gerado do dump da plataforma SonarCloud (2026-08-06).

Bead: `mro-2wjm.13`

## Resumo

**16 issues** — BLOCKER 0, CRITICAL 3, MAJOR 11, MINOR 2
Tipos: VULNERABILITY 5, BUG 0, CODE_SMELL 11 · **Debt total: 116min**

| regra | issues |
|---|---|
| `python:S108` | 5 |
| `python:S1192` | 3 |
| `githubactions:S8233` | 2 |
| `python:S5778` | 2 |
| `githubactions:S8264` | 1 |
| `text:S8565` | 1 |
| `python:S7504` | 1 |
| `python:S5332` | 1 |

## Como usar

Cada issue traz a **mensagem do SonarQube** (descreve o problema e o impacto), o **código real** (linha `>>>`), o tipo e o effort estimado.
**Decisão**: `corrigir` / `falso-positivo` (marcar na plataforma com justificativa) / `risco-aceito`. Ordem: BLOCKER → CRITICAL → VULNERABILITY → MAJOR. CODE_SMELL em volume pede correção de padrão.

## Issues

### 1 · 🟠 CRITICAL · CODE_SMELL · `python:S1192`
**Local**: `src/flext_oracle_oic/ext_client.py:255` · **Effort**: 6min

> Define a constant instead of duplicating this literal "application/json" 3 times.

```python
      251                  "base_url": base_url,
      252                  "timeout": self.connection_config.request_timeout,
      253                  "headers": {
      254                      "Authorization": f"Bearer {token}",
>>>   255                      "Content-Type": "application/json",
      256                      "Accept": "application/json",
      257                  },
      258              })
      259              client = FlextApi(settings=api_config)
```

**Decisão**: pendente

### 2 · 🟠 CRITICAL · CODE_SMELL · `python:S1192`
**Local**: `src/flext_oracle_oic/services/integration_crud.py:31` · **Effort**: 14min

> Define a constant instead of duplicating this literal "Client initialization failed" 7 times.

```python
       27  
       28          """
       29          client_result = self._get_client()
       30          if client_result.failure:
>>>    31              error_msg = client_result.error or "Client initialization failed"
       32              return r[FlextOracleOicClient].fail(error_msg)
       33          return client_result
       34  
       35      def _create_integration_impl(
```

**Decisão**: pendente

### 3 · 🟠 CRITICAL · CODE_SMELL · `python:S1192`
**Local**: `src/flext_oracle_oic/services/integration_lifecycle.py:40` · **Effort**: 6min

> Define a constant instead of duplicating this literal "Client initialization failed" 3 times.

```python
       36      def _activate_integration(self, integration_id: str) -> p.Result[bool]:
       37          """Activate Oracle OIC integration without exception translation."""
       38          client_result = self._get_client()
       39          if client_result.failure:
>>>    40              error_msg = client_result.error or "Client initialization failed"
       41              return r[bool].fail(error_msg)
       42          client = client_result.value
       43          activate_result = client.make_request(
       44              "POST", f"/integrations/{integration_id}/activate"
```

**Decisão**: pendente

### 4 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8264`
**Local**: `.github/workflows/docs.yml:18` · **Effort**: 5min

> Move this read permission from workflow level to job level.

```yaml
       14        - ".github/workflows/docs.yml"
       15    workflow_dispatch:
       16  
       17  permissions:
>>>    18    contents: read
       19    pages: write
       20    id-token: write
       21  
       22  concurrency:
```

**Decisão**: pendente

### 5 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8233`
**Local**: `.github/workflows/docs.yml:19` · **Effort**: 5min

> Move this write permission from workflow level to job level.

```yaml
       15    workflow_dispatch:
       16  
       17  permissions:
       18    contents: read
>>>    19    pages: write
       20    id-token: write
       21  
       22  concurrency:
       23    group: pages
```

**Decisão**: pendente

### 6 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8233`
**Local**: `.github/workflows/docs.yml:20` · **Effort**: 5min

> Move this write permission from workflow level to job level.

```yaml
       16  
       17  permissions:
       18    contents: read
       19    pages: write
>>>    20    id-token: write
       21  
       22  concurrency:
       23    group: pages
       24    cancel-in-progress: false
```

**Decisão**: pendente

### 7 · 🟡 MAJOR · VULNERABILITY · `text:S8565`
**Local**: `pyproject.toml:-` · **Effort**: 5min

> Dependency versions are not predictable if the lock file (uv.lock, poetry.lock, pdm.lock or pylock.toml) is missing.

**Decisão**: pendente

### 8 · 🟡 MAJOR · CODE_SMELL · `python:S108`
**Local**: `src/flext_oracle_oic/_utilities/connection_validation.py:18` · **Effort**: 5min

> Either remove or fill this block of code.

```python
       14      ) -> p.Result[str]:
       15          """Validate one upper-cased string against a closed canonical set."""
       16          match value:
       17              case str():
>>>    18                  pass
       19              case _:
       20                  return r[str].fail(f"{field_label} must be a string")
       21          normalized_value = value.upper().strip()
       22          if normalized_value not in valid_values:
```

**Decisão**: pendente

### 9 · 🟡 MAJOR · CODE_SMELL · `python:S108`
**Local**: `src/flext_oracle_oic/_utilities/connection_validation.py:42` · **Effort**: 5min

> Either remove or fill this block of code.

```python
       38  
       39          """
       40          match base_url:
       41              case str():
>>>    42                  pass
       43              case _:
       44                  return r[str].fail("Base URL must be a string")
       45          base_url = base_url.strip()
       46          if not base_url:
```

**Decisão**: pendente

### 10 · 🟡 MAJOR · CODE_SMELL · `python:S108`
**Local**: `src/flext_oracle_oic/_utilities/monitoring.py:45` · **Effort**: 5min

> Either remove or fill this block of code.

```python
       41                          "Review error logs and implement error handling improvements",
       42                          False,
       43                      )
       44              case _:
>>>    45                  pass
       46          return (None, None, False)
       47  
       48      @staticmethod
       49      def _components_validation_error(components: p.AttributeProbe) -> str | None:
```

**Decisão**: pendente

### 11 · 🟡 MAJOR · CODE_SMELL · `python:S108`
**Local**: `src/flext_oracle_oic/services/base.py:71` · **Effort**: 5min

> Either remove or fill this block of code.

```python
       67          match value:
       68              case str():
       69                  return value
       70              case _:
>>>    71                  pass
       72          if value is None:
       73              return default
       74          return str(value)
       75  
```

**Decisão**: pendente

### 12 · 🟡 MAJOR · CODE_SMELL · `python:S108`
**Local**: `src/flext_oracle_oic/services/base.py:92` · **Effort**: 5min

> Either remove or fill this block of code.

```python
       88          match value:
       89              case list() | tuple():
       90                  return [FlextOracleOicServiceBase._to_general_value(v) for v in value]
       91              case _:
>>>    92                  pass
       93          return str(value)
       94  
       95      def _build_integration_info(
       96          self, data: t.JsonMapping, *, fallback_id: str, default_status: str
```

**Decisão**: pendente

### 13 · 🟡 MAJOR · CODE_SMELL · `python:S5778`
**Local**: `tests/unit/test_models.py:86` · **Effort**: 5min

> Refactor this exception test to have only one invocation possibly throwing an exception.

```python
       82              client_id="cid",
       83              client_value="secret",
       84              idcs_url="https://idcs.example.com/oauth2/v1/token",
       85          )
>>>    86          with pytest.raises(c.ValidationError):
       87              getattr(config, "__setattr__")("oauth_scope", "mutated")
       88  
       89      def test_auth_config_equality_is_by_value(self) -> None:
       90          """Two auth configs with identical inputs compare equal."""
```

**Decisão**: pendente

### 14 · 🟡 MAJOR · CODE_SMELL · `python:S5778`
**Local**: `tests/unit/test_models.py:145` · **Effort**: 5min

> Refactor this exception test to have only one invocation possibly throwing an exception.

```python
      141  
      142      def test_connection_config_is_immutable(self) -> None:
      143          """Connection config is a frozen value object."""
      144          config = m.OracleOic.OICConnectionConfig(base_url="https://oic.example.com")
>>>   145          with pytest.raises(c.ValidationError):
      146              getattr(config, "__setattr__")("verify_ssl", False)
      147  
      148      @pytest.mark.parametrize("timeout", [0, -1, -30])
      149      def test_connection_config_rejects_non_positive_timeout(self, timeout: int) -> None:
```

**Decisão**: pendente

### 15 · ⚪ MINOR · CODE_SMELL · `python:S7504`
**Local**: `conftest.py:20` · **Effort**: 5min

> Remove this unnecessary `list()` call on an already iterable object.

```python
       16      if (
       17          existing_package is None
       18          or Path(getattr(existing_package, "__file__", "")).resolve() != init_file
       19      ):
>>>    20          for module_name in list(sys.modules):
       21              if module_name == package_name or module_name.startswith(
       22                  f"{package_name}."
       23              ):
       24                  sys.modules.pop(module_name, None)
```

**Decisão**: pendente

### 16 · ⚪ MINOR · VULNERABILITY · `python:S5332`
**Local**: `src/flext_oracle_oic/_utilities/connection_validation.py:48` · **Effort**: 30min

> Using HTTP protocol is insecure. Use HTTPS instead.

```python
       44                  return r[str].fail("Base URL must be a string")
       45          base_url = base_url.strip()
       46          if not base_url:
       47              return r[str].fail("Base URL cannot be empty")
>>>    48          if not base_url.startswith(("http://", "https://")):
       49              return r[str].fail("Base URL must start with http:// or https://")
       50          return r[str].ok(base_url)
       51  
       52      @staticmethod
```

**Decisão**: pendente
