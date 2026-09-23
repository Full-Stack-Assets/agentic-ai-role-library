---
name: skl-050-guard-target-correctness
description: "Use when a workflow requires checking that a guard watches the RIGHT predicate, not merely that it can fail — particularly for QA, engineering, or governance roles writing or reviewing guards, checks, gates, or metrics."
---

# Guard Target-Correctness

**Skill ID:** `SKL-050`  
**Primary category:** Evaluation  
**Common role families:** QA, engineering, governance, MLOps.

## Overview

Proving a guard can fail (mutation-testing it) proves it is REACHABLE, not that it is CORRECT. Mutation harnesses are bounded by the mutations you declared. A guard passes both while being wrong whenever reality produces an input shape nobody enumerated — and that untested region is precisely the region you did not think of, which is exactly where the next incident comes from. This skill is the discipline for that gap: check that a guard watches the RIGHT predicate, not merely that it can fail. It is cheap, it is manual, and it is not replaceable by running the harness again. This is a narrow, independently testable capability. It must be installed inside a role contract that defines authority, approved sources, integrations, and human approval boundaries.

## When to Use

Use this capability when writing or reviewing any guard, check, gate, metric, or assertion — especially one written in response to an incident. Do not use it to smuggle broader decision rights or hidden tool access into a role.

## Operating Contract

| Element | Requirement |
|---|---|
| Inputs | The guard under review: its stated concept, its predicate as implemented, and (for the breadth arm) the live corpus it will police. |
| Transformation | Enumerates the equivalence class the concept covers, tabulates should-trip vs does-trip per member, and measures breadth over a pinned corpus — in both directions (too narrow, too wide). |
| Outputs | The equivalence-class table, disagreements fixed or recorded as accepted gaps, and the breadth measurement. |
| Non-goals | Final human approval, unscoped inference, silent source substitution, external action, or permission expansion. |
| Stop conditions | The concept cannot be stated; the predicate cannot be read; the corpus cannot be pinned for the breadth arm. |

## Procedure

### 1. Know the shape of the failure

A guard is almost always written **after** an incident, so it encodes the shape *that* incident had. The concept it is meant to protect is wider than the shape. The predicate silently becomes the narrow one. Then a value in the same conceptual class but a different literal shape arrives, the predicate says fine, and the guard reports green while the thing it exists to prevent happens.

> Worked miss: a counter tracked callers acting without a valid identity fence. The predicate was `value is None`. Production also produced `""` — and `"" is not None` is True, so every empty-string caller was counted as properly fenced. The guard was reachable and it was wrong. Worse: because `""` was accepted as an identity, two distinct callers sending `""` compared equal and were handed the same registration — a uniqueness invariant broken under a guard that reported clean.

> Worked miss: a scheduler compared model identity with exact string equality `observed != expected`. The environment tags models with a device-variant suffix, so `name` and `name-<device>` are the same model wearing different labels. Every reconciliation logged a divergence for two identical models — and the same equality test gated the "job is genuinely running" confirmation, so a variant-tagged job could never be confirmed and became eligible for eviction mid-task.

**And the obvious fix can be wrong too.** The first correction to the identity counter normalized `""` to `None` so the counter would tally it — fixing the *measurement* while leaving the *behavior* intact. The invalid fence was still accepted: fail-open. When you find a guard watching the wrong predicate, ask whether the right predicate should also *refuse* something, not just count it.

### 2. For each guard, in writing

1. **State the concept in one sentence.** Not the code — the thing you actually mean. "No caller may act without a unique identity." "A job that is really running must be confirmed."
2. **Write down the predicate as implemented.** The literal comparison. `x is None`. `a != b`. `count > 0`.
3. **Enumerate the equivalence class the concept covers.** Adversarially, and specifically include:
   - **falsy siblings** — `""`, `0`, `[]`, `{}`, false, whitespace-only
   - **aliases and normalizations** — case, suffixes, prefixes, tags, trailing separators, unicode forms
   - **absent vs empty vs default** — three distinct states that collapse into each other constantly
   - **the value equal to itself but shouldn't be** — two callers legitimately sending the same placeholder, and whether the identity check can tell them apart
   - **the type you did not expect** — a string where a number was assumed, and vice versa
4. **For each member, decide: should the guard trip? Does it?** Any row where those two disagree is a finding. This is a table, not a feeling.
5. **Check what the guard does on a trip.** Counting an invalid value is not rejecting it. If the concept says the input is invalid, something must refuse it, not merely tally it.

### 3. Check the other direction — a guard that is too WIDE

The mirror failure is the guard that flags everything: nobody deletes it — it is switched off *socially*. Its alerts get acknowledged on reflex, then batched, then ignored, and the end state is no guard at all. **A guard that never fires and a guard that always fires are the same defect: zero information.**

So: **measure the population before the invariant lands.** Run the candidate predicate over the live corpus it will police and read flagged/scanned before the guard ships. Pin the corpus in a manifest first, so the denominator cannot drift under the measurement; a predicate flagging more than a configured share of that pinned corpus (default: half) fails its own review. And breadth alone is not a pass — the review also names the labelled positives it checked, because a guard can be narrow and still wrong.

**Define ONE exit code as the flag.** "Nonzero means flagged" quietly counts crashes, usage errors, and timeouts as detections — and fails in the direction that looks like success: a checker crashing on exactly the file it was meant to detect reads as a narrow, accurate guard that caught its labelled positive. Every other nonzero, and any timeout, means the checker did not answer the question — so the breadth ratio measures nothing and the review is CANNOT CHECK, with the checker's own stderr retained per path.

### 4. When the field name lies

A guard reading a field with a stable name is not reading a stable meaning. A back-compat alias can keep a field's name identical while its semantics invert underneath — and every suite reading that field stays green through the inversion. **Assert on observable behavior, not on field presence or field name.** If a guard's evidence is "the field is there" or "the field is non-empty," it is watching a label, not a property. Related: a checker that searches for prose describing a rule can be satisfied by the prose *about* the rule rather than by the rule holding — check structure, not substrings.

## Verification checklist — before you call it done

- [ ] The concept is written in one sentence, separate from the code.
- [ ] The equivalence-class table exists, with a should-trip / does-trip column per row.
- [ ] Falsy siblings, aliases, and absent-vs-empty are each represented in the table.
- [ ] Every disagreement is either fixed or recorded as a known, accepted gap — not left implicit.
- [ ] Where the concept implies invalidity, something **rejects**; a counter alone is fail-open.
- [ ] The guard asserts on behavior, not on the presence of a named field.
- [ ] The candidate ran over the PINNED live corpus; flagged/scanned is recorded and under the configured ceiling (default: half the corpus).
- [ ] The review names the labelled positives it checked — breadth alone is not a pass.

## Guardrails

- The skill does not grant role authority or system access.
- Never infer authority from the capability name, model confidence, or connected system.
- Use the minimum data required and preserve originals, lineage, and reversible drafts.
- Separate verified evidence, inference, and unresolved uncertainty.
- High-consequence legal, clinical, financial, safety, privacy, employment, access, or public actions remain human-controlled.

## Required Output

```yaml
status: COMPLETE | NEEDS_REVIEW | BLOCKED | REJECTED
skill_id: "SKL-050"
work_item_id: "required"
input_refs: []
result:
  artifact_refs: []
  equivalence_table: []   # per member: should_trip, does_trip, finding
  breadth: {}             # flagged, scanned, ceiling, labelled positives checked
provenance:
  source_ids: []
  tools: []
  skill_version: "required"
uncertainties: []
```

## Provenance & License

- **Origin:** Third-party skill adapted from `guard-target-correctness` in [Agent-FleetOps](https://github.com/sherifican/Agent-FleetOps) by Micah P.G. (sherifican). This is NOT original library content.
- **License:** MIT — Copyright (c) 2026 Micah P.G. This skill remains MIT-licensed; it may not be relicensed as proprietary. Per the MIT terms, this copyright notice must be preserved in all copies. The full MIT license text is reproduced in `ADOPTED.md` at the library root.
- **Adaptation:** Rewritten into this library's capability format; the author's repo-relative guard paths (`guard/teeth_prover.py`, `guard/population_arm.py`) generalized to any guard under review. The worked failures are the original author's field evidence, kept because the failure *modes* transfer across setups. This skill carried explicit `license: MIT` frontmatter upstream; the assessment verifying this adoption is at `~/workspace/agent-fleetops-eval/ASSESSMENT.md`.
