class User:
    def __init__(self, first_name, surname, email, password, dateOfBirth, sex, weight=0, height=0):
        self.__first_name = first_name
        self.__surname = surname
        self.__email = email
        self.__password = password
        self.__dateOfBirth = dateOfBirth
        self.__sex = sex
        self.__weight = weight
        self.__height = height
    
    def _getPassword(self):
        return self.__password
    
    def _setpassword(self, newPassword):
        self.__password = newPassword
    
    def _getSex(self):
        return self.__sex
    
    def _getWeight(self):
        return self.__weight
    
    def _setWeight(self, newWeight):
        self.__weight = newWeight

    def _getHeight(self):
        return self.__height
    
    def _setHeight(self, newHeight):
        self.__height = newHeight

