---
name: int-011-support-case-management-system
description: "Integration definition INT-011 (Support/case-management system): Read assigned cases, draft replies, classify/tag, create escalation tasks. Default scope: Agent-specific queue access; draft-only external responses."
---

# Support/case-management system

**Integration ID:** `INT-011`
**Kind:** Integration definition (named data source / system profile — not a permission grant)

## Allowed Activities

Read assigned cases, draft replies, classify/tag, create escalation tasks.

## Default Scope

Agent-specific queue access; draft-only external responses.

## Prohibited

Account action, refund, benefit/eligibility decision, sensitive external communication.

## Guardrails

- Integrations are named data sources and system profiles referenced by role skills. A reference is not authorization: every role's operating contract still requires the named human decision owner for I3/I4 actions.
- Do not treat a listed integration as a credential, connection, or permission grant.
