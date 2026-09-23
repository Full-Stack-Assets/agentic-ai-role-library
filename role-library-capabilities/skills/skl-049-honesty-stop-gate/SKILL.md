---
name: skl-049-honesty-stop-gate
description: "Use when a workflow requires wiring an honesty stop gate into an agent's stack — particularly for orchestrators, automation, or any role whose turns assert live state."
---

# Honesty Stop Gate

**Skill ID:** `SKL-049`  
**Primary category:** Safety  
**Common role families:** Orchestrator, automation, MLOps, engineering.

## Overview

An honesty stop gate is a turn-end hook that blocks a turn asserting **live state it never measured** — "the deploy is still running," "the build passed," "no commits landed" — when no observation backs the claim. The mechanism is simple and fixed: the gate confirms a probe RAN and named the subject; it does not read the probe's output. This skill is the adaptation procedure: wiring the gate into the operator's own stack so it actually fires on their vocabulary, their subjects, and their probes. The danger in this job is **building a stair to nowhere**: a check that reads as coverage and verifies nothing, because it points at a command the system does not have, or one that cannot fail. This is a narrow, independently testable capability. It must be installed inside a role contract that defines authority, approved sources, integrations, and human approval boundaries.

## When to Use

Use this capability when an agent's turns make claims about live, changing state (background jobs, builds, deploys, services, other agents) and those claims need to be backed by an observed probe before the turn ends. If the agent launches nothing in the background and works synchronously — its output is always in the transcript — say so and do NOT ship a running-claim gate: there are no subjects to guard, and an empty subject list is a degenerate config. Do not manufacture subjects to have something to configure. Do not use it to smuggle broader decision rights or hidden tool access into a role.

## Operating Contract

| Element | Requirement |
|---|---|
| Inputs | The agent stack's hook contract, the subjects the agent claims state about, candidate verification commands, and the gate implementation to wire. |
| Transformation | Maps the gate's config to verified facts about this system (subjects, real probes, claim phrasing), confirms the harness fires the hook, and proves the gate can fail end-to-end. |
| Outputs | Working gate config, the harness diff, the self-test result, and the end-to-end teeth result (a real unbacked claim blocked, a real backed claim passed). |
| Non-goals | Final human approval, unscoped inference, silent source substitution, external action, or permission expansion. |
| Stop conditions | No real verification command exists (gate cannot function); the harness does not fire the hook; required facts cannot be determined without reading private data. |

## Procedure

### 1. Verify everything you can — before writing it into config

Anything checkable about the system, check — before it goes into config, not after. A command goes into the verification list only after its binary is confirmed to resolve on this box.

### 2. Ask about anything you cannot

When you cannot determine how jobs are named, which command observes a service's state, or whether the harness even fires stop hooks, ASK — one concrete question with your best guess offered. Do not invent an answer.

### 3. Keep private things private

Do not read secrets, credential files, `.env` files, tokens, or private data to infer configuration. This includes conversation transcripts, logs, and history — they are a tempting source for "how does this agent phrase claims" and they routinely contain private data. You need command names and subject vocabulary, not file *contents*; get those by asking for representative phrasings, or from non-secret places (process lists, service names, public scripts). If configuring correctly seems to require reading a private file or a past transcript, that is a signal to ASK, not to read.

### 4. No stair to nowhere

Every verification command must be a real, existing command that can fail. An unconditional `echo`, a bare `&`, a file-existence read (`ls`, `stat`), or a log read (`cat`/`tail` a `.log`) does not observe liveness and verifies nothing. Enforce the existence half mechanically (binary resolves); enforce the observes-liveness half by listing only process/service probes for running-claims.

### 5. Discover the SUBJECTS — what live things does this agent claim state about?

Ask, or infer from what is safely visible: what does this agent launch and then report on? Background jobs, CI runs, deploys, services, containers, other agents, long builds. Prefer distinct single tokens (a service name) over generic compounds — "build" and "job" as separate subjects make "build job" demand both be verified. If there is a naming convention (e.g. logs named `<subject>_run.log`), note it.

### 6. Discover and VERIFY the verification commands — the critical step

For each way the agent could observe live state, find the actual command: process supervisor status, container/orchestration queries, process table, the job runner's own status command, real health endpoints. It must *observe* state (able to return "not running"), not always succeed. A candidate that fails the existence check is dropped, and the operator is told it was dropped and why — silent omission reads as "covered everything." If, after dropping unresolved commands, the verification list would be empty, STOP: the gate cannot function without at least one real probe — surface the gap rather than shipping a gate that can never verify. Do not proceed past a red config check.

### 7. Write the claim patterns conservatively

Cover how *this* agent phrases live-state claims (keep both running-type and completion-type families). When unsure whether a phrase is a claim, leave it in — a false block is recoverable (run the check, delete, or label); a missed claim is the silent failure the gate exists to prevent. But do not add a pattern so broad it matches ordinary prose every turn — an always-firing gate gets disabled, which is the same as no guard at all (see SKL-050).

### 8. Confirm the harness will actually run the hook

The hook contract typically requires: the harness (a) invokes stop hooks, (b) passes the turn's transcript path, and (c) honors a block decision. If any of those is untrue, the hook silently no-ops and the install *reads as done while the gate never fires*. Confirm all three, or ASK. Show the exact settings diff and back up the settings file before writing; add only the hook entry — do not modify settings you were not asked to.

### 9. Prove it can fail END-TO-END, on this box, with the operator's own config

Three acceptance checks, all required:

1. The **config check** is green under the operator's config (every verification command's binary confirmed present).
2. The **self-test** is green (the mechanism itself is intact). These check different things: the config check validates the operator's vocabulary and probes; the self-test runs built-in fixtures. Do not read a self-test result as evidence about the operator's config.
3. **A real trigger with a real subject.** The self-test does not prove the harness fires the hook or that the subjects/commands work. Drive the hook the way the harness does: build a tiny transcript naming one of the operator's subjects with an unbacked claim, and confirm the hook emits a block decision. Then add a line running one of the operator's real verification commands naming that subject before the claim, and confirm it goes silent. **A gate you have not watched block a real unbacked claim and pass a real backed one on this machine is not yet trusted** — no guard without a proof it can fail.

### 10. Report what you wired and what you skipped

Tell the operator, in plain terms: the subjects configured, the verification commands confirmed to exist (and any dropped and why), the harness-support facts confirmed or the questions still open, and the self-test / end-to-end teeth result. Unanswered questions make the config provisional — say so; do not present it as done.

## Guardrails

- The skill does not grant role authority or system access.
- Never infer authority from the capability name, model confidence, or connected system.
- Use the minimum data required and preserve originals, lineage, and reversible drafts.
- Separate verified evidence, inference, and unresolved uncertainty.
- High-consequence legal, clinical, financial, safety, privacy, employment, access, or public actions remain human-controlled.

## Required Output

```yaml
status: COMPLETE | NEEDS_REVIEW | BLOCKED | REJECTED
skill_id: "SKL-049"
work_item_id: "required"
input_refs: []
result:
  artifact_refs: []     # gate config, harness diff, test transcripts
  subjects: []
  verification_commands: []   # confirmed present
  dropped_commands: []         # with reasons
  teeth_result: "blocked unbacked claim + passed backed claim | FAILED"
provenance:
  source_ids: []
  tools: []
  skill_version: "required"
uncertainties: []
```

## Provenance & License

- **Origin:** Third-party skill adapted from `honesty-stop-gate` in [Agent-FleetOps](https://github.com/sherifican/Agent-FleetOps) by Micah P.G. (sherifican). This is NOT original library content. The reference implementation (`guard/honesty_stop_gate.py` in that repo) is the mechanism this procedure adapts; the mechanism itself was NOT copied into this library.
- **License:** MIT — Copyright (c) 2026 Micah P.G. This skill remains MIT-licensed; it may not be relicensed as proprietary. Per the MIT terms, this copyright notice must be preserved in all copies. The full MIT license text is reproduced in `ADOPTED.md` at the library root.
- **Adaptation:** Rewritten into this library's capability format; repo-relative paths and the author's harness specifics generalized to any agent stack with a stop-hook contract. This skill carried explicit `license: MIT` frontmatter upstream; the assessment verifying this adoption is at `~/workspace/agent-fleetops-eval/ASSESSMENT.md`.
