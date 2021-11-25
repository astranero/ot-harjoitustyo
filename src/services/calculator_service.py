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
        
        self.protein_calories = self.__protein_calorie_per_gram * int(protein_grams)
        return self.protein_calories

    def carbohydrates_calorie_count(self, carbohydrates_grams: int):
    
        self.carbohydrates_calories = self.__carbohydrates_calorie_per_gram * int(carbohydrates_grams)
        return self.carbohydrates_calories
    
    def fat_calorie_count(self, fat_grams: int):
        
        self.fat_calories = self.__fat_calorie_per_gram * int(fat_grams)
        return self.fat_calories
        
    
    def lean_body_mass_calculator(self, knowing_body_fat_percentage: bool,body_fat_percent : float, weight_kg, height_cm , sex: str):
        if knowing_body_fat_percentage == True:
            lean_body_mass_kg = weight_kg * ((100 - body_fat_percent)/100)
        else:
            if sex == "male":
                lean_body_mass_kg= 0.407 * weight_kg + 0.267 * height_cm - 19.2
            elif sex == "female":
                lean_body_mass_kg = 0.252 * weight_kg + 0.473 * height_cm - 48.3
        return lean_body_mass_kg
        
    def basal_metabolic_rate_calculator(self, knowing_lean_body_mass = False, knowing_body_fat_percentage = False, body_fat_percent: int = 0, weight_kg: int = 0, height_cm :int = None, sex :str= None):
        if knowing_lean_body_mass:
            basal_metabolic_rate = 370 + (21.6 * self.lean_body_mass_calculator())
        elif knowing_body_fat_percentage: 
            basal_metabolic_rate = 370 + (21.6 * self.lean_body_mass_calculator(knowing_body_fat_percentage, body_fat_percent, weight_kg))
        else:
            basal_metabolic_rate = 370 + (21.6 * self.lean_body_mass_calculator( body_fat_percent, weight_kg, height_cm, sex))
        return basal_metabolic_rate

    def total_daily_energy_expenditure(self, activity_level):
        
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

        total_daily_energy_expenditure = activity_multiplier * self.basal_metabolic_rate_calculator()
        return total_daily_energy_expenditure
    
