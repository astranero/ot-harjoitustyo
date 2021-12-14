# Käyttöohje

Projektin viimeisin lähdekoodi saadaan valitsemalla Assets-osion alapuolelta Source code (zip).

## Konfigurointi

Tallentamiseen käytettävän tiedoston nimi on alustettu merkkijonolla "Softfit", mutta se voidaan muuttaa halutessaan database_connection.py tiedostossa.
Tallentamiseen käytettävä tietokanta luodaaan automaattisesti database-hakemistoon, jos sitä ei ole jo valmiiksi siinä.

## Ohjelman käynnistäminen. 

Ennen käynnistämistä on asennettava riippuvuudet seuraavalla komennolla:
`poetry install`

Seuraavaksi on alustettava tietokanta komennolla:
`poetry run invoke build`

Nyt ohjelma voidaan käynnistää seuraavasti:
`poetry run invoke start`

## Kirjautuminen

Sovelluksen käynnistyessä aloitusnäkymä on seuraava:

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kirjautuminen.png" width=760>

Kirjautuminen tapahtuu syöttämällä uniikin sähköpostin ja salasanan, jonka jälkeen painamalla login siirrytään sovelluksen käyttäjänäkymään.

## Rekisteröityminen

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/rekisteroityminen.png" width=760>

## Käyttäjänäkymän selostus

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kayttaja_nakyma.png" width=760>

## Laskin näkymän selostus

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/laskin.png" width=760>