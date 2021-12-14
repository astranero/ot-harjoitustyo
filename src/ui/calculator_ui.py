from tkinter import Button, Label, OptionMenu, StringVar, Tk, Frame, Toplevel, constants, Entry
import tkinter as tk
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
        self._calculator = calculator_service.Calculator()
        self._usser = entity_service.EntityService(self._email)
        self.bmr = None
        self.framesec = None
        self._leanmass = None
        self._activity_level = None
        self._bodyfat = None
        self._frame = None
        self._tdee = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def framesec_destroy(self):
        self._framesec.destroy

    def popwin(self, message):
        showerror("Error!", message)

    def count_bmr_with_leanmass(self):
        lean_mass = self._leanmass.get()
        if lean_mass is not None:
            try:
                self.bmr = round(
                    self._calculator.bmr_count(float(lean_mass)), 3)
            except ValueError as error:
                self.popwin(
                    f"Please insert only lean mass in kilograms and as Integer. Example: 16 , 17.4 , 12: {error}")
        self._var.set(f"{self.bmr} kcal/per day")

    def count_bmr_with_bodyfat(self):
        user = self._usser.return_user_entity()
        weight = user.get_weight()
        body_fat = self._bodyfat.get()
        if body_fat is not None:
            try:
                leanmass = round(self._calculator._count_lean_body_mass_with_fatpercent(
                    float(body_fat), float(weight)))
                self.bmr = round(
                    self._calculator.bmr_count(float(leanmass)), 3)
            except ValueError as error:
                self.popwin(
                    f"Please insert weight and body fat as a float. {error}")
        self._var.set(f"{self.bmr} kcal/per day")

    def count_bmr_with_estimated_leanmass(self):
        try:
            user = self._usser.return_user_entity()
            weight = float(user.get_weight())
            gender = user.get_gender()
            height = float(user.get_height())
            estimate = self._calculator._lean_body_mass_estimate(
                weight, height, gender)
            self.bmr = round(self._calculator.bmr_count(estimate), 2)
        except ValueError as error:
            self.popwin(f"{error}")
        self._var.set(f"{self.bmr} kcal/per day")

    def calculator_frame1(self, frame):
        self._leanframe = frame
        self._leanmass = StringVar(self._leanframe)
        Label(self._leanframe, text="Lean body mass (kg): ").grid(
            row=0, column=0, sticky="nsew")
        self.lean_body_mass = Entry(
            self._leanframe, textvariable=self._leanmass)
        self.lean_body_mass.grid(row=0, column=1, sticky="nsew")
        self.calculator_frame3(self._leanframe, lambda: [
                               self.count_bmr_with_leanmass()])

    def calculator_frame2(self, frame):
        self._fatframe = frame
        self._bodyfat = StringVar(self._fatframe)
        Label(self._fatframe, text="Body fat %: ").grid(
            row=0, column=0, sticky="nsew")
        self.bodyfat_percentage = Entry(
            self._fatframe, textvariable=self._bodyfat)
        self.bodyfat_percentage.grid(row=0, column=1, sticky="nsew")
        self.calculator_frame3(self._fatframe, lambda: [
                               self.count_bmr_with_bodyfat()])

    def calculator_frame3(self, frame, xcommand):
        self._allframe = frame
        Label(self._allframe, text="Basal Metabolic rate: ").grid(
            row=1, column=0, sticky="nsew")
        self._var = StringVar(self._allframe)
        self.label = Label(self._allframe, textvariable=self._var).grid(
            row=1, column=1, sticky="nsew")
        Button(self._allframe, text="Calculate BMR", command=lambda: [xcommand(), self.button_tdee()]).grid(
            row=2, column=0, sticky="nsew")

    def button_tdee(self):
        tdee_btn = Button(self._allframe, text="Continue to TDEE Calculation",
                          command=lambda: self.total_expenditure_frame(self._allframe))
        tdee_btn.grid(row=2, column=1)

    def tdee_calculation(self):
        activity_level = self._activity_level.get()
        self._tdee_var.set(self._calculator.total_daily_energy_expenditure(
            self.bmr, activity_level))

    def total_expenditure_frame(self, frame):
        self._frame_expend = frame
        self._activity_level = StringVar(self._frame_expend)
        Label(self._frame_expend, text="Choose activity level to count TDEE.").grid(
            row=3, column=0, sticky="nsew")
        activity_levels = ["Inactive", "Low",
                           "Medium", "Medium-high", "High", "Intense"]
        self._activity_level.set("Inactive")
        self._tdee_var = StringVar(self._frame_expend)
        Label(self._frame_expend, text="Total Daily Energy Expenditure: ").grid(
            row=4, column=0, sticky="nsew")
        Label(self._frame_expend, textvariable=self._tdee_var).grid(
            row=4, column=1, sticky="nsew")
        OptionMenu(self._frame_expend, self._activity_level, *activity_levels,
                   command=lambda x: [self.tdee_calculation()]).grid(row=3, column=1, sticky="nsew")

    def _refresh_frame(self):
        if self._framesec is not None:
            self._framesec.destroy()
        self._framesec = Frame(self._frame)

    def _span_suitable_screen(self):
        choosed_option = self._choosed_var.get()
        if choosed_option == "I'll count with my Lean Body Mass":
            self._refresh_frame()
            self.calculator_frame1(self._framesec)
            self._framesec.grid()
        elif choosed_option == "I'll count with my Body fat %":
            self._refresh_frame()
            self.calculator_frame2(self._framesec)
            self._framesec.grid()
        elif choosed_option == "I'll count by estimating my Lean Body Mass":
            self._refresh_frame()
            self.calculator_frame3(self._framesec, lambda: [
                                   self.count_bmr_with_estimated_leanmass()])
            self._framesec.grid()

    def _basal_frame(self):
        self._choosed_var = StringVar(self._frame)
        self._choosed_var.set("I'll count with my Lean Body Mass")
        question_lbl = Label(
            master=self._frame, text="Choose one of the following options to count your BMR/TDEE?")
        question_lbl.grid(row=3, column=0, sticky="nsew")
        options = ["I'll count with my Lean Body Mass",
                   "I'll count with my Body fat %", "I'll count by estimating my Lean Body Mass"]
        menu = OptionMenu(self._frame, self._choosed_var, *options, command=lambda x: [
            self._span_suitable_screen()])
        menu.grid(row=4, column=0, sticky="nsew")

    def _initialize(self):
        self._frame = Frame(master=self._root)
        Button(self._frame, text="Go back", command=lambda: [self._user_view(
            self._email, self._password)]).grid(row=0, column=0, sticky="nsew")
        self._framesec = Frame(master=self._frame)
        self._basal_frame()
        self.pack()
