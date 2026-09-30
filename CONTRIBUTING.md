# Bijdragen aan de registry

Je kunt een eigen skill toevoegen of een skill van derden aanbevelen. Eén pull request voegt één
skill toe, werkt er één bij of haalt er één weg.

## Een skill toevoegen

### Eigen skill

Skills volgen de [Agent Skills-specificatie](https://agentskills.io/specification), dus ze werken
in vrijwel elk agent-harnas, ook in GitHub Copilot. De specificatie legt ook uit hoe je een goede
skill schrijft.

Je hebt minimaal `skills/<naam>/SKILL.md` nodig, met de [frontmatter](#frontmatter) en de
instructies voor de agent. Scripts, templates en naslag zet je ernaast in `skills/<naam>/`; ze
worden samen met de skill geïnstalleerd.

We mergen een skill als:

1. Geen bestaande skill hetzelfde doet, ook niet buiten het UWV. Kijk in de catalogus in de
   [README](README.md) en zoek met `gh skill search <trefwoord>`. Bestaat er al een goede skill
   van derden, [beveel die dan aan](#skill-van-derden). Een eigen kopie loopt achter zodra de
   maker iets verbetert.
2. Het doel duidelijk is. `metadata.use-case` is één Nederlandse zin in de vorm
   `<doe wat> wanneer <situatie>` en komt in de catalogus. Aan de `description` ziet de agent of
   hij de skill moet laden, dus beschrijf wanneer de skill nodig is, met de woorden die een
   gebruiker typt (minstens 40 tekens).
3. Collega's er ook iets aan hebben. Gebruik je hem alleen zelf, zet hem dan in je eigen
   `~/.agents/skills/`.

### Skill van derden

1. Voeg een regel toe aan "Aanbevolen skills van derden" in de [README](README.md). Zeg in de
   kolom "Waarom" in één zin wat de skill doet en wanneer hij nuttig is.
2. Zet de skill in [`marketplace.json`](.github/plugin/marketplace.json). Elke bronrepository is
   daar één plugin, genoemd naar de eigenaar, met `"strict": false` en de volledige commit-SHA in
   `source`. Staat de bron er al, voeg dan alleen het pad toe aan `skills` van die plugin. Zet de
   pluginnaam in de kolom "Plugin".

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

## Frontmatter

```markdown
---
name: mijn-skill                    # gelijk aan de mapnaam, kebab-case
description: Use when <situatie> to <resultaat>. Covers <woorden die een gebruiker typt>.
license: MIT
metadata:
  use-case: Eén zin voor de catalogus in de README.
  owner: '@jouw-github-naam'
  status: experimental              # experimental, supported of deprecated
---

Instructies...
```

Voorbeelden staan in `skills/`.

## Werkwijze

`main` is beschermd. Wijzigingen komen er via een pull request in en we squashen bij het mergen.
Gebruik [Conventional Commits](https://www.conventionalcommits.org/) voor branchnamen en
PR-titels.

## Checks

Draai deze voordat je een pull request opent. CI draait dezelfde checks.

```bash
python3 -m pip install pyyaml              # eenmalig
gh skill publish --dry-run                 # Agent Skills-specificatie (GitHub CLI 2.90+)
python3 scripts/validate_skills.py --fix   # werkt de catalogus in de README bij
python3 scripts/validate_skills.py         # registry-eisen; moet 'ok' geven
```

De validator controleert de metadata, of de catalogus actueel is en of `marketplace.json` klopt
met de README.
