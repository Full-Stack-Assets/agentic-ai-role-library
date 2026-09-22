---
name: int-018-maps-gis-field-service-eam-cmms
description: "Integration definition INT-018 (Maps, GIS, field service, EAM/CMMS): View locations/assets/work orders and create draft plans/checklists. Default scope: Read assigned locations; draft work orders."
---

# Maps, GIS, field service, EAM/CMMS

**Integration ID:** `INT-018`
**Kind:** Integration definition (named data source / system profile — not a permission grant)

## Allowed Activities

View locations/assets/work orders and create draft plans/checklists.

## Default Scope

Read assigned locations; draft work orders.

## Prohibited

Dispatch, work authorization, safety closure, engineering sign-off.

## Guardrails

- Integrations are named data sources and system profiles referenced by role skills. A reference is not authorization: every role's operating contract still requires the named human decision owner for I3/I4 actions.
- Do not treat a listed integration as a credential, connection, or permission grant.
