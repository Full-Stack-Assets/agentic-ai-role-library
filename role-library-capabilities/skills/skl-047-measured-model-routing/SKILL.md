---
name: skl-047-measured-model-routing
description: "Use when a workflow requires routing tasks to the cheapest capable model from a living, evidence-cited routing table — particularly for orchestrators, MLOps, or multi-model dispatch."
---

# Measured Model Routing

**Skill ID:** `SKL-047`  
**Primary category:** Operations  
**Common role families:** Orchestrator, MLOps, AI evaluator.

## Overview

The orchestrator's job is to dispatch each task to the **cheapest model that can actually do it**, after guardrails. This skill consolidates scattered routing evidence into one decision procedure plus a LIVING routing table. Consult it before any non-trivial dispatch. Routing decisions are made against real measured capability on the operator's own setup — never vendor claims. This is a narrow, independently testable capability. It must be installed inside a role contract that defines authority, approved sources, integrations, and human approval boundaries.

## When to Use

Use this capability when a role dispatches work across multiple models or providers and the pick must be justified by measured evidence rather than habit. Do not use it to smuggle broader decision rights or hidden tool access into a role.

## Operating Contract

| Element | Requirement |
|---|---|
| Inputs | The task to dispatch, the current routing table (with evidence + dates), applicable project gates and guardrails. |
| Transformation | Classifies the task's dimensions, applies guardrails (which override the table), checks target capability health, and selects the cheapest capable model with its measured step-budget. |
| Outputs | Routing decision: chosen model + lane, step-budget, guardrail overrides applied, and the evidence cited. |
| Non-goals | Final human approval, unscoped inference, silent source substitution, external action, or permission expansion. |
| Stop conditions | No capable model available; guardrail conflict unresolved; routing table stale beyond its review horizon. |

## Procedure

### 1. Check the PROJECT GATE first

If a project is pinned to a lane set by operator policy (e.g. "thin margins; cloud legs only, no local first pass"), that gate OVERRIDES everything below. Encode such gates as step 0, not as a footnote in a table row — a subtly-wrong harness on a thin-margin project yields plausible numbers that gate real decisions.

### 2. Delegate-first default

Even minor/quick task-steps go to the cheapest capable lane FIRST, then evaluate and revise/correct. "Fast to do myself" is not a license to skip delegation. Orchestrator-direct is reserved for true orchestration/governance: sequencing, writing the dispatch brief, verifying reports, integration/wiring, memory/skill writes, operator comms. Everything else — code, audit, tests, boilerplate, grep-heavy digging, drafts, condensing, routine analysis — dispatch, don't hand-do.

### 3. Classify the task's dimensions

What is it really? Code generation / code audit / agentic coding / tool-call chains / web research / convergent analysis / reasoning-heavy / long-session / visual / media / simple-cheap. A task can be multi-dimension — split it.

### 4. Apply the GUARDRAILS — they OVERRIDE the table

- **Project economics:** thin-margin work stays on its pinned lanes regardless of capability rank.
- **Content/policy routing:** some model families decline or skew certain content categories — route that lane to a family known to handle it, regardless of capability rank.
- **Confabulation-prone legs:** if a leg's documented risk is confabulating specifics or overclaiming, verify its facts and externally verify every deliverable — and never hand it a premise: ask "how many?" not "list all six."
- **Stated context window ≠ orchestration ceiling:** models degrade before their max. Keep window-limited legs to bounded slices; never hand a window-limited leg the full corpus in a multi-leg reconcile.
- **Co-hosting:** models too large for one device run sequentially; small models can run concurrently.
- **Device availability (occupancy, not just fit):** before dispatching to a local model, check the device is actually FREE. If a long job is running, local dispatch is blocked — queue it or route the interim to a cloud leg.
- **Context budget:** a discipline prepend plus data/doc files plus accumulating tool output can overflow a small default context window — raise the window or trim the prepend; never let blind front-truncation silently eat the prompt.
- **Step-budget:** curate the dispatch to the model's MEASURED step budget; when the task exceeds it, decompose or route up. Re-measure after head-to-heads — a budget inherited from an old eval may belong to a reassigned model.
- **Token-cost = paid legs only:** token-spend applies to cloud legs; local generation optimizes quality and context-space, never token-frugality.
- **Effort-bump gate:** each lane has a STANDING effort level; a per-task bump above standing is operator-gated — flag it before applying, never self-escalate. Do not escalate for routine implementation, mechanical refactors, docs, or design polish — the benefit there is unestablished.
- **Whole-file edit verification:** a whole-file local edit can silently truncate (exit 0, functions dropped, no warning). After any whole-file local edit, diff line count and symbol inventory against the pre-edit file; prefer read-only context plus a targeted spec over whole-file rewrites past a few hundred lines.
- **Sizing = headroom over maximum fit:** do not promote the largest model that fits; the metric is quality per unit of resource with context headroom left. Keep new-hardware routing rows unpromoted until real throughput is measured on the actual box.
- **A failure report is not a failure:** a leg reporting failure is as unverified as one reporting success — check the artifact before believing either.
- **Honesty:** honesty-enforce dispatched work; verify deliverables, never trust a self-report.
- **Test before adopting** a new backbone; match the eval instrument to the model's design.

### 5. Look up the ROUTING TABLE — then pre-flight the target

Pick the model and note its measured step-budget; if the task exceeds the budget, decompose or route up. Before dispatching — especially to an on-demand or network endpoint — run the read-only health check: the target must report available, or route to the table's Alt. Use the health check at session start, before network/on-demand/cloud routing, and as the first diagnostic when a dispatch errors ("is the capability even up?" before deeper debugging).

### 6. Cheapest-capable wins; cloud legs delegate DOWN

Don't send premium what cheap handles; reserve premium legs for one-shot polished artifacts. A cloud orchestrator/worker decomposes and hands local-sized sub-tasks to local models; the cloud keeps only the hard/long parts. Paid quota is for escalation, not routine legwork.

## The routing table — living, evidence-cited, negative results kept

Each row cites its evidence + a date. Example rows show the shape — replace with the operator's own roster, measured on their own setup:

| Task dimension | Primary | Alt / notes | Evidence |
|---|---|---|---|
| **Code generation** | mid-tier local coding model | best generator in a head-to-head on real project tasks. Gotcha: dispatch via the alias the agent framework recognizes, not the raw model-ID string | coding-lane eval + date |
| **Code audit / review leg** | best model on the fastest capable device | thinking stays ON for audits; disabling it is the measured FALLBACK only. Re-derive the pick when hardware or roster changes; never pin a model name as standing policy | audit-lane head-to-head + date |
| **Tool-call-heavy chains** | mid-tier local MoE | perfect at every chain length tested. ⚠ a small local instruct model is NOT a safe unassisted chain-driver — deterministically wrong arithmetic at 12 calls (3/3 runs); its "beats every larger model" result was WITH a harness retry layer | head-to-head + date |
| **Reasoning-heavy / hard delegated work** | cloud frontier model | **escalation leg, NOT default** — local first to conserve paid quota; decompose and escalate only the hardest parts | eval + date |
| **Local research synthesis** | ⚠ small local model — **NOT adopted** | transcript-only trial clean (5/5) but the live-evidence trial FAILED (confabulated fake sources). Row stays to record the negative result + the retry precondition | trial notes + date |

Conventions: a row can carry a ⚠ warning; a negative result stays in the table (marked NOT adopted) so the failure isn't re-tried blindly; superseded rows get marked, not silently deleted.

### Serving path is a routing fact

A table cell naming a port or endpoint is not evidence of which server answers on it. Before attributing any result to a known upstream defect, establish which binary/port/process actually served it. Do not cite a changelog entry as a reason to re-open a model's ranking — test it on YOUR path.

### Score the outcome, not the mechanism

When head-to-heading models, score the end artifact against known ground truth, not the steps taken (see SKL-046: a model can use the exact minimum call count with zero malformed calls and still submit the wrong total — the differentiator was arithmetic, not tool-calling). Make the answer unguessable so subjects cannot skip the work and still score.

### Intra-task topology — the edge-advisor sandwich (10/80/10)

The table picks a model PER TASK; the complementary INTRA-task pattern for a single hard task: put the strong model on the EDGES, the cheap one in the MIDDLE. (1) The strong model writes the plan + success test + risks + verification rubric (first ~10%). (2) A cheap/local worker executes the bounded middle (~80%). (3) A strong model AUDITS the output against that plan for false confidence, missed constraints, hidden assumptions (last ~10%). Optional advisor consult: mid-task the cheap executor asks the strong model ONE short bounded question instead of escalating the whole task. Pay top rates only where intelligence moves the needle — the plan and the review — not the mechanical middle.

## Refresh protocol — how the table evolves

The table is LIVING; stale routing = bad dispatches. Refresh it:
- **REACTIVELY** — after any model eval, bake-off, or new-model trial, update the affected rows + bump the evidence + date.
- **PERIODICALLY** — at each curation checkpoint, scan the findings ledger and recent eval notes for new model findings and reconcile the table. Piggyback on an existing checkpoint — no new hook needed.
- Keep every row's evidence pointer current so staleness is visible at a glance.

## Propagation

Canonical copy lives with the top orchestrator. Summarize the table + guardrails into the dispatch headers/onboarding files of the other agents that delegate down, so every orchestrator routes consistently; re-propagate after each refresh. If a wrapper prepends a different copy than the canonical one, update BOTH — the first propagation is also when you discover the headers had no routing summary at all.

## Guardrails

- The skill does not grant role authority or system access.
- Never infer authority from the capability name, model confidence, or connected system.
- Use the minimum data required and preserve originals, lineage, and reversible drafts.
- Separate verified evidence, inference, and unresolved uncertainty.
- High-consequence legal, clinical, financial, safety, privacy, employment, access, or public actions remain human-controlled.

## Required Output

```yaml
status: COMPLETE | NEEDS_REVIEW | BLOCKED | REJECTED
skill_id: "SKL-047"
work_item_id: "required"
input_refs: []
result:
  artifact_refs: []
  routing: []         # per task: dimension, chosen model + lane, step-budget, evidence cited
  guardrail_overrides: []
provenance:
  source_ids: []
  tools: []
  skill_version: "required"
uncertainties: []
```

## Provenance & License

- **Origin:** Third-party skill adapted from `model-routing-table` in [Agent-FleetOps](https://github.com/sherifican/Agent-FleetOps) by Micah P.G. (sherifican). This is NOT original library content.
- **License:** MIT — Copyright (c) 2026 Micah P.G. This skill remains MIT-licensed; it may not be relicensed as proprietary. Per the MIT terms, this copyright notice must be preserved in all copies. The full MIT license text is reproduced in `ADOPTED.md` at the library root.
- **Adaptation:** Rewritten into this library's capability format; the author's host-specific hardware, model names, and ports generalized to lanes. The worked failures are the original author's field evidence, kept because the failure *modes* transfer across setups. The repo-level MIT `LICENSE` in Agent-FleetOps covers this skill (it carries no per-file license line); the assessment verifying this adoption is at `~/workspace/agent-fleetops-eval/ASSESSMENT.md`.
