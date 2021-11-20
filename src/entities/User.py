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
    
    def getPassword(self):
        return self.__password
    
    def setpassword(self, newPassword):
        self.__password = newPassword
    
    def getSex(self):
        return self.__sex
    
    def getWeight(self):
        return self.__weight
    
    def setWeight(self, newWeight):
        self.__weight = newWeight

    def getHeight(self):
        return self.__height
    
    def setHeight(self, newHeight):
        self.__height = newHeight

