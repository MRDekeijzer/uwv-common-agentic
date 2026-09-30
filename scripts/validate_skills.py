#!/usr/bin/env python3
"""Controleert de registry-eisen in skills/ en werkt de catalogus in README.md bij.

De agentskills.io-spec zelf (naamgeving, mapnaam, verplichte velden) controleert
`gh skill publish --dry-run`; dit script doet alleen wat daar bovenop komt.

Gebruik:
  python3 scripts/validate_skills.py          # controleren (zoals CI; stopt met 1 bij problemen)
  python3 scripts/validate_skills.py --fix    # catalogus in README.md bijwerken
  python3 scripts/validate_skills.py --selftest
"""
import json
import re
import sys
import tempfile
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML ontbreekt - draai: python3 -m pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
README = ROOT / "README.md"
MARKETPLACE = ROOT / ".github" / "plugin" / "marketplace.json"
THIRD_PARTY = "## Aanbevolen skills van derden"
START, END = "<!-- catalog:start -->", "<!-- catalog:end -->"

REQUIRED_META = ("use-case",)
MIN_DESC_CHARS = 40
EMPTY_CATALOG = "_Nog geen skills._"
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---", re.S)


def check_skill(path):
    """Return (meta, [problems]) for one skills/<dir>/SKILL.md."""
    m = FRONTMATTER.match(path.read_text())
    if not m:
        return {}, ["bestand moet beginnen met een '---' YAML-frontmatterblok"]
    try:
        front = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        return {}, [f"frontmatter is geen geldige YAML: {e}"]
    problems = []

    if len(str(front.get("description", ""))) < MIN_DESC_CHARS:
        problems.append(f"description moet minstens {MIN_DESC_CHARS} tekens zijn en zeggen WANNEER de skill nodig is")
    meta = front.get("metadata") if isinstance(front.get("metadata"), dict) else {}
    for key in REQUIRED_META:
        if not meta.get(key):
            problems.append(f"metadata.{key} is verplicht en mag niet leeg zijn")
    return meta, problems


def collect():
    skills, problems = [], []
    for d in sorted(p for p in SKILLS.iterdir() if p.is_dir() and not p.name.startswith(".")):
        f = d / "SKILL.md"
        if not f.is_file():
            problems.append(f"skills/{d.name}/: geen SKILL.md")
            continue
        meta, errs = check_skill(f)
        problems += [f"skills/{d.name}/SKILL.md: {e}" for e in errs]
        if not errs:
            skills.append((d.name, meta))
    return skills, problems


# ponytail: splits cells on "|", so a literal pipe in a table cell breaks it.
def third_party_rows(readme):
    """{(plugin, skill, pinned sha)} from the third-party table in README.md."""
    if THIRD_PARTY not in readme:
        return set()
    section = readme.split(THIRD_PARTY, 1)[1].split("\n## ", 1)[0]
    rows = [[c.strip().strip("`") for c in line.strip().strip("|").split("|")]
            for line in section.splitlines() if line.startswith("|")]
    if not rows:
        return set()
    plugin, skill = rows[0].index("Plugin"), rows[0].index("Skill")
    pin = lambda r: (re.findall(r"--pin ([0-9a-f]+)", " ".join(r)) or [""])[0]
    return {(r[plugin], r[skill], pin(r)) for r in rows[2:]}


def check_marketplace(readme, market):
    """Return [problems]: the README table and marketplace.json must list the same third-party skills at the same SHA."""
    third = [p for p in market["plugins"] if p["source"] != "./"]
    listed = {(p["name"], s.rstrip("/").rsplit("/", 1)[-1], p["source"].get("sha", ""))
              for p in third for s in p.get("skills", [])}
    table = third_party_rows(readme)
    problems = [f"marketplace.json: plugin {p['name']!r} moet in source een volledige commit-SHA hebben"
                for p in third if not re.fullmatch(r"[0-9a-f]{40}", str(p["source"].get("sha", "")))]
    problems += [f"README noemt {s!r} (plugin {pl!r}, pin {sha[:7] or '-'}), maar marketplace.json niet"
                 for pl, s, sha in sorted(table - listed)]
    problems += [f"marketplace.json noemt {s!r} (plugin {pl!r}, sha {sha[:7] or '-'}), maar de README-tabel niet"
                 for pl, s, sha in sorted(listed - table)]
    return problems


def render_catalog(skills):
    if not skills:
        return EMPTY_CATALOG
    rows = ["| Skill | Waarvoor |", "| --- | --- |"]
    rows += [f"| [`{n}`](skills/{n}/SKILL.md) | {m['use-case']} |" for n, m in skills]
    return "\n".join(rows)


def apply_catalog(text, catalog):
    if START not in text or END not in text:
        raise SystemExit(f"README.md mist de markers {START} / {END}")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    return f"{head}{START}\n{catalog}\n{END}{tail}"


def selftest():
    with tempfile.TemporaryDirectory() as tmp:
        bad = Path(tmp) / "SKILL.md"
        bad.write_text("---\nname: x\ndescription: short\nmetadata:\n  other: x\n---\n\n# Bad\n")
        problems = check_skill(bad)[1]
        for expect in ("description moet", "use-case"):
            assert any(expect in p for p in problems), (expect, problems)

        # Block scalars and quoted values are plain YAML, so they must pass.
        bad.write_text(
            "---\nname: good-skill\ndescription: >\n  Use when you need a fixture that satisfies\n"
            "  every rule this validator enforces.\nmetadata:\n  use-case: Bewijst het gelukkige pad.\n"
            "---\n\nInstructies zonder vaste koppen.\n"
        )
        meta, problems = check_skill(bad)
        assert problems == [] and meta["use-case"] == "Bewijst het gelukkige pad.", problems
    one = render_catalog([("s", {"use-case": "Doet iets."})])
    assert one.splitlines()[-1] == "| [`s`](skills/s/SKILL.md) | Doet iets. |", one
    assert apply_catalog(f"a{START}old{END}b", "new") == f"a{START}\nnew\n{END}b"

    readme = f"{THIRD_PARTY}\n\n| Skill | Bron | Plugin |\n| --- | --- | --- |\n| `a` | x | `src` | `gh skill install o/r a --pin {'f' * 40}` |\n\n## Verder\n"
    plugin = {"name": "src", "source": {"source": "github", "repo": "o/r", "sha": "f" * 40}, "skills": ["./skills/a"]}
    assert check_marketplace(readme, {"plugins": [plugin]}) == []
    plugin["source"].pop("sha")
    plugin["skills"].append("./skills/b")
    problems = check_marketplace(readme, {"plugins": [plugin]})
    assert len(problems) == 4 and "SHA" in problems[0] and "pin fffffff" in problems[1], problems
    print("zelftest ok")


def main():
    if "--selftest" in sys.argv:
        return selftest()
    skills, problems = collect()
    text = README.read_text()
    problems += check_marketplace(text, json.loads(MARKETPLACE.read_text()))
    updated = apply_catalog(text, render_catalog(skills))
    if "--fix" in sys.argv:
        if updated != text:
            README.write_text(updated)
            print("catalogus in README.md bijgewerkt")
    elif updated != text:
        problems.append("catalogus in README.md is verouderd - draai: python3 scripts/validate_skills.py --fix")
    if problems:
        print(f"{len(problems)} probleem/problemen:\n" + "\n".join(f"  - {p}" for p in problems), file=sys.stderr)
        sys.exit(1)
    print(f"ok: {len(skills)} skill(s) geldig, catalogus actueel")


if __name__ == "__main__":
    main()
