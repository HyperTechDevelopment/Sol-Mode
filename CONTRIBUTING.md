# Contributing to Sol Mode

## The SKILL.md word budget (binding)

`SKILL.md` must stay at or below 3,000 words; `scripts/verify.py` enforces this
(`skill-md-size`). The file currently sits near 2,600 words, so the margin is
narrow by design: the always-loaded surface stays small.

- A pull request that adds words to `SKILL.md` must remove or relocate at
  least as many words. Relocation target is `references/`.
- Detail belongs in `references/`; `SKILL.md` keeps posture, loop, decision
  rules, and pointers. New rules land in the matching reference file.
- New project-wide rules must add an anchor to `RULE_ANCHORS` in
  `scripts/verify.py`, so silent weakening fails loudly.

## Voice and encoding

- Third person, ASCII-only, no second-person pronouns outside quotes and
  fenced blocks. `README.md` and `README_pt_br.md` are marketing copy and
  exempt from the voice check; every other markdown file is checked.
- One main point per paragraph. Plain verbs over abstract phrasing.
- No slop vocabulary in skill prose: "delve", "leverage", "seamless",
  "robust", "cutting-edge", contrastive "not X, but Y" framing.

## References and namespaces

- Every file under `references/` and `scripts/` must be reachable from
  `SKILL.md`, directly or through its folder. The verifier checks this.
- Namespace blocks follow `references/domains/TEMPLATE.md` exactly.
- Namespaces other than design are experimental until exercised in a real
  demo. A pull request promoting one out of experimental status must include
  the demo evidence: what rendered or ran, where, and what stayed unverified.

## Modes

- Four modes exist: Default, Plan, Audit, UI. A fifth mode is a catalog,
  not a method; propose it as an issue first.
- Removing a mode removes its trigger words from `SKILL.md`,
  `references/modes.md`, `references/operating-protocol.md`,
  `references/provenance-and-limits.md`, and both READMEs.

## Verification

```
python scripts/verify.py
```

The pull request merges only on exit 0. No dependencies beyond Python 3.
