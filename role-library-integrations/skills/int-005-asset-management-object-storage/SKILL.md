---
name: int-005-asset-management-object-storage
description: "Integration definition INT-005 (Asset management / object storage): Read/write versioned artifacts and metadata; compute checksums. Default scope: Scoped project folders; append-only provenance."
---

# Asset management / object storage

**Integration ID:** `INT-005`
**Kind:** Integration definition (named data source / system profile — not a permission grant)

## Allowed Activities

Read/write versioned artifacts and metadata; compute checksums.

## Default Scope

Scoped project folders; append-only provenance.

## Prohibited

Deleting originals, changing master labels, public sharing.

## Guardrails

- Integrations are named data sources and system profiles referenced by role skills. A reference is not authorization: every role's operating contract still requires the named human decision owner for I3/I4 actions.
- Do not treat a listed integration as a credential, connection, or permission grant.
