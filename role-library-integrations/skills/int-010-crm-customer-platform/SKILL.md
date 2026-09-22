---
name: int-010-crm-customer-platform
description: "Integration definition INT-010 (CRM / customer platform): Retrieve account context, create internal notes, draft communications/tasks. Default scope: Read selected accounts; internal-note/task write."
---

# CRM / customer platform

**Integration ID:** `INT-010`
**Kind:** Integration definition (named data source / system profile — not a permission grant)

## Allowed Activities

Retrieve account context, create internal notes, draft communications/tasks.

## Default Scope

Read selected accounts; internal-note/task write.

## Prohibited

External email/send, changes to customer records/terms, exports of sensitive data.

## Guardrails

- Integrations are named data sources and system profiles referenced by role skills. A reference is not authorization: every role's operating contract still requires the named human decision owner for I3/I4 actions.
- Do not treat a listed integration as a credential, connection, or permission grant.
