import sqlite3
import string
import re
from tkinter.messagebox import askyesno, showinfo
from repositories.user_repository import DatabaseTools
from datetime import date


class UserService:
    def __init__(self):
        self._datatools = DatabaseTools()
        self._password1 = None
        self._password2 = None
        self._email = None
        self._password = None

    def _error_window(self, message):
        showinfo("Error:", message)

    def user_delete(self, email, password):
        fun_email = email
        fun_password = password
        answer = askyesno(
            "Confirmation", "Are you sure that you want to continue?")
        if answer:
            try:
                self._datatools.delete_user(fun_email, fun_password)
            except sqlite3.Error as error:
                showinfo("Error", "Error:" + f"{error}")
        return answer

    def change_password(self, in_email, password, in_password1, in_password2):
        self._password1 = in_password1
        self._password2 = in_password2
        email = in_email
        self._password = password
        try:
            if self._password1 == self._password2 and self._password1 is not None and self._password1 != "":
                self._datatools.update_password(
                    email,  self._password, self._password2)
                showinfo("Done", "Password has been changed!")
        except sqlite3.Error as error:
            showinfo(f"Error, {error}")

    def gender_check(self, gender):
        if gender == "male" or gender == "female":
            error = True
        else:
            error = False
            self._error_window("Please choose gender.")
        return error

    def name_check(self, name):
        error = True
        letters = string.ascii_letters + " "
        for i in name:
            if i not in letters:
                error = False
        if name is None or error is False or name == "":
            error = False
            self._error_window("Name fields should contain letters.")
        return error

    def fetch_weights_to_frame(self, email):
        weight_list = []
        date_list = []
        datacontent = self._datatools.fetch_40_from_weights(email)
        for row in datacontent:
            weight_list.append(row[0])
            date_list.append(row[1])
        return (weight_list, date_list)

    def email_check(self, in_email):
        email = in_email
        error = False
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (re.fullmatch(regex, email)) is not None:
            try:
                email_available = self._datatools.check_email_available(
                    email)
                if email_available is not None:
                    self._error_window("Email is already in use!")
                error = True
            except sqlite3.Error as error_war:
                self._error_window(f"Error: {error_war}")
        else:
            self._error_window("Incorrect Email Address.")
        return error

    def password_check(self, password1, password2):
        error = False
        if password1 == password2 == "":
            self._error_window("Password can't be null.")
            return error
        if password1 == password2 and not password1 == password2 == "":
            error = True
        else:
            self._error_window("Passwords don't match!")
        return error

    def check_height_digit(self, height):
        error = True
        new_height = height
        dig = string.digits + "."
        for i in height:
            if i not in (dig):
                error = False
        if error is False or new_height is None or new_height == "":
            self._error_window(
                "Please insert height as centimeters in digits and dots, please.")
            return False
        error = self._check_value_type(new_height)
        return error

    def _check_value_type(self, height):
        new_heigh = height
        error = True

        try:
            new_heigh = float(height)
            if 0.0 > new_heigh > 300.0:
                error = False
                showinfo("Are you even human?")
        except ValueError:
            pass
        return error
