# Sol Mode

<img width="2400" height="1792" alt="Sol mode" src="https://github.com/user-attachments/assets/8b74f1fe-c6e5-4af2-8aae-199b313bfa3c" />


A working method for agents that must carry a task from request to verified result, with progress the user can follow and evidence behind every claim.

## What it changes

Most agent failures are not knowledge failures. They are process failures: work stopped half-done to ask for permission already granted, a result reported as done without being observed, a domain where nobody defined what counts as evidence, a conversation that gets compacted and restarts.

Sol Mode sets the behavior around the work:

- **Scoping before ceremony.** Trivial work is exempted, and where the answer lives decides how much process it gets.
- **Permission that matches risk.** Reversible work proceeds; irreversible work is finished first and approved as a concrete result.
- **Progress you can follow.** Frequent short notes while working, with assumptions and decisions stated, and a final answer that stands on its own.
- **Evidence per domain.** Namespace blocks define what evidence is binding for design, data, DevOps, finance, legal, marketing, operations, and research. Design is exercised in a real demo (`references/examples.md`); the other seven are experimental and welcome demos.
- **Verification by observation.** It ran, it rendered, it counted. Reading the code back is not verification.
- **Reporting that names its own limits.** Unverified parts are labelled, not implied.

## Why try it

Most method skills on the internet hand over tips: be simple, be surgical, verify. Sol Mode hands over a loop with an order, plus the evidence rules per kind of work. That is the differential.

- **A loop, not a list.** Eight phases run in order every turn: frame intent, check authority, recon in parallel with orient-first, plan the turn out loud, execute, verify by observation then stop, report self-contained, persist across compaction. Surprises route the loop instead of being ignored.
- **Permission that matches risk.** Reversible work proceeds without asking. Irreversible work is finished first as something concrete, so approval lands on a reviewable result instead of a vague plan. Authorization given once holds for later turns.
- **Evidence per domain, binding.** Eight namespace blocks state what must be opened before acting, who wins when sources disagree, and which situations mean the work is not done. Design, data, DevOps, finance, legal, marketing, operations, research. Coding stays the default. Medical work is excluded on purpose.
- **Verification with a stop rule.** It ran, it rendered, it counted. Tests stay meaningful and necessary, never mirrors of the implementation. After three failed fix-and-verify cycles, work hands back actual output plus a hypothesis instead of looping forever.
- **Reporting built for collapsed context.** Progress notes carry assumptions and direction while work runs. The final answer stands alone, because notes collapse. Outcome first, evidence and caveats present, unverified parts named.
- **Portable across models and harnesses.** A mapping table translates generic concepts to the harness in use, and harness execution machinery does not count as delegation. No model name, no proprietary tool, no single-agent assumption in the rules.
- **A verifier, not just promises.** `scripts/verify.py` checks structure, references, encoding, and a rule inventory, so silent regressions fail loudly. Few method skills ship anything like it.
- **Honest limits.** `provenance-and-limits.md` states what no skill can guarantee: hierarchy, compaction, tools, model parameters, tuning, measurement. That section exists so teams adopt the method with eyes open.

Try it when agents stall on permission, report done without observation, skip states on rendered surfaces, or restart after compaction. Run `sol-mode plan <task>` first to see the classification, the observation that proves done, and one recommendation before anything is touched. Compare with `references/examples.md`, which runs one login-page task through three methods side by side.

## Using it

```
sol-mode <task>          run the full method on a task
sol-mode plan <task>     deliver the plan and stop, touching nothing
sol-mode audit           grade the most recent completed work against the rules
sol-mode ui <task>       build an interface with the design rules mandatory
sol-mode off             deactivate for the rest of the session
```

It also applies on its own when work beyond the trivial gate starts and no task-specific skill covers it. The request that follows the reference in the same message is the task; there is no separate activation step.

## Contents

```
SKILL.md                      the method: posture, scoping, loop, decision rules, communication, writing
references/
  operating-protocol.md       permission, ambiguity, scoping, done, verifying, editing, skills, delegation
  communication-style.md      progress notes, final answer, formatting, visuals
  tooling-and-research.md     batching, shell safety, browsing boundary, citations, quoting limits
  modes.md                    Plan, Audit, UI
  examples.md                 login-page comparison across three methods
  provenance-and-limits.md    where the method came from and what no skill can guarantee
  domains/                    namespace blocks: design (exercised), data, DevOps, finance, legal, marketing, operations, research (experimental)
scripts/
  verify.py                   structure, references, encoding, and rule coverage checks
```

Only `SKILL.md` (about 2,600 words) loads by default; everything under `references/` loads on demand.

## Verifying it

```
python scripts/verify.py
```

Exits 0 when every check passes. No dependencies beyond Python 3.

## License

MIT. See `LICENSE`.

## Provenance

The behavioral rules began as an adaptation of a system prompt that circulates publicly for a frontier coding agent. Every line here is original writing: no text is reproduced from that source, nothing is quoted from it, and no line-by-line mapping to it exists. The domain namespace blocks, the modes, and the verifier are original to this skill.
