# Bijdragen aan de registry

Elke pull request voegt één skill toe en bestaat uit twee bestanden:

- `skills/<naam>/SKILL.md`, met de frontmatter en de instructies die het agent-harnas leest.
- `docs/<naam>.md`, met de Nederlandse uitleg voor collega's.

De registry richt zich op GitHub Copilot. Omdat de skills de agent-skills-conventie volgen,
werken ze ook in andere harnassen.

De `SKILL.md` mag Engels zijn, omdat dat voor het model doorgaans beter werkt. De uitleg in
`docs/` is Nederlands, conform UWV-beleid. Die uitleg beschrijft wanneer een collega de skill
moet gebruiken; de `SKILL.md` beschrijft wanneer de agent hem moet laden.

## De vijf eisen

Een pull request wordt alleen gemerged wanneer aan alle vijf de eisen is voldaan. Het
PR-sjabloon vraagt hier in dezelfde volgorde naar.

### 1. Er bestaat nog geen skill die dit doet

Controleer dit voordat je begint met schrijven:

```bash
npx skills add MRDekeijzer/uwv-common-agentic --list   # wat deze registry al bevat
npx skills find <trefwoord>                            # wat er buiten het UWV al bestaat
```

Neem ook de catalogus in [README.md](README.md) door. Noem in je pull request de skill die
het dichtst bij je geval ligt, en licht in één zin toe waarom die het niet afdekt.

Dekt een bestaande skill je geval al voor ongeveer 80 procent af, verbeter dan die skill. Een
pull request die een bestaande `SKILL.md` aanpast is sneller te reviewen en voor gebruikers
beter dan een duplicaat.

### 2. De use case is duidelijk en staat opgeschreven

`metadata.use-case` is één zin in de vorm `<doe wat> wanneer <situatie>`. Deze zin komt
rechtstreeks in de catalogus in de README terecht. Schrijf hem daarom in het Nederlands en
voor iemand die de skill nog niet kent, ook wanneer de rest van de skill Engels is.

Het veld `description` is iets anders en weegt zwaarder: het is de enige tekst die een agent
ziet op het moment dat hij besluit jouw skill te laden. Formuleer het als een trigger in
plaats van als een samenvatting, en gebruik de woorden die een gebruiker daadwerkelijk zou
typen. De minimumlengte is 40 tekens; kortere waarden wijst de validator af.

### 3. Je benoemt voor welke projecten de skill van pas komt

`metadata.projects` is een niet-lege lijst met concrete contexten, bijvoorbeeld
`[python-backends, azure-data-pipelines, react-frontends]`. Zijn er geen twee te noemen, dan
is de skill vermoedelijk persoonlijk in plaats van gemeenschappelijk. Bewaar hem in dat geval
in je eigen `~/.agents/skills/`.

### 4. De verplichte secties staan in de SKILL.md

Twee secties zijn verplicht en worden door CI gecontroleerd:

- `## When to use`: de situaties waarin de skill moet aanslaan.
- `## When not to use`: de grens van de skill. Deze sectie houdt de registry bruikbaar bij
  vijftig skills en wordt door een reviewer als eerste gelezen.

De koppen zijn Engels omdat een skill zelf Engels mag zijn; de tekst eronder mag Nederlands
zijn.

### 5. Er is een Nederlandse uitleg in docs/

Bij elke skill hoort een `docs/<naam>.md` met dezelfde naam als de map in `skills/`. De map
`docs/` is daarmee een spiegel van `skills/`. CI controleert dat het bestand bestaat, dat er
geen uitleg achterblijft zonder skill, en dat twee secties aanwezig zijn:

- `## Wanneer gebruiken`: de situaties waarin een collega deze skill pakt.
- `## Wanneer niet gebruiken`: de gevallen waarin iets anders beter past, met een verwijzing
  naar dat alternatief.

Deze uitleg is bedoeld voor iemand die de skill nog nooit heeft gebruikt en de `SKILL.md` niet
gaat lezen. Schrijf hem daarom in het Nederlands en zonder termen die alleen binnen jouw team
gangbaar zijn.

## Het SKILL.md-contract

```markdown
---
name: mijn-skill                    # gelijk aan de mapnaam, kebab-case
description: Use when <situatie> to <resultaat>. Covers <woorden die een gebruiker typt>.
metadata:
  use-case: Eén zin voor de catalogus in de README.
  projects: [python-backends, azure-data-pipelines]
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

`npx skills init <naam>` genereert een startsjabloon; vul dat aan met het `metadata:`-blok.

## Het docs-contract

```markdown
# mijn-skill

Eén regel over wat de skill doet.

## Wanneer gebruiken
...

## Wanneer niet gebruiken
...

## Wat de skill doet
Wat de agent achtereenvolgens doet, en wat hij aan de gebruiker vraagt.
```

## Indeling van een bijdrage

```
skills/mijn-skill/
  SKILL.md        # frontmatter, When to use, When not to use, How it works
  <overig>        # scripts, templates, naslag; wordt samen met de skill geïnstalleerd
docs/mijn-skill.md  # Nederlandse uitleg, Wanneer gebruiken, Wanneer niet gebruiken
```

Alles wat de skill verder nodig heeft, zoals scripts, naslag en templates, plaats je in
`skills/<naam>/` naast `SKILL.md`. Die bestanden worden samen met de skill geïnstalleerd. De
uitleg in `docs/` wordt niet meegeïnstalleerd en blijft in de repository.

## Werkwijze: trunk-based

De werkwijze is trunk-based. `main` is de bron van waarheid en is beschermd: wijzigingen komen
er alleen via een pull request in, en bij het mergen wordt gesquasht.

- Vertak van een actuele `main` en houd de branch kort: uren tot enkele dagen.
- Eén skill per pull request. Klein en frequent mergen is sneller te reviewen dan één grote
  wijziging.
- Na het mergen wordt je branch verwijderd. Haal `main` op en begin daar opnieuw vanaf.

Branch- en PR-namen volgen [Conventional Commits](https://www.conventionalcommits.org/):

```
feat/<korte-omschrijving>     # nieuwe skill of nieuwe functionaliteit
fix/<korte-omschrijving>      # herstel van een bestaande skill of van tooling
docs/<korte-omschrijving>     # alleen documentatie
chore/<korte-omschrijving>    # onderhoud, CI, opruimen
```

Commitberichten en PR-titels zijn Engels, ook al is de documentatie Nederlands. De
git-historie leest daarmee hetzelfde als die van elk ander project, en een skill die we ooit
buiten het UWV delen hoeft niet te worden herschreven.

De titel van de pull request is de commitregel die na het squashen in `main` belandt. Schrijf
hem daarom in dezelfde vorm: `feat: add skill for alembic migrations`.

## Voordat je de pull request opent

```bash
python3 scripts/validate_skills.py --fix   # werkt de catalogus in de README bij
python3 scripts/validate_skills.py         # moet 0 teruggeven; dezelfde controle als in CI
```

De validator controleert de mechanische regels: naamgeving, verplichte metadata, verplichte
secties in `SKILL.md` en in `docs/<naam>.md`, en een actuele catalogus. De review gaat daarmee
alleen nog over de inhoudelijke afweging, namelijk of dit een duplicaat is en of de use case
reëel is.

## Review

`@FrisoHarlaar` en `@MRDekeijzer` beheren deze registry en worden via CODEOWNERS automatisch
als reviewer toegevoegd. Eén goedkeuring is voldoende om te mergen. We streven naar een review
binnen twee werkdagen.

Een skill wordt gemerged met `status: experimental`. Zet de status in een volgende pull request
op `supported` zodra de skill in een echt project is gebruikt. Dat is het moment om te
verhelpen wat dat eerste gebruik aan het licht heeft gebracht.

Voor uitfaseren geldt: zet `status: deprecated`, beschrijf in `## When not to use` en in
`## Wanneer niet gebruiken` welk alternatief gebruikt moet worden, en laat de skill nog een
kwartaal staan voordat je hem verwijdert. Verwijder bij het opruimen ook `docs/<naam>.md`,
omdat CI een achtergebleven uitleg afkeurt.

## Repo-instellingen (alleen beheerders)

De trunk-based werkwijze hierboven berust op instellingen die eenmalig worden gezet. Daarvoor
zijn admin-rechten op de repository nodig. De onderstaande commando's zetten ze alle.

Alleen squashen bij het mergen, en de branch daarna opruimen:

```bash
gh api -X PATCH repos/MRDekeijzer/uwv-common-agentic \
  -F allow_squash_merge=true \
  -F allow_merge_commit=false \
  -F allow_rebase_merge=false \
  -F delete_branch_on_merge=true \
  -f squash_merge_commit_title=PR_TITLE \
  -f squash_merge_commit_message=PR_BODY
```

`main` beschermen, zodat wijzigingen alleen via een pull request binnenkomen, met een groene
`validate` en één goedkeuring van een CODEOWNER:

```bash
gh api -X PUT repos/MRDekeijzer/uwv-common-agentic/branches/main/protection \
  --input - <<'JSON'
{
  "required_status_checks": { "strict": true, "contexts": ["validate"] },
  "required_pull_request_reviews": {
    "required_approving_review_count": 1,
    "require_code_owner_reviews": true,
    "dismiss_stale_reviews": true
  },
  "enforce_admins": false,
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "required_linear_history": true
}
JSON
```

`enforce_admins` staat bewust op `false`. De registry heeft twee beheerders; met
`enforce_admins: true` kan er niets meer worden gemerged zodra een van beiden afwezig is.
`strict: true` betekent dat een branch bij moet zijn met `main` voordat er gemerged kan
worden. Dat hoort bij trunk-based werken en is haalbaar zolang branches kort blijven.

De instellingen controleren:

```bash
gh api repos/MRDekeijzer/uwv-common-agentic/branches/main/protection --jq '{
  checks: .required_status_checks.contexts,
  reviews: .required_pull_request_reviews.required_approving_review_count,
  codeowners: .required_pull_request_reviews.require_code_owner_reviews
}'
```
