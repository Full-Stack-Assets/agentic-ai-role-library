# Adopted Third-Party Skills

This file records third-party content adopted into the Agentic AI Role Library. **These skills are NOT original library content and are NOT covered by the library's own licensing choices** — each remains under its original license and must keep its attribution intact wherever it ships (MIT repo, paid packs, or any derivative). They must never be relicensed as proprietary.

## Agent-FleetOps adoption (2026-09-22)

**Source:** [Agent-FleetOps](https://github.com/sherifican/Agent-FleetOps) by Micah P.G. (sherifican) — a public pattern library for multi-agent fleet operations and verification. Adopted from the zip at `~/workspace/user/files/Agent-FleetOps-main.zip`. Full intake assessment: `~/workspace/agent-fleetops-eval/ASSESSMENT.md`.

**License:** MIT (see full text below). Four of the six skills carried explicit `license: MIT` frontmatter upstream (`should-we`, `honesty-stop-gate`, `guard-target-correctness`, `generate-review-fix-loop`); the other two (`eval-integrity`, `model-routing-table`) are covered by the repo-level MIT `LICENSE` in Agent-FleetOps. All six are unambiguously MIT-licensed. The adaptation notes in each skill's Provenance section record exactly which applies.

**Adopted skills:**

| Library ID | Source skill | Upstream license marking |
|---|---|---|
| `SKL-046` Eval Integrity Audit | `eval-integrity` | Repo-level MIT LICENSE |
| `SKL-047` Measured Model Routing | `model-routing-table` | Repo-level MIT LICENSE |
| `SKL-048` Directive Interrogation ("Should We") | `should-we` | Per-file `license: MIT` |
| `SKL-049` Honesty Stop Gate | `honesty-stop-gate` | Per-file `license: MIT` |
| `SKL-050` Guard Target-Correctness | `guard-target-correctness` | Per-file `license: MIT` |
| `SKL-051` Generate → Review → Fix Loop | `generate-review-fix-loop` | Per-file `license: MIT` |

**What was NOT taken:** the `bench/` throughput numbers (author's two-box operating log — method transfers, cells don't), the `fleet-tui` app wholesale, and video-pipeline-specific fixtures. Adaptation generalized host-specific hardware, model names, and ports to lanes; the worked failures are the original author's field evidence, kept because the failure modes transfer.

## MIT License text (applies to all six skills above)

```
MIT License

Copyright (c) 2026 Micah P.G.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
