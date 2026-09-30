# uwv-common-agentic

Centrale registry voor gedeelde Skills binnen het UWV.

## Wat is een Skill?

Een Skill is een instructie die een AI-agent kan inladen om extra context aan een vraag toe te voegen. Dit kan handmatig gebeuren of zodra een prompt erom vraagt. De invulling van de instructies kan veel kanten op gaan. Het kan belangrijke informatie over een specifiek onderwerp geven, of aangeven welke stappen je zet voor een klus, bijvoorbeeld hoe de AI-agent een pull request moet openen volgens het template van de repository. Je hoeft die uitleg dan niet in elke chat opnieuw te geven, en de agent doet het elke keer op dezelfde manier, zoals beschreven in de `SKILL.md`.

In deze registry delen we onze kennis en de skills die ons helpen, om binnen UWV elkaar te helpen en van elkaar te leren.

De skills volgen de [Agent Skills-specificatie](https://agentskills.io/specification), dus ze
werken in vrijwel alle agent-harnassen, zoals GitHub Copilot. De documentatie is Nederlands, conform UWV-beleid.
Een `SKILL.md` mag Engels zijn, omdat de AI-modellen daar meestal beter mee werken.

## Installeren

### Installeren via de plugin-marketplace (aangeraden)

Deze repository is een plugin-marketplace voor o.a. GitHub Copilot
([`.github/plugin/marketplace.json`](.github/plugin/marketplace.json)).

Deze bevat meerdere plugins, zodat je bij het installeren makkelijk kan kiezen wat je wel en niet wilt gebruiken.

- De plugin `uwv-common` bevat alle zelfgemaakte UWV-skills uit deze
  repository.
- De [aanbevolen skills van derden](#aanbevolen-skills-van-derden) staan in een losse plugin per bron. De kolom "Plugin" in die [catalogus](#aanbevolen-skills-van-derden) laat zien welke skills onder welke bron vallen.

Nieuwe versies van de UWV-skills haal je met één update-commando op. Skills van derden blijven op de gepinde commit staan tot een pull request de pin ophoogt.

#### Optie 1: Via de Copilot CLI

Installeer de marketplace via de Copilot CLI:

```bash
copilot plugin marketplace add MRDekeijzer/uwv-common-agentic
copilot plugin install uwv-common@uwv
copilot plugin install <plugin>@uwv    # optioneel, maar aangeraden: skills van derden
copilot plugin update --all            # later: wijzigingen ophalen
```

#### Optie 2: VS Code

Voeg de marketplace toe aan je gebruikersinstellingen en installeer de plugins via de
Plugins-pagina van de Agent Customizations-editor.

```json
"chat.plugins.marketplaces": ["MRDekeijzer/uwv-common-agentic"]
```

#### Optie 3: Per project

Voor één project kan een team de marketplace ook in `.github/copilot/settings.json` in de repo van dat
project zetten, zodat iedereen die aan het project werkt de plugins aangeboden krijgt:

```json
{
  "extraKnownMarketplaces": {
    "uwv": { "source": { "source": "github", "repo": "MRDekeijzer/uwv-common-agentic" } }
  },
  "enabledPlugins": { "uwv-common@uwv": true }
}
```

<details>
<summary>Installeren via de GitHub CLI (afgeraden)</summary>

> Installeren kan ook via de GitHub CLI. Dat raden we af, omdat je dan zelf updates moet bijhouden.

Je hebt de [GitHub CLI](https://cli.github.com/) 2.90 of nieuwer nodig.

```bash
gh skill install MRDekeijzer/uwv-common-agentic                # kies skills, in dit project
gh skill install MRDekeijzer/uwv-common-agentic create-pr --scope user   # voor al je projecten
gh skill install MRDekeijzer/uwv-common-agentic --all          # alle UWV-skills
```

Met `gh skill update` haal je latere wijzigingen op.

</details>

<details>
<summary>Handmatig kopiëren (afgeraden)</summary>

> Installeren kan ook zonder marketplace of GitHub CLI. Dat raden we af, omdat je dan zelf updates moet bijhouden.

Een Skill is in de basis een map. Zo installeer je een skill handmatig:

- Globaal gebruik: kopieer `skills/<naam>/` uit deze repo naar `~/.copilot/skills/` of `~/.agents/skills/` om de skill in al je projecten te kunnen gebruiken.
- Voor een specifiek project: kopieer `skills/<naam>/` uit deze repo naar `.github/skills/` of `.agents/skills/` in dat project.

</details>

## UWV-skills

Deze skills zijn binnen het UWV gemaakt en worden in deze repository onderhouden.

<!-- prettier-ignore-start -->
<!-- catalog:start -->
| Skill | Waarvoor |
| --- | --- |
| [`create-pr`](skills/create-pr/SKILL.md) | Open een draft pull request op basis van het PR-template van de repository, gevuld met de commits op de huidige branch. |
<!-- catalog:end -->
<!-- prettier-ignore-end -->

`scripts/validate_skills.py` genereert deze tabel, dus pas hem niet met de hand aan.

## Aanbevolen skills van derden

Deze skills komen van buiten het UWV. Ze staan niet in deze repository: je installeert ze uit
de bron, vastgezet op een commit die wij hebben bekeken.

<!-- prettier-ignore-start -->
| Skill | Bron | Plugin | Waarom | Installeren |
| --- | --- | --- | --- | --- |
| `grilling` | [mattpocock/skills](https://github.com/mattpocock/skills/tree/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/productivity/grilling) | `mattpocock` | Bevraagt je plan of ontwerp kritisch, zodat je de gaten vindt voordat er code is. | `gh skill install mattpocock/skills grilling --pin d81f3a183412e71a5b1e84ca21bc1a35eea03a60` |
| `grill-me` | [mattpocock/skills](https://github.com/mattpocock/skills/tree/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/productivity/grill-me) | `mattpocock` | Start een grilling-sessie alleen als jij `/grill-me` typt; de agent stelt het nooit zelf voor. Vereist `grilling`. | `gh skill install mattpocock/skills grill-me --pin d81f3a183412e71a5b1e84ca21bc1a35eea03a60` |
<!-- prettier-ignore-end -->

## Bijdragen

Heb je een eigen skill geschreven die handig en breed inzetbaar kan zijn voor anderen? Of gebruik je regelmatig een skill van een andere partij die je graag deelt met je collega's? Draag dan bij aan de registry!

De [CONTRIBUTING.md](CONTRIBUTING.md) legt uit hoe je kan bijdragen.

## Owners

`@MRDekeijzer` en `@FrisoHarlaar` beheren de registry. We proberen elke pull request binnen een week te reviewen.

## Licentie

[MIT](LICENSE).
