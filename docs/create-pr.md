# create-pr

Gebruik deze skill als het werk op je branch gecommit is en klaar is voor review. De agent
bepaalt de huidige branch en de basisbranch, zoekt het PR-sjabloon van de repository op en
leest de commits en diffs ten opzichte van de basisbranch. Daarmee vult hij het sjabloon in en
stelt hij een titel in conventional-commit vorm voor. Hij vraagt eerst of er nog tests gedraaid
moeten worden, pusht de branch als dat nodig is en opent daarna een draft pull request. De
skill kijkt alleen naar gecommitte wijzigingen, dus commit voordat je hem aanroept. Heeft de
repository geen PR-sjabloon, of loopt de branch niet voor op de basisbranch, dan stopt de agent
en zegt hij waarom. Hij verzint dan geen eigen indeling.
