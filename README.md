# uwv-common-agentic

[![skills.sh](https://skills.sh/b/MRDekeijzer/uwv-common-agentic)](https://skills.sh/MRDekeijzer/uwv-common-agentic)

Agent skills die collega's binnen het UWV met elkaar delen.

De skills zijn geschreven voor GitHub Copilot. Het zijn gewone `SKILL.md`-bestanden volgens de
[agent skills](https://skills.sh)-conventie, dus ze werken ook in andere harnassen.

De documentatie is Nederlands, conform UWV-beleid. Een `SKILL.md` mag Engels zijn, omdat het
model daar meestal beter mee werkt. Per skill staat een Nederlandse uitleg in [`docs/`](docs/).

## Installeren

```bash
npx skills add MRDekeijzer/uwv-common-agentic
```

Met `npx skills update` haal je latere wijzigingen op. Voor een private repository gebruikt de
CLI je bestaande git- of `gh`-credentials; je hebt geen apart token nodig.

Zonder CLI kan het ook. Een skill is een map: kopieer `skills/<naam>/` naar `~/.agents/skills/`
voor al je projecten, of naar `.agents/skills/` voor één project.

### Installeren via de Copilot plugin-marketplace

Deze repository is ook een plugin-marketplace voor GitHub Copilot
([`.github/plugin/marketplace.json`](.github/plugin/marketplace.json)). Daarvoor heb je geen
toestemming van een beheerder nodig. De plugin `uwv-common` bevat alle UWV-skills uit deze
repository. De [aanbevolen skills van derden](#aanbevolen-skills-van-derden) staan in één plugin
per bron, vastgezet op een gecontroleerde commit; de kolom "Plugin" in die tabel zegt welke.
Een nieuwere versie komt er pas na een pull request in.

Copilot CLI:

```bash
copilot plugin marketplace add MRDekeijzer/uwv-common-agentic
copilot plugin install uwv-common@uwv
copilot plugin install <plugin>@uwv    # optioneel: skills van derden
copilot plugin update --all            # later: wijzigingen ophalen
```

VS Code: voeg de marketplace toe aan je gebruikersinstellingen en installeer de plugins via de
Plugins-pagina van de Agent Customizations-editor.

```json
"chat.plugins.marketplaces": ["MRDekeijzer/uwv-common-agentic"]
```

Voor één project kan een team de marketplace ook in `.github/copilot/settings.json` van dat
project zetten, zodat iedereen die er werkt de plugins aangeboden krijgt:

```json
{
  "extraKnownMarketplaces": {
    "uwv": { "source": { "source": "github", "repo": "MRDekeijzer/uwv-common-agentic" } }
  },
  "enabledPlugins": { "uwv-common@uwv": true }
}
```

## UWV-skills

Deze skills zijn binnen het UWV gemaakt en worden in deze repository onderhouden.

<!-- catalog:start -->
| Skill | Waarvoor | Status |
| --- | --- | --- |
| [`create-pr`](skills/create-pr/SKILL.md) | Open een draft pull request op basis van het PR-template van de repository, gevuld met de commits op de huidige branch. | experimental |
<!-- catalog:end -->

`scripts/validate_skills.py` genereert deze tabel, dus pas hem niet met de hand aan.

## Aanbevolen skills van derden

Deze skills komen van buiten het UWV. Ze staan niet in deze repository: je installeert ze uit
de bron, zodat `npx skills update` de wijzigingen van de maker ophaalt.

> Derden onderhouden deze skills. UWV controleert hun updates niet.

| Skill | Bron | Plugin | Waarom | Installeren |
| --- | --- | --- | --- | --- |
| `grilling` | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling) | `mattpocock` | Bevraagt je plan of ontwerp kritisch, zodat je de gaten vindt voordat er code is. | `npx skills add mattpocock/skills --skill grilling` |
| `grill-me` | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) | `mattpocock` | Start een grilling-sessie alleen als jij `/grill-me` typt; de agent stelt het nooit zelf voor. Vereist `grilling`. | `npx skills add mattpocock/skills --skill grill-me` |

## Bijdragen

Eén pull request voegt één eigen skill toe, of één regel aan de tabel met aanbevolen skills.
[CONTRIBUTING.md](CONTRIBUTING.md) beschrijft de eisen voor allebei. Voor een eigen skill:

```bash
npx skills init mijn-skill                 # sjabloon (verplaats naar skills/mijn-skill/)
gh skill publish --dry-run                 # agentskills.io-spec
python3 scripts/validate_skills.py --fix   # catalogus bijwerken (vereist pyyaml)
python3 scripts/validate_skills.py         # dezelfde controle als in CI
```

[@MRDekeijzer](https://github.com/MRDekeijzer) en [@FrisoHarlaar](https://github.com/FrisoHarlaar)
beheren de registry en worden automatisch als reviewer aan elke pull request toegevoegd.

## Licentie

[MIT](LICENSE).
