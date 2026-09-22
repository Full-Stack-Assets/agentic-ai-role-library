---
name: int-003-project-workflow-management
description: "Integration definition INT-003 (Project/workflow management): Create bounded tasks, dependencies, statuses, and reminders. Default scope: Create/update role-owned tasks; read dependencies."
---

# Project/workflow management

**Integration ID:** `INT-003`
**Kind:** Integration definition (named data source / system profile — not a permission grant)

## Allowed Activities

Create bounded tasks, dependencies, statuses, and reminders.

## Default Scope

Create/update role-owned tasks; read dependencies.

## Prohibited

Changing portfolio scope, budgets, deadlines, or approvals without owner.

## Guardrails

- Integrations are named data sources and system profiles referenced by role skills. A reference is not authorization: every role's operating contract still requires the named human decision owner for I3/I4 actions.
- Do not treat a listed integration as a credential, connection, or permission grant.
