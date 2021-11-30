class User:
    def __init__(self, first_name, surname, email, password, age, gender, weight=0, height=0):
        self.__first_name = first_name
        self.__surname = surname
        self.__email = email
        self.__password = password
        self.__age = age
        self.__gender = gender
        self.__weight = weight
        self.__height = height

    def _get_password(self):
        return self.__password

    def _set_password(self, newPassword):
        self.__password = newPassword

    def _get_sex(self):
        return self.__sex

    def _get_weight(self):
        return self.__weight

    def _set_weight(self, newWeight):
        self.__weight = newWeight

    def _get_height(self):
        return self.__height

    def _set_height(self, newHeight):
        self.__height = newHeight
