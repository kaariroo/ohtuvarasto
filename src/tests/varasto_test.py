import unittest
from varasto import Varasto

#testimuutos


class TestVarasto1(unittest.TestCase):
    def setUp(self):
        self.varasto1 = Varasto(-1, -1)

    def test_konstruktori_luo_tyhjan_varaston_vaikka_tilavuus_on_negatiivinen(self):
        self.assertAlmostEqual(self.varasto1.tilavuus, 0)

    def test_kostruktori_asettaa_negatiivise_saldon_nollaksi(self):
        self.assertAlmostEqual(self.varasto1.saldo, 0)

class TestVarasto2(unittest.TestCase):
    def setUp(self):
        self.varasto2 = Varasto(10, 5)

    def test_konstruktori_luo_oikeankokoisen_saldon(self):
        self.assertAlmostEqual(self.varasto2.saldo, 5)

class TestVarasto3(unittest.TestCase):
    def setUp(self):
        self.varasto3 = Varasto(10, 12)

    def test_konstruktori_luo_oikeankokoisen_saldon_kun_alkusaldo_on_siompi_kuin_tilavuus(self):
        self.assertAlmostEqual(self.varasto3.saldo, 10)

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_liika_lisays_ei_ylitayta_varastoa(self):
        self.varasto.lisaa_varastoon(12)

        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_negatiivinen_lisays_ei_muuta_varastoa(self):
        self.varasto.lisaa_varastoon(-2)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varastosta_ei_voi_ottaa_negatiivista(self):
        self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varastosta_yritetaan_ottaa_liikaa(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(6)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_printti_kunnossa(self):
        self.varasto.__str__()

        self.assertEqual(self.varasto.__str__(), "saldo = 0, vielä tilaa 10")

