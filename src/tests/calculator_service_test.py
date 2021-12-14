import unittest
import services.calculator_service as service


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.service = service.Calculator()
        self.weight_kg = 90
        self.height_cm = 194.5

    def test_protein_calorie_count(self):
        calories = self.service.protein_calorie_count(40)
        self.assertEqual(160, calories)

    def test_carbohydrates_calorie_count(self):
        calories = self.service.carbohydrates_calorie_count(40)
        self.assertEqual(160, calories)

    def test_fat_calorie_count(self):
        calories = self.service.fat_calorie_count(40)
        self.assertEqual(360, calories)

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
        self.assertEqual(68.31, round(lean_mass, 2))

    def test_bmr_count(self):
        leanmass = int(80)
        bmr = self.service.bmr_count(leanmass)
        self.assertEqual(2098, bmr)

    def test_total_daily_energy_expenditure(self):
        bmr = int(2000)

        activity_level = "Inactive"
        total_expenditure = self.service.total_daily_energy_expenditure(
            bmr, activity_level)
        self.assertEqual(2400, total_expenditure)

        activity_level = "Low"
        total_expenditure = self.service.total_daily_energy_expenditure(
            bmr, activity_level)
        self.assertEqual(2750, total_expenditure)

        activity_level = "Medium"
        total_expenditure = self.service.total_daily_energy_expenditure(
            bmr, activity_level)
        self.assertEqual(3100, total_expenditure)

        activity_level = "Medium-high"
        total_expenditure = self.service.total_daily_energy_expenditure(
            bmr, activity_level)
        self.assertEqual(3300, total_expenditure)

        activity_level = "High"
        total_expenditure = self.service.total_daily_energy_expenditure(
            bmr, activity_level)
        self.assertEqual(3450, total_expenditure)

        activity_level = "Intense"
        total_expenditure = self.service.total_daily_energy_expenditure(
            bmr, activity_level)
        self.assertEqual(3800, total_expenditure)

        activity_level = "None"
        total_expenditure = self.service.total_daily_energy_expenditure(
            bmr, activity_level)
        self.assertEqual(0, total_expenditure)
