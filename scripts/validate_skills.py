#!/usr/bin/env python3
"""Controleert skills/ en docs/ tegen het registry-contract en werkt de catalogus in README.md bij.

Gebruik:
  python3 scripts/validate_skills.py          # controleren (zoals CI; stopt met 1 bij problemen)
  python3 scripts/validate_skills.py --fix    # catalogus in README.md bijwerken
  python3 scripts/validate_skills.py --selftest
"""
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
README = ROOT / "README.md"
DOCS = ROOT / "docs"
START, END = "<!-- catalog:start -->", "<!-- catalog:end -->"

REQUIRED_META = ("use-case", "owner", "status")
REQUIRED_HEADINGS = ("## When to use", "## When not to use")
MIN_DOC_CHARS = 200
STATUSES = {"experimental", "supported", "deprecated"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
EMPTY_CATALOG = "_Nog geen skills._"


# ponytail: deliberately a 2-level parser, not PyYAML. The contract below is the
# whole schema; anything fancier is rejected with a message instead of parsed.
def parse_frontmatter(text):
    if not text.startswith("---\n"):
        raise ValueError("bestand moet beginnen met een '---' YAML-frontmatterblok")
    end = text.find("\n---", 3)
    if end == -1:
        raise ValueError("frontmatterblok wordt nooit afgesloten met '---'")
    data, section = {}, None
    for raw in text[4:end].splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indented = raw.startswith((" ", "\t"))
        if ":" not in raw:
            raise ValueError(f"geen 'sleutel: waarde'-regel: {raw.strip()!r}")
        key, _, value = raw.strip().partition(":")
        key, value = key.strip(), value.strip()
        if value in (">", "|", ">-", "|-"):
            raise ValueError(
                f"{key!r} gebruikt een YAML-blok ({value}); zet de waarde op één regel achter de dubbele punt"
            )
        if indented:
            if section is None:
                raise ValueError(f"ingesprongen sleutel {key!r} heeft geen bovenliggende sleutel")
            data[section][key] = parse_value(value)
        elif value == "":
            section, data[key] = key, {}
        else:
            section, data[key] = None, parse_value(value)
    return data, text[end + 4:]


def parse_value(value):
    if value.startswith("[") and value.endswith("]"):
        return [v.strip().strip("\"'") for v in value[1:-1].split(",") if v.strip()]
    return value.strip().strip("\"'")


def check_skill(path):
    """Return (name, description, meta, [problems]) for one skills/<dir>/SKILL.md."""
    problems, name, desc, meta = [], path.parent.name, "", {}
    try:
        front, body = parse_frontmatter(path.read_text())
    except ValueError as e:
        return name, desc, meta, [str(e)]

    if front.get("name") != name:
        problems.append(f"name {front.get('name')!r} in de frontmatter moet gelijk zijn aan de mapnaam {name!r}")
    if not NAME_RE.match(name):
        problems.append(f"{name!r} moet kebab-case zijn (kleine letters, cijfers, enkele streepjes)")

    desc = front.get("description", "")
    if not isinstance(desc, str) or len(desc) < 40:
        problems.append("description moet minstens 40 tekens zijn en zeggen WANNEER de skill nodig is, niet alleen wat hij doet")
    elif len(desc) > 1024:
        problems.append("description is langer dan de 1024 tekens die agents toestaan")

    meta = front.get("metadata") if isinstance(front.get("metadata"), dict) else {}
    for key in REQUIRED_META:
        if not meta.get(key):
            problems.append(f"metadata.{key} is verplicht en mag niet leeg zijn")
    if meta.get("status") and meta["status"] not in STATUSES:
        problems.append(f"metadata.status moet een van {sorted(STATUSES)} zijn")

    for heading in REQUIRED_HEADINGS:
        if not re.search(rf"^{re.escape(heading)}\s*$", body, re.M):
            problems.append(f"verplichte sectie '{heading}' ontbreekt in de tekst")
    return name, desc, meta, problems


def check_doc(path, name):
    """Return [problems] for the Dutch docs/<name>.md that belongs to a skill."""
    if not path.is_file():
        return [f"docs/{name}.md ontbreekt; elke skill heeft een Nederlandse uitleg in docs/"]
    if len(path.read_text().strip()) < MIN_DOC_CHARS:
        return [f"docs/{name}.md is korter dan {MIN_DOC_CHARS} tekens; schrijf een of twee alinea's"]
    return []


def collect():
    skills, problems = [], []
    if not SKILLS.is_dir():
        return skills, ["de map skills/ bestaat niet"]
    for d in sorted(p for p in SKILLS.iterdir() if p.is_dir() and not p.name.startswith(".")):
        problems += check_doc(DOCS / f"{d.name}.md", d.name)
        f = d / "SKILL.md"
        if not f.is_file():
            problems.append(f"{d.relative_to(ROOT)}/: geen SKILL.md")
            continue
        name, desc, meta, errs = check_skill(f)
        problems += [f"skills/{d.name}/SKILL.md: {e}" for e in errs]
        if not errs:
            skills.append((name, desc, meta))
    for doc in sorted(DOCS.glob("*.md")) if DOCS.is_dir() else []:
        if not (SKILLS / doc.stem / "SKILL.md").is_file():
            problems.append(f"docs/{doc.name} hoort bij geen skill in skills/")
    return skills, problems


def render_catalog(skills):
    if not skills:
        return EMPTY_CATALOG
    rows = ["| Skill | Waarvoor | Status |", "| --- | --- | --- |"]
    for name, _, meta in skills:
        rows.append(
            f"| [`{name}`](skills/{name}/SKILL.md) | {meta.get('use-case', '')} | {meta.get('status', '')} |"
        )
    return "\n".join(rows)


def apply_catalog(text, catalog):
    if START not in text or END not in text:
        raise SystemExit(f"README.md mist de markers {START} / {END}")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    return f"{head}{START}\n{catalog}\n{END}{tail}"


def selftest():
    front, body = parse_frontmatter(
        "---\nname: a-b\ndescription: x\nmetadata:\n  tags: [p, q]\n  owner: '@me'\n---\n## When to use\n"
    )
    assert front["name"] == "a-b", front
    assert front["metadata"]["tags"] == ["p", "q"], front
    assert front["metadata"]["owner"] == "@me", front
    assert body.strip() == "## When to use", body
    for bad in ("no frontmatter", "---\nname: a\n", "---\nnot-a-mapping\n---\n",
                "---\ndescription: >\n  meerdere regels\n---\n"):
        try:
            parse_frontmatter(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"had afgewezen moeten worden: {bad!r}")
    assert check_doc(Path("nergens/x.md"), "x") == ["docs/x.md ontbreekt; elke skill heeft een Nederlandse uitleg in docs/"]
    assert render_catalog([]) == EMPTY_CATALOG
    one = render_catalog([("s", "d", {"use-case": "Doet iets.", "status": "supported"})])
    assert one.splitlines()[0].count("|") == 4, one          # Skill | Waarvoor | Status
    assert one.splitlines()[-1].endswith("| Doet iets. | supported |"), one
    assert apply_catalog(f"a{START}old{END}b", "new") == f"a{START}\nnew\n{END}b"

    with tempfile.TemporaryDirectory() as tmp:
        bad = Path(tmp) / "bad-skill" / "SKILL.md"
        bad.parent.mkdir()
        bad.write_text("---\nname: wrong-name\ndescription: short\nmetadata:\n  owner: x\n---\n\n# Bad\n")
        problems = check_skill(bad)[3]
        for expect in ("gelijk zijn aan de mapnaam", "description moet", "use-case",
                       "status", "When to use", "When not to use"):
            assert any(expect in p for p in problems), (expect, problems)

        good = Path(tmp) / "good-skill" / "SKILL.md"
        good.parent.mkdir()
        good.write_text(
            "---\nname: good-skill\n"
            "description: Use when you need a fixture that satisfies every rule this validator enforces.\n"
            "metadata:\n  use-case: Bewijst het gelukkige pad.\n"
            "  owner: '@me'\n  status: supported\n---\n\n## When to use\nx\n\n## When not to use\ny\n"
        )
        assert check_skill(good)[3] == [], check_skill(good)[3]

        doc = Path(tmp) / "good-skill.md"
        doc.write_text("# good-skill\n\nte kort\n")
        assert [p for p in check_doc(doc, "good-skill") if "korter dan" in p]
        doc.write_text("# good-skill\n\n" + "een zinnige alinea. " * 20)
        assert check_doc(doc, "good-skill") == [], check_doc(doc, "good-skill")
    print("zelftest ok")


def main():
    if "--selftest" in sys.argv:
        return selftest()
    skills, problems = collect()
    catalog, text = render_catalog(skills), README.read_text()
    updated = apply_catalog(text, catalog)
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
