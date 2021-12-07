""" sources: 
https://www.reddit.com/r/nutrition/comments/bb90l0/most_accurate_bmrtdee_calculator/
https://www.omnicalculator.com/health/bmr-katch-mcardle#what-is-the-katch-mcardle-calculator
"""


class Calculator:
    def __init__(self):
        self.__protein_calorie_per_gram = 4
        self.__carbohydrates_calorie_per_gram = 4
        self.__fat_calorie_per_gram = 9

    def protein_calorie_count(self, protein_grams: int):
        self.protein_calories = self.__protein_calorie_per_gram * \
            int(protein_grams)
        return self.protein_calories

    def carbohydrates_calorie_count(self, carbohydrates_grams: int):
        self.carbohydrates_calories = self.__carbohydrates_calorie_per_gram * \
            int(carbohydrates_grams)
        return self.carbohydrates_calories

    def fat_calorie_count(self, fat_grams: int):
        self.fat_calories = self.__fat_calorie_per_gram * int(fat_grams)
        return self.fat_calories

    def _lean_body_mass_estimate(self, weight_kg=None, height_cm=None, gender=None):
        if gender == "male":
            lean_body_mass_kg = 0.407 * weight_kg + 0.267 * height_cm - 19.2
        elif gender == "female":
            lean_body_mass_kg = 0.252 * weight_kg + 0.473 * height_cm - 48.3
        return lean_body_mass_kg

    def _count_lean_body_mass_with_fatpercent(self, body_fat_percent, weight_kg):
        lean_body_mass_kg = weight_kg - weight_kg * \
            ((100 - body_fat_percent)/100)
        return lean_body_mass_kg

    def bmr_count(self, lean_body_mass: float):
        try:
            basal_metabolic_rate = 370 + (21.6*lean_body_mass)
            return basal_metabolic_rate
        except ValueError as error:
            return error

    def total_daily_energy_expenditure(self, bmr, activity_level):
        if activity_level == "Inactive":
            activity_multiplier = 1.2
        elif activity_level == "Low":
            activity_multiplier = 1.375
        elif activity_level == "Medium":
            activity_multiplier = 1.55
        elif activity_level == "Medium-high":
            activity_multiplier = 1.65
        elif activity_level == "High":
            activity_multiplier = 1.725
        elif activity_level == "Intense":
            activity_multiplier = 1.9
        total_daily_energy_expenditure = bmr * activity_multiplier
        return round(total_daily_energy_expenditure, 3)
