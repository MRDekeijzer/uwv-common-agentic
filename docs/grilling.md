# grilling

Bevraag een plan of ontwerp kritisch voordat het gebouwd wordt, met één vraag per keer.

## Wanneer gebruiken

- Voordat je iets bouwt waarvan de vorm nog ter discussie staat.
- Bij een plan, ontwerp, specificatie of architectuurbesluit dat nog niet is getoetst.
- Je vraagt de agent om je plan onder druk te zetten of er gaten in te zoeken.

## Wanneer niet gebruiken

- Het werk is al besloten en je wilt het laten bouwen. Doorvragen houdt de uitvoering dan op.
- Bij een enkele feitelijke vraag met één juist antwoord. Zoek dat antwoord op.
- Wanneer de agent zelf iets moet beslissen. De skill legt jouw beslissingen bloot en geeft
  geen eigen oordeel terug als vraag.

## Wat de skill doet

De agent bevraagt het plan punt voor punt en werkt de beslisboom af, waarbij afhankelijkheden
tussen beslissingen één voor één worden opgelost. Bij elke vraag geeft hij zijn eigen
voorkeursantwoord.

De vragen komen één per keer, en de agent wacht op je antwoord voordat hij verdergaat.
Feiten die hij zelf kan opzoeken in de omgeving, bijvoorbeeld in het bestandssysteem, zoekt
hij op in plaats van ze te vragen. De beslissingen blijven aan jou. De agent gaat pas tot
uitvoering over nadat je hebt bevestigd dat jullie hetzelfde beeld hebben.
