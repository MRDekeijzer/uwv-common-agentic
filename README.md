# uwv-common-agentic

Een gedeelde registry van agent skills. Skills staan hier zodat een afspraak die één keer
is uitgezocht door elk project en elke coding agent hergebruikt kan worden, in plaats van
per repo opnieuw te worden bedacht.

Skills zijn gewone `SKILL.md`-bestanden volgens de [agent skills](https://skills.sh)-conventie
en werken daarmee in Claude Code, Codex, Cursor, OpenCode en andere agents.

De documentatie in deze repo is Nederlands. Een skill zelf mag Engels zijn — dat werkt vaak
beter voor het model en maakt hergebruik buiten UWV makkelijker.

## Installeren

```bash
# alles, voor Claude Code, globaal
npx skills add MRDekeijzer/uwv-common-agentic --skill '*' -a claude-code -g

# één skill, in het huidige project
npx skills add MRDekeijzer/uwv-common-agentic --skill skill-authoring

# kijken wat er is, zonder te installeren
npx skills add MRDekeijzer/uwv-common-agentic --list
```

`npx skills update` haalt latere wijzigingen op. Toegang tot een private repo loopt via je
bestaande git- of `gh`-credentials; je hoeft dus geen token in te stellen.

Liever zonder CLI? Een skill is niet meer dan een map: kopieer `skills/<naam>/` naar
`~/.claude/skills/` (globaal) of `.claude/skills/` (één project).

## Catalogus

<!-- catalog:start -->
| Skill | Waarvoor | Nuttig in | Status |
| --- | --- | --- | --- |
| [`create-pr-from-template`](skills/create-pr-from-template/SKILL.md) | Open een pull request die het PR-sjabloon van de repo zelf gebruikt, gevuld vanuit de commits op je branch. | elk-github-project, repos-met-pr-sjabloon, uwv-common-agentic | supported |
| [`grill-me`](skills/grill-me/SKILL.md) | Start zelf een grilling-sessie met /grill-me, zonder te wachten tot het model het voorstelt. | elk-project, architectuurbesluiten, plan-review | supported |
| [`grilling`](skills/grilling/SKILL.md) | Een plan of ontwerp aan stukken vragen voordat je het bouwt, één vraag per keer. | elk-project, architectuurbesluiten, plan-review | supported |
| [`skill-authoring`](skills/skill-authoring/SKILL.md) | Schrijf een SKILL.md die aan het registry-contract voldoet, en bepaal of een nieuwe skill überhaupt nodig is. | uwv-common-agentic, any-claude-code-project, agent-tooling | experimental |
<!-- catalog:end -->

<sub>Gegenereerd met `python3 tools/validate_skills.py --fix` — pas de tabel niet met de hand aan.</sub>

## Bijdragen

Eén skill per pull request, met de documentatie ín de `SKILL.md`. Vier eisen: er bestaat nog
geen skill die dit doet, de use case staat beschreven, je noemt voor welke projecten het
nuttig is, en de documentatie zit in het bestand.

Lees [CONTRIBUTING.md](CONTRIBUTING.md) en doe dan:

```bash
npx skills init mijn-skill               # sjabloon (verplaats naar skills/mijn-skill/)
python3 tools/validate_skills.py --fix   # catalogus bijwerken
python3 tools/validate_skills.py         # dit draait CI ook
```

Beheerders: [@FrisoHarlaar](https://github.com/FrisoHarlaar) en
[@MRDekeijzer](https://github.com/MRDekeijzer). Beiden worden automatisch als reviewer
toegevoegd aan elke pull request.

## Licentie

[MIT](LICENSE).
