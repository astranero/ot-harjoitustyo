import src.services.calculator_service as calculator


class Intake:
    def __init__(self):
        self.__protein = 0
        self.__carbohydrates = 0
        self.__fat = 0
        self.counter = calculator.Calculator()

    def set_protein(self, protein_gram):
        self.__protein += protein_gram
        if self.__protein <= 0:
            self.__protein = 0

    def get_protein(self):
        return self.__protein

    def set_carbohydrates(self, carbohydrates_gram):
        self.__carbohydrates += carbohydrates_gram
        if self.__carbohydrates <= 0:
            self.__carbohydrates = 0

    def get_carbohydrates(self):
        return self.__carbohydrates

    def set_fat(self, fat_gram):
        self.__fat += fat_gram
        if self.__fat <= 0:
            self.__fat = 0

    def get_fat(self):
        return self.__fat

    def total_calorie_intake(self):
        protein_calories = self.counter.protein_calorie_count(self.__protein)
        carbohydrate_calories = self.counter.carbohydrates_calorie_count(
            self.__carbohydrates)
        fat_calories = self.counter.fat_calorie_count(self.__fat)
        return protein_calories + carbohydrate_calories + fat_calories

    def __str__(self):
        return f"""Protein: {self.__protein}g | Carbohydrates: {self.__carbohydrates}g | Fat: {self.__fat}g"""
