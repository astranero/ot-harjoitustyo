
# SoftFit-Assist

<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Fit-man.png" width=760> 
<a href="https://unsplash.com/photos/9dzWZQWZMdE "> Source of the picture</a>



Sovelluksella käyttäjät pystyvät laskemaan erilaisia urheiluun liittyviä asioita, kuten Basal Metabolic rate eli lepoaikaista energian kulutusta ja TDEE eli päivän aikana kaikkiaan kulutettua energiamäärää, jotka lasketaan käyttäen Katch-Mcardlen laskukaavoja. Ennen sovelluksen käyttämistä on rekisteröidyttävä, sillä käyttäjän tietojen tallentamiseen tarvitaan tunnusta. Tunnuksen avulla voi myöhemmin kirjautua uudelleen takaisin ja saada näkyville aiemmin tallennetut tiedot. 


## Dokumentaatio

[vaatimusmäärittely](https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/Alustava_vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Seuraavalla komennolla saadaan asennettua riippuvuuksia:

    ```Poetry install```img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kuva_1.png" width=760

## Komentorivitoiminnot

### Ohjelman suorittaminen
Ohjelman voi suorittaa komennolla:
    
    Poetry run invoke start 

### Testaus
Ohjelman testit suoritetaan komennolla:
     
    Poetry run coverage test

### Testikattavuus
Ohjelman testikattavuusraportti generoidaan htmlcov-hakemistoon komennolla:

    Poetry run invoke coverage-report
