from datetime import datetime
import csv
from repositories.user_repository import DatabaseTools
from services.intake_trace_service import Intake


class RecordService:
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
        self._intake = None

    def write_record(self, protein, carbohydrates, fat):
        with open("records.txt", "a", encoding="utf-8") as file:
            file.write(
                f"{self._email};{datetime.now()};{protein};{carbohydrates};{fat} \n")

    def user_intake_load(self):
        self._intake = Intake()
        try:
            data = csv.reader(
                open("records.txt", "r", encoding="utf-8"), delimiter=";")
            data_by_email = sorted(
                (row for row in data if row[0] == self._email))
            sorted_data = sorted(data_by_email, key=lambda row: datetime.strptime(
                row[1], "%Y-%m-%d %H:%M:%S.%f"))
            data_csv = sorted_data[-1]
            self._record_reset_timer(data_csv[1])

            if data_csv != "" and data_csv is not None:
                protein = float(data_csv[2])
                carbohydrates = float(data_csv[3])
                fat = float(data_csv[4])
                self._intake.set_protein(protein)
                self._intake.set_carbohydrates(carbohydrates)
                self._intake.set_fat(fat)
        except Exception:
            pass
        return self._intake

    def _record_reset_timer(self, date):
        """Metodi, joka alustaa päivittäin tiedoston records.txt.
        """
        updatedate = date
        updatedate_obj = datetime.strptime(updatedate, "%Y-%m-%d %H:%M:%S.%f")
        updatedate_str = datetime.strftime(updatedate_obj, "%Y-%m-%d")
        date_str = datetime.strftime(datetime.now(), "%Y-%m-%d")

        if date_str != updatedate_str:
            with open("records.txt", "w", encoding="utf-8"):
                pass
