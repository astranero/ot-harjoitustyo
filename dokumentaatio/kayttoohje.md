# Käyttöohje

Projektin viimeisin lähdekoodi saadaan valitsemalla Assets-osion alapuolelta Source code (zip).

## Konfigurointi

Käyttäjän tietojen tallentamiseen käytettävän tiedoston nimi on alustettu merkkijonolla "Softfit", mutta se voidaan muuttaa halutessaan database_connection.py tiedostossa. Tekstitiedostoon records.txt tallennetaan käyttäjän päivänaikana asettamat proteiini-, hiilihydraatti ja rasvamäärät csv-tiedostona. 
Tallentamiseen käytettävä tietokannat luodaaan automaattisesti database-hakemistoon, jos sitä ei ole jo valmiiksi siinä.

## Ohjelman käynnistäminen. 

Ennen käynnistämistä on asennettava riippuvuudet seuraavalla komennolla:
`poetry install`

Seuraavaksi on alustettava tietokannat komennolla:
`poetry run invoke build`

Nyt ohjelma voidaan käynnistää seuraavasti:
`poetry run invoke start`

## Kirjautuminen

Sovelluksen käynnistyessä aloitusnäkymä on seuraava:

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kirjautuminen.png" width=760>

Kirjautuminen tapahtuu syöttämällä uniikki sähköposti ja salasana, jonka jälkeen painamalla __Login__ siirrytään sovelluksen käyttäjänäkymään.

## Rekisteröityminen

__Create User__ painikkeen avulla pystytään luomaan käyttäjän sovellukselle. Tämä siirtää meidät kirjautumisnäkymään.

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/rekisteroityminen.png" width=760>

Täyttämällä vaaditut kentät ohjeiden mukaisesti ja painamalla __Register__ saadaan luotua käyttäjä. Tämän jälkeen päästään takaisin aloitusnäkymään painammalla 
__Change to login Screen__ 

## Käyttäjänäkymän selostus

Käyttäjänäkymässä painamalla __change password__ voidaan vaihtaa salasana ja painamalla __Delete Account__ poistaa käyttäjätili. Näiden painaminen käynnistää pop-up ikkunan, jonka avulla varmistetaan toiminta. 

- __Log out__ kirjaa meidät ulos aloitusnäkymään.
- __Add weight__ lisää halutun painon tietokantaan.
- __Delete weight__ poistaa painon tietokannasta.
- __Track__ käynnistää matplotlib modulin avulla toteutetun ikkunan, jonka avulla seurataan painon muutosta.
- Painamalla __Calculator__ siirrytään laskin-näkymään.

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kayttaja_nakyma.png" width=760>

## Laskin näkymän selostus

Laskin näkymässä on erilaisia vaihtoehtoja laskea BMR. Seuraamalla näkymän ohjeita saadaan laskettua kalorimäärä.
Loogisista syistä ensin on laskettava BMR, jonka jälkeen voi laskea vasta TDEE.

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/laskin.png" width=760>
