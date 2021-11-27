import unittest
from src.services.intake_trace_service import Intake


class TestIntakeTraceService(unittest.TestCase):

    def setUp(self):
        self.mouth = Intake()

    def test_strMethod(self):
        print(self.mouth)
        self.assertEqual(self.mouth.__str__(),
                         "Protein: 0g | Carbohydrates: 0g | Fat: 0g")

    def test_get_protein(self):
        self.assertEqual(self.mouth.get_protein(), 0)

    def test_get_fat(self):
        self.assertEqual(self.mouth.get_fat(), 0)

    def test_get_carbohydrates(self):
        self.assertEqual(self.mouth.get_carbohydrates(), 0)

    def test_set_protein(self):
        self.mouth.set_protein(29)
        self.assertEqual(self.mouth.get_protein(), 29)

    def test_set_protein_not_negative(self):
        self.mouth.set_protein(-20)
        self.assertEqual(self.mouth.get_protein(), 0)

    def test_set_protein_reduce_works(self):
        self.mouth.set_protein(25)
        self.mouth.set_protein(-20)
        self.assertEqual(self.mouth.get_protein(), 5)

    def test_set_fat(self):
        self.mouth.set_fat(29)
        self.assertEqual(self.mouth.get_fat(), 29)

    def test_set_fat_not_negative(self):
        self.mouth.set_fat(-20)
        self.assertEqual(self.mouth.get_fat(), 0)

    def test_set_fat_reduce_works(self):
        self.mouth.set_fat(25)
        self.mouth.set_fat(-20)
        self.assertEqual(self.mouth.get_fat(), 5)

    def test_set_carbohydrates(self):
        self.mouth.set_carbohydrates(29)
        self.assertEqual(self.mouth.get_carbohydrates(), 29)

    def test_set_carbohydrates_not_negative(self):
        self.mouth.set_carbohydrates(-20)
        self.assertEqual(self.mouth.get_carbohydrates(), 0)

    def test_set_carbohydrates_reduce_works(self):
        self.mouth.set_carbohydrates(25)
        self.mouth.set_carbohydrates(-20)
        self.assertEqual(self.mouth.get_carbohydrates(), 5)

    def test_totalCalorieIntake_isOk(self):
        self.mouth.set_protein(12)
        self.mouth.set_fat(23)
        self.mouth.set_carbohydrates(13)
        calories = self.mouth.totalCalorieIntake()
        self.assertEqual(calories, 307)
