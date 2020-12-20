# Käyttöohje

Lataa projektin viimeisin versio lähdekoodista ja navigoi komentorivillä kansioon minne purit sen.

## Ohjelman käynnistäminen

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

## Ohjelma käyttäminen
Seuraa komentoriville ilmestyviä ohjeita.

### Näppäinkomennot
**Ennen käden aloittamista:**

- d - Aloita uusi peli / jaa uusi kortti
- +/- Muuta panoksen kokoa
- o - Lisävalinnat
  - s - Tallenna peli
  - l - Lataa peli
  - q - Lopeta sovellus

**Pelin aikana:**

- h - Ota uusi kortti
- s - Luovuta vuorosi jakajalle

**Käden jakaminen (split):**

- p - Älä jaa kättä
- s - Jaa käsi
  - h - Ota uusi kortti
  - p - Jatka seuraavaan käteen tai luovuta vuoro jakajalle