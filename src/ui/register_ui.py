from tkcalendar import Calendar
import tkinter as tk
from tkinter import Toplevel, constants, messagebox
import repositories.user_repository as tools
import services.user_service as usertool


class Register:
    def __init__(self, root, show_login_view, show_user_view):
        self._checktool = CheckUi()
        self._root = root
        self._login_screen = show_login_view
        self._user_screen = show_user_view
        self._datatools = tools.DatabaseTools("Softfit.db")
        self.padding = {"padx": 5, "pady": 5}
        self._font = ("Roboto", 12)
        self._birthdate_entry = None
        self._frame = None
        self._register_screen()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _get_date(self):
        self._birthdate_entry = self._cal.get_date()

    def _popWindow(self, message_head, message):
        messagebox.showinfo(message_head, message)

    def _destroy_date_screen(self):
        self._new_win.destroy()
        self._date_btn["state"] = "active"

    def _fetch_date(self):
        self._date_btn["state"] = "disabled"
        self._new_win = Toplevel()
        self._new_win.title("Date of Birth")
        self._new_win.geometry("400x400")
        self._cal = Calendar(
            self._new_win, font=self._font, cursor="hand1",
            year=2001, day=1, month=1,  date_pattern="dd/MM/yyyy")
        self._cal.grid(row=0, column=0, **self.padding, sticky="nsew")
        self._choose_btn = tk.Button(
            self._new_win, text="Choose", command=lambda: [self._get_date(), self._destroy_date_screen()], font=self._font)
        self._choose_btn.grid(row=1, column=0, **self.padding, sticky="nsew")
        self._new_win.protocol("WM_DELETE_WINDOW", lambda: [
                               self._destroy_date_screen()])
        self._choose_btn.bind("<Return>", lambda click: [
                              self._get_date(), self._destroy_date_screen()])

    def _fetch_name(self):
        name_lbl = tk.Label(self._frame, text="First name", font=self._font)
        name_lbl.grid(row=2, column=0, sticky="nsew", **self.padding)
        self._name_entry = tk.StringVar()
        name_ent = tk.Entry(
            self._frame, textvariable=self._name_entry, font=self._font)
        name_ent.grid(row=2, column=1, **self.padding, sticky="nsew")

    def _fetch_surname(self):
        surname_lbl = tk.Label(self._frame, text="Last name", font=self._font)
        surname_lbl.grid(row=4, column=0, sticky="nsew", **self.padding)
        self._surname_entry = tk.StringVar()
        surname_ent = tk.Entry(
            self._frame, textvariable=self._surname_entry, font=self._font)
        surname_ent.grid(row=4, column=1, **self.padding, sticky="nsew")

    def _fetch_email(self):
        email_lbl = tk.Label(
            self._frame, text="Enter Email Address", font=self._font)
        email_lbl.grid(row=5, column=0, sticky="nsew", **self.padding)
        self._email_entry = tk.StringVar()
        email_ent = tk.Entry(
            self._frame, textvariable=self._email_entry, font=self._font)
        email_ent.grid(row=5, column=1, **self.padding, sticky="nsew")

    def _fetch_passwords(self):
        password1_lbl = tk.Label(
            self._frame, text="Enter Password", font=self._font)
        password1_lbl.grid(row=6, column=0, sticky="nsew", **self.padding)
        self._password1_entry = tk.StringVar()
        password1_ent = tk.Entry(
            self._frame, textvariable=self._password1_entry, show="*")
        password1_ent.grid(row=6, column=1, **self.padding, sticky="nsew")
        password2_lbl = tk.Label(
            self._frame, text="Enter Password", font=self._font)
        password2_lbl.grid(row=7, column=0, sticky="nsew", **self.padding)
        self._password2_entry = tk.StringVar()
        password2_ent = tk.Entry(
            self._frame, textvariable=self._password2_entry, show="*")
        password2_ent.grid(row=7, column=1, **self.padding, sticky="nsew")

    def _fetch_height(self):
        height_lbl = tk.Label(self._frame, text="Height (cm)", font=self._font)
        height_lbl.grid(row=11, column=0, sticky="nsew", **self.padding)
        self._height_lbl_entry = tk.StringVar()
        height_lbl_ent = tk.Entry(
            self._frame, textvariable=self._height_lbl_entry, font=self._font)
        height_lbl_ent.grid(row=11, column=1, **self.padding, sticky="nsew")

    def _fetch_gender(self):
        gender_lbl = tk.Label(
            self._frame, text="Select Gender", font=self._font)
        gender_lbl.grid(row=9, column=0, sticky="nsew", **self.padding)
        self._gender_var = tk.StringVar()
        self._radiobutton_value = False
        radio_btn_male = tk.Radiobutton(
            self._frame, text="Male", value="male", variable=self._gender_var, activeforeground="green", font=self._font)
        radio_btn_female = tk.Radiobutton(
            self._frame, text="Female", value="female", variable=self._gender_var, activeforeground="green", font=self._font)
        radio_btn_male.grid(row=9, column=1, columnspan=3,
                            **self.padding, sticky="nsew")
        radio_btn_female.grid(row=10, column=1, columnspan=3,
                              **self.padding, sticky="nsew")

    def _date_handle(self):
        date_of_birth_lbl = tk.Label(
            self._frame, text="Date of Birth", font=self._font)
        date_of_birth_lbl.grid(row=8, column=0, sticky="nsew", **self.padding)
        self._date_btn = tk.Button(
            self._frame, text="Choose Date of Birth", command=self._fetch_date, font=self._font)
        self._date_btn.bind("<Return>", lambda button_click: [
                            self._fetch_date()])
        self._date_btn.grid(row=8, column=1, **self.padding, sticky="nsew")

    def _screen_buttons(self):
        login_btn = tk.Button(
            self._frame, text="Change to login Screen", command=self._login_screen, font=self._font)
        login_btn.bind("<Return>", lambda button_click: [self._login_screen()])
        login_btn.grid(row=12, column=0, **self.padding, sticky="nsew")
        register_btn = tk.Button(
            self._frame, text="Register", command=self._savedata, font=self._font)
        register_btn.bind("<Return>", lambda button_click: [self._savedata()])
        register_btn.grid(row=12, column=1, **self.padding, sticky="nsew")

    def _register_screen(self):
        self._frame = tk.Frame(master=self._root)
        self._space = tk.Label(self._frame, text="     ", font=self._font)
        self._space.grid(row=1, column=0, columnspan=2,
                         **self.padding, sticky="nsew")
        self._fetch_name()
        self._fetch_surname()
        self._fetch_email()
        self._fetch_passwords()
        self._date_handle()
        self._fetch_gender()
        self._fetch_height()
        self._screen_buttons()

    def _information_authentication(self, name, surname, email, password1, password2, birthdate, gender, height):
        try:
            if self._checktool.name_check_handling(name):
                if self._checktool.name_check_handling(surname):
                    if self._checktool.email_check_handling(email):
                        if self._checktool.password_check_handling(password1, password2):
                            if self._checktool.birthdate_check_handling(birthdate):
                                if self._checktool.gender_check_handling(gender):
                                    if self._checktool.height_check_handling(height):
                                        self._datatools.create_user(
                                            name, surname, email, password1, birthdate, gender, height)
                                        self._popWindow(
                                            "Hurray!", "Registration Succesful!")
                                        self._user_screen(email, password1)
        except Exception as error:
            self._popWindow("Error!",
                            f"There's something wrong with registration, Error: {error}")

    def _savedata(self):
        name = self._name_entry.get()
        surname = self._surname_entry.get()
        email = self._email_entry.get().lower()
        password1 = self._password1_entry.get()
        password2 = self._password2_entry.get()
        birthdate = self._birthdate_entry
        gender = self._gender_var.get().lower()
        height = self._height_lbl_entry.get()
        self._information_authentication(
            name, surname, email, password1, password2, birthdate, gender, height)


class CheckUi:
    def __init__(self):
        self._usertool = usertool.UserService()

    def _error_window(self, message):
        messagebox.showinfo("Notification:", message)

    def name_check_handling(self, name):
        bol_value = self._usertool.name_check(name)
        if bol_value == False:
            self._error_window("Name fields should contain letters.")
        else:
            return True

    def birthdate_check_handling(self, birthdate):
        if birthdate is None:
            self._error_window("Please choose Date of Birth.")
            return False
        return True

    def email_check_handling(self, email):
        try:
            bol_value = self._usertool.email_check(email)
            if bol_value == False:
                self._error_window("Incorrect Email Address.")
                return False
            else:
                return True
        except Exception as error:
            self._error_window(f"Error: {error}")

    def password_check_handling(self, password1, password2):
        try:
            return_value = self._usertool.password_check(password1, password2)
            if not return_value:
                self._error_window("Password can't be null.")
            elif return_value:
                return True
            else:
                self._error_window("Passwords don't match!")
        except Exception as error:
            self._error_window(f"Error: {error}")

    def gender_check_handling(self, gender):
        return_value = self._usertool.gender_check(gender)
        if return_value:
            return True
        self._error_window("Please choose gender.")
        return False

    def height_check_handling(self, height):
        return_value = self._usertool.check_height_digit(height)
        if return_value is False:
            self._error_window("""Please insert height as centimeters
             in digits and dots, between range of 0.0 to 400.0 cm, please.""")
            return False
        return True
