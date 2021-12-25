# Softfit Assist


<img src="https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Fit-man.png" width="760"> 
<a href="https://unsplash.com/photos/9dzWZQWZMdE "> Source of the picture</a>  
<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>



Sovelluksella käyttäjät pystyvät laskemaan erilaisia urheiluun liittyviä asioita, kuten Basal Metabolic rate eli lepoaikaista energian kulutusta ja TDEE eli päivän aikana kaikkiaan kulutettua energiamäärää, jotka lasketaan käyttäen Katch-Mcardlen laskukaavoja. Ennen sovelluksen käyttämistä on rekisteröidyttävä, sillä käyttäjän tietojen tallentamiseen tarvitaan tunnusta. Tunnuksen avulla voi myöhemmin kirjautua uudelleen takaisin ja saada näkyville aiemmin tallennetut tiedot. 


## Dokumentaatio

[Käyttöohje](https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuurikuvaus](https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/testausdokumentti.md)

[Työaikakirjanpito](https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Seuraavalla komennolla saadaan asennettua riippuvuuksia:

    ```poetry install```

2. Tarvittavat alustustoimeenpiteet suoritettava komennolla:
    
    ```poetry run invoke build```

3. Käynnistetään sovellus:

    ```poetry run invoke start```

## Komentorivitoiminnot

### Ohjelman suorittaminen
Ohjelman voi suorittaa komennolla:
    
    poetry run invoke start 

### Testaus
Ohjelman testit suoritetaan komennolla:
     
    poetry run coverage test

### Testikattavuus
Ohjelman testikattavuusraportti generoidaan htmlcov-hakemistoon komennolla:

    poetry run invoke coverage-report
  

### Pylint
Pylint voidaan käynnistää komennolla:

    Poetry run invoke lint
  
