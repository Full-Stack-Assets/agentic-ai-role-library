---
name: int-019-external-research-search-services
description: "Integration definition INT-019 (External research/search services): Retrieve publicly available or licensed information with source metadata. Default scope: Search/read; download only to governed workspace."
---

# External research/search services

**Integration ID:** `INT-019`
**Kind:** Integration definition (named data source / system profile — not a permission grant)

## Allowed Activities

Retrieve publicly available or licensed information with source metadata.

## Default Scope

Search/read; download only to governed workspace.

## Prohibited

Credential sharing, automated scraping outside terms, external account actions.

## Guardrails

- Integrations are named data sources and system profiles referenced by role skills. A reference is not authorization: every role's operating contract still requires the named human decision owner for I3/I4 actions.
- Do not treat a listed integration as a credential, connection, or permission grant.
