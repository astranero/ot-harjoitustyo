from entities.intakeCounter import MouthInput
class User(MouthInput):
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
        self.__mouth = MouthInput()

user = User("Pekka","peke@Gamil")
user.set_protein(10)
user.set_protein(35)
print((user.get_protein))