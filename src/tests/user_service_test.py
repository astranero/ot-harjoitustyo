from tkinter.messagebox import showinfo
import unittest
from services.user_service import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.service = UserService()
        self.service.user_delete("Pekkis@gmail.com", "1234")

    def test_error_window(self):
        self.service._datatools.create_user("Pekka", "Pekkanen", 
        "Pekkis@gmail.com", "1234","21/03/2021", gender="male", height=192)
        test_through = True
        try:
            self.service._error_window("Error")
        except Exception:
            test_through = False
        self.assertEqual(test_through,True)
        self.service.user_delete("Pekkis@gmail.com", "1234")
    
    def test_user_delete(self):
        answer = self.service.user_delete("Pekkis@gmail.com", "1234")
        if answer:
            return_value = self.service._datatools.check_email("Pekkis@gmail.com", "1234")
            self.assertEqual(return_value, None)
    
    def test_password_check(self):
        return_value = self.service.password_check("This","This")
        self.assertEqual(return_value,True)
        return_value = self.service.password_check("This","That")
        self.assertEqual(return_value, False)
        return_value = self.service.password_check("","")
        self.assertEqual(return_value, False)
    
    def test_check_height_digit(self):
        return_value = self.service.check_height_digit("195.3")
        self.assertEqual(return_value, True)
        return_value = self.service.check_height_digit("195,3")
        self.assertEqual(return_value, False)
    
    def test_check_value_type(self):
        return_value = self.service._check_value_type(500)
        self.assertEqual(return_value, True)
        return_value = self.service._check_value_type(-1)
        self.assertEqual(return_value, False)
        return_value = self.service._check_value_type(230)
        self.assertEqual(return_value, True)
    
    def test_email_check(self):
        return_value = self.service.email_check("ad.ad@ad.com")
        self.assertEqual(return_value, True)
        return_value = self.service.email_check("adda")
        self.assertEqual(return_value, False)
    
    def test_name_check