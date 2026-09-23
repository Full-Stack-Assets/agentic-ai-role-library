---
name: skill-router
description: "Use when a natural-language task needs to be mapped to the right role skills, reusable capabilities, and integration definitions from the Agentic AI Role Library (202 entries). Turns plain-English intent into role+capability assemblies so no one has to memorize ID abbreviations."
---

# Skill Router (Natural-Language Activation)

Maps a natural-language request to the role skills (`CMM-07`, `CMA-12`, ...),
reusable capabilities (`SKL-001`..`SKL-051`), and integration definitions
(`INT-001`..`INT-020`) of the Agentic AI Role Library. Works across all installed role-library plugins; the router needs no domain pack installed to suggest one.

## Overview

The library's abbreviations are stable IDs, not a user interface. This router
is the natural-language interface: describe the task in plain English and it
returns the ranked role assemblies that apply, each with its operating contract
elements (mission, gate, handoff), suggested capabilities, and suggested
integrations. Nothing is installed or executed by the router — it only selects.

## When to Use

- Any substantive request where a role/capability assembly might improve the work.
- When the requester describes intent in plain English instead of skill IDs.
- Before delegating bounded work to a subagent or the browser task.

Do not route purely conversational or trivial requests; the library is for
bounded work with a gate, not for chit-chat.

## Procedure

1. Summarize the task in one sentence of natural language.
2. Run the matcher:
   `python3 <plugin-dir>/scripts/route.py "<task>" --top 3`
3. Read the top result's `SKILL.md` in the role directory it names.
4. Adopt that role's Operating Contract for the work: approved inputs, allowed
   work, required output schema, quality gate, handoff, and stop conditions.
   Layer in the suggested capabilities as narrow transformations.
5. If the task is an irreversible or externally-visible action (I3/I4
   permission baseline), the human gate is mandatory and cannot be waived.

## Guardrails

- The router selects contracts; it never grants authority, access, or permissions.
- Suggested integrations are named data sources, not permission grants.
- If no role scores meaningfully, say so — do not force-fit a role onto the task.
- Keep abbreviations as IDs in artifacts and handoffs; use plain-English names
  in conversation with the user.

## Required Output

The router prints ranked assemblies. For agent use, `--json` returns
machine-readable role IDs, capability IDs, integration IDs, gates, and handoffs.
