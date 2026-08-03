# AGENTS.md — flext-oracle-oic

> **Parent workspace law** lives in [`../AGENTS.md`](../AGENTS.md) — read it first.
> Universal engineering core: `~/.agents/UNIVERSAL_CORE.md`. Composition: global skills + parent/root `AGENTS.md` + this scope delta. Do not re-embed universal law.
>
> **Standalone / independent mode:** when `../AGENTS.md` does not resolve, pin the parent raw `AGENTS.md` URL to the same branch/release as this package (never `main`).

<!-- AIHUB-AGENTS-SCOPE-LOCAL-BEGIN -->
**Package:** `flext_oracle_oic` · deps: `flext-api`, `flext-auth`, `flext-cli`, `flext-core`

## Overview

Oracle Integration Cloud (OIC) extension library — integration CRUD, orchestration, monitoring. Base for `flext-tap-oracle-oic` and `flext-target-oracle-oic`.

## Structure

```text
src/flext_oracle_oic/
├── api.py                # FlextOracleOicApi facade (async context manager)
├── ext_client.py         # FlextOracleOicClient
├── service.py main.py __main__.py
├── services/             # integration CRUD, lifecycle, orchestration, monitoring, authentication mixins
├── constants.py typings.py protocols.py models.py utilities.py   # AUTO-GENERATED facets
└── _utilities/
```

## Code Map

| Symbol | Kind | Location | Role |
|--------|------|----------|------|
| `FlextOracleOicApi` | class | `api.py` | facade: integration CRUD, orchestration, health/metrics, auth/token |
| `FlextOracleOicClient` | class | `ext_client.py` | OIC REST client |
| `FlextOracleOicService` | class | `service.py` | service layer |
| `FlextOracleOicIntegrationCrudMixin` | class | `services/integration_crud.py` | CRUD mixin |

## Conventions (specific to this package)

- `FlextOracleOicApi` is an **async context manager** and depends on `flext-auth` for authentication/token handling.

## Anti-Patterns / Gotchas

- Authentication lifecycle is separate from the service mixins — go through the facade's auth/token operations.

## Commands

```bash
make check PROJECT=flext-oracle-oic
make test  PROJECT=flext-oracle-oic
```
<!-- AIHUB-AGENTS-SCOPE-LOCAL-END -->
