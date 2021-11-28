from tkinter import Frame, StringVar, Toplevel, constants, Button, Label, Entry
from tkinter.messagebox import askyesno, showinfo
from repositories.user_repository import DatabaseTools
from services.user_service import UserService

class User:
    def __init__(self, root, email, password, login_view):
        self._root = root
        self._email = email
        self._password = password
        self._datatools = DatabaseTools()
        self._user_serv = UserService()
        self._login_view = login_view
        self._weightvar = None
        self._passwordvar1 = None
        self._passwordvar2 = None
        self._frame = None
        self._user_screen_init()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _user_delete(self):
        answer = self._user_serv.user_delete(self._email, self._password)
        if answer: self._login_view()

    def _popask_win(self):
        return askyesno("Confirmation", "Are you sure that you want to continue?")

    def _track_handling(self):
        self._track_btn = Button(
            self._frame, text="Track", command=None)
        self._track_btn.grid(row=5, column=1, sticky="nsew")
    
    def _reset_box(self):
        self._weight_ent.delete(0, constants.END)
        
    def _weight_handling(self):
        self._weightvar = StringVar() 
        self._weight_ent = Entry(self._frame, textvariable=self._weightvar, border=1, background="white", foreground="black", width=15)
        self._weightvar.set(" Insert weight here!")
        self._weight_ent.bind("<Button-1>", lambda Button_click:[self._reset_box()])
        self._weight_ent.grid(row=4, column=1, sticky="nsew")
        self._update_weight = Button(
            self._frame, text="Add weight", command=lambda:[self._weight_update(), self._config_weight()])
        self._update_weight.grid(row=3, column=1, sticky="nsew")
        self._delete_weight = Button(
            self._frame, text="Delete weight", command=lambda:[self._weight_delete(), self._config_weight()] 
        ).grid(row=3, column=2)
        
    def _weight_update(self):
        try:
            email = self._email
            weight = float(self._weightvar.get())
            self._datatools.insert_weight(email, weight)
        except ValueError:
            showinfo("Error:", f"Please insert weight in kilograms. For example: 192 or 195.12") 
            
    def _weight_show(self):
        self._weight = self._datatools.fetch_weight(self._email)
        self._weight_var = StringVar()
        if self._weight is None:
             self._weight_var.set(f"{0.0} kg")
        else:self._weight_var.set(f"{self._weight} kg")
        self._weight_label = Label(self._frame, text="Current Weight:", fg="black", background="white",borderwidth=2).grid(row=2, column=1, sticky="nsew")
        self._weight_label_show = Label(self._frame, textvariable=self._weight_var, fg="black", background="white", borderwidth=2).grid(row=2, column=2, sticky="nsew")     
    
    def _weight_delete(self):
        self._datatools.delete_weight(self._email)
    
    def _config_weight(self):
        self._weight = self._datatools.fetch_weight(self._email)
        if self._weight is None:
             self._weight_var.set(f"{0.0} kg")
        else: self._weight_var.set(f"{self._weight} kg")
        
    def _picture_handling(self):
        self._picture_btn = Button(self._frame, text="Pictures", command=None)
        self._picture_btn.grid(row=1, column=3, sticky="nsew")

    def _delete_user_handling(self):
        self._delete_account_btn = Button(
            self._frame, text="Delete Account", command=self._user_delete)
        self._delete_account_btn.grid(row=1, column=2, sticky="nsew")
    
    def _calculator_handling(self):
        self._calculator_btn = Button(self._frame, text="Calculator", command=None)
        self._calculator_btn.grid(row=5, column= 2, sticky="nsew")

    def _password_handling(self):
        self._password_btn = Button(
            self._frame, text="Change password", command=self._password_change)
        self._password_btn.grid(row=1, column=1, sticky="nsew")

    def _logout_handling(self):
        self._logout_btn = Button(
            self._frame, text="Log out", command=self._log_out)
        self._logout_btn.grid(row=1, column=3, sticky="nsew")
    
    def _log_out(self):
        self._login_view()

    def _user_screen_init(self):
        self._frame = Frame(self._root)
        self._delete_user_handling()
        self._picture_handling()
        self._password_handling()
        self._track_handling()
        self._weight_handling()
        self._logout_handling()
        self._calculator_handling()
        self._weight_show()

    def _password_change(self):
        self._password_btn["state"] = "disabled"
        answer = self._popask_win()
        if answer:
            self._win = Toplevel(self._frame)
            self._win.title("Password Change")
            self._password1_lbl = Label(
                self._win, text="Enter password: ").grid(row=1, column=1, sticky="nsew")
            self._passwordvar1 = StringVar(self._win)
            self._password_entry = Entry(
                self._win, textvariable=self._passwordvar1, show="*")
            self._password_entry.grid(row=1, column=2, sticky="nsew")
            self._password2_lbl = Label(
                self._win, text="Re-enter password: ").grid(row=2, column=1, sticky="nsew")
            self._passwordvar2 = StringVar(self._win)
            self._password_entry2 = Entry(
                self._win, textvariable=self._passwordvar2, show="*")
            self._password_entry2.grid(row=2, column=2, sticky="nsew")
            self._pass_done_btn = Button(
                self._win, text="Done", command=self._password_finalization).grid(row=3, column=1, sticky="nsew")
        else: self._password_btn["state"] = "active"

    def _password_finalization(self):
        first_password = self._passwordvar1.get()
        second_password = self._passwordvar2.get()
        self._user_serv.change_password(
            self._email, self._password, first_password, second_password)
        self._win.destroy()
        self._password_btn["state"] = "active"
