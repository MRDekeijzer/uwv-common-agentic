# uwv-common-agentic

[![skills.sh](https://skills.sh/b/MRDekeijzer/uwv-common-agentic)](https://skills.sh/MRDekeijzer/uwv-common-agentic)

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

## UWV-skills

Skills die binnen het UWV zijn gemaakt en in deze repository worden onderhouden.

<!-- catalog:start -->
| Skill | Waarvoor | Status |
| --- | --- | --- |
| [`create-pr`](skills/create-pr/SKILL.md) | Open een draft pull request op basis van het PR-template van de repository, gevuld met de commits op de huidige branch. | supported |
<!-- catalog:end -->

De tabel wordt gegenereerd door `scripts/validate_skills.py` en mag niet met de hand worden
aangepast. Wanneer een skill moet aanslaan, staat per skill beschreven in `docs/<naam>.md`.

## Aanbevolen skills van derden

Skills van buiten het UWV die we aanraden. Ze staan niet in deze repository: je installeert ze
rechtstreeks uit de bron, zodat `npx skills update` de wijzigingen van de maker ophaalt.

> Deze skills worden door derden onderhouden; updates worden niet door UWV gecontroleerd.

| Skill | Bron | Waarom | Installeren |
| --- | --- | --- | --- |
| `grilling` | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling) | Bevraagt een plan of ontwerp kritisch voordat het gebouwd wordt, zodat gaten boven water komen voordat er code is. | `npx skills add mattpocock/skills --skill grilling` |
| `grill-me` | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) | Start een grilling-sessie alleen wanneer jij `/grill-me` typt; de agent stelt het nooit zelf voor. Vereist `grilling`. | `npx skills add mattpocock/skills --skill grill-me` |

## Bijdragen

Een bijdrage is één skill per pull request: een eigen skill, of een aanbeveling van een skill
van derden. Voor een eigen skill gelden vier eisen: er bestaat nog geen skill die dit doet, de
use case is beschreven, de verplichte secties staan in de `SKILL.md`, en er is een Nederlandse
uitleg in `docs/<naam>.md`. Een aanbeveling is één regel in de tabel hierboven; zie
[CONTRIBUTING.md](CONTRIBUTING.md#een-skill-van-derden-aanbevelen).

Lees [CONTRIBUTING.md](CONTRIBUTING.md) en voer daarna uit:

```bash
npx skills init mijn-skill                 # sjabloon (verplaats naar skills/mijn-skill/)
python3 scripts/validate_skills.py --fix   # catalogus bijwerken
python3 scripts/validate_skills.py         # dezelfde controle als in CI
```

Beheerders: [@MRDekeijzer](https://github.com/MRDekeijzer) en [@FrisoHarlaar](https://github.com/FrisoHarlaar). Beiden worden automatisch als reviewer
toegevoegd aan elke pull request.

## Licentie

[MIT](LICENSE).
