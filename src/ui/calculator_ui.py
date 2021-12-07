from tkinter import Button, Label, OptionMenu, StringVar, Tk, Frame, Toplevel, constants, Entry
from tkinter.messagebox import showerror
import services.calculator_service as calculator_service
import services.entity_service as entity_service


class CalculatorScreen:
    def __init__(self, root, user_view, email, password):
        self._root = root
        self._email = email
        self._password = password
        self._user_view = user_view
        self._intake_entity = None
        self._calc = calculator_service.Calculator()
        self._usser = entity_service.EntityService(self._email)
        self.bmr = None
        self._leanmass = None
        self._mode = None
        self._frame = None
        self._toplevel = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def toplev_destroy(self):
        if self._toplevel is not None:
            self._toplevel.destroy()

    def popwin(self, message):
        showerror("Error!", message)

    def count_leanmass_bmr(self):
        lean_mass = self._lean_body_mass.get()
        if lean_mass is not None:
            try:
                self.bmr = self._calc.bmr_count(float(self._lean_mass))
            except ValueError as error:
                self.popwin(
                    f"Please insert only lean mass in kilograms and as Integer. Example: 16 , 17.4 , 12: {error}")
        print(self.bmr)

    def count_via_lbm(self):
        self._toplevel = Toplevel(self._frame)
        self._leanmass = StringVar()
        self.lean_body_mass = Entry(
            self._toplevel, textvariable=self._leanmass)
        self.lean_body_mass.grid(row=0, column=0, sticky="nsew")
        self._bmr_var = StringVar()
        self._bmr_var.set(self.bmr)
        self.label = Label(self._toplevel, textvariable=self._bmr_var).grid(
            row=1, column=0, sticky="nsew")
        Button(self._toplevel, text="Calculate", command=lambda: []).grid(
            row=4, column=0, sticky="nsew")
        Button(self._toplevel, text="Go Back", command=lambda: [
               self.toplev_destroy(), self._initialize()]).grid(row=4, column=1, sticky="nsew")

    def _span_suitable_screen(self):
        user = self._usser.return_user_entity()
        gender = user.get_gender
        height = user.get_height
        weight = user.get_weight
        user.get_entity_data_csv
        choosed_option = self._choosed_var.get()

        if choosed_option == "I'll count with my Lean Body Mass":
            self.count_via_lbm()
        elif choosed_option == "I'll count with my Body fat %":
            self._toplevel = Toplevel(self._frame)
            Button(self._toplevel, text="Go Back", command=lambda: [
                   self.toplev_destroy(), self._initialize()]).grid(row=4, column=4)
        elif choosed_option == "I'll count by estimating my Lean Body Mass":
            self._toplevel = Toplevel(self._frame)
            Button(self._toplevel, text="Go Back", command=lambda: [
                   self.toplev_destroy(), self._initialize()]).grid(row=4, column=4)

    def config_choosed_var(self):
        new_var = self._choosed_var.get()
        self._choosed_var.set(new_var)

    def config_calc_var(self):
        new_var = self.calc_var.get()
        self.calc_var.set(new_var)

    def _calculation_handle(self):
        calculate_mode_lbl = Label(self._frame, text="I want to calculate:").grid(
            row=0, column=0, sticky="nsew")
        calculation_options = ["Basal Metabolic Rate",
                               "Total Daily Energy Expenditure"]
        self.calc_var = StringVar()
        self.calc_var.set("Basal Metabolic Rate")
        calculate_menu = OptionMenu(
            self._frame, self.calc_var, *calculation_options, command=lambda x: [self.config_calc_var()])
        calculate_menu.grid(row=1, column=0, sticky="nsew")

    def _mode_handle(self):
        self._choosed_var = StringVar()
        self._choosed_var.set("I'll count with my Lean Body Mass")
        question_lbl = Label(
            master=self._frame, text="Choose one of the following options to count your BMR/TDEE?")
        question_lbl.grid(row=3, column=0)
        options = ["I'll count with my Lean Body Mass",
                   "I'll count with my Body fat %", "I'll count by estimating my Lean Body Mass"]
        menu = OptionMenu(self._frame, self._choosed_var, *options, command=lambda x: [
                          self.toplev_destroy(), self.config_choosed_var(), self._span_suitable_screen()])
        menu.grid(row=4, column=0, sticky="nsew")
        Button(self._frame, text="Go back", command=lambda: [self._user_view(
            self._email, self._password)]).grid(row=5, column=0, sticky="nsew")

    def _initialize(self):
        if self._frame is not None:
            self._frame.destroy()
        self._frame = Frame(master=self._root)
        self._mode_handle()
        self._calculation_handle()
        self.pack()
