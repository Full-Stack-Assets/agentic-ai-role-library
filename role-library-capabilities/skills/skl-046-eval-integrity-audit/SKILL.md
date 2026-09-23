---
name: skl-046-eval-integrity-audit
description: "Use when a workflow requires auditing a test, benchmark, or evaluation BEFORE trusting its result — particularly for QA, MLOps, or any role presenting measured results."
---

# Eval Integrity Audit

**Skill ID:** `SKL-046`  
**Primary category:** Evaluation  
**Common role families:** QA, MLOps, AI evaluator, engineering.

## Overview

A test, benchmark, or eval is the instrument you make decisions with. A miscalibrated instrument doesn't just give a wrong number — it gives a **confident** wrong number, and you ship the decision on it. The audit is cheap; the wrong decision is not. **Run this audit before running ANY test you built, and before presenting its results.** Skimming this step is the single highest-leverage way to be confidently wrong. This is a narrow, independently testable capability. It must be installed inside a role contract that defines authority, approved sources, integrations, and human approval boundaries.

## When to Use

Use this capability when a role needs to validate an evaluation instrument before trusting its output — and when presenting results to a human, where an unaudited number reads as evidence. Do not use it to smuggle broader decision rights or hidden tool access into a role.

## Operating Contract

| Element | Requirement |
|---|---|
| Inputs | The test/benchmark/eval to be audited: its inputs, ground truth, scorer, and the claim its result will support. |
| Transformation | Audits the instrument against rendered/executed reality using the cardinal rules below; returns a verdict of TRUSTED, READING-DEPENDENT, or NOT EVALUATED per claim. |
| Outputs | Audit verdict per claim, the specific rules checked, failures found, and what was re-verified. |
| Non-goals | Final human approval, unscoped inference, silent source substitution, external action, or permission expansion. |
| Stop conditions | Instrument cannot be audited (no access to inputs/scorer); a rule violation is found and cannot be repaired; the bar is reading-dependent. |

## Procedure

### 1. Verify against RENDERED/EXECUTED reality, not intent

Your spec is NOT the artifact. Tools transform inputs silently: chart libraries sort categories, templates fill defaults, quantization changes behavior, endpoints sleep. Before running, **render and eyeball every test input, print every ground-truth label, and read every generated prompt** — then confirm they are what you think. Never trust the spec over the produced artifact.

> Worked miss: an evaluator eyeballed 4 defect charts but skipped the "clean control." The charting library had reordered its months, so the control carried a real defect; 4 models correctly flagged it and were scored wrong. Eyeballing the control would have caught it in 5 seconds.

### 2. The CONTROL is sacred — audit it hardest

The control is the most important single data point: it calibrates true-negative vs false-positive. If the "clean" case isn't actually clean, you cannot interpret ANY result — a wrong control silently inverts conclusions. Verify the control by direct inspection **every time**, before anything else.

### 3. Run the ANCHOR before the population

Before a new instrument touches the real population, make it reproduce a **known-answer anchor** and STOP if it does not. The anchor catches design flaws, not just coding bugs: it can invalidate a whole method whose logic looked sound on paper.

> Worked case: a residual-energy metric gated on the one section where the answer was known read 0.914 against 0.154 for the working metric — the metric had **no discriminative power at all**; the band was occupied regardless. Nothing in the method's description revealed this; only the anchor did.

**When the anchor fails, DIAGNOSE — never loosen the gate.** A gate you relax on failure is not a gate.

### 4. An AGGREGATE anchor is only valid on the population it was measured on

A per-item anchor is valid at any sample size only if the per-item quantity is reproducible. An aggregate anchor (does the corpus-wide rate reproduce?) is **not** — run it on a subset and a perfectly healthy harness fails, because the expectation was never about that population.

**Rules:** (1) When a gate cannot be evaluated, say NOT EVALUATED — never PASSED, never a widened tolerance. Widening the band to make subsets "pass" converts a false alarm into a false all-clear. (2) Keep the per-item gate running at every size.

### 5. Across runs with different INPUTS, compare DELTAS — never LEVELS

Two runs are comparable only if they saw the same inputs. Change the input and you change the matched-item set, hence the denominator, hence every accuracy LEVEL — while the metric keeps its name. Before subtracting two numbers, confirm they were computed over the SAME item set — quote **n** next to every level, always. Carry **arm DELTAS** across runs, never levels.

### 6. Compute the metric WITHIN each group before you pool

A discriminator scored over pooled groups (videos, songs, sessions) can earn its score from *which group an item came from*, not the property you meant to measure. The tell is arithmetic and cheap: **pooled > every within-group value.** Always report per-group values beside the pooled one; if pooled exceeds every within-group value, the metric is partly answering *which group is this* — name it before acting on it.

### 7. Judge a predictor on its OUTPUT, not its correlation

A calibration that asks only "does the feature correlate?" can green-light a predictor whose recommendation never changes. A classifier emitting one class has zero discriminating power at any correlation. Before any calibration gate prints USABLE: (1) **OUTPUT VARIANCE** — does the recommendation actually differ across the set? (2) **TIE INSPECTION** — read the outcomes of items that tie on the feature; (3) **n-AWARENESS** — quote the p-value/CI beside any rank correlation at small n. **A gate that checks correlation but not output variance has the same zero-information defect it was written to detect.**

### 8. A file with the RIGHT NAME can hold the WRONG CONTENT

Before an experiment whose inputs come from a vendored artifact, **verify the artifact by hash against the source of truth**, not its filename or directory. Ask for hashes of weights/sidecars too, not just source — they are the part that silently changes behavior.

### 9. Score the OUTCOME, not the mechanism

Score the end artifact against known ground truth, not the steps taken to produce it. When every subject aces the mechanism, that is a signal the mechanism is no longer the bottleneck — go find what is, don't declare a tie.

### 10. When subjects disagree with you, suspect YOURSELF first

**Consensus disagreement = a test bug until proven otherwise.** If N independent subjects all "fail" a case or all flag your "clean" control, STOP and re-verify the test before concluding anything about the subjects. Be equally skeptical of a result you WANT — motivated reasoning cuts both ways; audit a flattering result just as hard.

### 11. The scorer must not be gameable

Adversarially test your auto-scorer against a KNOWN-WRONG output before trusting it. If a wrong answer can score right, fix the scorer, not the conclusion. **And a FIX's success metric must be able to FALL when the fix gets worse.** When a fix's own success metric can rise while the fix gets worse, that metric is the bug.

### 12. A CLEAN / "nothing found" verdict is unproven until the detector has gone RED on a known positive

A scan, gate, or regression test that has only ever returned clean proves nothing: a working detector and a broken one produce byte-identical output. Before you trust any negative, feed it a **known positive** and confirm it fails.

> Worked miss: a secret-scan regex `sk-[a-zA-Z0-9]{16,}` returned clean — but the planted fixture `sk-prod-…` never matches, because the character class breaks at the hyphen. Caught only because the fixture was already known to be there.

**Never report "clean" / "no leaks" / "no regressions" from a pattern, query, or gate whose failure path you have not observed this session.** Prefer the fixture live in the repo so the validation re-runs.

### 13. Match 1:1, not nearest-neighbor

When scoring detections against a reference by proximity, use 1:1 greedy/bipartite matching — each reference item matched at most once. Many-to-one double-credits duplicates: two detections on one real event both score "real," inflating hits and undercounting false positives. A second detection on an already-matched item MUST count as a false positive.

### 14. Report the single-feature baseline beside any FUSED number

Fusion often DILUTES: a fused score is frequently worse than the strongest single feature alone. Always report the best single-feature baseline next to the fused number. Default assumption on any "combine these signals" proposal: it dilutes until proven otherwise.

### 15. Disaggregate before naming the CAUSE of an aggregate loss

An aggregate is a symptom, not a diagnosis. Before attributing it, break it down along the dimension whose SIGNATURE would confirm/refute that cause — and check the signature actually holds. Name a cause only after its signature survives the disaggregation.

### 16. Keep conditions fair and equal across subjects

Control for chain-of-thought leaks into format checks, slept endpoints, stale/warm loads BEFORE the run. **And a probe must replicate the SUBJECT'S OWN resilience** — a harness that omits the retries, warm-ups, timeouts, or fallbacks the real caller has is not a faster version of production; it is a different program. Import the call path — do not copy it. A copy of a call path is a fork with no merge.

### 17. A FIDELITY CLAIM is a critical assertion nobody tests

A comment asserting an instrument "mirrors / replicates the real X" is a testable proposition — and worse than no comment, because it actively discourages the check. Ask the fidelity question explicitly, and prove refactors equivalent by loading the OLD code (e.g. from git), never by hand-copying it. Then mutation-check the equivalence proof itself: an equivalence test that passes when nothing changed is indistinguishable from one that always passes.

### 18. Compare at MATCHED operating points; calibrate OFF the eval set

Sweep BOTH sides, quote the fair matched-shift delta, never the candidate-only lift. And never pick the "optimal" threshold on the same eval set you report on — calibrate on an independent set.

### 19. The BAR is part of the instrument

Enumerate and score every defensible READING of a pass/fail bar — the reading your stated target implies is BINDING. Convert a %-bar into item units before trusting a verdict near it (margin under one item = "not provable at this n," never PASS). "Pre-registered" is a property of the AUDIT TRAIL, not intent: a threshold whose first committed appearance sits in the same commit as a favorable result is not pre-registered in any checkable sense.

### 20. Every budget inside the HARNESS is a constant of the comparison

A budget, cap, or keep-count keyed on an arm's own output gives each arm a different budget — the composition defect relocates from the product into the instrument. The shape only bites when the arm under test can move the count. When reporting absolute counts across arms, state the shared denominator explicitly.

### 21. Don't score the lane you FIT the registration to

If you align/register signals by maximizing agreement on lane X, lane X's score is optimistically biased. Fit the registration on a lane you are NOT scoring, name every parameter you fit and the lane you fit it on, or flag that lane's number as fit-biased.

### 22. Judge the WORDING, not just catch/miss

For quality-sensitive evals, binary pass/fail hides the real signal. Capture the raw outputs and judge completeness, precision, wording — the auto-score is advisory; the raw output is the truth.

### 23. Validate a COST optimization on OUTPUT EQUIVALENCE

When a change buys speed/cost with no quality change, the metric is byte-level agreement with the incumbent's output. Every speed arm reports an equivalence result beside its speedup; a non-identical output is a FAILURE until argued otherwise. Before capping a resource, confirm it is the one being consumed.

### 24. If a swept parameter OUGHT to be monotone, assert that it IS

A larger budget must be a superset of a smaller one. Name the monotonicity before sweeping; a violation has exactly two explanations — a coupled/unstable instrument or too small an n — and both invalidate the sweep. Never report the peak of a non-monotone curve.

### 25. On a guard failure, read the FIXTURE before the code

Twice in practice the code was right and the fixture did not test what its author believed. State what the fixture is supposed to exercise and check the input actually has that property and only that property. This is not permission to blame the test — the honest verdict is often *both*.

### 26. A PASSING TEST can be pinning the DEFECT

When you fix a defect, search the suite for tests asserting the OLD behavior and update them deliberately, in the same commit as the fix. A green test protects whatever it asserts, including the bug — it converts the eventual fix into an apparent regression. Name the tests the search returned; "no test asserts the old behavior" is a finding you state, not an absence you assume.

### 27. Re-test on the FULL population before globalizing a change from a SELECTED sample

A favorable result on material selected because the change helps there is a selection artifact, not evidence for a global change. Re-measure on the full, unselected population before shipping a blanket change.

### 28. Ground truth by hand

Every expected answer / pass-criterion is verified against the ACTUAL artifact by a careful check — never assumed from the intended value. Generating the data does not exempt you from checking the render.

## Pre-flight checklist — run before EVERY test

- [ ] Rendered/executed every test input and EYEBALLED it — especially the control.
- [ ] The control is genuinely clean/correct, verified by inspection (not assumption).
- [ ] Every ground-truth label checked against the actual artifact.
- [ ] The scorer cannot pass a KNOWN-WRONG output (adversarially checked).
- [ ] Any detector whose result is "clean / nothing found" has gone RED on a known positive — this session.
- [ ] Every guard and measurement probe IMPORTS the shipping module it protects/measures and exercises the SHIPPING entry point.
- [ ] Any comment claiming an instrument MIRRORS production was VERIFIED this session, or the claim deleted.
- [ ] Conditions fair + equal across subjects (no chain-of-thought leak, no slept endpoint, matched loads).
- [ ] Numbers compared across runs were computed over the SAME item set (n quoted); cross-run comparisons carry DELTAS, not levels.
- [ ] Grouped-corpus metrics reported PER GROUP as well as pooled.
- [ ] Correlation-cleared gates also checked for OUTPUT VARIANCE, ties, and n.
- [ ] Speed/cost arms checked for OUTPUT EQUIVALENCE against the incumbent.
- [ ] Swept parameters with expected monotonicity were ASSERTED monotone.
- [ ] Comparisons at MATCHED operating points; thresholds calibrated on an INDEPENDENT set.
- [ ] No reported lane was used to FIT a registration offset.
- [ ] The BAR: every defensible reading enumerated + scored (target-implied reading binds); %-bar converted to item units (margin ≥ 1 item, else "not provable"); threshold's commit provably predates the result.
- [ ] Harness budgets are constants of the comparison, not derived from the arm under test; shared denominators stated.
- [ ] Fix-validation metrics checked for direction: they must be able to FALL if the fix is wrong.
- [ ] On a FIX: suite searched for tests asserting OLD behavior; each found updated deliberately in the same commit.
- [ ] Quality evals: raw outputs captured for human judgment, not just a binary.
- [ ] Subject-consensus contradicting GT → re-audit the test; do NOT blame the subjects.

## Guardrails

- The skill does not grant role authority or system access.
- Never infer authority from the capability name, model confidence, or connected system.
- Use the minimum data required and preserve originals, lineage, and reversible drafts.
- Separate verified evidence, inference, and unresolved uncertainty.
- High-consequence legal, clinical, financial, safety, privacy, employment, access, or public actions remain human-controlled.

## Required Output

```yaml
status: COMPLETE | NEEDS_REVIEW | BLOCKED | REJECTED
skill_id: "SKL-046"
work_item_id: "required"
input_refs: []
result:
  artifact_refs: []
  verdicts: []        # per-claim: TRUSTED | READING-DEPENDENT | NOT EVALUATED
  findings: []        # rule violations found, with the evidence
provenance:
  source_ids: []
  tools: []
  skill_version: "required"
uncertainties: []
```

## Provenance & License

- **Origin:** Third-party skill adapted from `eval-integrity` in [Agent-FleetOps](https://github.com/sherifican/Agent-FleetOps) by Micah P.G. (sherifican). This is NOT original library content.
- **License:** MIT — Copyright (c) 2026 Micah P.G. This skill remains MIT-licensed; it may not be relicensed as proprietary. Per the MIT terms, this copyright notice must be preserved in all copies. The full MIT license text is reproduced in `ADOPTED.md` at the library root.
- **Adaptation:** Rewritten into this library's capability format; author-specific host references generalized. The failure stories are the original author's field evidence, kept because the failure *modes* transfer across setups. The repo-level MIT `LICENSE` in Agent-FleetOps covers this skill (it carries no per-file license line); the assessment verifying this adoption is at `~/workspace/agent-fleetops-eval/ASSESSMENT.md`.
