# uwv-common-agentic

Agent skills die collega's binnen het UWV met elkaar delen.

De skills zijn geschreven voor GitHub Copilot. Het zijn gewone `SKILL.md`-bestanden volgens de
[agent skills](https://agentskills.io/specification)-conventie, dus ze werken ook in andere harnassen.

De documentatie is Nederlands, conform UWV-beleid. Een `SKILL.md` mag Engels zijn, omdat het
model daar meestal beter mee werkt. Per skill staat een Nederlandse uitleg in [`docs/`](docs/).

## Installeren

Je hebt de [GitHub CLI](https://cli.github.com/) 2.90 of nieuwer nodig; `gh skill` is nog in
preview.

```bash
gh skill install MRDekeijzer/uwv-common-agentic                # kies skills, in dit project
gh skill install MRDekeijzer/uwv-common-agentic create-pr --scope user   # voor al je projecten
gh skill install MRDekeijzer/uwv-common-agentic --all          # alle UWV-skills
```

Zonder `--agent` installeert `gh skill` voor GitHub Copilot. Met `gh skill update` haal je latere
wijzigingen op. `gh` gebruikt je `gh auth login`, dus een private repository werkt zonder apart
token.

Zonder CLI kan het ook. Een skill is een map: kopieer `skills/<naam>/` naar `~/.copilot/skills/`
of `~/.agents/skills/` voor al je projecten, of naar `.github/skills/` of `.agents/skills/` voor
één project.

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
de bron, vastgezet op een commit die wij hebben bekeken.

> Derden onderhouden deze skills. Het installatiecommando pint een commit (`--pin`), dus je krijgt
> precies de versie die wij hebben gelezen. `gh skill update` slaat gepinde skills over. Een nieuwe
> versie komt er via een pull request die de pin ophoogt, nadat iemand de wijzigingen van de maker
> heeft bekeken (`gh skill preview` of de compare-weergave op GitHub).

| Skill | Bron | Waarom | Installeren |
| --- | --- | --- | --- |
| `grilling` | [mattpocock/skills](https://github.com/mattpocock/skills/tree/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/productivity/grilling) | Bevraagt je plan of ontwerp kritisch, zodat je de gaten vindt voordat er code is. | `gh skill install mattpocock/skills grilling --pin d81f3a183412e71a5b1e84ca21bc1a35eea03a60` |
| `grill-me` | [mattpocock/skills](https://github.com/mattpocock/skills/tree/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/productivity/grill-me) | Start een grilling-sessie alleen als jij `/grill-me` typt; de agent stelt het nooit zelf voor. Vereist `grilling`. | `gh skill install mattpocock/skills grill-me --pin d81f3a183412e71a5b1e84ca21bc1a35eea03a60` |

## Bijdragen

Eén pull request voegt één eigen skill toe, of één regel aan de tabel met aanbevolen skills.
[CONTRIBUTING.md](CONTRIBUTING.md) beschrijft de eisen voor allebei. Voor een eigen skill:

```bash
cp -r skills/create-pr skills/mijn-skill     # of begin met het contract in CONTRIBUTING.md
gh skill publish --dry-run                 # agentskills.io-spec
python3 scripts/validate_skills.py --fix   # catalogus bijwerken (vereist pyyaml)
python3 scripts/validate_skills.py         # dezelfde controle als in CI
```

[@MRDekeijzer](https://github.com/MRDekeijzer) en [@FrisoHarlaar](https://github.com/FrisoHarlaar)
beheren de registry en worden automatisch als reviewer aan elke pull request toegevoegd.

## Licentie

[MIT](LICENSE).
