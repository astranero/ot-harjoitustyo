# Vaatimusmäärittely 

## Sovelluksen tarkoitus


Sovelluksen avulla käyttäjän on mahdollista seurata ja laskea kalorin liittyviä ominaisuuksia, kuten proteiini-, hiilihydraatti- ja rasvamäärää sekä näiden yhteenlaskettua kalorimäärää. Käyttäjä pystyy lisämään myös oman painon sovellukseen ja seuraamaan painon muutosta. Käyttäjätietojen perusteella laskurilla on myös toiminnallisuus laskea Basal Metabolic Rate ja Total daily energy expenditure. 
Sovellusta voi käyttää vain rekisteröitynyt käyttäjä, joista jokaisen yksityiset tiedot on turvassa toisilta käyttäjiltä. 

## Käyttöliittymäluonnos 

Sovelluksella on usea näkymä. 
Ensin ennen kirjautumista käyttäjälle aukeaa ikkuna, jossa näkyvät napit "Register" ja "Login". 
Painamalla "Register" käyttäjä voi tehdä käyttäjätilin uuteen aukeavaan ikkunaan.
Rekisteröitymisessä vaaditaan "Email id", "Password", "Rewrite Password" ja "Date of Birth" 
Tämän jälkeen täyttämällä ensimmäisen taulukon taulut "Email id" ja "Password". Painamalla "Login" voi kirjautua sisään sovellukseen.

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kuva_1.png" width=760>

## Perusversion tarjoama toiminnallisuus 

- [x] Käyttäjä pystyy rekisteröitymään ja kirjautumaan sovellukseen
- [x] Käyttäjän tunnuksen tulee olla sähköpostimuodossa ja käyttämätön. Ohjelma ilmoittaa kelvottomasta sähköpostista.
- [x] Käyttäjä pystyy lisäämään oman sukupuolensa, pituudensa ja painonsa
- [x] Painon mukana tallennetaan päivämäärä, jolloin se on lisätty.
- [x] Taulukko, josta näkyy painon kehitys kuvaajana.
- [x] Käyttäjä voi laskea lepokalorikulutuksensa (BMR, Basal Metabolic Rate)
- [x] Käyttäjä voi laskea päivän aikaisen energian kulutuksensa (TDEE, Total Daily Energy Expenditure) 
- [x] Käyttäjä voi poistaa tilinsä
- [x] Käyttäjä voi kirjautua ulos tilistä

## Toteuttamatta jääneet toiminnallisuudet
Nämä toiminnallisuudet saatetaan lisätä vielä tulevaisuudessa.
- Historia ravintoaineille
- Postaus-palsta
- Kommentti-toiminnallisuus
- BMI laskuri
- Veden tarve laskuri
- Calorie laskuri



