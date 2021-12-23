import tkinter as tk
from tkinter import constants, messagebox
from tkinter import font
import repositories.user_repository as tools


class LoginScreen:
    def __init__(self, root, show_register_view, show_user_view):
        self._cur = tools.DatabaseTools()
        self._root = root
        self._email_entry = None
        self._password_entry = None
        self.padding = {"padx": 5, "pady": 5}
        self._font = ("Roboto", 12)
        self._show_register_view = show_register_view
        self._show_user_view = show_user_view
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _popup_win(self, message):
        messagebox.showinfo("Notification", message)

    def _user_handling(self, in_email, in_password):
        email = in_email
        password = in_password
        try:
            email_value = self._cur.check_email(email, password)
            password_value = self._cur.check_password(email, password)
            if email_value is not None and password_value is not None:
                if email_value[0] == email and password_value[0] == password:
                    self._show_user_view(email, password)
            else:
                self._popup_win("Email or password is incorrect.")
        except Exception as e:
            self._popup_win(f"Something went wrong: {e}!")

    def _email_handing(self):
        email_lbl = tk.Label(self._frame, text="Email", font=self._font)
        email_lbl.grid(row=2, column=0, sticky="nsew", **self.padding)
        self._email_entry = tk.StringVar(self._frame)
        email_ent = tk.Entry(
            self._frame, textvariable=self._email_entry, font=self._font)
        email_ent.grid(row=2, column=1, sticky="nsew")

    def _password_handling(self):
        password_lbl = tk.Label(self._frame, text="Password", font=self._font)
        password_lbl.grid(row=3, column=0, sticky="nsew", **self.padding)
        self._password_entry = tk.StringVar(self._frame)
        password_ent = tk.Entry(
            self._frame, textvariable=self._password_entry, show="*", font=self._font)
        password_ent.grid(row=3, column=1, sticky="nsew")

    def _screen_handling(self):
        btn_login = tk.Button(
            self._frame,
            text="Login",
            command=self._login_start,
            font=self._font)
        btn_login.grid(row=4, column=0, sticky="nsew", **self.padding)
        btn_login.bind("<Return>", lambda button_click: [self._login_start()])
        btn_register = tk.Button(
            master=self._frame,
            text="Create User",
            command=self._show_register_view,
            font=self._font)
        btn_register.grid(row=4, column=1, sticky="nsew", **self.padding)
        btn_register.bind("<Return>", lambda button_click: [
                          self._show_register_view()])

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)
        heading_lbl = tk.Label(
            self._frame, text="Login Screen", font=self._font)
        heading_lbl.grid(row=1, column=1, sticky="nsew", **self.padding)
        self._email_handing()
        self._password_handling()
        self._screen_handling()

    def _login_start(self):
        email = self._email_entry.get()
        password = self._password_entry.get()
        self._user_handling(email, password)
