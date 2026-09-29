#!/usr/bin/env python3
"""Verifier for the Sol Mode skill.

Checks structure, encoding, markdown integrity, reference resolution, and that
every rule in the inventory is present in the skill. Runs anywhere Python 3 is
installed, with no dependencies and no absolute paths.

Usage:
    python scripts/verify.py

Exits 0 when every check passes and 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"

# Rule inventory: phrases that must exist somewhere in the skill. If a rule is
# removed or weakened during an edit, its anchor disappears and this check
# fails, which makes silent regressions visible.
RULE_ANCHORS = [
    "Activation needs no ceremony",
    "Treat whatever follows the reference in the same message as the task",
    "Proactive application",
    "Trivial work: one file",
    "Where the answer lives",
    "A namespace block changes the nouns",
    "Verify by observation rather than inference",
    "never write tests that mirror the implementation",
    "After three failed fix-and-verify cycles",
    "A compacted conversation is not a finished task",
    "Waiting is not approval",
    "Finish the whole job",
    "never goes quiet for more than about a minute",
    "Never praise the plan by contrasting",
    "Never use contrastive framing",
    "When in doubt, verify",
    "Cite sources as inline markdown links",
    "Spawn sub-agents only when",
    "An authorization given once holds for later turns",
    "Tests are for changes that carry risk",
    "Verify by observation. It ran, it rendered, it counted",
    "Warnings, disclaimers, approval steps, and compliance checklists belong to present risk",
    "Name variables for the task",
    "Choose familiar words and concrete examples",
    "Do not quote more than 25 words verbatim",
    "The mode is Default unless the user names another",
    "It reproduces no text from that source",
    "# Namespace: design",
    "# Namespace: data",
    "# Namespace: devops",
    "# Namespace: finance",
    "# Namespace: legal",
    "# Namespace: marketing",
    "# Namespace: operations",
    "# Namespace: research",
    "## Decision boundary",
    "<situations_where_the_work_is_not_done>",
]


def main() -> int:
    failures: list[str] = []

    def report(name: str, ok: bool, detail: str = "") -> None:
        status = "PASS" if ok else "FAIL"
        line = "{:<28} {:<5} {}".format(name, status, "" if ok else detail)
        print(line.rstrip())
        if not ok:
            failures.append(name)

    report("skill-md-present", SKILL.is_file(), "SKILL.md not found")
    if not SKILL.is_file():
        return 1

    raw = SKILL.read_text(encoding="utf-8")
    lines = raw.splitlines()

    boundaries = [i for i, l in enumerate(lines[:12]) if l.strip() == "---"]
    report("frontmatter-present", len(boundaries) >= 2, "missing opening or closing --- block")

    head = lines[:12]
    name_line = next((l for l in head if l.startswith("name:")), "")
    name = name_line[5:].strip()
    report("name-format", bool(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name)), "invalid name: " + name)
    report("name-matches-folder", name == ROOT.name, "name {} differs from folder {}".format(name, ROOT.name))

    desc_line = next((l for l in head if l.startswith("description:")), "")
    desc = desc_line[12:].strip()
    report("description-length", 80 <= len(desc) <= 1024, "length {}".format(len(desc)))
    report(
        "description-third-person",
        bool(re.match(r"^(This skill should be used|Use this skill)", desc)),
        "description does not open in third person",
    )
    fm_block = []
    if len(boundaries) >= 2:
        fm_block = lines[boundaries[0] + 1 : boundaries[1]]
    expected_fields = {"name", "description", "version", "license", "trigger"}
    stray = []
    for raw_line in fm_block:
        if not raw_line.strip():
            continue
        m = re.match(r"^([A-Za-z0-9_-]+): ", raw_line)
        if not m or m.group(1) not in expected_fields:
            stray.append(raw_line.strip()[:60])
    report("frontmatter-clean", not stray, "unexpected frontmatter content: " + "; ".join(stray))
    report("version-present", any(l.startswith("version:") for l in fm_block), "version field missing")

    words = len(raw.split())
    report("skill-md-size", words <= 3000, "word count {}".format(words))

    # Per-file checks: encoding, voice, fences, and tables.
    md_files = sorted(p for p in ROOT.rglob("*.md"))
    non_ascii: list[str] = []
    fence_issues: list[str] = []
    table_issues: list[str] = []
    voice_issues: list[str] = []

    for path in md_files:
        rel = path.relative_to(ROOT).as_posix()
        marketing_copy = rel in ("README.md", "README_pt_br.md")
        text = path.read_text(encoding="utf-8", errors="replace")
        if not marketing_copy and any(ord(ch) > 127 for ch in text):
            non_ascii.append(rel)

        fenced = False
        fence_count = 0
        pipes: list[int] = []
        in_table = False
        for line in text.splitlines():
            if line.startswith("```"):
                fence_count += 1
                fenced = not fenced
                continue
            if fenced:
                continue
            if not marketing_copy:
                if line.startswith("> "):
                    continue
                if re.search(r"\b(you|your|yours|yourself)\b", line):
                    voice_issues.append("{}: {}".format(rel, line.strip()[:80]))
            if line.startswith("|"):
                pipes.append(line.count("|"))
                in_table = True
            else:
                if in_table and len(set(pipes)) > 1:
                    table_issues.append(rel)
                pipes = []
                in_table = False
        if in_table and len(set(pipes)) > 1:
            table_issues.append(rel)
        if fence_count % 2:
            fence_issues.append(rel)

    report("ascii-only", not non_ascii, ", ".join(sorted(set(non_ascii))))
    report("no-second-person-prose", not voice_issues, " ; ".join(voice_issues[:3]))
    report("code-fences-balanced", not fence_issues, ", ".join(sorted(set(fence_issues))))
    report("table-integrity", not table_issues, ", ".join(sorted(set(table_issues))))

    # References named in SKILL.md must exist.
    pattern = re.compile(r"(references|scripts)/(?:[A-Za-z0-9\-]+/)*[A-Za-z0-9\-]+\.[A-Za-z0-9]+")
    mentions = sorted({m.group(0) for line in lines for m in pattern.finditer(line)})
    missing = [m for m in mentions if not (ROOT / m).exists()]
    report("referenced-files-exist", not missing, ", ".join(missing))

    # Every resource under references/ and scripts/ is reachable from SKILL.md,
    # directly or through its folder.
    resource_files = [
        p for p in list((ROOT / "references").rglob("*")) + list((ROOT / "scripts").rglob("*")) if p.is_file()
    ]
    unmentioned = []
    for path in sorted(resource_files):
        rel = path.relative_to(ROOT).as_posix()
        folder = rel.rsplit("/", 1)[0] + "/"
        if rel not in raw and folder not in raw:
            unmentioned.append(rel)
    report("all-resources-mentioned", not unmentioned, ", ".join(unmentioned))

    report(
        "readme-and-license-present",
        (ROOT / "README.md").is_file() and (ROOT / "LICENSE").is_file(),
        "README.md or LICENSE missing",
    )

    # Rule inventory coverage across the whole skill. Case-insensitive so that a
    # capitalization tweak does not fail the gate.
    corpus = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in md_files)
    folded = corpus.casefold()
    absent = [anchor for anchor in RULE_ANCHORS if anchor.casefold() not in folded]
    report("rule-inventory-coverage", not absent, "{} missing: {}".format(len(absent), absent[:3]))

    print()
    if failures:
        print("Failed checks: {}".format(len(failures)))
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
