---
name: skl-001-structured-intake-normalization
description: "Use when a workflow requires structured intake normalization, particularly for intake, procurement, or support."
---

# Structured Intake Normalization

**Skill ID:** `SKL-001`  
**Primary category:** Operations  
**Common role families:** Intake, procurement, support, casework, release packaging.

## Overview

Converts forms, briefs, tickets, and unstructured requests into a validated schema; flags missing mandatory data. This is a narrow, independently testable capability. It must be installed inside a role contract that defines authority, approved sources, integrations, and human approval boundaries.

## When to Use

Use this capability when a role needs structured intake normalization and the required input, expected output, and acceptance test can be stated before execution. Do not use it to smuggle broader decision rights or hidden tool access into a role.

## Operating Contract

| Element | Requirement |
|---|---|
| Inputs | Approved source objects, required schema or file types, data classification, work-item ID, and applicable upstream gate. |
| Transformation | Converts forms, briefs, tickets, and unstructured requests into a validated schema; flags missing mandatory data. |
| Outputs | Versioned result, source references, findings, uncertainty, quality evidence, and escalation state. |
| Non-goals | Final human approval, unscoped inference, silent source substitution, external action, or permission expansion. |
| Stop conditions | Missing authoritative source, conflicting evidence, forbidden data/action, low confidence on a material point, or tool failure. |

## Procedure

1. Confirm the calling role, work item, preconditions, approved inputs, and integration scopes.
2. Validate the input schema and identify missing, provisional, conflicting, or restricted material.
3. Perform only this transformation: Converts forms, briefs, tickets, and unstructured requests into a validated schema; flags missing mandatory data.
4. Record source IDs, tool/runtime version, transformation version, findings, and limitations.
5. Test the result against the minimum fixture and return the artifact or a structured abstention/escalation.

## Guardrails

- The skill does not grant role authority or system access.
- Never infer authority from the capability name, model confidence, or connected system.
- Use the minimum data required and preserve originals, lineage, and reversible drafts.
- Separate verified evidence, inference, and unresolved uncertainty.
- High-consequence legal, clinical, financial, safety, privacy, employment, access, or public actions remain human-controlled.

## Required Output

```yaml
status: COMPLETE | NEEDS_REVIEW | BLOCKED | REJECTED
skill_id: "SKL-001"
work_item_id: "required"
input_refs: []
result:
  artifact_refs: []
  findings: []
provenance:
  source_ids: []
  tools: []
  skill_version: "required"
uncertainties: []
escalation:
  required: false
  owner: "named owner when required"
```

## Evaluation

- **Minimum fixture:** Incomplete/ambiguous intake with expected missing-field and escalation outputs.
- **Happy path:** Valid inputs yield the expected schema and evidence.
- **Missing/ambiguous input:** The skill identifies the gap and abstains or escalates correctly.
- **Restricted/adversarial input:** The skill blocks unauthorized use and records the reason.
- **Integration failure:** No silent partial success or duplicate side effect occurs.
- **Regression:** Previously accepted fixtures continue to meet the same threshold after changes.

Passing requires correct transformation, explicit uncertainty, complete provenance, policy-safe behavior, and a machine-readable result.

## Common Failure Modes

- Treating the skill as an autonomous role or approval authority.
- Producing polished output from incomplete or unverified inputs.
- Omitting negative tests, provenance, or abstention behavior.
- Expanding integrations or data scope to improve convenience.
