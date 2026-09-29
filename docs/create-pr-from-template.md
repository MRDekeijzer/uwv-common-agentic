# create-pr-from-template

Opent een pull request op basis van het PR-sjabloon van de repository, gevuld met de commits
op de huidige branch.

## Wanneer gebruiken

- Je wilt een pull request openen voor werk dat op de huidige branch is gecommit.
- De branch loopt voor op de basisbranch en het werk is klaar voor review.
- Je vraagt de agent om een PR te maken, te openen of in te dienen.

## Wanneer niet gebruiken

- Het werk is nog niet gecommit. De skill leest alleen gecommitte wijzigingen; commit eerst.
- De branch loopt niet voor op de basisbranch. Er is dan niets om in een pull request te zetten.
- De repository heeft geen PR-sjabloon en je wilt een eigen indeling. Geef die indeling dan
  zelf op, zodat de agent er geen bedenkt.

## Wat de skill doet

De skill bepaalt de huidige branch en de basisbranch, zoekt het PR-sjabloon op de plaatsen
waar GitHub het verwacht, en leest de commits en diffs ten opzichte van de basisbranch. Op
basis daarvan vult hij de secties van het sjabloon en stelt hij een titel voor in
conventional-commit vorm.

Voordat de pull request wordt aangemaakt, vraagt de skill twee dingen: of er nog tests moeten
worden gedraaid en of er een regel aan `CHANGELOG.md` moet worden toegevoegd. De pull request
wordt pas aangemaakt nadat je die vragen hebt beantwoord.
