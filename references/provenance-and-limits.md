# Provenance and limits

## Where the method came from

The behavioral rules in this skill began as an adaptation of a system prompt that circulates publicly for a frontier coding agent. That prompt describes a general working posture, independent of any single product.

This skill is a rewrite. It reproduces no text from that source, quotes nothing from it, and carries no line-by-line mapping to it. The domain namespace blocks, the modes, the verifier, and the wording throughout are original to this skill. What remains shared with the source is general professional practice stated in this skill's own terms.

## What this skill adds beyond a behavioral core

1. **Activation.** Signal words, the rule that the request in the same message is the task, proactive application to uncovered non-trivial work, and deactivation phrases.
2. **Harness mapping.** Channel and tool names differ between agents. The table in `SKILL.md` translates them.
3. **Scoping.** An exemption for trivial work, and a rule for locating where the answer lives.
4. **Knowing when the work is done.** Naming the observation that proves completion, and the precedence that applies when sources disagree about intended behavior.
5. **Editing.** Smallest correct change, matching existing style, the recovery sequence after a failed edit, and looking before overwriting.
6. **Writing from memory.** API shapes, endpoints, configuration keys, prices, and figures written from recall are opened or labelled.
7. **Namespaces.** Eight domain blocks plus a shape template, so the evidence required is stated per kind of work.
8. **Modes.** Plan, Audit, and UI as named modes.
9. **Verification.** `scripts/verify.py`, which checks structure, references, encoding, and rule coverage.

## What no skill can guarantee

These limits are structural. They apply to this skill as much as to any other.

1. **Instruction hierarchy.** A skill sits below the platform's system prompt, its safety rules, and the user's instructions. Where they conflict, the skill loses.
2. **Context.** A skill cannot control when a conversation is compacted or what survives it.
3. **Tools.** The rules assume file reads, a shell, search, and web access. A harness without them cannot execute them.
4. **Model parameters.** Reasoning depth is set by the serving layer. A skill biases behavior; it does not raise capability.
5. **Tuning.** These rules were written and checked for internal consistency. They were not fitted against a large sample of real tasks, so expect rough edges.
6. **No measurement.** Nothing here proves that work done with this skill beats work done without it. That requires the same tasks run both ways and graded blind.

## Reading the checks honestly

`verify.py` proves the files are well formed and that every rule in the inventory is present. That is a statement about the artifact. It says nothing about whether an agent follows the rules at runtime.
