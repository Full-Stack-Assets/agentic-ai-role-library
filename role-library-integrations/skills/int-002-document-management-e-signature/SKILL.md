---
name: int-002-document-management-e-signature
description: "Integration definition INT-002 (Document management & e-signature): Store controlled documents, route review, manage redlines, and retain evidence. Default scope: Read/write draft workspace; create review task."
---

# Document management & e-signature

**Integration ID:** `INT-002`
**Kind:** Integration definition (named data source / system profile — not a permission grant)

## Allowed Activities

Store controlled documents, route review, manage redlines, and retain evidence.

## Default Scope

Read/write draft workspace; create review task.

## Prohibited

Signing, sending final documents, changing retention/legal hold.

## Guardrails

- Integrations are named data sources and system profiles referenced by role skills. A reference is not authorization: every role's operating contract still requires the named human decision owner for I3/I4 actions.
- Do not treat a listed integration as a credential, connection, or permission grant.
