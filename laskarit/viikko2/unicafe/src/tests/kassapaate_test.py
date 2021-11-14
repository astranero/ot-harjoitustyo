import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    
    def setUp(self): 
        self.kassa = Kassapaate()

    def test_kassapaate_alkutilanne_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.edulliset, 0)
        
    def test_syominen_kasvattaa_rahaakassassa(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100640)
    
    def test_syominen_palauttaa_oikean_maaran_rahaa(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(340), 100)
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(540), 140)
    
    def test_syominen_kasvattaa_myytyjen_lounaiden_maaran(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.edulliset, 1)  
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.maukkaat, 1)
          
    def test_syominen_riittamaton_maksu_palauttaa_oikein(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(140), 140)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(140), 140)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        
    def test_syo_edullisesti_kortilla_toimiva(self):
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(kortti),True)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(kortti), True)
    
    def test_syo_edullisesti_kortilla_myydyt_lounaat_kasvaa(self):
        kortti = Maksukortti(1000)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_syo_kortilla_riittamaton_raha_kortilla_ei_muutoksia(self):
        kortti = Maksukortti(230)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 230)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(kortti), False)
    
    def test_korttiosto_ei_muutosta_kassaan(self):
        kortti = Maksukortti(1000)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        
    def test_kortin_lataus_muuttaa_kortin_saldoa(self):
        kortti = Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, 250)
        self.assertEqual(kortti.saldo, 1250)
    
    def test_kortin_lataus_muuttaa_kassan_rahamaaraa(self):
        kortti = Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, 250)
        self.assertEqual(self.kassa.kassassa_rahaa, 100250)
    
    def test_kortin_lataus_ei_onnistu_negatiivisella_summalla(self):
        kortti = Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, -200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)