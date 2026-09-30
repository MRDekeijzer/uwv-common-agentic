<!-- Titel in conventional-commit vorm, bijvoorbeeld "feat: add skill for alembic migrations".
     Na het squashen is dat de commitregel in main.

     "Voor elke pull request" blijft altijd staan. Van de rest houd je het deel dat past; bij een
     fix, docs of chore verwijder je dat en beschrijf je wat er verandert. Zie CONTRIBUTING.md. -->

## Voor elke pull request

- [ ] Er staat geen gevoelige of interne UWV-informatie in; deze repository is openbaar
- [ ] `gh skill publish --dry-run` en `python3 scripts/validate_skills.py` slagen

## Eigen skill

### Toevoegen

- [ ] Dichtstbijzijnde bestaande skill: `<naam, of "geen">`, die dit niet afdekt omdat ...
- [ ] Use case: <gelijk aan metadata.use-case>
- [ ] `description` gebruikt de woorden die een gebruiker typt
- [ ] Ik heb de skill minstens eenmaal zelf gebruikt

### Updaten

- [ ] Wat er verandert en waarom: ...

### Verwijderen

- [ ] Reden: ...
- [ ] `skills/<naam>/` is weg

## Third party skill aanbeveling

### Toevoegen

- [ ] Geen UWV-skill of eerdere aanbeveling dekt dit af
- [ ] Ik heb de skill minstens eenmaal zelf gebruikt
- [ ] De bron heeft een open licentie (MIT, Apache-2.0 of vergelijkbaar)
- [ ] De bron is een onderhouden repository van een bekende maker, en ik heb `SKILL.md` en eventuele scripts op die commit gelezen
- [ ] Het installatiecommando pint een volledige commit-SHA (`--pin`), dezelfde als in `marketplace.json`
- [ ] De skill staat in `marketplace.json` onder de plugin van de bron, en die plugin staat in de kolom "Plugin"

### Updaten

- [ ] Ik heb het verschil gelezen: `https://github.com/<eigenaar>/<repo>/compare/<oude-sha>...<nieuwe-sha>`
- [ ] De nieuwe SHA staat in `marketplace.json` en in de link en `--pin` in de README
- [ ] Ik heb ook de wijzigingen in de andere skills van die plugin gelezen

### Verwijderen

- [ ] Reden: ...
- [ ] De regel is uit de README en het pad uit `marketplace.json`; een lege plugin is weg
