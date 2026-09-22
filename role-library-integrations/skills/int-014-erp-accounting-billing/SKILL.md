---
name: int-014-erp-accounting-billing
description: "Integration definition INT-014 (ERP/accounting/billing): Retrieve approved reports, prepare reconciliations, create internal review items. Default scope: Read-only; draft journal/support workspaces where available."
---

# ERP/accounting/billing

**Integration ID:** `INT-014`
**Kind:** Integration definition (named data source / system profile — not a permission grant)

## Allowed Activities

Retrieve approved reports, prepare reconciliations, create internal review items.

## Default Scope

Read-only; draft journal/support workspaces where available.

## Prohibited

Payments, journal posting, tax filing, refund, credit, vendor/customer changes.

## Guardrails

- Integrations are named data sources and system profiles referenced by role skills. A reference is not authorization: every role's operating contract still requires the named human decision owner for I3/I4 actions.
- Do not treat a listed integration as a credential, connection, or permission grant.
