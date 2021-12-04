class User:
    def __init__(self,age, gender, weight=0, height=0):
        self.__age = age
        self.__gender = gender
        self.__weight = weight
        self.__height = height
        self.__entity_data = ""

    def set_entity_data(self, data):
        self.__entity_data = data
    
    def get_entity_data_csv(self):
        return self.__entity_data

    def get_gender(self):
        return self.__gender
    
    def get_age(self):
        return self.__age
    
    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

    def set_weight(self, newWeight):
        self.__weight = newWeight
