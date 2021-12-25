from re import template
from tkinter import Frame, StringVar, Toplevel, constants, Button, Label, Entry
from tkinter.messagebox import askyesno, showinfo
from repositories.user_repository import DatabaseTools
from services.user_service import UserService
from ui.matplotlib_ui import MatplotlibUI
from repositories.intake_record_repository import RecordService


class UserUI:
    def __init__(self, root, email, password, login_view, calculator_view):
        self._root = root
        self._email = email
        self._password = password
        self._datatools = DatabaseTools()
        self._nutrition_function = NutritionFunctionalityUI
        self._user_serv = UserService()
        self._login_view = login_view
        self._calculator_view = calculator_view
        self._mathplo = MatplotlibUI(self._root, self._email)
        self.padding = {"padx": 5, "pady": 5}
        self._font = ("Roboto", 12)
        self._weightvar = None
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
            self._frame, text="Track", font=self._font,
            command=lambda: [self._mathplo._mathplotframe()])
        self._track_btn.grid(row=5, column=1, sticky="nsew", **self.padding)
        self._track_btn.bind("<Return>",
                             lambda click: [self._mathplo._mathplotframe()])

    def _weight_reset_field(self):
        self._weight_ent.delete(0, "end")

    def _weight_handling(self):
        self._weightvar = StringVar()
        self._weight_ent = Entry(self._frame, textvariable=self._weightvar,
                                 background="white", foreground="black", font=self._font, width=15)
        self._weightvar.set(" Insert weight here!")
        self._weight_ent.grid(row=4, column=1, sticky="nsew", **self.padding)
        self._update_weight = Button(
            self._frame, text="Add weight", font=self._font,
            command=lambda: [self._weight_update(), self._config_weight()])
        self._update_weight.bind("<Return>",
                                 lambda click: [self._weight_update(), self._config_weight()])
        self._update_weight.grid(
            row=3, column=1, sticky="nsew", **self.padding)
        self._delete_weight = Button(
            self._frame, text="Delete weight", font=self._font,
            command=lambda: [self._weight_delete(), self._config_weight()])
        self._delete_weight.bind(
            "<Return>", lambda click: [self._weight_delete(), self._config_weight()])
        self._delete_weight.grid(
            row=3, column=2, **self.padding, sticky="nsew")
        self._weight_ent.bind(
            "<Button-1>", lambda click: [self._weight_reset_field()])

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
        self._weight_label_show = Label(self._frame, textvariable=self._weight_var, fg="black", font=self._font,
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
        self._delete_account_btn.grid(
            row=1, column=2, sticky="nsew", **self.padding)
        self._delete_account_btn.bind(
            "<Return>", lambda click: [self._user_delete()])

    def _calculator_handling(self):
        self._calculator_btn = Button(
            self._frame, text="Calculator", font=self._font,
            command=lambda: [self._calculator_view(self._email, self._password)])
        self._calculator_btn.grid(
            row=5, column=2, sticky="nsew", **self.padding)
        self._calculator_btn.bind(
            "<Return>", lambda click: [self._calculator_view(self._email, self._password)])

    def _password_handling(self):
        self._password_btn = Button(
            self._frame, text="Change password", font=self._font,
            command=lambda: [self._password_change()])
        self._password_btn.grid(row=1, column=1, sticky="nsew", **self.padding)
        self._password_btn.bind("<Return>", lambda click: [
                                self._password_change()])

    def _logout_handling(self):
        self._logout_btn = Button(
            self._frame, text="Log out", font=self._font,
            command=lambda: [self._login_view()])
        self._logout_btn.grid(row=1, column=3, sticky="nsew", **self.padding)
        self._logout_btn.bind("<Return>", lambda click: [self._login_view()])

    def _user_screen_init(self):
        self._frame = Frame(self._root)
        self._password_handling()
        self._delete_user_handling()
        self._logout_handling()
        self._weight_show()
        self._weight_handling()
        self._track_handling()
        self._calculator_handling()
        self._nutrition_function(
            self._frame, self._email).initialize_functionality()

    def _win_destroy(self):
        self._password_btn["state"] = "active"
        self._win.destroy()

    def _password_change(self):
        answer = self._popask_win()
        if answer:
            self._password_btn["state"] = "disabled"
            self._win = Toplevel(self._frame)
            self._password1_lbl = Label(
                self._win, text="Enter password: ", font=self._font)
            self._password1_lbl.grid(
                row=1, column=1, sticky="nsew", **self.padding)
            self._passwordvar1 = StringVar(self._win)
            self._password_entry = Entry(
                self._win, textvariable=self._passwordvar1, show="*")
            self._password_entry.grid(
                row=1, column=2, sticky="nsew", **self.padding)
            self._password2_lbl = Label(
                self._win, font=self._font, text="Re-enter password: ").grid(row=2, column=1, sticky="nsew", **self.padding)
            self._passwordvar2 = StringVar(self._win)
            self._password_entry2 = Entry(
                self._win, textvariable=self._passwordvar2, show="*")
            self._password_entry2.grid(
                row=2, column=2, sticky="nsew", **self.padding)
            self._pass_done_btn = Button(
                self._win, text="Done", command=lambda: [self._password_change_finalization()])
            self._pass_done_btn.grid(
                row=3, column=1, sticky="nsew", **self.padding)
            self._pass_done_btn.bind(
                "<Return>", lambda click: [self._password_change_finalization()])
            self._win.protocol("WM_DELETE_WINDOW", self._win_destroy)

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
        self._win_destroy()


class NutritionFunctionalityUI:
    def __init__(self, root, email):
        self._email = email
        self._frame = root
        self._entity_serv = RecordService(self._email)
        self.intake = self._entity_serv.user_intake_load()
        self.padding = {"padx": 5, "pady": 5}
        self._font = ("Roboto", 12)

    def _add_del_protein(self, bool_val):
        try:
            if bool_val:
                self.intake.set_protein(int(self.protein_ent_var.get()))
            elif not bool_val:
                self.intake.set_protein(-int(self.protein_ent_var.get()))
            protein = self.intake.get_protein()
            self.protein_var.set(f"Protein: {protein} grams")
            self.calorie_var.set(
                f"Total calories: {self.intake._total_calorie_intake()}")
        except ValueError:
            showinfo("Error", f"Please, insert only integers.")

    def _protein_reset_field(self):
        self.protein_ent.delete(0, "end")
        return None

    def _protein_info_handling(self):
        self.protein_var = StringVar()
        self.protein_var.set(f"Protein: {self.intake.get_protein()} grams")
        protein_lbl = Label(self._frame, textvariable=self.protein_var,
                            bg="white", fg="Black", font=self._font)
        protein_lbl.grid(row=6, column=1, sticky="nsew", **self.padding)
        self.protein_ent_var = StringVar()
        self.protein_ent = Entry(
            self._frame, textvariable=self.protein_ent_var, font=self._font)
        self.protein_ent_var.set("Insert protein")
        self.protein_ent.grid(row=6, column=2)
        add_btn = Button(self._frame, text="+", font=self._font,
                         command=lambda: [self._add_del_protein(True), self._writing_to_file()])
        add_btn.grid(row=6, column=3, sticky="nsew")
        add_btn.bind("<Return>",
                     lambda click: [self._add_del_protein(True), self._writing_to_file()])
        del_btn = Button(self._frame, text="-", font=self._font,
                         command=lambda: [self._add_del_protein(False), self._writing_to_file()])
        del_btn.grid(row=6, column=4, sticky="nsew")
        del_btn.bind("<Return>",
                     lambda click: [self._add_del_protein(False), self._writing_to_file()])
        self.protein_ent.bind(
            "<Button-1>", lambda click: [self._protein_reset_field()])

    def _add_del_carbohydrates(self, bool_var):
        try:
            if bool_var:
                self.intake.set_carbohydrates(int(self.carbo_ent_var.get()))
            elif not bool_var:
                self.intake.set_carbohydrates(-int(self.carbo_ent_var.get()))
            carbos = self.intake.get_carbohydrates()
            self.carbo_var.set(f"Carbohydrates: {carbos} grams")
            self.calorie_var.set(
                f"Total calories: {self.intake._total_calorie_intake()}")
        except ValueError:
            showinfo("Error", f"Please, insert only integers.")

    def _carbo_reset_field(self):
        self.carbo_ent.delete(0, "end")
        return None

    def _carbohydrates_info_handling(self):
        self.carbo_var = StringVar()
        self.carbo_var.set(
            f"Carbohydrates: {self.intake.get_carbohydrates()} grams")
        carbo_lbl = Label(self._frame, textvariable=self.carbo_var,
                          bg="white", fg="Black", font=self._font)
        carbo_lbl.grid(row=7, column=1, sticky="nsew", **self.padding)
        self.carbo_ent_var = StringVar()
        self.carbo_ent = Entry(
            self._frame, textvariable=self.carbo_ent_var, font=self._font)
        self.carbo_ent_var.set("Insert carbohydrates")
        self.carbo_ent.grid(row=7, column=2)
        add_btn = Button(self._frame, text="+", font=self._font, command=lambda: [
                         self._add_del_carbohydrates(True), self._writing_to_file()])
        add_btn.grid(row=7, column=3, sticky="nsew")
        add_btn.bind("<Return>", lambda click: [
                     self._add_del_carbohydrates(True), self._writing_to_file()])
        del_btn = Button(self._frame, text="-", font=self._font, command=lambda: [
            self._add_del_carbohydrates(False), self._writing_to_file()])
        del_btn.grid(row=7, column=4, sticky="nsew")
        del_btn.bind("<Return>",
                     lambda click: [self._add_del_carbohydrates(False), self._writing_to_file()])
        self.carbo_ent.bind(
            "<Button-1>", lambda click: [self._carbo_reset_field()])

    def _add_del_fat(self, bool_var):
        try:
            if bool_var:
                self.intake.set_fat(int(self.fat_ent_var.get()))
            elif not bool_var:
                self.intake.set_fat(-int(self.fat_ent_var.get()))
            fats = self.intake.get_fat()
            self.fat_var.set(f"Fat: {fats} grams")
            self.calorie_var.set(
                f"Total calories: {self.intake._total_calorie_intake()}")
        except ValueError:
            showinfo("Error", f"Please, insert only integers.")

    def _reset_field(self):
        self.fat_ent.delete(0, "end")
        return None

    def _fat_info_handling(self):
        self.fat_var = StringVar()
        self.fat_var.set(f"Fat: {self.intake.get_fat()} grams")
        fat_lbl = Label(self._frame, textvariable=self.fat_var,
                        bg="white", fg="Black", font=self._font)
        fat_lbl.grid(row=8, column=1, sticky="nsew", **self.padding)
        self.fat_ent_var = StringVar()
        self.fat_ent = Entry(
            self._frame, textvariable=self.fat_ent_var, font=self._font)
        self.fat_ent_var.set("Insert fat")
        self.fat_ent.grid(row=8, column=2)
        add_btn = Button(self._frame, text="+", font=self._font,
                         command=lambda: [self._add_del_fat(True), self._writing_to_file()])
        add_btn.grid(row=8, column=3, sticky="nsew")
        add_btn.bind("<Return>", lambda click: [
            self._add_del_fat(True), self._writing_to_file()])
        del_btn = Button(self._frame, text="-", font=self._font,
                         command=lambda: [self._add_del_fat(False), self._writing_to_file()])
        del_btn.grid(row=8, column=4, sticky="nsew")
        del_btn.bind("<Return>", lambda click: [
                     self._add_del_fat(False), self._writing_to_file()])
        self.fat_ent.bind("<Button-1>", lambda click: [self._reset_field()])

    def _nutrition_calorie_handling(self):
        self.calorie_var = StringVar()
        self.calorie_var.set(
            f"Total calories: {self.intake._total_calorie_intake()}")
        calorie_lbl = Label(self._frame, textvariable=self.calorie_var,
                            bg="white", fg="Black", font=self._font)
        calorie_lbl.grid(row=9, column=1, sticky="nsew", **self.padding)

    def _writing_to_file(self):
        protein = self.intake.get_protein()
        carbohydrates = self.intake.get_carbohydrates()
        fat = self.intake.get_fat()
        self._entity_serv.write_record(protein, carbohydrates, fat)

    def initialize_functionality(self):
        self._protein_info_handling()
        self._carbohydrates_info_handling()
        self._fat_info_handling()
        self._nutrition_calorie_handling()
