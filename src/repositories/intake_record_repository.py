from datetime import datetime
import csv
import database_connection as conn
from services.intake_trace_service import IntakeTrace


class RecordService:
    """Luokka, jonka avulla alustetaan User-olio.

        Attributes:
            email: Käyttäjän sähköpostiosoite.
            Intake(): Luokka-olio, joka alustetaan käyttäjän tiedoilla.
    """

    def __init__(self, email, file_name):
        """Luokan konstruktori, joka luo uuden instanssin.

        Args:
            email (String): Käyttäjän sähköpostiosoite.
        """
        self._email = email
        self._intake = IntakeTrace()
        self.file_path = conn.return_file_path(file_name)

    def write_record(self, protein, carbohydrates, fat):
        """Metodi, jonka avulla voidaan kirjoittaa records-tiedostoon

        Args:
            protein: proteiinimäärä grammoina
            carbohydrates: hiilihydraattimäärä grammoina
            fat: rasvamäärä grammoina
        """
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write(
                f"{self._email};{datetime.now()};{protein};{carbohydrates};{fat} \n")

    def _read_record(self):
        """Funktio, jonka avulla voidaan lukea records-tiedosto.

        Returns:
            List: Palauttaa käyttäjän tuoreimman rivin päivämäärän perusteella.
        """
    
        data = csv.reader(
            open(self.file_path, "r", encoding="utf-8"), delimiter=";")
        data_by_email = sorted(
            (row for row in data if row[0] == self._email))
        sorted_data = sorted(data_by_email, key=lambda row: datetime.strptime(
            row[1], "%Y-%m-%d %H:%M:%S.%f"))
        return sorted_data[-1]

    def user_intake_load(self):
        """Alustaa Intake-olion käyttäjän tuoreimmalla records.txt rivillä.

        Returns:
            Object: Palautta Intake-olin funktion kutsujalle.
        """

        try:
            data_csv = self._read_record()
            self.record_reset_timer(data_csv[1])
            data_csv = self._read_record()

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

    def record_reset_timer(self, date):
        """Metodi, joka alustaa päivittäin tiedoston records.txt.
        """
        updatedate = date
        updatedate_obj = datetime.strptime(updatedate, "%Y-%m-%d %H:%M:%S.%f")
        updatedate_str = datetime.strftime(updatedate_obj, "%Y-%m-%d")
        date_str = datetime.strftime(datetime.now(), "%Y-%m-%d")

        if date_str != updatedate_str:
            self.reset_records()

    def reset_records(self):
        with open(self.file_path, "w", encoding="utf-8"):
                pass