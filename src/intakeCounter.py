
class MouthInput:
    def __init__(self):
        self.__protein = 0
        self.__carbohydrates = 0
        self.__fat = 0
        
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
    
    def __str__(self):
        return f"Protein: {self.__protein}g | Carbohydrates: {self.__carbohydrates}g | Fat: {self.__fat}g"
    
suu = MouthInput()
suu.set_protein(19)
suu.set_carbohydrates(120)
suu.set_fat(12)
suu.set_protein(12)
print(suu.get_protein())
print(suu)