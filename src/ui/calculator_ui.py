from tkinter import Button, Label, OptionMenu, StringVar, Tk, Frame, Toplevel, constants, Entry
import tkinter as tk
from tkinter.messagebox import showerror
import services.calculator_service as calculator_service
import repositories.intake_record_repository as intake_record_repository
import repositories.user_repository as user_repo


class CalculatorScreen:
    def __init__(self, root, user_view, email, password):
        self._root = root
        self._email = email
        self._password = password
        self._user_view = user_view
        self._datatools = user_repo.DatabaseTools("Softfit.db")
        self._calculator = calculator_service.Calculator()
        self._usser = intake_record_repository.RecordService(self._email,"records.txt")
        self.bmr = None
        self.framesec = None
        self._leanmass = None
        self._activity_level = None
        self._bodyfat = None
        self._frame = None
        self._tdee = None
        self.padding = {"padx": 5, "pady": 5}
        self._font = ("Roboto", 12)
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _popwin(self, message):
        showerror("Error!", message)

    def _count_bmr_with_leanmass(self):
        lean_mass = self._leanmass.get()
        if lean_mass is not None:
            try:
                self.bmr = round(
                    self._calculator.bmr_count(float(lean_mass)), 3)
            except ValueError as error:
                self._popwin(
                    f"Please insert only lean mass in kilograms and as Integer. Example: 16 , 17.4 , 12: {error}")
        self._var.set(f"{self.bmr} kcal/per day")

    def _count_bmr_with_bodyfat(self):
        weight = self._datatools.fetch_weight(self._email)
        body_fat = self._bodyfat.get()
        if body_fat is not None:
            try:
                leanmass = round(self._calculator.count_lean_body_mass_with_fatpercent(
                    float(body_fat), float(weight)))
                self.bmr = round(
                    self._calculator.bmr_count(float(leanmass)), 3)
            except ValueError as error:
                self._popwin(
                    f"Please insert weight and body fat as a float. {error}")
        self._var.set(f"{self.bmr} kcal/per day")

    def _count_bmr_with_estimated_leanmass(self):
        try:
            data = self._datatools.fetch_user_info(self._email)
            gender = data[6]
            height = float(data[7])
            weight = float(self._datatools.fetch_weight(self._email))
            estimate = self._calculator.lean_body_mass_estimate(
                weight, height, gender)
            self.bmr = round(self._calculator.bmr_count(estimate), 2)
        except ValueError as error:
            self._popwin(f"{error}")
        self._var.set(f"{self.bmr} kcal/per day")

    def _refresh_frame(self):
        if self._framesec is not None:
            self._framesec.destroy()
        self._framesec = Frame(self._frame)

    def _span_suitable_screen(self):
        choosed_option = self._choosed_var.get()
        if choosed_option == "I'll count with my Lean Body Mass":
            self._refresh_frame()
            self._calculator_frame1(self._framesec)
            self._framesec.grid()
        elif choosed_option == "I'll count with my Body fat %":
            self._refresh_frame()
            self._calculator_frame2(self._framesec)
            self._framesec.grid()
        elif choosed_option == "I'll count by estimating my Lean Body Mass":
            self._refresh_frame()
            self._calculator_frame3(self._framesec, lambda: [
                self._count_bmr_with_estimated_leanmass()])
            self._framesec.grid()

    def _calculator_frame1(self, frame):
        self._leanframe = frame
        self._leanmass = StringVar(self._leanframe)
        Label(self._leanframe, font=self._font, text="Lean body mass (kg): ").grid(
            row=0, column=0, sticky="nsew", **self.padding)
        self.lean_body_mass = Entry(
            self._leanframe, textvariable=self._leanmass, font=self._font)
        self.lean_body_mass.grid(
            row=0, column=1, sticky="nsew", **self.padding)
        self._calculator_frame3(self._leanframe, lambda: [
            self._count_bmr_with_leanmass()])

    def _calculator_frame2(self, frame):
        self._fatframe = frame
        self._bodyfat = StringVar(self._fatframe)
        Label(self._fatframe, font=self._font, text="Body fat %: ").grid(
            row=0, column=0, sticky="nsew", **self.padding)
        self.bodyfat_percentage = Entry(
            self._fatframe, textvariable=self._bodyfat, font=self._font)
        self.bodyfat_percentage.grid(
            row=0, column=1, sticky="nsew", **self.padding)
        self._calculator_frame3(self._fatframe, lambda: [
            self._count_bmr_with_bodyfat()])

    def _calculator_frame3(self, frame, xcommand):
        self._allframe = frame
        Label(self._allframe, text="Basal Metabolic rate: ", font=self._font).grid(
            row=1, column=0, sticky="nsew", **self.padding)
        self._var = StringVar(self._allframe)
        self.label = Label(self._allframe, textvariable=self._var, font=self._font).grid(
            row=1, column=1, sticky="nsew", **self.padding)
        cal_btn = Button(self._allframe, text="Calculate BMR", font=self._font,
                         command=lambda: [xcommand(), self._button_tdee()])
        cal_btn.bind("<Return>", lambda click: [
                     xcommand(), self._button_tdee()])
        cal_btn.grid(row=2, column=0, sticky="nsew", **self.padding)

    def _button_tdee(self):
        tdee_btn = Button(self._allframe, text="Continue to TDEE Calculation",
                          command=lambda: self._total_expenditure_frame(self._allframe), font=self._font)
        tdee_btn.bind(
            "<Return>", lambda click: self._total_expenditure_frame(self._allframe))
        tdee_btn.grid(row=2, column=1, **self.padding)

    def _tdee_calculation(self):
        activity_level = self._activity_level.get()
        self._tdee_var.set(
            f"""{self._calculator.total_daily_energy_expenditure(self.bmr, activity_level)} kcal/ per""")

    def _total_expenditure_frame(self, frame):
        self._frame_expend = frame
        self._activity_level = StringVar(self._frame_expend)
        Label(self._frame_expend, text="Choose activity level to count TDEE.", font=self._font).grid(
            row=3, column=0, sticky="nsew", **self.padding)
        activity_levels = ["Inactive", "Low",
                           "Medium", "Medium-high", "High", "Intense"]
        self._activity_level.set("Inactive")
        self._tdee_var = StringVar(self._frame_expend)
        Label(self._frame_expend, text="Total Daily Energy Expenditure: ", font=self._font).grid(
            row=4, column=0, sticky="nsew", **self.padding)
        Label(self._frame_expend, textvariable=self._tdee_var, font=self._font).grid(
            row=4, column=1, sticky="nsew", **self.padding)
        expenditure_menu = OptionMenu(self._frame_expend, self._activity_level, *activity_levels,
                                      command=lambda x: [self._tdee_calculation()])
        expenditure_menu.grid(row=3, column=1, sticky="nsew", **self.padding)
        expenditure_menu.config(font=self._font)

    def _basal_frame(self):
        self._choosed_var = StringVar(self._frame)
        self._choosed_var.set("I'll count with my Lean Body Mass")
        question_lbl = Label(
            master=self._frame, text="Choose one of the following options to count your BMR/TDEE?", font=self._font)
        question_lbl.grid(row=3, column=0, sticky="nsew", **self.padding)
        options = ["I'll count with my Lean Body Mass",
                   "I'll count with my Body fat %", "I'll count by estimating my Lean Body Mass"]
        menu = OptionMenu(self._frame, self._choosed_var, *options, command=lambda x: [
            self._span_suitable_screen()])
        menu.grid(row=4, column=0, sticky="nsew", **self.padding)
        menu.bind("Return", lambda x: [self._span_suitable_screen()])
        menu.config(font=self._font)

    def _initialize(self):
        self._frame = Frame(master=self._root)
        goback_btn = Button(self._frame, text="Go back", command=lambda: [self._user_view(
            self._email, self._password)], font=self._font)
        goback_btn.bind("<Return>", lambda click: [
                        self._user_view(self._email, self._password)])
        goback_btn.grid(row=0, column=0, sticky="nsew", **self.padding)
        self._framesec = Frame(master=self._frame)
        self._basal_frame()
        self.pack()
