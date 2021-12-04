from services.intake_trace_service import Intake
from services.entity_service import EntityService
class CalculatorScreen:
    def __init__(self, root, user_view):
        self._root = root
        self._user_view = user_view
        self._user_entity = EntityService().create_user_entity()
        self._intake_entity = None
    
    def user_intake_load(self):
        self._intake_entity = Intake()
        data_csv = self._user_entity.get_entity_data_csv()
        if data_csv != "":
            data = data_csv.split(";")
            protein = float(data[0])
            carbohydrates = float(data[1])
            fat = float(data[2])
            self._intake_entity.set_protein(protein)
            self._intake_entity.set_carbohydrates(carbohydrates)
            self._intake_entity.set_fat(fat)