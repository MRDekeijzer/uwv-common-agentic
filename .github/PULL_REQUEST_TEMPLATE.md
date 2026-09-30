<!-- Titel in conventional-commit vorm, bijvoorbeeld "feat: add skill for alembic migrations".
     Na het squashen is dat de commitregel in main.

     Houd het deel dat past en verwijder het andere. Bij een fix, docs of chore verwijder je
     beide en beschrijf je wat er verandert. Zie CONTRIBUTING.md. -->

## Eigen skill

### Toevoegen

- [ ] Dichtstbijzijnde bestaande skill: `<naam, of "geen">`, die dit niet afdekt omdat ...
- [ ] Use case: <gelijk aan metadata.use-case>
- [ ] `description` gebruikt de woorden die een gebruiker typt
- [ ] Ik heb de skill minstens eenmaal zelf gebruikt
- [ ] `python3 scripts/validate_skills.py` geeft 'ok'

### Updaten

### Verwijderen

## Third party skill aanbeveling

### Toevoegen

- [ ] Geen UWV-skill of eerdere aanbeveling dekt dit af
- [ ] Ik heb de skill minstens eenmaal zelf gebruikt
- [ ] De bron heeft een open licentie (MIT, Apache-2.0 of vergelijkbaar)
- [ ] De bron is een onderhouden repository van een bekende maker, en ik heb `SKILL.md` en eventuele scripts op die commit gelezen
- [ ] Het installatiecommando pint een volledige commit-SHA (`--pin`), dezelfde als in `marketplace.json`
- [ ] De skill staat in `marketplace.json` onder de plugin van de bron, en die plugin staat in de kolom "Plugin"

### Updaten

### Verwijderen
