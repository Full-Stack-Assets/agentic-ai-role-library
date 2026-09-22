---
name: int-008-cloud-infrastructure-observability
description: "Integration definition INT-008 (Cloud/infrastructure & observability): Read approved logs/metrics/configs and create nonproduction diagnostic changes. Default scope: Read-only by default; sandbox/test scopes."
---

# Cloud/infrastructure & observability

**Integration ID:** `INT-008`
**Kind:** Integration definition (named data source / system profile — not a permission grant)

## Allowed Activities

Read approved logs/metrics/configs and create nonproduction diagnostic changes.

## Default Scope

Read-only by default; sandbox/test scopes.

## Prohibited

Production changes, access-policy changes, destructive actions, public status updates.

## Guardrails

- Integrations are named data sources and system profiles referenced by role skills. A reference is not authorization: every role's operating contract still requires the named human decision owner for I3/I4 actions.
- Do not treat a listed integration as a credential, connection, or permission grant.
