<!-- Titel in conventional-commit vorm, bijv. "feat: skill voor alembic-migraties".
     Die titel wordt na het squashen de commitregel in main.

     Voeg je een skill toe? Vul de vier eisen in. Iets anders (fix, docs, chore)?
     Haal de vier eisen weg en beschrijf gewoon wat er verandert. Zie CONTRIBUTING.md. -->

## 1. Geen duplicaat

Dichtstbijzijnde bestaande skill: `<naam, of "die is er niet">`
Waarom die dit geval niet afdekt:

## 2. Use case

<!-- Eén zin: "<doe wat> wanneer <situatie>". Gelijk aan metadata.use-case. -->

## 3. Voor welke projecten is dit nuttig

<!-- Concrete contexten, gelijk aan metadata.projects. Noem er minstens twee. -->

## 4. De documentatie staat in de SKILL.md

- [ ] `## When to use` en `## When not to use` zijn ingevuld en concreet
- [ ] `description` leest als een trigger (de woorden die een gebruiker typt), niet als samenvatting
- [ ] `status: experimental`, tenzij dit al in een echt project is gebruikt

## Controles

- [ ] `python3 tools/validate_skills.py` geeft lokaal 0 terug
- [ ] Ik heb deze skill minstens één keer echt gebruikt, en beschrijf hieronder hoe dat ging
