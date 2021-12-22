class User:
    """Luokka, johon tallennetaan käyttäjän tietoja väliaikaisesti.
        Attributes:
            age: Käyttäjän ikä (Tulevaisuuden lisätoiminnallisuutta varten).
            gender: Käyttäjän sukupuoli.
            weight: Paino kilogrammoina.
            height: Pituus senttimetreinä
            entity_data: Tietoa proteiinin, hiilihydraatin, rasvan sekä kokonaiskalorin määrästä.
    """

    def __init__(self, age=None, gender=None, weight=0, height=0, entity_data=None):
        """ Luokan konstruktori, joka luo uuden käyttäjä instanssin.

            Args: 
                gender: sukupuoli, mies tai nainen.
                weight: paino kilogrammoina.
                height: Pituus senttimerteinä.
        """
        self.__gender = gender
        self.__weight = weight
        self.__height = height
        self.__entity_data = entity_data

    def set_entity_data_csv(self, data):
        """Asettaa instanssin entity_datan arvon

           Args:
                data: entity_data muuttujaan sijoitettava arvo. 
        """

        self.__entity_data = data

    def get_entity_data_csv(self):
        """Palauttaa instanssin entity_data muuttujan arvon kutsukohtaan.

            return: Palauttaa csv-muodossa olevan string arvon. Tällainen olisi merkkijono "23;45;65"
        """
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
