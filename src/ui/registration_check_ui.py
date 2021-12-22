import services.user_service as usertool
from tkinter.messagebox import showinfo


class CheckUi:
    def __init__(self):
        self._usertool = usertool.UserService()

    def _error_window(self, message):
        showinfo("Notification:", message)

    def _name_check_handling(self, name):
        bol_value = self._usertool.name_check(name)
        if bol_value == False:
            self._error_window("Name fields should contain letters.")
        else:
            return True

    def _birthdate_check_handling(self, birthdate):
        if birthdate is None:
            self._error_window("Please choose Date of Birth.")
            return False
        return True

    def _email_check_handling(self, email):
        try:
            bol_value = self._usertool.email_check(email)
            if bol_value == False:
                self._error_window("Incorrect Email Address.")
                return False
            else:
                return True
        except Exception as error:
            self._error_window(f"Error: {error}")

    def _password_check_handling(self, password1, password2):
        try:
            return_value = self._usertool.password_check(password1, password2)
            if return_value is None:
                self._error_window("Password can't be null.")
            elif return_value:
                return True
            else:
                self._error_window("Passwords don't match!")
        except Exception as error:
            self._error_window(f"Error: {error}")

    def _gender_check_handling(self, gender):
        return_value = self._usertool.gender_check(gender)
        if return_value:
            return True
        self._error_window("Please choose gender.")
        return False

    def _height_check_handling(self, height):
        return_value = self._usertool.check_height_digit(height)
        if return_value is False:
            self._error_window("""Please insert height as centimeters
             in digits and dots, between range of 0.0 to 400.0 cm, please.""")
            return False
        return True
