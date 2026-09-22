---
name: int-009-data-warehouse-bi
description: "Integration definition INT-009 (Data warehouse / BI): Query approved views, publish draft analyses, refresh non-sensitive sandbox assets. Default scope: Read-only curated views; workspace-level draft write."
---

# Data warehouse / BI

**Integration ID:** `INT-009`
**Kind:** Integration definition (named data source / system profile — not a permission grant)

## Allowed Activities

Query approved views, publish draft analyses, refresh non-sensitive sandbox assets.

## Default Scope

Read-only curated views; workspace-level draft write.

## Prohibited

Data deletion, source-table writes, broad sharing, sensitive export.

## Guardrails

- Integrations are named data sources and system profiles referenced by role skills. A reference is not authorization: every role's operating contract still requires the named human decision owner for I3/I4 actions.
- Do not treat a listed integration as a credential, connection, or permission grant.
