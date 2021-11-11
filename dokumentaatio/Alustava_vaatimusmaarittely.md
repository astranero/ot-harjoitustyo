# Vaatimusmäärittely 

## Sovelluksen tarkoitus


Sovelluksen avulla käyttäjän on mahdollista laskea kalorin liittyviä ominaisuuksia, kuten proteiinin, hiilihydraatin ja rasvan kalorimäärää. Myös lisäämään oman painon sovellukseen ja seuraamaan painon muutosta. 
Sovellusta voi käyttää vain rekisteröitynyt käyttäjä, joista jokaisen yksityiset tiedot on turvassa toisilta käyttäjiltä. 

## Käyttäjät 

Sovellukselle saatetaan lisätä administration käyttäjä, joka pystyy poistamaan epäasialliset postaukset ja tarvittaessa antamaan käyttäjälle postauskiellon.

## Käyttöliittymäluonnos 

Sovelluksella on usea näkymä. 
Ensin ennen kirjautumista käyttäjälle aukeaa ikkuna, jossa näkyvät napit "Register" ja "Login". Painamalla "Register" käyttäjä voi tehdä käyttäjätilin uuteen aukeavaan ikkunaan.
Rekisteröitymisessä vaaditaan "Email id", "Password", "Rewrite Password" ja "Date of Birth" 
Tämän jälkeen täyttämällä ensimmäisen taulukon taulut "Email id" ja "Password". Painamalla "Login" voi kirjautua sisään sovellukseen.

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kuva_1.png" width=760>

## Perusversion tarjoama toiminnallisuus 

- Käyttäjä pystyy rekisteröitymään ja kirjautumaan sovellukseen
 - Käyttäjän tunnuksen tulee olla sähköpostimuodossa ja käyttämätön. Ohjelma ilmoittaa kelvottomasta sähköpostista.

- Käyttäjä pystyy lisäämään oman sukupuolensa, pituudensa ja painonsa
  - Ikä saadaan "Date of Birth" muuttujasta
  - Painon mukana näkymään tulee myös päivämäärä, jolloin se on lisätty.
- Käyttäjä voi laskea lepokalorikulutuksensa (BMR, Basal Metabolic Rate)
- Käyttäjä voi poistaa tilinsä
- Käyttäjä voi kirjautua ulos tilistä

## Jatkokehitysideoita

- Taulukko, josta näkyy painon kehitys kuvaajana. 
- BMI laskuri
- Veden tarve laskuri
- Calorie laskuri


