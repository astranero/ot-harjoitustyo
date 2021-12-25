# Arkkitehtuurikuvaus

## Rakenne

Ohjelmakoodin pakkausrakenne on seuraavan kaavion mukainen:

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Pakkauskaavio.png" width=760>

Sovelluksen rakenne koostuu käyttöliittymäkerroksesta, sovelluslogiikkakerroksesta  ja tallennuslogiikasta vastaavasta kerroksesta.
ui-hakemistossa on sovelluksen käyttöliittymästä ja services-hakemistossa sovelluslogiikasta vastaava koodi. repositories-hakemisto sisältää tallentamisesta huolehtivaa koodia. 

## Käyttöliittymä

Käyttöliittymällä on useita erillisiä näkymiä.
Sovelluksen käynnistäminen johtaa kirjautumisnäkymään. Tästä voidaan kirjautumalla siirtyä käyttäjänäkymään, josta edelleen päästään joko laskuri- tai track-näkymään. Toisaalta painamalla "Create User" siirrytään uuden käyttäjän luomiselle tarkoitettuun näkymään.

Käyttöliittymä on parhaan mukaan eristetty sovelluslogiikasta. Käyttöliittymä kutsuu sekä UserService-, Calculator-luokkien että RecordService- ja DatabaseTools-luokkien metodeja.
Käyttäjän kirjautumisen yhteydessä tietokannoista haetaan fetch_weight() ja user_intake_load() metodeilla käyttäjän tiedot, jonka perusteella käyttäjänäkymä renderöidään.

## Sovelluslogiikka

Toiminnallisuuksista vastaavat luokkien UserService, EntityService, Calculator, Intake oliot.
Luokat tarjoavat käyttöliittymälle toimintoja metodeillaan. 
UserService-luokan metodeja ovat esimerkiksi: 
- `user_delete(email, password)`
- `change_password(in_email, password, in_password1, in_password2)`
- `password_check(password1, password2)`
- `email_check(in_email)`

UserService on riippuvainen DatabaseTools-luokasta, joka on käyttäjän tietojen tallentamisesta huolehtiva luokka. UserService käsittelee kirjautumiseen, rekisteröitymiseen ja käyttäjän muokkaamiseen liittyviä toiminnallisuuksia. 

Intake-luokan metodeja ovat esimerkiksi:
- `set_protein(protein_gram)`
- `set_fat(fat_gram)`
- `get_protein()`

Calculator-luokan metodeja ovat esimerkiksi:
- `protein_calorie_count(protein_grams)`
- `carbohydrates_calorie_count(carbohydrates_grams)`
- `lean_body_mass_estimate()`
- `bmr_count(lean_body_mass)`
- `total_daily_energy_expenditure(bmr, activity_level)`

Calculator-luokka käsittelee metodiensa avulla repositorion tallennettujen arvojen ja käyttäjän käyttöliittymästä valitsemien vaihtoehtojen perusteella erilaisia laskutoimituksia, kuten lepoaikaisen energiakulutuksen laskemista.

Suhteita kuvaava luokka/pakkauskaavio:

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/luokka_pakkauskaavio.png" width=760>


## Tietojen pysyväistallennus
Pakkauksessa repositories olevat luokat RecordService ja DatabaseTools huolehtivat käyttäjän tietojen tallentamisesta. RecordService tallentaa tietoa records.txt nimiseen CSV-tiedostoon. Vastaavasti DatabaseTools tallentaa tietoa Sqlite3-tietokantaan. 

Sovellus tallentaa records.txt tiedostoon vain käyttäjän päivän aikana syöttämät proteiini-, hiilihydraatti- ja rasvamäärät sekä näiden tietojen seulomiseen käyttäjän sähköposti ja tietojen tallentamisen aika.
Tallennus CSV-tiedostoon tapahtuu formaatissa:
...
account@gmail.com;2021-12-25 17:24:29.484410;12;13;14 
epkka@hotmail.com;2021-12-25 17:24:29.484410;112;13;4 
...
, eli käyttäjän sähköpostiosoitteen, päivämäärän, proteiinimäärän, hiilihydraattimäärän ja rasvamäärän. Kentät erotetaan toisistaan puolipisteellä.

Käyttäjät sekä käyttäjän henkilökohtaiset tiedot, kuten etunimi, sukunimi, syntymäaika, pituus yms, tallennetaan Softfit.db tietokantaan tauluun Users ja käyttäjän painot tauluun Weights.
Tietokannan alustus tapahtuu user_repository.py-tiedostossa. 

## Päätoiminnallisuudet

Jotkut sovelluksen toimintalogiikka sekvenssikaaviolla kuvattuna.

### Käyttäjän kirjautuminen

Kun käyttäjä on kirjoittanut sähköpostiosoitteensa ja salasanansa, ja sen jälkeen painannut painiketta "_Login_". Niin kontrolli siirtyy seuraavasti:

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Login.png" width=760>

kutsuu DatabaseTools metodia check_email ja che


### Uuden käyttäjän luominen
Jos halutaan luoda käyttäjä, niin se tehdään painamalla painiketta "Create User", päästään käyttäjän luomisnäkymään. Kun käyttäjän tiedot on syötetty ja painetaan painiketta "Register", niin kontrolli siirtyy seuraavasti:

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/register.png" width=760>

### Basal metabolic rate -laskeminen
Calculator-näkymässä valinta vaihtoehtoista riippuen kontrolli siirtyy eri tavalla. Tässä on yksi mahdollisista tapauksista:

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Calculator.png" width=760>


### Salasanan vaihtaminen ja käyttäjän poistaminen

Käyttäjänäkymässä painamalla "Change password" päästään vaihtamaan salasanan vaihtonäkymään. Kun käyttäjä syöttää uudet salasanat ja painaa "Done" kontrolli siirtyy seuraavasti:

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Change_password.png" width=760>


Käyttäjänäkymässä on myös painike käyttäjän poistamiseen "Delete Account", jota painamalla kontrolli siirtyy seuraavasti.

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/delete_account.png" width=760>

### Muut toiminnallisuudet

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Add_weight.png" width=760>

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/delete_weight.png" width=760>


<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/mathplotframe.png" width=760>

## Ohjelman rakenteeseen jääneet heikoudet

### Sovelluslogiikka

En ole tyytyväinen sovelluksen logiikkaan, sillä monet toiminnallisuuksista tapahtuu suoraan käyttöliittymän ja tietokannan välillä ilman epäsuoraa välittäjää. Onko tämä tarpeeksi turvallinen? 

### Käyttöliittymä

Käyttöliittymässä on minulla jonkin verran toistuvia koodeja, sillä en osannut eristää tkinter-koodeja yleisiksi metodeiksi, joita voisi kutsua tarvittaessa uudelleen käyttöön. En tiedä, onko tämmöinen edes mahdollista.

