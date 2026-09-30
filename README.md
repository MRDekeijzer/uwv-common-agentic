# uwv-common-agentic

Skills die collega's binnen het UWV met elkaar delen.

Een skill is een map met een `SKILL.md`: instructies die een AI-agent zoals GitHub Copilot laadt
zodra een taak erom vraagt. Er staat in hoe je een klus aanpakt, bijvoorbeeld een pull request
openen volgens het sjabloon van de repository. Je hoeft die uitleg dan niet in elke chat opnieuw
te geven, en de agent doet het elke keer op dezelfde manier.

Wat de een uitzoekt, heeft de ander vaak ook nodig. In deze registry delen we daarom onze kennis
en de skills die ons helpen, samen met skills van buiten het UWV die we aanraden.

De skills volgen de [Agent Skills-specificatie](https://agentskills.io/specification), dus ze
werken ook in andere harnassen dan Copilot. De documentatie is Nederlands, conform UWV-beleid.
Een `SKILL.md` mag Engels zijn, omdat het model daar meestal beter mee werkt.

## Installeren

### Installeren via de plugin-marketplace (aangeraden)

Deze repository is een plugin-marketplace voor o.a. GitHub Copilot
([`.github/plugin/marketplace.json`](.github/plugin/marketplace.json)). De plugin `uwv-common` bevat alle UWV-skills uit deze
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

<details>
<summary>Installeren via de Github CLI</summary>

Je hebt de [GitHub CLI](https://cli.github.com/) 2.90 of nieuwer nodig.

```bash
gh skill install MRDekeijzer/uwv-common-agentic                # kies skills, in dit project
gh skill install MRDekeijzer/uwv-common-agentic create-pr --scope user   # voor al je projecten
gh skill install MRDekeijzer/uwv-common-agentic --all          # alle UWV-skills
```

Zonder `--agent` installeert `gh skill` voor GitHub Copilot. Met `gh skill update` haal je latere
wijzigingen op. `gh` gebruikt je `gh auth login`, dus een private repository werkt zonder apart
token.

</details>

<details>
<summary>Handmatig kopiëren (afgeraden)</summary>

Zonder CLI kan het ook. Een skill is een map: kopieer `skills/<naam>/` naar `~/.copilot/skills/`
of `~/.agents/skills/` voor al je projecten, of naar `.github/skills/` of `.agents/skills/` voor
één project.

</details>

## UWV-skills

Deze skills zijn binnen het UWV gemaakt en worden in deze repository onderhouden.

<!-- catalog:start -->
| Skill | Waarvoor |
| --- | --- |
| [`create-pr`](skills/create-pr/SKILL.md) | Open een draft pull request op basis van het PR-template van de repository, gevuld met de commits op de huidige branch. |
<!-- catalog:end -->

`scripts/validate_skills.py` genereert deze tabel, dus pas hem niet met de hand aan.

## Aanbevolen skills van derden

Deze skills komen van buiten het UWV. Ze staan niet in deze repository: je installeert ze uit
de bron, vastgezet op een commit die wij hebben bekeken.

| Skill | Bron | Plugin | Waarom | Installeren |
| --- | --- | --- | --- | --- |
| `grilling` | [mattpocock/skills](https://github.com/mattpocock/skills/tree/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/productivity/grilling) | `mattpocock` | Bevraagt je plan of ontwerp kritisch, zodat je de gaten vindt voordat er code is. | `gh skill install mattpocock/skills grilling --pin d81f3a183412e71a5b1e84ca21bc1a35eea03a60` |
| `grill-me` | [mattpocock/skills](https://github.com/mattpocock/skills/tree/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/productivity/grill-me) | `mattpocock` | Start een grilling-sessie alleen als jij `/grill-me` typt; de agent stelt het nooit zelf voor. Vereist `grilling`. | `gh skill install mattpocock/skills grill-me --pin d81f3a183412e71a5b1e84ca21bc1a35eea03a60` |

## Bijdragen

Heb je een eigen skill geschreven die handig en breed inzetbaar kan zijn voor anderen? Of gebruik je regelmatig een skill van een andere partij die je graag deelt met je collega's? Draag dan bij aan de registry!

De [CONTRIBUTING.md](CONTRIBUTING.md) legt uit hoe je kan bijdragen.

## Owners

`@MRDekeijzer` en `@FrisoHarlaar` beheren de registry. We proberen elke pull request binnen een week te reviewen.

## Licentie

[MIT](LICENSE).
