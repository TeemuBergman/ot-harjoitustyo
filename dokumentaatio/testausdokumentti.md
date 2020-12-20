# Testausdokumentti

Ohjelmaa on testattu sekä automatisoiduin yksikkö- ja integraatiotestein unittestilla sekä manuaalisesti tapahtunein järjestelmätason testein.

## Testikattavuus

Testauksia on laajennettu koskemaan jokaista luokkaa ja testauksen haarautumakattavuus on tällä hetkellä 70%`.

![](kattavuusraportti.jpg)

## Pylint

Pylintillä suoritettujen testien arvosana on tällä hetkellä `10.0/10`. Koodia on muokattu Pylintin antamien ilmoitusten mukaisesti ja jokaiselle luokalle, metodille sekä funktiolle on pyritty lisäämään sen toimintaa selittävä docstring.

## Järjestelmätestaus

Sovelluksen järjestelmätestausta on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovellus on haettu ja sen asennusta on testattu [käyttöohjeen](kayttoohje.md) mukaisesti Windows-ympäristössä. Tulevaisuudessa nämä testit laajennetaan myös Linux-ympäristöön.

