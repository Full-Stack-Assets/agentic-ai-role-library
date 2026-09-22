# Agentic AI Role Library — Claude Code Plugins

The **Agentic AI Role Library** (196 entries) packaged as installable [Claude Code](https://code.claude.com) plugins: bounded agent roles, each with an operating contract (mission, approved inputs, allowed work, required output schema, quality gate, handoff, stop conditions).

Nic speaks plain English; the library speaks IDs. The `role-library-router` plugin is the bridge: describe a task in natural language and it returns the ranked role+capability assemblies that apply.

## Packs

| Plugin | Contents | Entries |
|---|---|---|
| `role-library-router` | Natural-language router + matcher script | 1 skill |
| `role-library-built-environment` | Built Environment, Science, Field Ops (BSF) | 6 |
| `role-library-music-audio` | Music and Audio Production (CMA) | 14 |
| `role-library-knowledge-rights` | Knowledge, Library, and Rights (CMK) | 3 |
| `role-library-content-marketing` | Content, Marketing, Community, Growth (CMM) | 9 |
| `role-library-control-canon` | Control and Canon (CMO) | 6 |
| `role-library-release-distribution` | Release and Distribution (CMR) | 8 |
| `role-library-visual-video` | Visual, Video, and Storyworld (CMV) | 10 |
| `role-library-data-analytics` | Data, Analytics, AI, Experimentation (DAA) | 8 |
| `role-library-engineering` | Software Engineering, Security, Platform Ops (ESP) | 9 |
| `role-library-finance-risk` | Finance, Risk, Legal, Compliance (FRC) | 8 |
| `role-library-governance` | Governance, Knowledge, Enterprise Control (GKE) | 7 |
| `role-library-healthcare-public` | Healthcare, Public Service, Education, Casework (HPE) | 6 |
| `role-library-operations` | Operations, Supply Chain, Procurement (OSP) | 8 |
| `role-library-sector-overlays` | Sector Overlay Roles (OVL) | 8 |
| `role-library-people-learning` | People, Learning, Org Enablement (PLE) | 6 |
| `role-library-product-design` | Product, Experience, and Design (PXD) | 7 |
| `role-library-revenue-customer` | Revenue, Customer, Partnership Ops (RCP) | 8 |
| `role-library-capabilities` | Reusable capabilities SKL-001–SKL-045 | 45 |
| `role-library-integrations` | Integration definitions INT-001–INT-020 | 20 |

**Total: 196 library entries + 1 router skill, 20 plugins.**

Recommended starting install: the router plus whichever domain packs match your work. Role skills reference SKL/INT IDs as *suggested* capabilities and integrations; install `role-library-capabilities` alongside any domain pack to resolve them.

## Install

Add this repository as a plugin marketplace, then install packs individually:

```
/plugin marketplace add <owner>/<repo>
/plugin install role-library-router
/plugin install role-library-music-audio
```

## How it works

1. Describe the task in plain English.
2. Run the router: `python3 <plugin-dir>/scripts/route.py "<task>" --top 3` (or let the `skill-router` skill do it).
3. Read the top result's skill file and adopt its Operating Contract for the work.
4. If the task is I3/I4 (reversible-with-authority / human-confirmed), the human gate is mandatory.

## Guardrails (from the library itself)

- The router selects contracts; it never grants authority, access, or permissions.
- Suggested integrations are named data sources, not permission grants.
- If no role scores meaningfully, say so — never force-fit a role onto a task.
- Abbreviations are stable IDs in artifacts and handoffs; use plain-English names in conversation.

## License

**Pending.** Licensing has not been decided. See `LICENSE and COMMERCIAL-LICENSE.md` — do not commercially redistribute until real license text ships.

## Provenance

Packaged 2026-09-22 from the Agentic AI Role Library source (131 role skills, 45 capability skills, 20 integration definitions, plus the natural-language router). Role and capability skill bodies are preserved verbatim; integration definitions are rendered from the library's canonical index. Validation results: see `VALIDATION.md`.
