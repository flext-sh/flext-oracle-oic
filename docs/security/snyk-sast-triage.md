# Triagem Snyk Code (SAST) — flext-sh/flext-oracle-oic

Gerado do scan Snyk (dump 2026-08-06). Bead: `mro-rq8y`

## Resumo

**1 achados** — critical 0, high 0, medium 0, low 1

| categoria | achados |
|---|---|
| Hardcoded Non-Cryptographic Secret | 1 |

## Como usar este documento

Cada achado traz o **código real** extraído da worktree (linha `>>>` = sink reportado), a regra completa e o CWE.
Preencha **Decisão**: `corrigir` / `falso-positivo` (registrar em `.snyk`) / `risco-aceito` (com prazo).

## Achados

### 1 · ⚪ LOW · Hardcoded Non-Cryptographic Secret
**Local**: `tests/unit/test_ext_client.py:29` · **CWE**: -

```python
       25  ) -> m.OracleOic.OICAuthConfig:
       26      """Build an OICAuthConfig without exposing literals to sensitive arg names."""
       27      return m.OracleOic.OICAuthConfig(
       28          oauth_client_id=client_id,
>>>    29          oauth_client_secret=client_value,
       30          oauth_token_url=idcs_url,
       31          oauth_client_aud=audience,
       32          oauth_scope=scope,
       33      )
```

**Decisão**: 

