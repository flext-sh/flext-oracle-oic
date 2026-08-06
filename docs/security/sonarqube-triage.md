# Triagem SonarCloud — flext-sh/flext-oracle-oic

Gerado do dump da plataforma SonarCloud (2026-08-06).

Bead de rastreio: `mro-2wjm.13`

## Resumo

**16 issues** — BLOCKER 0, CRITICAL 3, MAJOR 11, MINOR 2
Tipos: VULNERABILITY 5, BUG 0, CODE_SMELL 11

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

## Issues

Coluna **Decisão**: `corrigir` / `falso-positivo` / `risco-aceito`.

| # | sev | tipo | regra | componente | linha | Decisão |
|---|---|---|---|---|---|---|
| 1 | CRITICAL | CODE_SMELL | `python:S1192` | `src/flext_oracle_oic/ext_client.py` | 255 | |
| 2 | CRITICAL | CODE_SMELL | `python:S1192` | `src/flext_oracle_oic/services/integration_crud.py` | 31 | |
| 3 | CRITICAL | CODE_SMELL | `python:S1192` | `src/flext_oracle_oic/services/integration_lifecycle.py` | 40 | |
| 4 | MAJOR | VULNERABILITY | `githubactions:S8264` | `.github/workflows/docs.yml` | 18 | |
| 5 | MAJOR | VULNERABILITY | `githubactions:S8233` | `.github/workflows/docs.yml` | 19 | |
| 6 | MAJOR | VULNERABILITY | `githubactions:S8233` | `.github/workflows/docs.yml` | 20 | |
| 7 | MAJOR | VULNERABILITY | `text:S8565` | `pyproject.toml` | - | |
| 8 | MAJOR | CODE_SMELL | `python:S108` | `src/flext_oracle_oic/_utilities/connection_validation.py` | 18 | |
| 9 | MAJOR | CODE_SMELL | `python:S108` | `src/flext_oracle_oic/_utilities/connection_validation.py` | 42 | |
| 10 | MAJOR | CODE_SMELL | `python:S108` | `src/flext_oracle_oic/_utilities/monitoring.py` | 45 | |
| 11 | MAJOR | CODE_SMELL | `python:S108` | `src/flext_oracle_oic/services/base.py` | 71 | |
| 12 | MAJOR | CODE_SMELL | `python:S108` | `src/flext_oracle_oic/services/base.py` | 92 | |
| 13 | MAJOR | CODE_SMELL | `python:S5778` | `tests/unit/test_models.py` | 86 | |
| 14 | MAJOR | CODE_SMELL | `python:S5778` | `tests/unit/test_models.py` | 145 | |
| 15 | MINOR | CODE_SMELL | `python:S7504` | `conftest.py` | 20 | |
| 16 | MINOR | VULNERABILITY | `python:S5332` | `src/flext_oracle_oic/_utilities/connection_validation.py` | 48 | |

## Como triar

1. **BLOCKER e CRITICAL primeiro**, e todo VULNERABILITY independente de severidade.
2. Classificar: **corrigir**, **falso-positivo** (marcar na plataforma SonarCloud com justificativa), **risco-aceito** (com prazo).
3. CODE_SMELL em volume alto sugere padrão — corrigir a causa raiz, não issue a issue.

Dados brutos: `~/sonarqube-violations/by-repo/flext-sh__flext-oracle-oic.json`

