---
name: int-016-identity-iam-and-hris
description: "Integration definition INT-016 (Identity, IAM, and HRIS): Retrieve limited directory/role/authority information for approved workflows. Default scope: Read minimum needed attributes, generally de-identified where possible."
---

# Identity, IAM, and HRIS

**Integration ID:** `INT-016`
**Kind:** Integration definition (named data source / system profile — not a permission grant)

## Allowed Activities

Retrieve limited directory/role/authority information for approved workflows.

## Default Scope

Read minimum needed attributes, generally de-identified where possible.

## Prohibited

Account creation/termination, permission change, employment action, compensation changes.

## Guardrails

- Integrations are named data sources and system profiles referenced by role skills. A reference is not authorization: every role's operating contract still requires the named human decision owner for I3/I4 actions.
- Do not treat a listed integration as a credential, connection, or permission grant.
