import unittest
from repositories.intake_record_repository import RecordService
from datetime import datetime
class TestRecordService(unittest.TestCase):

    def setUp(self):
        self.serv = RecordService("account@gmail.com","records_test.txt")
        self.serv.reset_records()
        self.serv.write_record(12,13,14)

    def test_write_record(self):
        record_list = self.serv._read_record()
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        email = record_list[0]
        rec_date_str = datetime.strptime(record_list[1],"%Y-%m-%d %H:%M:%S.%f").strftime("%Y-%m-%d %H:%M:%S")
        
        protein = record_list[2].strip()
        carbohydrates = record_list[3].strip()
        fat = record_list[4].strip()
        new_list = [protein, carbohydrates, fat]

        self.assertEqual(email,"account@gmail.com")
        self.assertEqual(rec_date_str,date_str)
        self.assertEqual(new_list,["12","13","14"])
    
    def test_user_intake_load(self):
        intake = self.serv.user_intake_load()
        protein = intake.get_protein()
        fat = intake.get_fat()
        carbo = intake.get_carbohydrates()
        test_list = [protein, carbo, fat]
        self.assertEqual(test_list, [12.0,13.0,14.0])