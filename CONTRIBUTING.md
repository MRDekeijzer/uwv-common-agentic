# Bijdragen aan de registry

Elke pull request voegt **één skill** toe als één map: `skills/<naam>/SKILL.md`.
De documentatie is geen apart bestand — die staat in de frontmatter en in de verplichte
secties van diezelfde `SKILL.md`. Zo wordt de documentatie meegeïnstalleerd met de skill
en kan ze er niet van af gaan drijven.

De documentatie in deze repo is Nederlands. De inhoud van een skill mag Engels zijn.

## De vier eisen

Een pull request wordt pas gemerged als alle vier kloppen. Het PR-sjabloon vraagt precies
hierom, in deze volgorde.

### 1. Er bestaat nog geen skill die dit doet

Kijk dit na vóórdat je iets schrijft:

```bash
npx skills add MRDekeijzer/uwv-common-agentic --list   # wat deze registry al heeft
npx skills find <trefwoord>                            # wat er buiten UWV al is
```

Loop ook de catalogustabel in [README.md](README.md) door. Noem in je pull request de skill
die er het dichtst bij zit, en leg in één zin uit waarom die jouw geval niet afdekt.
"Ik heb gekeken en niets gevonden" telt niet — noem de dichtstbijzijnde buur.

Komt een bestaande skill al voor 80% in de buurt? **Verbeter die skill dan.** Een pull
request die een bestaande `SKILL.md` aanpast is sneller te reviewen en beter voor gebruikers
dan een bijna-duplicaat.

### 2. De use case is duidelijk en staat opgeschreven

`metadata.use-case` is één zin, in de vorm *"<doe wat> wanneer <situatie>"*. Die zin komt
rechtstreeks in de catalogus in de README, dus schrijf hem in het Nederlands en voor iemand
die jouw skill nog nooit heeft gezien — ook als de rest van de skill Engels is.

Het veld `description` is iets anders, en belangrijker: dat is de **enige** tekst die een
agent ziet bij de beslissing om jouw skill te laden. Schrijf het als een trigger, niet als
een samenvatting, en gebruik de woorden die een gebruiker echt zou typen. Minimaal 40
tekens; korter wijst de validator af.

### 3. Je benoemt voor welke projecten het nuttig is

`metadata.projects` is een niet-lege lijst met concrete contexten, bijvoorbeeld
`[python-backends, azure-data-pipelines, react-frontends]`. Kun je er geen twee noemen, dan
is de skill waarschijnlijk persoonlijk in plaats van gemeenschappelijk — houd hem dan in je
eigen `~/.claude/skills`.

### 4. De documentatie staat in de SKILL.md

Twee secties zijn verplicht en CI controleert erop:

- `## When to use` — de situaties waarin de skill moet aanslaan.
- `## When not to use` — de grens. Deze sectie houdt de registry bruikbaar bij 50 skills,
  en het is de sectie die een reviewer als eerste leest.

De koppen zijn Engels omdat een skill zelf Engels mag zijn; de tekst eronder mag Nederlands.

## Het SKILL.md-contract

```markdown
---
name: mijn-skill                    # moet gelijk zijn aan de mapnaam, kebab-case
description: Use when <situatie> to <resultaat>. Covers <woorden die een gebruiker typt>.
metadata:
  use-case: Eén zin voor de catalogus in de README.
  projects: [python-backends, azure-data-pipelines]
  owner: '@je-github-handle'        # wie je aanspreekt als het stuk gaat
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

`npx skills init <naam>` genereert een startsjabloon; voeg daar het `metadata:`-blok aan toe.

Alles wat de skill verder nodig heeft (scripts, naslag, templates) zet je in dezelfde map
naast `SKILL.md` en wordt mee geïnstalleerd.

## Werkwijze: trunk-based

We werken trunk-based. `main` is altijd de waarheid en is beschermd: je kunt er alleen via
een pull request in, en er wordt gesquasht bij het mergen.

- Vertak van een actuele `main` en houd de branch kort — uren tot een paar dagen, niet weken.
- Eén skill per pull request. Klein en vaak mergen is sneller te reviewen dan één grote stapel.
- Na het mergen wordt je branch verwijderd; haal `main` op en begin opnieuw vanaf daar.

Branch- en PR-namen volgen [Conventional Commits](https://www.conventionalcommits.org/):

```
feat/<korte-omschrijving>     # nieuwe skill of nieuwe functionaliteit
fix/<korte-omschrijving>      # herstel van een bestaande skill of tooling
docs/<korte-omschrijving>     # alleen documentatie
chore/<korte-omschrijving>    # onderhoud, CI, opruimen
```

**Commitberichten en PR-titels zijn Engels**, ook al is de documentatie Nederlands. De
git-historie leest zo hetzelfde als die van elk ander project, en een skill die we ooit
buiten UWV delen hoeft niet te worden herschreven.

De titel van de pull request is de commitregel die na het squashen in `main` belandt, dus
schrijf hem in dezelfde vorm: `feat: add skill for alembic migrations`.

## Voordat je de pull request opent

```bash
python3 tools/validate_skills.py --fix   # werkt de catalogus in de README bij
python3 tools/validate_skills.py         # moet 0 teruggeven — dit draait CI ook
```

De validator controleert de mechanische regels (naamgeving, verplichte metadata, verplichte
secties, actuele catalogus), zodat de review alleen over de afweging gaat: *is dit een
duplicaat, en is de use case echt?*

## Review

`@FrisoHarlaar` en `@MRDekeijzer` beheren deze registry en worden via CODEOWNERS automatisch
als reviewer toegevoegd. Eén goedkeuring is genoeg om te mergen. We streven naar een review
binnen twee werkdagen.

Een skill wordt gemerged met `status: experimental`. Zet hem in een volgende pull request op
`supported` zodra hij in een echt project is gebruikt — dat is het moment om te repareren wat
dat eerste echte gebruik aan het licht bracht.

Uitfaseren: zet `status: deprecated`, schrijf in `## When not to use` wat je in plaats
daarvan gebruikt, en laat de skill nog een kwartaal staan voordat je hem verwijdert.

## Repo-instellingen (alleen beheerders)

De trunk-based werkwijze hierboven leunt op instellingen die je één keer zet. Ze vragen
admin-rechten op de repository. Onderstaande commando's zetten ze allemaal.

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

`main` beschermen: alleen via een pull request, met een groene `validate` en één
goedkeuring van een CODEOWNER:

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

`enforce_admins` staat bewust op `false`: we zijn met twee beheerders, en anders kan er
niets meer gemerged worden zodra er één afwezig is. `strict: true` betekent dat een branch
bij moet zijn met `main` voordat er gemerged kan worden — dat hoort bij trunk-based werken
en is te doen zolang branches kort blijven.

Controleren of het goed staat:

```bash
gh api repos/MRDekeijzer/uwv-common-agentic/branches/main/protection --jq '{
  checks: .required_status_checks.contexts,
  reviews: .required_pull_request_reviews.required_approving_review_count,
  codeowners: .required_pull_request_reviews.require_code_owner_reviews
}'
```
