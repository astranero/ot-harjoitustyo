import unittest
import services.calculator_service as service


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.service = service.Calculator()
        self.weight_kg = 90
        self.height_cm = 194.5

    def test_lean_body_mass_estimate_male(self):
        gender = "male"
        estimate = self.service._lean_body_mass_estimate(
            self.weight_kg, self.height_cm, gender)
        self.assertAlmostEqual(69.3615, estimate)

    def test_lean_body_mass_estimate_female(self):
        gender = "female"
        estimate = self.service._lean_body_mass_estimate(
            self.weight_kg, self.height_cm, gender)
        self.assertAlmostEqual(66.38, round(estimate, 2))

    def test_count_lean_body_mass_with_fatpercent(self):
        fat_percent = 24.1
        lean_mass = self.service._count_lean_body_mass_with_fatpercent(
            fat_percent, self.weight_kg)
        self.assertEqual(68.31, round(lean_mass,2))

    def test_total_daily_energy_exepnditure(self):
        lean_body_mass = float(76.4)
        bmr = float(self.service.bmr_count(lean_body_mass))
        activity_level = "Low"
        total_expenditure = self.service.total_daily_energy_expenditure(
            bmr, activity_level)
        self.assertEqual(2777.83, total_expenditure)

        activity_level = "Medium"
        total_expenditure = self.service.total_daily_energy_expenditure(
            bmr, activity_level)
        self.assertEqual(3131.372, total_expenditure)

        activity_level = "Intense"
        total_expenditure = self.service.total_daily_energy_expenditure(
            bmr, activity_level)
        self.assertEqual(3838.456, total_expenditure)
