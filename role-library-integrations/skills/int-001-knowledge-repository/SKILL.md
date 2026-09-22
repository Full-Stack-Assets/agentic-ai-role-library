---
name: int-001-knowledge-repository
description: "Integration definition INT-001 (Knowledge repository): Retrieve approved policies, canon, procedures, product docs, and playbooks. Default scope: Read approved collections; propose versioned drafts."
---

# Knowledge repository

**Integration ID:** `INT-001`
**Kind:** Integration definition (named data source / system profile — not a permission grant)

## Allowed Activities

Retrieve approved policies, canon, procedures, product docs, and playbooks.

## Default Scope

Read approved collections; propose versioned drafts.

## Prohibited

Publishing/replacing source-of-truth content.

## Guardrails

- Integrations are named data sources and system profiles referenced by role skills. A reference is not authorization: every role's operating contract still requires the named human decision owner for I3/I4 actions.
- Do not treat a listed integration as a credential, connection, or permission grant.
