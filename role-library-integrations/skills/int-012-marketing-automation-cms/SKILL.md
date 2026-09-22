---
name: int-012-marketing-automation-cms
description: "Integration definition INT-012 (Marketing automation & CMS): Draft content, build non-live campaigns, validate assets, retrieve reporting. Default scope: Staging/draft workspace and read analytics."
---

# Marketing automation & CMS

**Integration ID:** `INT-012`
**Kind:** Integration definition (named data source / system profile — not a permission grant)

## Allowed Activities

Draft content, build non-live campaigns, validate assets, retrieve reporting.

## Default Scope

Staging/draft workspace and read analytics.

## Prohibited

Publishing, emailing, posting, changing audiences, increasing spend.

## Guardrails

- Integrations are named data sources and system profiles referenced by role skills. A reference is not authorization: every role's operating contract still requires the named human decision owner for I3/I4 actions.
- Do not treat a listed integration as a credential, connection, or permission grant.
