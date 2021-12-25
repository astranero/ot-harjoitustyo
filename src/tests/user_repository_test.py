import unittest
import repositories.user_repository as repository


class TestDatabaseTools(unittest.TestCase):
    def setUp(self):
        self.database = repository.DatabaseTools()
        self.database.database_init()
        self.name = "Pekka"
        self.surname = "Pekkanen"
        self.email = "Pekka@pekkanen.com"
        self.password = "Pekkis123"
        self.date = "9.11.2021"
        self.sex = "male"
        self.height = 195

    def test_create_user(self):
        self.database.create_user(
            self.name, self.surname, self.email, self.password, self.date, self.sex, self.height)
        user_info = self.database.fetch_user_info(self.email)
        self.assertEqual(user_info[3], self.email)

    def test_fetch_user_info(self):
        self.database.create_user(
            self.name, self.surname, self.email, self.password, self.date, self.sex, self.height)
        user_info = self.database.fetch_user_info(self.email)
        self.assertEqual(user_info[1], self.name)

    def test_check_email(self):
        self.database.create_user(
            self.name, self.surname, self.email, self.password, self.date, self.sex, self.height)
        email = self.database.check_email(self.email, self.password)
        self.assertEqual(email[0], self.email)

    def test_check_email_available(self):
        self.database.create_user(
            self.name, self.surname, self.email, self.password, self.date, self.sex, self.height)
        email = self.database.check_email_available(self.email)[0]
        self.assertEqual(email, self.email)

    def test_check_password(self):
        self.database.create_user(
            self.name, self.surname, self.email, self.password, self.date, self.sex, self.height)
        password = self.database.check_password(self.email, self.password)[0]
        self.assertEqual(password, self.password)

    def test_insert_weight(self):
        self.database.create_user(
            self.name, self.surname, self.email, self.password, self.date, self.sex, self.height)
        self.database.insert_weight(self.email, 198)
        weight = self.database.fetch_weight(self.email)
        self.assertEqual(weight, 198)

    def test_delete_user(self):
        self.database.create_user(
            self.name, self.surname, self.email, self.password, self.date, self.sex, self.height)
        self.database.insert_weight(self.email, 198)
        self.database.insert_weight(self.email, 193)
        self.database.insert_weight(self.email, 192)
        self.database.delete_user(self.email, self.password)
        weight = self.database.fetch_weight(self.email)
        self.assertEqual(weight, None)
