# Blackjack

Sovelluksen avulla on mahdollista pelata virtuaalirahalla Blackjack-korttipeliä talon jakajaa vastaan.

Sovellus on tässä vaiheessa suoritettavissa vain komentoriviltä, mutta seuraavilla viikoilla se saa graafisen käyttöliittymän, sekä pelaajahallinnan rekisteröitymisen ja tuloslistauksen muodossa.

Sovellus on tehty Helsingin yliopiston Tietojenkäsittelytieteen kurssin Ohjelmistotekniikka harjoitustyönä.

## Python-versio
Sovellus on testattu Python-versiolla `3.8.6` ja tätä Python-versiota vanhemmilla toimintaa ei voida taata.

## Dokumentaatio
- [Käyttöohje](./Blackjack/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./Blackjack/dokumentaatio/vaatimusmaarittely.md)
- [Testausdokumentti](./Blackjack/dokumentaatio/testausdokumentti.md)
- [Arkkitehtuurikuvaus](./Blackjack/dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](työaikakirjanpito.txt)

## Asennus

1. Asenna riippuvuudet komennolla:

```
python3 -m pipenv install
```

2. Käynnistä sovellus komennolla:

```
python3 -m pipenv run start
```

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