---
name: int-013-social-community-platform
description: "Integration definition INT-013 (Social/community platform): Retrieve approved metrics/inbox messages, create drafts, tag/rout cases. Default scope: Read-only and draft queue."
---

# Social/community platform

**Integration ID:** `INT-013`
**Kind:** Integration definition (named data source / system profile — not a permission grant)

## Allowed Activities

Retrieve approved metrics/inbox messages, create drafts, tag/rout cases.

## Default Scope

Read-only and draft queue.

## Prohibited

Posts, DMs, replies to sensitive/high-reach accounts, moderation sanctions.

## Guardrails

- Integrations are named data sources and system profiles referenced by role skills. A reference is not authorization: every role's operating contract still requires the named human decision owner for I3/I4 actions.
- Do not treat a listed integration as a credential, connection, or permission grant.
