# Bijdragen aan de registry

Een pull request voegt één eigen skill toe, of beveelt één skill van derden aan
([zie hieronder](#een-skill-van-derden-aanbevelen)). Een eigen skill bestaat uit twee bestanden:

- `skills/<naam>/SKILL.md`, met de frontmatter en de instructies die het agent-harnas leest.
- `docs/<naam>.md`, met de Nederlandse uitleg voor collega's.

De skills zijn geschreven voor GitHub Copilot en volgen de agent-skills-conventie, dus ze werken
ook in andere harnassen.

De `SKILL.md` mag Engels zijn, omdat het model daar meestal beter mee werkt. De uitleg in `docs/`
is Nederlands, conform UWV-beleid. Die uitleg vertelt een collega wanneer hij de skill kan
gebruiken; de `SKILL.md` vertelt de agent wanneer hij hem moet laden.

## Eisen voor een eigen skill

We mergen een eigen skill als hij aan de vier eisen hieronder voldoet. Het deel "Eigen skill"
in het PR-sjabloon loopt ze langs.

### 1. Er bestaat nog geen skill die dit doet

Controleer dit voordat je gaat schrijven:

```bash
npx skills add MRDekeijzer/uwv-common-agentic --list   # wat deze registry al bevat
npx skills find <trefwoord>                            # wat er buiten het UWV al bestaat
```

Kijk ook in de tabellen in [README.md](README.md). Noem in je pull request de skill die het
dichtst bij je geval ligt, en zeg in één zin waarom die het niet afdekt.

Dekt een bestaande skill ongeveer 80 procent van je geval, verbeter dan die skill. Een aanpassing
van een bestaande `SKILL.md` is sneller gereviewd, en gebruikers hebben dan geen twee skills
voor hetzelfde.

Dekt een skill van buiten het UWV je geval, [beveel hem dan aan](#een-skill-van-derden-aanbevelen)
en schrijf geen eigen versie. Een kopie loopt achter zodra de maker iets verbetert.

Heb alleen jij iets aan de skill, zet hem dan in je eigen `~/.agents/skills/`.

### 2. De use case staat opgeschreven

`metadata.use-case` is één zin in de vorm `<doe wat> wanneer <situatie>`. Die zin komt
letterlijk in de catalogus in de README. Schrijf hem in het Nederlands, voor iemand die de skill
nog niet kent, ook als de rest van de skill Engels is.

Het veld `description` is belangrijker. Een agent ziet alleen die tekst als hij beslist of hij
je skill laadt. Beschrijf dus wanneer de skill nodig is, met de woorden die een gebruiker
typt, en vat niet alleen samen wat hij doet. De validator wijst een `description` van minder
dan 40 tekens af.

### 3. De verplichte secties staan in de SKILL.md

CI controleert twee secties:

- `## When to use`: de situaties waarin de skill moet aanslaan.
- `## When not to use`: waar de skill ophoudt, zodat de agent hem niet laadt voor iets waar een andere skill beter past.

De koppen zijn Engels omdat de skill Engels mag zijn. De tekst eronder mag Nederlands zijn.

### 4. Er is een Nederlandse uitleg in docs/

Bij elke skill hoort een `docs/<naam>.md` met dezelfde naam als de map in `skills/`. CI
controleert dat het bestand bestaat en niet bijna leeg is, en dat er geen uitleg zonder skill
achterblijft.

Schrijf een of twee alinea's; vertaal de `SKILL.md` niet. Beschrijf wanneer een collega de
skill pakt en hoe hij zich verhoudt tot andere skills: welke je in plaats daarvan gebruikt, of
welke erop volgt. Schrijf voor iemand die de skill nog nooit heeft gebruikt en de `SKILL.md`
niet wil lezen, en gebruik geen termen die alleen in jouw team gangbaar zijn.

## Een skill van derden aanbevelen

Een goede skill van buiten het UWV kopieer je niet naar `skills/`. Je voegt één regel toe aan
de tabel "Aanbevolen skills van derden" in [README.md](README.md); dat kan in de webeditor van
GitHub. Collega's installeren de skill dan uit de bron, en `npx skills update` haalt de
verbeteringen van de maker op.

Latere versies heeft niemand van ons bekeken. We mergen een aanbeveling daarom alleen als:

1. geen UWV-skill en geen eerdere aanbeveling dit al afdekt;
2. de kolom "Waarom" één Nederlandse zin is voor een collega die de skill niet kent;
3. je de skill minstens eenmaal zelf hebt gebruikt;
4. de bronrepository een zichtbare open licentie heeft, zoals MIT of Apache-2.0;
5. de bron een onderhouden repository van een bekende maker is, geen willekeurige fork. De
   reviewer leest de `SKILL.md` en eventuele scripts van de huidige versie.

Controleer de skillnaam met `npx skills add <eigenaar>/<repo> --list` en zet het
installatiecommando in de laatste kolom. Vul in de pull request het deel "Aanbeveling" van het
PR-sjabloon in en verwijder het deel "Eigen skill".

Zet de skill ook in [`.github/plugin/marketplace.json`](.github/plugin/marketplace.json). Elke
bronrepository is daar één plugin, genoemd naar de eigenaar (`mattpocock`), met `"strict": false`
en in `source` de volledige commit-SHA die de reviewer heeft gelezen:

- Staat de bron er al in, voeg dan alleen het pad van de skill toe aan `skills` van die plugin.
  Heb je een nieuwere commit nodig, dan geldt de nieuwe SHA voor alle skills van die plugin; de
  reviewer bekijkt dan ook wat er in de andere skills veranderde.
- Is de bron nieuw, voeg dan een plugin toe.

Zet de pluginnaam in de kolom "Plugin" van de tabel. CI controleert dat de tabel en
`marketplace.json` dezelfde skills noemen en dat elke plugin van derden op een commit-SHA staat.
Een nieuwere versie van de maker is een nieuwe pull request die alleen die SHA aanpast.

Stopt de maker met onderhoud, of werkt de skill niet meer, haal de regel dan uit de tabel en het
pad uit `marketplace.json`; een plugin zonder skills haal je helemaal weg.

## Het SKILL.md-contract

```markdown
---
name: mijn-skill                    # gelijk aan de mapnaam, kebab-case
description: Use when <situatie> to <resultaat>. Covers <woorden die een gebruiker typt>.
license: MIT
metadata:
  use-case: Eén zin voor de catalogus in de README.
  owner: '@je-github-handle'        # wie verantwoordelijk is voor onderhoud
  status: experimental              # experimental | supported | deprecated
---

# Mijn skill

## When to use
...

## When not to use
...

## How it works
Stappen, commando's, voorbeelden.
```

`npx skills init <naam>` maakt een startsjabloon; voeg daar het `metadata:`-blok aan toe.

## Indeling van een bijdrage

```
skills/mijn-skill/
  SKILL.md        # frontmatter, When to use, When not to use, How it works
  <overig>        # scripts, templates, naslag; wordt samen met de skill geïnstalleerd
docs/mijn-skill.md  # Nederlandse uitleg in een of twee alinea's
```

Scripts, naslag en templates die de skill nodig heeft, zet je in `skills/<naam>/` naast
`SKILL.md`. Ze worden samen met de skill geïnstalleerd. De uitleg in `docs/` blijft in de
repository en wordt niet geïnstalleerd.

## Werkwijze: trunk-based

`main` is beschermd. Wijzigingen komen er alleen via een pull request in, en bij het mergen
squashen we.

- Houd pull requests klein: één skill per pull request reviewt sneller dan een grote wijziging.
- Hangen skills van elkaar af, gebruik dan stacked pull requests.
- Na het mergen wordt je branch verwijderd. Haal `main` op en begin daar een nieuwe branch.

Branch- en PR-namen volgen [Conventional Commits](https://www.conventionalcommits.org/):

```
feat/<korte-omschrijving>     # nieuwe skill of nieuwe functionaliteit
fix/<korte-omschrijving>      # herstel van een bestaande skill of van tooling
docs/<korte-omschrijving>     # alleen documentatie
chore/<korte-omschrijving>    # onderhoud, CI, opruimen
```

Commit-messages en PR-titels zijn Engels, ook al is de documentatie Nederlands. Na het squashen
is de titel van de pull request de commitregel in `main`, dus schrijf hem in die vorm:
`feat: add skill for alembic migrations`.

## Voordat je de pull request opent

```bash
python3 -m pip install pyyaml              # eenmalig
gh skill publish --dry-run                 # agentskills.io-spec: naamgeving, mapnaam, verplichte velden
python3 scripts/validate_skills.py --fix   # werkt de catalogus in de README bij
python3 scripts/validate_skills.py         # moet 0 teruggeven; dezelfde controle als in CI
```

`gh skill publish --dry-run` (GitHub CLI 2.90 of nieuwer) controleert de agentskills.io-spec. De
validator controleert wat de registry daarbovenop eist: verplichte metadata, de verplichte secties
in `SKILL.md`, of `docs/<naam>.md` bestaat en of de catalogus actueel is. In de review hoeven we dan alleen
nog te beoordelen of de skill een duplicaat is en of de use case reëel is.

## Review

`@MRDekeijzer` en `@FrisoHarlaar` beheren de registry en worden via CODEOWNERS automatisch als
reviewer toegevoegd. Eén goedkeuring is genoeg om te mergen. We proberen binnen een week te
reviewen.

Een nieuwe skill krijgt `status: experimental`. Heb je hem in een echt project gebruikt, zet de
status dan in een volgende pull request op `supported` en herstel meteen wat dat gebruik aan
problemen liet zien.

Om een skill uit te faseren zet je `status: deprecated` en beschrijf je in `## When not to use`
en in `docs/<naam>.md` welk alternatief collega's moeten gebruiken. Laat de skill daarna nog een
kwartaal staan. Verwijder bij het opruimen ook `docs/<naam>.md`, want CI keurt een uitleg zonder
skill af.
