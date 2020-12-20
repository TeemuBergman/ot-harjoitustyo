# Blackjack

Sovelluksen avulla on mahdollista pelata virtuaalirahalla Blackjack-korttipeliä talon jakajaa vastaan (jakajan täytyy ottaa kortteja 17 pisteeseen asti).

> Blackjack on suuresti  venttiä muistuttava korttipeli, jossa tavoitteena on saada kahdella tai  useammalla kortilla pelikäsi, jolla voittaa jakajan käden joko siten,  että pelaajan käden pistemäärä on lähempänä kahtakymmentäyhtä kuin  jakajan tai siten että jakajan käden pistemäärä menee yli  kahdenkymmenenyhden [Blackjack, 2020].

Sovellus on tässä vaiheessa suoritettavissa vain komentoriviltä, mutta seuraavilla viikoilla se saa graafisen käyttöliittymän, sekä pelaajahallinnan rekisteröitymisen ja tuloslistauksen muodossa.

Sovellus on tehty Helsingin yliopiston Tietojenkäsittelytieteen kurssin Ohjelmistotekniikka harjoitustyönä.

## Python-versio
Sovellus on testattu Python-versiolla `3.8.6` ja tätä Python-versiota vanhemmilla toimintaa ei voida taata.

## Release
Viikon 6 release löytyy [täältä](https://github.com/TeemuBergman/ot-harjoitustyo/releases/tag/viikko6).

Viikon 5 release löytyy [täältä](https://github.com/TeemuBergman/ot-harjoitustyo/releases/tag/viikko5).

## Dokumentaatio
- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Testausdokumentti](./dokumentaatio/testausdokumentti.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/työaikakirjanpito.txt)

## Asennus

1. Navigoi sovelluksen kansioon (./Blackjack)
2. Asenna riippuvuudet komennolla:
```
python3 -m pipenv install
```
3. Suorita alustustoimenpiteet komennolla:
```
python3 -m pipenv run build
```
4. Käynnistä sovellus komennolla:
```
python3 -m pipenv run start
```
5. Katso pelin komennot [käyttöohje](./dokumentaatio/kayttoohje.md) tiedostosta.

## Komentorivitoiminnot

#### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```
python3 -m pipenv run start
```

#### Testaus

Testit suoritetaan komennolla:

```
python3 -m pipenv run test
```

#### Testikattavuus

Testikattavuus kerätään kommenolla:

```
python3 -m pipenv run coverage
```

Tämän jälkeen raportin voi generoida komennolla:

```
python3 -m pipenv run coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

#### Pylint

Tiedoston [.pylintrc](./Blackjack/.pylintrc) määrittelemät koodin laatua tutkivat tarkastukset voi suorittaa komennolla:

```
python3 -m pipenv run lint
```

Tällä hetkellä tarkistusten arvosana on `10.00/10`

## Lähdeluettelo

Blackjack. (2020). Wikipedia. Haettu 20.12.2020 osoitteesta //fi.wikipedia.org/wiki/Blackjack