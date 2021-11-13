import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        
    def test_lataaminen_toimiva(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti),"saldo: 0.2")
            
    def test_luotu_kortti_on_olemassa(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1" )
        
    def test_rahan_otaaminen_toimiva(self):
        self.maksukortti.ota_rahaa(2)
        self.assertEqual(str(self.maksukortti), f"saldo: 0.08")
        
    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), f"saldo: 0.05")
    
    def test_saldoa_oltava_tarpeeksi(self):
        self.maksukortti.ota_rahaa(12)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        
    def test_rahat_riittaa_palauttaa_True(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)
    
    def test_rahat_vahissa_palauttaa_False(self):
        self.assertEqual(self.maksukortti.ota_rahaa(12), False)