from repositories.user_repository import DatabaseTools
from datetime import datetime, date
from entities.User import User
from services.intake_trace_service import Intake
class EntityService:
    def __init__(self, email):
        self._email = email
        self._datatools = DatabaseTools()
        self._user = User()
        self._intake = None
        self._user_entity = None
        self._create_user_entity()
    
    def _create_user_entity(self):
        data = self._datatools.fetch_user_info(self._email)
        dateOfBirth = data[5]
        age = self._age_count(dateOfBirth)
        gender = data[6]
        height = data[7]
        nutrient_data_csv = data[8]
        if not self.update_reset_timer(): nutrient_data_csv = "" 
        weight = self._datatools.fetch_weight(self._email)
        user_entity = User(age, gender, weight, height, nutrient_data_csv)
        self._user_entity = user_entity
    
    def return_user_entity(self):
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
    
    def _age_count(self, dateOfBirth):
        birthdate = datetime.strptime(dateOfBirth, "%d.%m.%Y")
        nowdate = datetime.now()
        age = nowdate - birthdate
        return age.days/(365.25)
    
    def update_reset_timer(self):
        updatedate = self._datatools.fetch_updatedate(self._email)
        updatedate_obj = datetime.strptime(updatedate, "%Y-%m-%d %H:%M:%S")
        updatedate_str = datetime.strftime(updatedate_obj, "%Y-%m-%d")
        date_now = datetime.now()
        date_str = datetime.strftime(date_now, "%Y-%m-%d")
        handle = True
        if date_str is not updatedate_str: handle=False
        return handle