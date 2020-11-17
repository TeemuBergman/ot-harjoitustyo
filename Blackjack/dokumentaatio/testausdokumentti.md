# Testausdokumentti

Ohjelmaa on testattu sekä automatisoiduin yksikkö- ja integraatiotestein unittestilla sekä manuaalisesti tapahtunein järjestelmätason testein.

## Testikattavuus

Testaukset ovat vasta aluillaan ja oikeastaan vain _player.py_ tämän hetkinen versio on testattu. Tästä johtuen testien kattavuus on tällä hetkellä vain 26%.

![](kattavuusraportti.jpg)

Testaamatta jäivät _game.py_, _main.py_ sekä osittain _shoe.py_. Nämä lisätään mukaan testeihin seuraavassa päivityksessä.

## Järjestelmätestaus

Sovelluksen järjestelmätestausta on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovellus on haettu ja sen asennusta on testattu käyttöohjen mukaisesti Windows-ympäristössä. Tulevaisuudessa nämä testit laajennetaan myös Linux-ympäristöön.

## Laatuongelmat

Sovellus on tällä hetkellä ensimmäisessä versiossaan, eikä se edusta lopullista tuotetta.
