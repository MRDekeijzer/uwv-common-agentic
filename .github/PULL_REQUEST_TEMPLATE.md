<!-- Titel in conventional-commit vorm, bijvoorbeeld "feat: skill voor alembic-migraties".
     Die titel wordt na het squashen de commitregel in main.

     Voor het toevoegen van een skill: vul de vijf eisen hieronder in. Voor een andere
     wijziging (fix, docs, chore): verwijder de vijf eisen en beschrijf wat er verandert.
     Zie CONTRIBUTING.md. -->

## 1. Geen duplicaat

Dichtstbijzijnde bestaande skill: `<naam, of "die bestaat niet">`
Waarom die skill dit geval niet afdekt:

## 2. Use case

<!-- Eén zin: "<doe wat> wanneer <situatie>". Gelijk aan metadata.use-case. -->

## 3. Voor welke projecten komt dit van pas

<!-- Concrete contexten, gelijk aan metadata.projects. Noem er minstens twee. -->

## 4. De verplichte secties staan in de SKILL.md

- [ ] `## When to use` en `## When not to use` zijn ingevuld en concreet
- [ ] `description` is geformuleerd als trigger, met de woorden die een gebruiker typt
- [ ] `status: experimental`, tenzij de skill al in een echt project is gebruikt

## 5. Er is een Nederlandse uitleg in docs/

- [ ] `docs/<naam>.md` bestaat en heeft dezelfde naam als de map in `skills/`
- [ ] `## Wanneer gebruiken` en `## Wanneer niet gebruiken` zijn ingevuld
- [ ] De uitleg is te volgen voor een collega die deze skill nog nooit heeft gebruikt

## Controles

- [ ] `python3 scripts/validate_skills.py` geeft lokaal 0 terug
- [ ] Ik heb deze skill minstens eenmaal in de praktijk gebruikt en beschrijf de uitkomst hieronder
