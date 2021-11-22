
# FitCalculator

Sovelluksella käyttäjät pystyvät laskemaan erilaisia urheiluun liittyviä asioita, kuten Basal Metabolic rate eli lepoaikaista energian kulutusta ja TDEE eli päivän aikana kaikkiaan kulutettua energiamäärää. Laskutoimitukset tehdään käyttäen Katch-Mcardlen laskukaavoja. Ennen sovelluksen käyttämistä on rekisteröidyttävä, sillä käyttäjän tietojen tallentamiseen tarvitaan tunnusta. Tunnuksen avulla voi myöhemmin kirjautua uudelleen takaisin ja saada näkyville aiemmin tallennetut tiedot. 


## Dokumentaatio

[vaatimusmäärittely](https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/Alustava_vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/Neroniuoso/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Seuraavalla komennolla saadaan asennettua riippuvuuksia:

    ```Poetry install```

2. Tarvittavat alustustoimeenpiteet suoritettava komennolla:
    
    ```Poetry run invoke build```

3. Käynnistetään sovellus:

    ```Poetry run invoke start```

## Komentorivitoiminnot

### Ohjelman suorittaminen
Ohjelman voi suorittaa komennon ```Poetry run invoke start``` avulla.

### Testaus
Ohjelman testit suoritetaan komennon ```Poetry run coverage test``` avulla.

### Testikattavuus
Ohjelman testikattavuusraportti generoidaan htmlcov-hakemistoon komennon ```Poetry run invoke coverage-report``` avulla.
