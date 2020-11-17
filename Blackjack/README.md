# Blackjack

Sovelluksen avulla on mahdollista pelata virtuaalirahalla Blackjack-korttipeliä talon jakajaa vastaan.

Sovellus on tässä vaiheessa suoritettavissa vain komentoriviltä, mutta seuraavilla viikoilla se saa graafisen käyttöliittymän, sekä pelaajahallinnan rekisteröitymisen ja tuloslistauksen muodossa.

Sovellus on tehty Helsingin yliopiston Tietojenkäsittelytieteen kurssin Ohjelmistotekniikka harjoitustyönä.

## Python-versio
Sovellus on testattu Python-versiolla '3.8.6'. Python-versiota '3.8' vanhemmilla toimintaa ei voida taata.

## Dokumentaatio


## Asennus

1. Asenna riippuvuut komennolla:
```bash
python3 -m pipenv install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:
```bash
python3 -m pipenv run build
```

3. Käynnistä sovellus komennolla:
```bash
python3 -m pipenv run start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
python3 -m pipenv run start
```

### Testaus

Testit suoritetaan komennolla:

```bash
python3 -m pipenv run test
```

### Testikattavuus

Testikattavuus kerätään kommenolla:

```bash
python3 -m pipenv run coverage
```

Tämän jälkeen raportin voi generoida komennolla:

```bash
python3 -m pipenv run coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.
