# create-pr

Gebruik deze skill wanneer het werk op je branch is gecommit en klaar is voor review. De agent
bepaalt de huidige branch en de basisbranch, zoekt het PR-sjabloon van de repository op, en
leest de commits en diffs ten opzichte van de basisbranch. Daaruit vult hij de secties van het
sjabloon en stelt hij een titel voor in conventional-commit vorm. Voordat er iets wordt
aangemaakt vraagt hij of er nog tests moeten worden gedraaid; daarna opent hij een draft pull
request. De skill werkt uitsluitend met gecommitte wijzigingen, dus commit voordat je hem
aanroept. Heeft de repository geen PR-sjabloon, of loopt de branch niet voor op de basisbranch,
dan stopt de agent en zegt hij waarom, in plaats van zelf een indeling te bedenken.

Deze skill is de tegenhanger van [`grilling`](../README.md#aanbevolen-skills-van-derden): grilling hoort aan het begin van
een branch, wanneer nog niet vaststaat wat je gaat bouwen, en `create-pr` hoort aan het eind,
wanneer het gebouwd en gecommit is. De inhoud is overgenomen uit de skills-map van
GAIT-kennisassistent-backend, zodat een pull request in beide repositories op dezelfde manier
tot stand komt.
