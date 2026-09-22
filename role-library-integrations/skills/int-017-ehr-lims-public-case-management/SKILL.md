---
name: int-017-ehr-lims-public-case-management
description: "Integration definition INT-017 (EHR, LIMS, public case-management): Retrieve the minimum authorized record fields for administrative support and draft documentation. Default scope: Strict read-only/draft-only, patient/case scoped."
---

# EHR, LIMS, public case-management

**Integration ID:** `INT-017`
**Kind:** Integration definition (named data source / system profile — not a permission grant)

## Allowed Activities

Retrieve the minimum authorized record fields for administrative support and draft documentation.

## Default Scope

Strict read-only/draft-only, patient/case scoped.

## Prohibited

Clinical orders, diagnoses, eligibility/outcome decisions, disclosure, final signatures.

## Guardrails

- Integrations are named data sources and system profiles referenced by role skills. A reference is not authorization: every role's operating contract still requires the named human decision owner for I3/I4 actions.
- Do not treat a listed integration as a credential, connection, or permission grant.
