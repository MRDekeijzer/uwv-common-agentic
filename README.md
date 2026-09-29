# uwv-common-agentic

Een gedeelde registry van agent skills voor hergebruik en kennisdeling binnen het UWV.

GitHub Copilot is het agent-harnas waarop deze registry zich richt. Skills zijn gewone
`SKILL.md`-bestanden volgens de [agent skills](https://skills.sh)-conventie en werken daardoor
ook in andere harnassen.

De documentatie in deze repository is Nederlands, conform UWV-beleid. De inhoud van een
`SKILL.md` mag Engels zijn, omdat dat voor het model doorgaans beter werkt. De Nederlandse
uitleg voor collega's staat per skill in [`docs/`](docs/).

## Installeren

```bash
npx skills add MRDekeijzer/uwv-common-agentic
```

`npx skills update` haalt latere wijzigingen op. Toegang tot een private repository verloopt
via je bestaande git- of `gh`-credentials; een apart token is niet nodig.

Installeren zonder CLI is ook mogelijk. Een skill is een map: kopieer `skills/<naam>/` naar
`~/.agents/skills/` voor alle projecten, of naar `.agents/skills/` voor één project.

## Catalogus

<!-- catalog:start -->
| Skill | Waarvoor | Status |
| --- | --- | --- |
| [`create-pr-from-template`](skills/create-pr-from-template/SKILL.md) | Open een pull request op basis van het PR-sjabloon van de repository, gevuld met de commits op de huidige branch. | supported |
| [`grill-me`](skills/grill-me/SKILL.md) | Start op eigen initiatief een grilling-sessie met /grill-me; het model stelt dit nooit zelf voor. | supported |
| [`grilling`](skills/grilling/SKILL.md) | Bevraag een plan of ontwerp kritisch voordat het gebouwd wordt, met één vraag per keer. | supported |
<!-- catalog:end -->

De tabel wordt gegenereerd door `scripts/validate_skills.py` en mag niet met de hand worden
aangepast. Wanneer een skill moet aanslaan, staat per skill beschreven in `docs/<naam>.md`.

## Bijdragen

Een bijdrage bestaat uit één skill per pull request. Aan vijf eisen moet zijn voldaan: er
bestaat nog geen skill die dit doet, de use case is beschreven, je benoemt voor welke projecten
de skill van pas komt, de verplichte secties staan in de `SKILL.md`, en er is een Nederlandse
uitleg in `docs/<naam>.md`.

Lees [CONTRIBUTING.md](CONTRIBUTING.md) en voer daarna uit:

```bash
npx skills init mijn-skill                 # sjabloon (verplaats naar skills/mijn-skill/)
python3 scripts/validate_skills.py --fix   # catalogus bijwerken
python3 scripts/validate_skills.py         # dezelfde controle als in CI
```

Beheerders: [@FrisoHarlaar](https://github.com/FrisoHarlaar) en
[@MRDekeijzer](https://github.com/MRDekeijzer). Beiden worden automatisch als reviewer
toegevoegd aan elke pull request.

## Licentie

[MIT](LICENSE).
