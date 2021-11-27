from tkinter import Frame, StringVar, Toplevel, constants, Button, Label, Entry
from services.calculator_service import *
from tkinter.messagebox import askyesno
from repositories.user_repository import DatabaseTools
from services.user_service import UserService


class User:
    def __init__(self, root, email, password, login_view):
        self._root = root
        self._email = email
        self._calculator = Calculator()
        self._datatools = DatabaseTools()
        self._user_serv = UserService()
        self._login_view = login_view
        self._password = password
        self._passwordvar1 = None
        self._passwordvar2 = None
        self._frame = None
        self._user_screen_init()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _user_delete(self):
        self._user_serv._user_delete(self._email, self._password)
        self._login_view()

    def _popask_win(self):
        return askyesno("Confirmation", "Are you sure that you want to continue?")

    def _calculate_handling(self):
        self._cal_btn = Button(
            self._frame, text="Calculate", command=lambda: print("pöö"))
        self._cal_btn.grid(row=10, column=1)

    def _track_handling(self):
        self._weight_btn = Button(
            self._frame, text="Track", command=lambda: print("pöö"))
        self._update_weight = Button(
            self._frame, text="Add weight", command=None)
        self._weight_btn.grid(row=1, column=2)

    def _picture_handling(self):
        self._picture_btn = Button(self._frame, text="Pictures", command=None)
        self._picture_btn.grid(row=1, column=3)

    def _delete_handling(self):
        self._delete_account_btn = Button(
            self._frame, text="Delete Account", command=self._user_delete)
        self._delete_account_btn.grid(row=1, column=1)

    def _password_handling(self):
        self._password_btn = Button(
            self._frame, text="Change password", command=self._password_change)
        self._password_btn.grid(row=5, column=5)

    def _logout_handling(self):
        self._logout_btn = Button(
            self._frame, text="LogOut", command=self._log_out)
        self._logout_btn.grid(row=1, column=5)

    def _log_out(self):
        self._login_view()

    def _user_screen_init(self):
        self._frame = Frame(self._root)
        self._calculate_handling()
        self._delete_handling()
        self._picture_handling()
        self._password_handling()
        self._track_handling()
        self._logout_handling()

    def _password_change(self):
        self._password_btn["state"] = "disabled"
        answer = self._popAskWin()
        if answer:
            self._win = Toplevel(self._frame)
            self._win.title("Password Change")
            self._password1_lbl = Label(
                self._win, text="Enter password: ").grid(row=1, column=1)
            self._passwordvar1 = StringVar(self._win)
            self._password_entry = Entry(
                self._win, textvariable=self._passwordvar1, show="*")
            self._password_entry.grid(row=1, column=2)
            self._password2_lbl = Label(
                self._win, text="Re-enter password: ").grid(row=2, column=1)
            self._passwordvar2 = StringVar(self._win)
            self._password_entry2 = Entry(
                self._win, textvariable=self._passwordvar2, show="*")
            self._password_entry2.grid(row=2, column=2)
            self._pass_done_btn = Button(
                self._win, text="Done", command=self._password_finalization).grid(row=3, column=1)

    def _password_finalization(self):
        first_password = self._passwordvar1.get()
        second_password = self._passwordvar2.get()
        self._user_serv._change_password(
            self._email, first_password, second_password)
        self._win.destroy()
        self._password_btn["state"] = "active"
