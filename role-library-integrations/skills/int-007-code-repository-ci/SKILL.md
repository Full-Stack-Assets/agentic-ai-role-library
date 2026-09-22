---
name: int-007-code-repository-ci
description: "Integration definition INT-007 (Code repository & CI): Read repositories, open draft changes, execute tests in isolated environments. Default scope: Branch-level write; CI sandbox; PR creation."
---

# Code repository & CI

**Integration ID:** `INT-007`
**Kind:** Integration definition (named data source / system profile — not a permission grant)

## Allowed Activities

Read repositories, open draft changes, execute tests in isolated environments.

## Default Scope

Branch-level write; CI sandbox; PR creation.

## Prohibited

Merge to protected branch, production secret access, production deploy.

## Guardrails

- Integrations are named data sources and system profiles referenced by role skills. A reference is not authorization: every role's operating contract still requires the named human decision owner for I3/I4 actions.
- Do not treat a listed integration as a credential, connection, or permission grant.
