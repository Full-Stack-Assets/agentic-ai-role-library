---
name: int-015-contract-clm-rights-system
description: "Integration definition INT-015 (Contract/CLM/rights system): Retrieve agreements, create metadata, track dates/obligations/rights evidence. Default scope: Read terms and write draft metadata/alerts."
---

# Contract/CLM/rights system

**Integration ID:** `INT-015`
**Kind:** Integration definition (named data source / system profile — not a permission grant)

## Allowed Activities

Retrieve agreements, create metadata, track dates/obligations/rights evidence.

## Default Scope

Read terms and write draft metadata/alerts.

## Prohibited

Signing, negotiation, granting licenses, legal interpretation, registration/submission.

## Guardrails

- Integrations are named data sources and system profiles referenced by role skills. A reference is not authorization: every role's operating contract still requires the named human decision owner for I3/I4 actions.
- Do not treat a listed integration as a credential, connection, or permission grant.
