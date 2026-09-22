---
name: int-020-communication-platforms
description: "Integration definition INT-020 (Communication platforms): Draft messages, create internal threads, route reviews, summarize approved meetings. Default scope: Internal draft/notification scope."
---

# Communication platforms

**Integration ID:** `INT-020`
**Kind:** Integration definition (named data source / system profile — not a permission grant)

## Allowed Activities

Draft messages, create internal threads, route reviews, summarize approved meetings.

## Default Scope

Internal draft/notification scope.

## Prohibited

Send external messages, invitations, high-impact announcements, sensitive disclosure.

## Guardrails

- Integrations are named data sources and system profiles referenced by role skills. A reference is not authorization: every role's operating contract still requires the named human decision owner for I3/I4 actions.
- Do not treat a listed integration as a credential, connection, or permission grant.
