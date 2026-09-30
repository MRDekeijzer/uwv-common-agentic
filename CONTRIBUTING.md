# Bijdragen aan de registry

Je kunt een eigen skill toevoegen of een skill van derden aanbevelen.

## Een skill toevoegen

### Eigen skill

Skills volgen de [Agent Skills-specificatie](https://agentskills.io/specification), dus ze werken
in vrijwel elk agent-harnas, waaronder GitHub Copilot. De specificatie legt ook uit hoe je een goede
skill schrijft.

#### Werkwijze 

> Gebruik [Conventional Commits](https://www.conventionalcommits.org/) voor branchnaam en PR-titel

De stappen om een skill toe te voegen:

1. Clone de repo en maak een branch vanaf `main`
2. Schrijf de Skill
   - Je hebt minimaal `skills/<naam>/SKILL.md` nodig, met de [frontmatter](#frontmatter) en de instructies voor de agent. Scripts, templates en naslag zet je indien nodig erbij in de folder `skills/<naam>/`.
3. Run de [checks](#checks)
4. Open een PR en doorloop de stappen in de PR-template

Om de kwaliteit van de registry te waarborgen, letten we er bij de review op dat:

1. Geen bestaande skill hetzelfde doet, ook niet buiten het UWV. Kijk in de catalogus in de
   [README](README.md) en zoek met `gh skill search <trefwoord>`. Bestaat er al een goede skill
   van derden, [beveel die dan aan](#skill-van-derden). Een eigen kopie loopt achter zodra de
   maker iets verbetert.
2. Het doel van de skill duidelijk is. Een concrete zin in de `metadata.use-case` in de vorm `<doe wat> wanneer <situatie>` helpt ons en je collega's en komt in de catalogus te staan. Aan de `description` ziet de agent of hij de skill moet laden, dus beschrijf wanneer de skill nodig is, met de woorden die een gebruiker typt.
3. Collega's er ook iets aan hebben. Gebruik je hem alleen zelf, zet hem dan in je eigen
   `~/.agents/skills/`.

### Skill van derden

Mocht je een Skill van iemand anders gebruiken, kan je hem ook aanbevelen. Dat kan als volgt:

1. Voeg een regel toe aan "Aanbevolen skills van derden" in de [README](README.md). Zeg in de
   kolom "Waarom" in één zin wat de skill doet en wanneer hij nuttig is.
2. Zet de skill in [`marketplace.json`](.github/plugin/marketplace.json). Elke bronrepository is
   daar één plugin, genoemd naar de eigenaar van de repo. Vul in `source` de volledige commit-SHA in; die pin zorgt dat iedereen precies de versie krijgt die wij hebben gelezen. Zet `"strict": false`, omdat de bron meestal geen eigen `plugin.json` heeft: de lijst `skills` in `marketplace.json` bepaalt dan welke skills de plugin bevat. Staat de bronrepository er al als plugin bij, voeg dan alleen het pad toe aan `skills` van die plugin. Zet de pluginnaam in de kolom "Plugin" in de [README](README.md).

De aanbeveling moet hieraan voldoen:

- Geen UWV-skill of eerdere aanbeveling dekt dit al af.
- Je hebt de skill minstens eenmaal zelf gebruikt.
- De bron heeft een open licentie, zoals MIT of Apache-2.0.
- De bron is een onderhouden repository van een bekende maker, geen willekeurige fork, en je hebt
  `SKILL.md` en eventuele scripts gelezen op de commit die je pint.

```bash
gh api repos/<eigenaar>/<repo>/commits/main --jq .sha    # laatste commit
gh skill preview <eigenaar>/<repo> <skill>@<sha>         # lees de skill op die commit
gh skill install <eigenaar>/<repo> <skill> --pin <sha>   # voor de kolom "Installeren"
```

CI controleert of de README-tabel en `marketplace.json` dezelfde skills op dezelfde SHA noemen.

## Een skill bijwerken of verwijderen

### Eigen skill

Bijwerken: pas `skills/<naam>/` aan en draai de [checks](#checks).

Verwijderen: haal `skills/<naam>/` weg en draai de [checks](#checks), zodat de skill uit de
catalogus verdwijnt.

### Skill van derden

Bijwerken: lees eerst wat de maker veranderde, op
`https://github.com/<eigenaar>/<repo>/compare/<oude-sha>...<nieuwe-sha>`. Zet daarna de nieuwe SHA
in `source` in `marketplace.json` en in de link en `--pin` in de README. De SHA geldt voor alle
skills van die plugin, dus lees ook de wijzigingen in de andere skills.

Verwijderen: stopt de maker met onderhoud of werkt de skill niet meer, haal dan de regel uit de
README en het pad uit `marketplace.json`. Een plugin zonder skills haal je helemaal weg.

## Frontmatter

```markdown
---
name: mijn-skill                    # gelijk aan de mapnaam, kebab-case
description: Use when <situatie> to <resultaat>. Covers <woorden die een gebruiker typt>.
license: MIT
metadata:
  use-case: Eén zin voor de catalogus in de README.
---

Instructies...
```

Voorbeelden staan in `skills/`.

## Checks

Draai deze voordat je een pull request opent. CI draait dezelfde checks.

```bash
gh skill publish --dry-run           # Agent Skills-specificatie (GitHub CLI 2.90+)
python3 scripts/validate_skills.py   # werkt de catalogus bij en controleert de registry
```

De validator zet de `use-case` van elke skill in de catalogus in de README en controleert of
`marketplace.json` klopt met de tabel met skills van derden.
