from repositories.user_repository import DatabaseTools
from datetime import datetime, date
from entities.user import User
from services.intake_trace_service import Intake


class EntityService:
    """Luokka, jonka avulla alustetaan User-olio.

        Attributes: 
            email: Käyttäjän sähköpostiosoite.
            DatabaseTools(): Luokka-olio, jonka avulla päästään käsiksi tietokantaan.
            User(): Luokka-olio, joka alustetaan käyttäjän tiedoilla. 
    """

    def __init__(self, email):
        """Luokan konstruktori, joka luo uuden instanssin.

        Args:
            email (String): Käyttäjän sähköpostiosoite.
        """
        self._email = email
        self._datatools = DatabaseTools()
        self._user = User()
        self._intake = None
        self._user_entity = None
        self._create_user_entity()

    def _create_user_entity(self):
        """Metodi, jonka avulla alustetaan tietokannasta löytyvät tiedot User-olioon.
        """

        data = self._datatools.fetch_user_info(self._email)
        date_of_birth = data[5]
        age = self._age_count(date_of_birth)
        gender = data[6]
        height = data[7]
        nutrient_data_csv = data[8]
        if not self.update_reset_timer():
            nutrient_data_csv = ""
        weight = self._datatools.fetch_weight(self._email)
        user_entity = User(age, gender, weight, height, nutrient_data_csv)
        self._user_entity = user_entity

    def return_user_entity(self):
        """Palauttaa User-olion kutsukohtaan.

        Returns:
            User-luokan instanssi: Palauttaa alustetun olion.
        """
        return self._user_entity

    def user_intake_load(self):
        self._intake = Intake()
        data_csv = self._user_entity.get_entity_data_csv()
        if data_csv != "":
            data = data_csv.split(";")
            protein = float(data[0])
            carbohydrates = float(data[1])
            fat = float(data[2])
            self._intake.set_protein(protein)
            self._intake.set_carbohydrates(carbohydrates)
            self._intake.set_fat(fat)
        return self._intake

    def _age_count(self, date_of_birth):
        """Lasketaan käyttäjän ikä

        Args:
            date_of_birth (string): Käyttäjän syntymäaika merkkijonona formaattimuodossa "dd/MM/yyyy".

        Returns:
            ikä (float): Käyttäjän ikä liukulukuarvona
        """
        birthdate = datetime.strptime(date_of_birth, "%d/%m/%Y")
        nowdate = datetime.now()
        age = nowdate - birthdate
        return age.days/(365.25)

    def update_reset_timer(self):
        """Metodi, joka alustaa päivittäin muuttujan nutrient_data_csv.

        Returns:
            True: Jos päivä on sama, niin palautetaan tosi. Muulloin epätosi.
        """
        updatedate = self._datatools.fetch_updatedate(self._email)
        updatedate_obj = datetime.strptime(updatedate, "%Y-%m-%d %H:%M:%S")
        updatedate_str = datetime.strftime(updatedate_obj, "%Y-%m-%d")
        date_now = datetime.now()
        date_str = datetime.strftime(date_now, "%Y-%m-%d")
        handle = True
        if date_str is not updatedate_str:
            handle = False
        return handle
