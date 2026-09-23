---
name: skl-051-generate-review-fix-loop
description: "Use when a workflow requires improving a non-trivial code change through separate generation, review, and repair stages — particularly for engineering or MLOps roles."
---

# Generate → Review → Fix Loop

**Skill ID:** `SKL-051`  
**Primary category:** Evaluation  
**Common role families:** Engineering, MLOps, QA.

## Overview

For non-trivial implementation work, use three distinct stages: a coding model drafts, an independent audit model compares the draft with the contract, and the coding model revises from that review. This reduces the chance that a single model overlooks its own edge cases; it does not replace a real test. This is a narrow, independently testable capability. It must be installed inside a role contract that defines authority, approved sources, integrations, and human approval boundaries.

## When to Use

Use this capability for non-trivial code changes where a second, independent pair of eyes materially reduces defect risk. Do not spend the multi-stage process on a trivial one-line edit when direct verification is cheaper. Do not use it to smuggle broader decision rights or hidden tool access into a role.

## Operating Contract

| Element | Requirement |
|---|---|
| Inputs | The full task contract, relevant code, constraints, and expected verification. |
| Transformation | Three stages — generate (draft), review (independent audit against the contract), fix (revise from review) — with findings labeled CONFIRMED or SUSPECTED and the final revision functionally tested. |
| Outputs | The final revised result, the preserved review, and the labeled findings with their disposition. |
| Non-goals | Final human approval, unscoped inference, silent source substitution, external action, or permission expansion. |
| Stop conditions | No independent reviewer available; review findings cannot be confirmed or shown red by a test; the change is trivial enough that direct verification is cheaper. |

## Procedure

1. **Generate.** Give the generator the full task contract, relevant code, constraints, and expected verification.
2. **Review.** Give a DIFFERENT reviewer the task contract and the generated diff. Ask for concrete defects, missing cases, and unsupported assumptions. For each finding, state what must be true on that path after the repair, not only the symptom. Mark each finding `CONFIRMED` only if the reviewer executed the case and recorded observed values; otherwise `SUSPECTED` (reasoned only, including could-not-execute). Keep suspected findings in the review; do not apply them as repairs until confirmed or shown red by a test.
3. **Fix.** Give the generator the review and require a revised final result. Preserve the review and the final output. Repair only concrete defects, missing cases, and unsupported assumptions. Record and leave unapplied findings that are only style or idiom. A same-file fact the change alters remains in scope.
4. **Test.** Functionally test the final result in the repository before reporting it as verified.

### Role selection

- Use a coding-oriented local model for draft and repair.
- Use a distinct audit-oriented model for review; **do not have the generator self-review as the only gate.**
- Prefer a more thorough reviewer for high-risk or edge-case-dense changes.

### Pitfalls

- Shipping the draft rather than the repaired output.
- Treating review as proof of runtime behavior.
- Spending the multi-stage process on a trivial one-line edit when direct verification is cheaper.
- Reviewing only the diff when the change alters a fact the same file asserts elsewhere. The reviewer's unit is then the file, and the search covers the old value and the subject's constraint language, not the old value alone.

## Verification checklist

- [ ] Generator and reviewer were separate roles.
- [ ] The repair addressed the review rather than merely restating it.
- [ ] The final revision, not an earlier draft, was tested.
- [ ] Every finding carried its `CONFIRMED`/`SUSPECTED` label, and each unapplied finding was recorded as either style/idiom only, or `SUSPECTED` and not yet confirmed or shown red by a test.

## Guardrails

- The skill does not grant role authority or system access.
- Never infer authority from the capability name, model confidence, or connected system.
- Use the minimum data required and preserve originals, lineage, and reversible drafts.
- Separate verified evidence, inference, and unresolved uncertainty.
- High-consequence legal, clinical, financial, safety, privacy, employment, access, or public actions remain human-controlled.

## Required Output

```yaml
status: COMPLETE | NEEDS_REVIEW | BLOCKED | REJECTED
skill_id: "SKL-051"
work_item_id: "required"
input_refs: []
result:
  artifact_refs: []
  findings: []        # each: CONFIRMED | SUSPECTED, with disposition
  final_revision: "ref to the tested revision"
provenance:
  source_ids: []
  tools: []
  skill_version: "required"
uncertainties: []
```

## Provenance & License

- **Origin:** Third-party skill adapted from `generate-review-fix-loop` in [Agent-FleetOps](https://github.com/sherifican/Agent-FleetOps) by Micah P.G. (sherifican). This is NOT original library content.
- **License:** MIT — Copyright (c) 2026 Micah P.G. This skill remains MIT-licensed; it may not be relicensed as proprietary. Per the MIT terms, this copyright notice must be preserved in all copies. The full MIT license text is reproduced in `ADOPTED.md` at the library root.
- **Adaptation:** Rewritten into this library's capability format with the Operating Contract, Guardrails, and Required Output sections this library requires; the author's local-lane model selections generalized to any coding/audit model pair. This skill carried explicit `license: MIT` frontmatter upstream; the assessment verifying this adoption is at `~/workspace/agent-fleetops-eval/ASSESSMENT.md`.
