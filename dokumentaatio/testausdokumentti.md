Lähdekoodin testit on toteutettu sekä automaattisesti unittest-modulin avulla että manuaalisesti syöttämällä erilaisia rajatapauksia.
Testaaminen on toteutettu yksikkötestaamisena, eli lähdekoodin osat testattu erikseen.

## Yksikkötestaus- ja integraatiotestaus

### Sovelluslogiikka

UserService-luokkaa testataan [TestUserService](https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/src/tests/user_service_test.py)-testiluokan avulla. `UserService-oliolle` alustetaan injektoimalla riipuvuksiksi **DatabaseTools**-olio, jonka avulla luodaan ja käsitellään "Softfit_test.db"-tiedosto. Tähän tiedostoon tallennetaan testitiedot.
`Intake`-luokkaa testataan [TestIntakeService](https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/src/tests/intake_trace_service_test.py)-testiluokalla. Vastaavasti `Calculator`-luokkaa testataan [TestCalculator](https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/src/tests/calculator_service_test.py)-testiluokalla.
`Intake`- ja `Calculator`-olioiden testit tehdään yksikkötestien avulla, missä testataan metodien toiminnallisuus.

### Repositorio-luokat

_Repositorio_-luokkia ovat `DatabaseTools`- ja `RecordService`-luokat, jotka testataan vain testeissä käytössä olevien tiedojen avulla.
[TestDatabaseTools](https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/src/tests/user_repository_test.py)-testiluokassa käytetään "Softfit_test.db"-tiedostoa, ja [TestRecordService](https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/src/tests/intake_record_repository_test.py#L10)-luokassa käytetään "records_test.txt"-tiedostoa.

### Testauskattavuus

Sovelluksen testauksen haarautumakattavuus on 84%. Testi ei sisällä käyttäliittymätestaus, eikä testeissä käyty läpi build.py ja database_connection.py tiedostoa, sillä niiden toiminnallisuus tarkistettiin manuaalisesti.

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/coverage.png" width=760>

### Järjestelmätestaus

Järjestelmäntestaus on toteutettu manuaalisesti.

#### Asennus ja konfigurointi

Sovellus on asennettu ja testattu käyttöohjeen ilmoittamalla tavalla Linux-ympräristön avulla.
Sovellusta on testattu sekä tilanteissa, jossa tiedostot ovat olleet olemassa jo valmiiksi, että tilanteessa, jossa ne on ei ole olleet olemassa. Jos tiedostoja ei ole olemassa, niin ohjelma on luoo ne itse.

#### Toiminnallisuudet

Kaikki määrittelydokumentin ja käyttöohjeen ilmoittamat toiminnallisuudet on suoritettu ongelmitta. Virheelliset arvot on käsitelty niin, ettei seurauksena ole ohjelman kaatuminen. Ohjelma käsittelee virheelliset syötteet ilmoituksena käyttäjälle.