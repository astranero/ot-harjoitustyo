from repositories.user_repository import DatabaseTools
from datetime import datetime, date
from services.intake_trace_service import Intake
import csv


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
        with open("records.txt","a") as file:
            file.write(f"{datetime.now()};{protein};{carbohydrates};{fat} \n")

    def user_intake_load(self):
        self._intake = Intake()
        
        try:
            data = csv.reader(open("records.txt", "r"), delimiter=";")
            sorted_data = sorted(data, key = lambda row: datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f"))
            data_csv = sorted_data[-1]
            self._record_reset_timer(data_csv[0])
            
            if data_csv != "" and data_csv is not None:
                protein = float(data_csv[1])
                carbohydrates = float(data_csv[2])
                fat = float(data_csv[3])
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
            data = csv.reader(open("records.txt", "r"), delimiter=";")
            sorted_data = sorted(data, key = lambda row: datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f"))
            data_csv = sorted_data[-1]
            history_record = ";".join(data_csv)
            with open("history.txt","a") as file:
                file.write(history_record)
            with open("records.txt", "w"):
                pass
