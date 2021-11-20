import unittest
import services.intake_trace_service as intake


def TestIntaketraceService(unittest.TestCase):
    
    def setUp(self):
        self.mouth = intake
        
    def test_strMethod(self):
        self.assertEqual(self.mouth, "Protein: 0g | Carbohydrates: 0g | Fat: 0g" )