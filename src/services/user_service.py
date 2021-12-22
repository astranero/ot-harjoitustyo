import string
import re
from repositories.user_repository import DatabaseTools


class UserService:
    def __init__(self):
        self._datatools = DatabaseTools()
        self._password1 = None
        self._password2 = None
        self._email = None
        self._password = None

    def user_delete(self, email, password):
        fun_email = email
        fun_password = password
        self._datatools.delete_user(fun_email, fun_password)

    def change_password(self, in_email, password, in_password1, in_password2):
        self._password1 = in_password1
        self._password2 = in_password2
        email = in_email
        self._password = password

        if self._password1 == self._password2 and self._password1 is not None and self._password1 != "":
            try:
                self._datatools.update_password(
                    email,  self._password, self._password2)
                return True
            except Exception as error:
                return error
        elif self._password1 != self._password2:
            return False
        else:
            raise ValueError

    def gender_check(self, gender):
        if gender == "male" or gender == "female":
            error = True
        else:
            error = False
        return error

    def name_check(self, name):
        error = True
        letters = string.ascii_letters + " "
        for i in name:
            if i not in letters:
                error = False
        if name is None or error is False or name == "":
            error = False
        return error

    def fetch_weights_to_frame(self, email):
        weight_list = []
        date_list = []
        datacontent = self._datatools.fetch_all_from_weights(email)
        for row in datacontent:
            weight_list.append(row[0])
            date_list.append(row[1])
        return (weight_list, date_list)

    def email_check(self, in_email):
        email = in_email
        error = False
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (re.fullmatch(regex, email)) is not None:
            email_available = self._datatools.check_email_available(
                email)
            if email_available is None:
                error = True
            else:
                error = False
        return error

    def password_check(self, password1, password2):
        if password1 == password2 == "":
            return None
        if password1 == password2 and not password1 == password2 == "":
            return True
        else:
            return False

    def check_height_digit(self, height):
        error = True
        new_height = height
        dig = string.digits + "."
        for i in height:
            if i not in (dig):
                error = False
        if error is False or new_height is None or new_height == "":
            return False
        error = self._check_value_type(new_height)
        return error

    def _check_value_type(self, height):
        new_height = height
        error = True
        try:
            new_height = float(height)
            if 0.0 > new_height < 400.0:
                error = False
        except ValueError:
            pass
        return error
