# Examples: login page across fable-method, karpathy-guidelines, and sol mode

A single task run through three specific methods, not a generic skill comparison. The task:

> Create a styled login page.

The two counterparts are fable-method and karpathy-guidelines: the method skills present in the author's daily work. The comparison exists to show where sol mode sits relative to those two, so anyone familiar with either can place it.

Each section shows the behavior, not the final code. Fenced blocks hold sample notes and reports.

## 1. Fable Method

Step 0 classifies the ask as task-shaped: verbs call for a completed change, verified. No plan-first signal is present. Scope covers one new surface plus styles. No settled decision is relitigated.

Step 1 defines done as observation: the page renders at desktop and narrow widths, states exist for idle, loading, error, and empty input, and the targeted check passes.

Step 2 gathers evidence in parallel: theme tokens, global styles, a neighboring form surface, and the auth path if one exists. Reading stays narrow: tokens first, then the nearest form, then the route where the page mounts. A surprise, such as no token system, is stated and changes the plan.

Step 3 commits to one recommendation, with each dismissed alternative in one line. The scope names the new files. No irreversible action exists, so no AUTH line is owed. The task stays local and reversible.

Step 4 acts surgically. Before the first behavior-affecting edit, the report line is prepared:

```
INTENT: no login surface exists; the task expects a styled login form; the spec names tokens in theme.css
```

The smallest correct change follows. Existing style is matched. No adjacent code is improved. No dependency is added. No secret is touched.

Step 5 verifies by observation: rendered at two widths, keyboard path walked, contrast checked for the new pairs, real submit path exercised or marked visual-only. The surrounding build or lint for the touched area still passes. No defect was fixed, so no TWINS line is owed.

Step 6 reports outcome first, in complete sentences, with the INTENT line included because behavior changed. Load-bearing lines are quoted. Caveats name what was not verified. Scratch files are removed. No method scaffolding appears besides the owed line.

Modes map directly: plan stops after Step 3, audit grades each step as followed, skipped, or faked, report rewrites per the Step 6 checklist.

## 2. Karpathy Guidelines

Think before coding: assumptions stated plainly, for example the auth endpoint, the expected fields, and the redirect after success. Ambiguity stops the work until resolved. A simpler approach, when one exists, is said out loud.

Simplicity first: the minimum that solves the task. No signup flow, no password recovery, no configurable theme engine, no speculative validation states. When the draft grows beyond the need, it is rewritten smaller.

Surgical changes: only the login surface and its styles are touched. Adjacent components keep existing formatting. Pre-existing dead code is mentioned, not deleted. Orphans created by the change, such as unused imports, are removed. Every changed line traces to the request.

Goal-driven execution: success criteria with checks, stated up front:

```
1. Form renders with email, password, submit -> check: render at two widths
2. Empty submit shows inline errors -> check: exercised submit with empty fields
3. Failed login shows error state -> check: exercised failure path or marked visual-only
4. Existing checks still pass -> check: build or lint for the touched area
```

The loop runs until the criteria pass. Weak criteria are rewritten before coding continues.

## 3. Sol Mode

Activation carries no ceremony. One short note states that the mode is on plus the load-bearing assumption, then the work starts in the same turn. A bare reference with no task asks once what to work on.

```
Sol Mode on. Assumption: a token system exists in theme files; falling back to stated defaults when absent.
```

Phase 0 frames intent from the instruction plus prior context, biased toward action. A mid-work message counts as steering unless it cancels the task or asks for something incompatible.

Phase 1 checks authority and risk. A local login surface is reversible, read-only safe, and reviewable, so it proceeds without permission. A later deploy or merge would finish first as a concrete result, with approval as the final step.

Phase 2 recons in parallel, orienting first. Directory listing and candidate enumeration precede specific reads. The matching namespace block, `references/domains/design-ux.md`, is read before gathering evidence because the deliverable is rendered and interactive. Independent reads batch in one pass and every result is inspected.

Phase 3 plans the turn in a progress note: the concrete plan, the assumptions, and done as observation, including the render widths and the states covered. Dependencies stay sequential. The cheapest reasoning depth carries the task.

Phase 4 executes the whole job in order. A surprise routes the loop: a contradiction, such as tokens disagreeing with a referenced design file, is stated with evidence on both sides. When the contradiction changes done, the plan updates. When it changes the ask, intent reframes. Otherwise the finding is reported and work continues.

Phase 5 verifies against the requirement by observation: the command ran, the page rendered, the states behaved. Design-ux rules bind the check: rendered before done, more than one width, no raw values beside tokens, contrast computed, keyboard path walked, real API path exercised or marked visual-only. Tests stay meaningful and necessary. After three failed fix-and-verify cycles on the same problem, work stops and hands back actual output plus a hypothesis.

```
Verified: page rendered at 1280 and 390, all four states exercised, contrast computed, keyboard path walked. Not verified: real auth round-trip against staging.
```

Phase 6 closes with a self-contained final answer: what changed, why, how it was verified, and material limits. Earlier progress notes are treated as collapsed, so nothing essential lives only there. No contrastive framing and no slop vocabulary appear.

Phase 7 persists across turns and compaction as one logical chain: no restart, no redone work, no repeated updates.

Plan mode delivers classification, done with its observation, evidence with sources, the governing namespace, and one recommendation, then stops without touching anything. Audit grades the recent work rule by rule with the risk each gap created plus the single highest-value fix. UI mode runs the same loop with the design namespace mandatory and delivers the surface plus its render evidence.
