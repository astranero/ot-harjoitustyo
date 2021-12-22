from re import template
from tkinter import Frame, StringVar, Toplevel, constants, Button, Label, Entry
from tkinter.messagebox import askyesno, showinfo
from repositories.user_repository import DatabaseTools
from services.user_service import UserService
from ui.matplotlib_ui import MatplotlibUI
from services.entity_service import EntityService

class UserUI:
    def __init__(self, root, email, password, login_view, calculator_view):
        self._root = root
        self._email = email
        self._password = password
        self._datatools = DatabaseTools()
        self._entity_serv = EntityService(self._email)
        self._user_serv = UserService()
        self._login_view = login_view
        self._calculator_view = calculator_view
        self._mathplo = MatplotlibUI(self._root, self._email)
        self.padding = {"padx": 5, "pady": 5}
        self._font = ("Roboto", 12)
        self._weightvar = None
        self._protein_var = None
        self._passwordvar1 = None
        self._passwordvar2 = None
        self._frame = None
        self._user_screen_init()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _user_delete(self):
        answer = askyesno(
            "Confirmation", "Are you sure that you want to continue?")
        try:
            if answer:
                self._login_view()
                self._user_serv.user_delete(self._email, self._password)
        except Exception as error:
            showinfo("Error", "Error:" + f"{error}")

    def _popask_win(self):
        return askyesno("Confirmation", "Are you sure that you want to continue?")

    def _track_handling(self):
        self._track_btn = Button(
            self._frame, text="Track", font=self._font, command=lambda: [self._mathplo._mathplotframe()])
        self._track_btn.grid(row=5, column=1, sticky="nsew", **self.padding)

    def _weight_handling(self):
        self._weightvar = StringVar()
        self._weight_ent = Entry(self._frame, textvariable=self._weightvar,
                               background="white", foreground="black", font=self._font, width=15)
        self._weightvar.set(" Insert weight here!")
        self._weight_ent.grid(row=4, column=1, sticky="nsew", **self.padding)
        self._update_weight = Button(
            self._frame, text="Add weight", font=self._font, command=lambda: [self._weight_update(), self._config_weight()])
        self._update_weight.grid(row=3, column=1, sticky="nsew", **self.padding)
        self._delete_weight = Button(
            self._frame, text="Delete weight", font=self._font, command=lambda: [self._weight_delete(), self._config_weight()]
        ).grid(row=3, column=2, **self.padding, sticky="nsew")

    def _weight_update(self):
        try:
            email = self._email
            weight = float(self._weightvar.get())
            self._datatools.insert_weight(email, weight)
        except ValueError:
            showinfo(
                "Error:", f"Please insert weight in kilograms. For example: 192 or 195.12")

    def _weight_show(self):
        self._weight = self._datatools.fetch_weight(self._email)
        self._weight_var = StringVar()
        if self._weight is None:
            self._weight_var.set(f"{0.0} kg")
        else:
            self._weight_var.set(f"{self._weight} kg")
        self._weight_label = Label(self._frame, text="Current Weight:", fg="black", font=self._font,
                                   background="white", borderwidth=2).grid(row=2, column=1, sticky="nsew", **self.padding)
        self._weight_label_show = Label(self._frame, textvariable=self._weight_var, fg="black", font=self._font ,
                                        background="white", borderwidth=2).grid(row=2, column=2, sticky="nsew", **self.padding)

    def _weight_delete(self):
        try:
            self._datatools.delete_weight(self._email)
        except Exception as error:
            showinfo(f"{error}")

    def _config_weight(self):
        self._weight = self._datatools.fetch_weight(self._email)
        if self._weight is None:
            self._weight_var.set(f"{0.0} kg")
        else:
            self._weight_var.set(f"{self._weight} kg")

    def _delete_user_handling(self):
        self._delete_account_btn = Button(
            self._frame, text="Delete Account", font=self._font, command=self._user_delete)
        self._delete_account_btn.grid(row=1, column=2, sticky="nsew", **self.padding)

    def _calculator_handling(self):
        self._calculator_btn = Button(
            self._frame, text="Calculator",font=self._font, command=lambda: [self._calculator_view(self._email, self._password)])
        self._calculator_btn.grid(row=5, column=2, sticky="nsew", **self.padding)

    def _password_handling(self):
        self._password_btn = Button(
            self._frame, text="Change password", font=self._font, command=self._password_change)
        self._password_btn.grid(row=1, column=1, sticky="nsew", **self.padding)

    def _logout_handling(self):
        self._logout_btn = Button(
            self._frame, text="Log out", font=self._font, command=lambda: [self._login_view()])
        self._logout_btn.grid(row=1, column=3, sticky="nsew", **self.padding)

    def _add_del_protein(self, bool_val):
        try:
            if bool_val: 
                self.intake.set_protein(int(self.protein_ent_var.get()))
                print(self.intake.get_protein())
            elif not bool_val: self.intake.set_protein(-int(self.protein_ent_var.get()))
            protein = self.intake.get_protein()
            self.protein_var.set(f"Protein: {protein} grams")
        except ValueError:
            showinfo("Error", f"Please, insert only integers.")

    def _protein_info_handling(self):
        self.intake = self._entity_serv.user_intake_load()
        self.protein_var = StringVar()
        self.protein_var.set(f"Protein: {self.intake.get_protein()} grams")
        protein_lbl = Label(self._frame, textvariable=self.protein_var, bg="white", fg="Black", font=self._font)
        protein_lbl.grid(row=6, column=1, sticky="nsew", **self.padding)
        self.protein_ent_var = StringVar()
        protein_ent = Entry(self._frame, textvariable=self.protein_ent_var, font=self._font)
        self.protein_ent_var.set("Insert protein")
        protein_ent.grid(row=6, column=2)
        add_btn = Button(self._frame, text="+", font=self._font, command=lambda:[self._add_del_protein(True)])
        add_btn.grid(row=6, column=3, sticky="nsew")
        del_btn = Button(self._frame, text="-", font=self._font, command=lambda:[self._add_del_protein(False)])
        del_btn.grid(row=6, column=4, sticky="nsew")
    
    def _add_del_carbohydrates(self, bool_var):
         
    def _carbohydrates_info_handling(self):
        self.intake = self._entity_serv.user_intake_load()
        carbo_var = StringVar()
        carbo_var.set(self.intake.get_carbohydrates)
        carbo_lbl = Label(self._frame, text=f"Carbohydrates: {carbo_var.get()} grams", bg="white", fg="Black", font=self._font)
        self.intake.set_carbo(3)
        carbo_lbl.grid(row=7, column=1, sticky="nsew", **self.padding)
        carbo_ent_var = StringVar()
        carbo_ent = Entry(self._frame, textvariable=carbo_ent_var, font=self._font)
        carbo_ent_var.set("Insert carbohydrates")
        carbo_ent.grid(row=7, column=2)
        add_btn = Button(self._frame, text="+", font=self._font, command=lambda:[self._add_protein(True)])
        add_btn.grid(row=7, column=3, sticky="nsew")
        del_btn = Button(self._frame, text="-", font=self._font, command=lambda:[self._add_protein(False)])
        del_btn.grid(row=7, column=4, sticky="nsew")

    def _user_screen_init(self):
        self._frame = Frame(self._root)
        self._delete_user_handling()
        self._password_handling()
        self._track_handling()
        self._weight_handling()
        self._logout_handling()
        self._calculator_handling()
        self._weight_show()
        self._protein_info_handling()

    def _password_change(self):
        answer = self._popask_win()
        if answer:
            self._password_btn["state"] = "disabled"
            self._win = Toplevel(self._frame)
            self._password1_lbl = Label(
                self._win, text="Enter password: ", font=self._font)
            self._password1_lbl.grid(row=1, column=1, sticky="nsew", **self.padding)
            self._passwordvar1 = StringVar(self._win)
            self._password_entry = Entry(
                self._win, textvariable=self._passwordvar1, show="*")
            self._password_entry.grid(row=1, column=2, sticky="nsew", **self.padding)
            self._password2_lbl = Label(
                self._win,font=self._font, text="Re-enter password: ").grid(row=2, column=1, sticky="nsew", **self.padding)
            self._passwordvar2 = StringVar(self._win)
            self._password_entry2 = Entry(
                self._win, textvariable=self._passwordvar2, show="*")
            self._password_entry2.grid(row=2, column=2, sticky="nsew", **self.padding)
            self._pass_done_btn = Button(
                self._win, text="Done", command=self._password_change_finalization)
            self._pass_done_btn.grid(row=3, column=1, sticky="nsew", **self.padding)

    def _password_change_finalization(self):
        first_password = self._passwordvar1.get()
        second_password = self._passwordvar2.get()
        try:
            bol_value = self._user_serv.change_password(
                self._email, self._password, first_password, second_password)
            if bol_value:
                showinfo("Done", "Password has been changed!")
            elif bol_value == False:
                showinfo("Error", f"Passwords don't match")
        except Exception as error:
            showinfo("Error", f"Insert valid values: {error}")
        self._win.destroy()
        self._password_btn["state"] = "active"
