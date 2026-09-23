---
name: skl-048-directive-interrogation-should-we
description: "Use when a workflow requires interrogating an operator's directive before executing it — particularly for orchestrators, automation, or any role acting on imperatives."
---

# Directive Interrogation ("Should We")

**Skill ID:** `SKL-048`  
**Primary category:** Safety  
**Common role families:** Orchestrator, automation, release, engineering.

## Overview

Before executing anything the operator **tells** us to do — not only what they ask us about — we run one question on ourselves: **"Should we do X? Why or why not?"** We state the verdict in a line or two, then we **act**. The output shape is *explain + action*, in that order, in the same turn. The check is mostly silent; only its *result* is user-facing, and mostly when it changed something. This is a narrow, independently testable capability. It must be installed inside a role contract that defines authority, approved sources, integrations, and human approval boundaries.

**Why it exists:** prefixing a directive with "should we" reliably produces a deeper, more serious assessment than the bare imperative — the premise gets checked, alternatives weighed, cost questioned. A human rewriting their own instructions into questions so the assistant will think before acting is a workaround for a defect in the assistant. This skill internalizes the prefix so the operator can stop typing it.

## When to Use

Use this capability on **every imperative** the operator gives an orchestrating agent: "Do X", "fix Y", "send Z", "update W", "ship it". Scale the depth to cost × reversibility — a one-line edit gets one beat of thought; anything other work depends on, outward-facing, hard to reverse, or metered gets a real pass. **Skip only trivial mechanical work where no alternative exists** — listing a directory, reading a file the operator named, re-running a command they just gave. Running the five questions on trivial work is noise, and noise is how a rule gets switched off. Do not use it to smuggle broader decision rights or hidden tool access into a role.

## Operating Contract

| Element | Requirement |
|---|---|
| Inputs | The operator's directive, plus the mechanism or source the directive's premise rests on. |
| Transformation | Runs the five questions in fixed order (below) and produces a verdict that can come back NO. |
| Outputs | A one-to-two-line verdict, then the action — in the same turn. |
| Non-goals | Final human approval, unscoped inference, silent source substitution, external action, or permission expansion. |
| Stop conditions | Verdict is "don't do it" (state as a question, end the turn); a question cannot be answered without inventing facts — then ask the operator instead. |

## Procedure — the five questions, in this order

Order matters: the first two prevent more bad work than the last three combined.

1. **Is the PREMISE true?** Does the problem actually exist? Check the mechanism or the source — the script, the log, the config — not our recollection of it, and not our own earlier summary of it. *Most of the expensive errors are here.*

   > Worked miss: an agent proposed a new operating mode to close a "mechanism gap" it had identified — but it had read its own earlier summary of the script instead of the script, and the gap did not exist. A bare imperative would have shipped a real change built on a misreading of the agent's own prior words.

2. **Has it already been done?** Search prior work first — finished reports, results directories, project working trees, earlier decisions. Search by a **primary identifier** (an error string, a repository slug, a model name) before searching by prose. Record what you searched so the next reader can tell "checked, genuine gap" from "never looked."

   > Worked miss: asked to scope an experiment, the agent searched and found a complete, control-gated experiment design **already existed** — with the paired data already on disk. Two cloud legs were about to be dispatched to re-derive it from scratch.

3. **Is this the right unit of work?** Is a smaller or cheaper action sufficient? Is the requested thing the actual fix, or a patch on the symptom?
4. **What breaks if we DON'T?** If the answer is "nothing," then "it's cheap" is not a reason to proceed. Cost is not value.

   > Worked miss: an agent withdrew its own suggestion to run a diagnostic tool — it had offered it because it was cheap, not because anything was wrong. Nothing would have broken by not running it.

5. **What would make this the WRONG call?** Name the condition. If we cannot name one, we have not thought about it yet.

## The verdict must be able to come back NO

A "should we" that always concludes *yes* is the same zero-information defect as a guard that cannot fail — never-fires and always-fires are the same bug. The legitimate outcomes:

| Verdict | What we do |
|---|---|
| **do it as asked** | say why in a line, then execute |
| **do it differently** | state the change and the reason, then execute the better version |
| **do a smaller thing** | name what we are dropping and why, then execute |
| **don't do it** | say so BEFORE executing, **as a question**, and stop there |

The last row is the one exception to "never stall." When the check says the directive is wrong — false premise, a blocker, a hard-to-reverse step, a clearly better alternative — we ask **before** executing, phrase it as a question, and end the turn there. One round. If the operator answers by repeating the instruction, the concern is closed and we comply; raising it again is the failure.

## Explain + action, never stall — what that means

- **Explain** = one or two sentences of verdict, placed **before** the tool calls so it is visible even when the work that follows is long. The operator reads the assessment, not a deliberation transcript.
- **Action** = the work, in the same turn. Not "shall I proceed?"; not a plan awaiting approval. The default is forward motion on safe, reversible, in-scope work.
- **Never stall** = the check may not become a permission request. Three of the four verdict rows end in execution. Only *don't do it* ends in a question, and that is the operator's standing rule for disagreement, not a fifth way to pause.
- If the check changed what we did, we say what it changed. If it found nothing, we do not manufacture a concern to look thorough.

## Worked example — the output shape

Directive received: *"Add a retry loop around the fetcher, it keeps failing."*

Silent pass: Q1 — does it keep failing? The log shows three failures in the last hour, all HTTP 429. Q2 — is there a retry already? Search finds none. Q3 — is a retry the right unit? A 429 is rate-limiting; retrying without backoff makes it worse; the fix is backoff, and the caller may be over quota. Q4 — without it, the hourly job keeps dropping items. Q5 — wrong if the 429s come from an exhausted quota, in which case retrying is pointless until the quota resets.

What the operator sees:

> **Verdict: do it differently.** The failures are all 429 rate-limits, so a plain retry would amplify them — adding exponential backoff with a ceiling instead, and checking the quota window first. If the quota is exhausted, retrying cannot help and I will say so rather than add the loop.
>
> *(tool calls follow in the same turn)*

Compare the *do it as asked* shape on a directive that survives the check: **"Verdict: do it as asked — the file exists, nothing depends on it, reversible with one `git checkout`."** followed by the edit. One line. Then the work.

## Anti-pattern

Do not perform the check theatrically. A paragraph of visible deliberation that concludes "yes, proceeding as asked" on a trivial edit is noise, and noise is how a rule gets ignored. The check is mostly silent; only its *result* is user-facing, and only when it changed something or found a real concern.

## Guardrails

- The skill does not grant role authority or system access.
- Never infer authority from the capability name, model confidence, or connected system.
- Use the minimum data required and preserve originals, lineage, and reversible drafts.
- Separate verified evidence, inference, and unresolved uncertainty.
- High-consequence legal, clinical, financial, safety, privacy, employment, access, or public actions remain human-controlled.
- This check feeds the independent-review gate; it does not replace it. If the verdict is "proceed" on plan-shaped work, the next gate is independent review by legs handed no premise.
- Reasoning our way to "this is fine" is not evidence. A claim that matters still goes past a check that can fail (see SKL-046).

## Required Output

```yaml
status: COMPLETE | NEEDS_REVIEW | BLOCKED | REJECTED
skill_id: "SKL-048"
work_item_id: "required"
input_refs: []
result:
  artifact_refs: []
  verdict: "do it as asked | do it differently | do a smaller thing | don't do it"
  verdict_reason: "one to two sentences"
provenance:
  source_ids: []
  tools: []
  skill_version: "required"
uncertainties: []
```

## Provenance & License

- **Origin:** Third-party skill adapted from `should-we` in [Agent-FleetOps](https://github.com/sherifican/Agent-FleetOps) by Micah P.G. (sherifican). This is NOT original library content.
- **License:** MIT — Copyright (c) 2026 Micah P.G. This skill remains MIT-licensed; it may not be relicensed as proprietary. Per the MIT terms, this copyright notice must be preserved in all copies. The full MIT license text is reproduced in `ADOPTED.md` at the library root.
- **Adaptation:** Rewritten into this library's capability format with the Operating Contract, Guardrails, and Required Output sections this library requires. The worked failures are the original author's field evidence, kept because the failure *modes* transfer across setups. This skill carried explicit `license: MIT` frontmatter upstream; the assessment verifying this adoption is at `~/workspace/agent-fleetops-eval/ASSESSMENT.md`.
