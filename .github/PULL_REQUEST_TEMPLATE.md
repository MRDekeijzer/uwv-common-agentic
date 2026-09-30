<!-- Titel in conventional-commit vorm, bijvoorbeeld "feat: add skill for alembic migrations".
     Na het squashen is dat de commitregel in main.

     Houd het deel dat past en verwijder het andere. Bij een fix, docs of chore verwijder je
     beide en beschrijf je wat er verandert. Zie CONTRIBUTING.md. -->

## Eigen skill

Dichtstbijzijnde bestaande skill: `<naam, of "geen">`, die dit niet afdekt omdat ...
Use case: <gelijk aan metadata.use-case>

- [ ] `When to use` en `When not to use` zijn concreet, en `description` gebruikt de woorden die een gebruiker typt
- [ ] `status: experimental`, tenzij de skill al in een echt project is gebruikt
- [ ] `docs/<naam>.md` legt in een of twee alinea's uit wanneer je de skill pakt en hoe hij zich verhoudt tot andere skills
- [ ] Ik heb de skill minstens eenmaal zelf gebruikt
- [ ] `python3 scripts/validate_skills.py` geeft 'ok'

## Aanbeveling

Bron: `<eigenaar>/<repo>`, skill `<naam>`

- [ ] Geen UWV-skill of eerdere aanbeveling dekt dit af
- [ ] "Waarom" is één Nederlandse zin voor een collega die de skill niet kent
- [ ] Ik heb de skill minstens eenmaal zelf gebruikt
- [ ] De bron heeft een open licentie (MIT, Apache-2.0 of vergelijkbaar)
- [ ] De bron is een onderhouden repository van een bekende maker, en ik heb `SKILL.md` en eventuele scripts gelezen
