# CLAUDE.md - FLEXT-ORACLE-OIC-EXT MODULE

**Hierarchy**: PROJECT-SPECIFIC
**Project**: Oracle OIC Extensions
**Status**: NEEDS VERIFICATION
**Last Updated**: 2025-07-12

**Reference**: `/home/marlonsc/CLAUDE.md` → Universal principles
**Reference**: `/home/marlonsc/internal.invalid.md` → Cross-workspace issues
**Reference**: `../CLAUDE.md` → FLEXT workspace standards

---

## ⛔ ANTI-CHAOS PROTOCOL

### FORBIDDEN ACTIONS WITHOUT EXPLICIT USER PERMISSION:
1. **NEVER modify pyproject.toml** - Dependencies are carefully managed
2. **NEVER modify .gitignore** - Version control rules are set
3. **NEVER modify Makefile** - Build automation is configured
4. **NEVER create fix_*.py scripts** - They cause more problems than solutions
5. **NEVER duplicate code** - Use existing patterns and imports
6. **NEVER make fake implementations** - Only real, working code

### MANDATORY ACTIONS:
1. **ALWAYS use debug/trace** for diagnostics (no print statements)
2. **ALWAYS check project docs** before making changes
3. **ALWAYS follow existing patterns** in the codebase
4. **ALWAYS run quality gates** before completing work
5. **ALWAYS use workspace venv** at `/home/marlonsc/flext/.venv`

---

## 🎯 PROJECT PURPOSE

Oracle Integration Cloud (OIC) Extensions module providing:
- Custom OIC adapters and connectors
- Extended OIC functionality
- Integration patterns for Oracle cloud
- OIC-specific utilities and helpers

---

## 📊 PROJECT STATUS

**Current State**: NEEDS VERIFICATION
- Project structure needs investigation
- Dependencies need documentation
- Implementation status unknown

---

## 🔧 DEVELOPMENT STANDARDS

### Environment
```bash
# MANDATORY: Use workspace venv
source /home/marlonsc/flext/.venv/bin/activate
# NOT project-specific venv
```

### Quality Gates (MANDATORY)
```bash
# Before completing ANY work:
make lint      # Must pass
make typecheck # Must pass
make test      # Must pass
make check     # Must pass ALL checks
```

---

## 📁 PROJECT STRUCTURE

```
flext-oracle-oic-ext/
├── src/
│   └── flext_oracle_oic_ext/
│       ├── __init__.py
│       ├── adapters/        # OIC custom adapters
│       ├── connectors/      # OIC connectors
│       ├── patterns/        # Integration patterns
│       └── utils/           # OIC utilities
├── tests/
├── pyproject.toml
├── Makefile
├── README.md
└── CLAUDE.md               # This file
```

---

## 🚨 KNOWN ISSUES

- Implementation status needs verification
- Dependencies on OIC SDK need documentation
- Integration with main FLEXT framework unclear

---

**MANTRA**: INVESTIGATE FIRST, IMPLEMENT REAL SOLUTIONS, NO SHORTCUTS