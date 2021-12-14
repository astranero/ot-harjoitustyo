# Arkkitehtuurikuvaus

## Rakenne

Ohjelmakoodin pakkausrakenne on seuraavan kaavion mukainen:

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Pakkauskaavio.png" width=760>

Sovelluksen rakenne koostuu käyttöliittymäkerroksesta, sovelluslogiikkakerroksesta  ja tallennuslogiikasta vastaavasta kerroksesta.
ui-hakemistossa on sovelluksen käyttöliittymästä ja services-hakemistossa sovelluslogiikasta vastaava koodi. repositories-hakemisto sisältää tallentamisesta huolehtivaa koodia. Hakemistossa entities sisältää toisaalta luokkia, jotka kuvaavat oikean maailman olioita. Tässä tapauksessa käyttäjä-oliota.

## Käyttöliittymä

Ei vielä päivitetty

## Sovelluslogiikka

Toiminnallisuuksista vastaavat luokkien UserService, EntityService, Calculator, Intake oliot.
Luokat tarjoavat käyttöliittymälle toimintoja metodeillaan. 
UserService-luokan metodeja ovat esimerkiksi: 
- 'user_delete(email, password)'
- 'change_password(in_email, password, in_password1, in_password2)'
- 'password_check(password1, password2)'
- 'email_check(in_email)'

UserService on riippuvainen DatabaseTools-luokasta, joka on käyttäjän tietojen tallentamisesta huolehtiva luokka. UserService käsittelee kirjautumiseen, rekisteröitymiseen ja käyttäjän muokkaamiseen liittyviä toiminnallisuuksia. 

EntityService-luokan metodeja ovat esimerkiksi:
- `_create_user_entity()`
- 'return_user_entity()'

Calculator-luokan metodeja ovat esimerkiksi:
- 'protein_calorie_count(protein_grams)'
- 'carbohydrates_calorie_count(carbohydrates_grams)'
- '_lean_body_mass_estimate()'
- 'bmr_count(lean_body_mass)'
- 'total_daily_energy_expenditure(bmr, activity_level)'

Calculator-luokka käsittelee metodiensa avulla repositorion tallennettujen arvojen ja käyttäjän käyttöliittymästä valitsemien vaihtoehtojen perusteella erilaisia laskutoimituksia, kuten lepoaikaisen energiakulutuksen laskemista.

Suhteita kuvaava luokka/pakkauskaavio:

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/luokka_pakkauskaavio.png" width=760>


## Tietojen pysyväistallennus

## Päätoiminnallisuudet

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Sekvenssikaavio.png" width=760>
