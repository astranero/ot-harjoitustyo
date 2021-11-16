from intakeCounter import MouthInput
from calorieCalculator import Calculator

class TotalCalorie:
    
    def __init__(self):
        self.protein = MouthInput.get_protein()
        self.carbohydrates = MouthInput.get_carbohydrates()
        self.fat = MouthInput.get_fat()
        self.counter = Calculator()
        
    def totalCalorie(self):
        protein_calories = self.counter.protein_calorie_count(self.protein)
        carbohydrate_calories = self.counter.carbohydrates_calorie_count(self.carbohydrates)
        fat_calories = self.counter.fat_calorie_count(self.fat)
        
        return protein_calories + carbohydrate_calories + fat_calories        
    

print(TotalCalorie.totalCalorie)