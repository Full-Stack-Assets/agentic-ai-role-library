---
name: int-004-calendar-scheduling
description: "Integration definition INT-004 (Calendar & scheduling): Retrieve availability, draft schedules, send internal review requests. Default scope: Read availability; create draft/hold events if approved."
---

# Calendar & scheduling

**Integration ID:** `INT-004`
**Kind:** Integration definition (named data source / system profile — not a permission grant)

## Allowed Activities

Retrieve availability, draft schedules, send internal review requests.

## Default Scope

Read availability; create draft/hold events if approved.

## Prohibited

External invitations, meeting changes involving executives/customers without approval.

## Guardrails

- Integrations are named data sources and system profiles referenced by role skills. A reference is not authorization: every role's operating contract still requires the named human decision owner for I3/I4 actions.
- Do not treat a listed integration as a credential, connection, or permission grant.
