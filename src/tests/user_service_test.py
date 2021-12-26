import unittest
from services.user_service import UserService
from repositories.user_repository import DatabaseTools


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.service = UserService()
        self.service.user_delete("Pekkis@gmail.com", "1234")

    def test_user_delete(self):
        DatabaseTools("Softfit_test.db").create_user("name","surname","Pekkis@gmail.com","1234","21.02.2021","male","195")
        answer = self.service.user_delete("Pekkis@gmail.com", "1234")
        if answer:
            return_value = self.service._datatools.check_email(
                "Pekkis@gmail.com", "1234")
            self.assertEqual(return_value, None)

    def test_password_check(self):
        return_value = self.service.password_check("This", "This")
        self.assertEqual(return_value, True)
        return_value = self.service.password_check("This", "That")
        self.assertEqual(return_value, None)
        return_value = self.service.password_check("", "")
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

    def test_name_check(self):
        return_value = self.service.name_check("name")
        self.assertEqual(return_value, True)
        return_value = self.service.name_check("bom21")
        self.assertEqual(return_value, False)
