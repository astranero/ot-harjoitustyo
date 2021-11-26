from calendar import month
import tkinter as tk
from tkinter import Toplevel, constants, messagebox
import repositories.user_repository as tools
from tkcalendar import *
import services.user_service as usertool

class Register:
    
    def __init__(self, root, show_login_view):
        self._userServ = usertool.UserService()
        self._root = root
        self._loginScreen = show_login_view
        self._datatools = tools.DatabaseTools()
        self._name_entry = None
        self._surname_entry = None
        self._email_entry = None
        self._password1_entry = None
        self._password2_entry = None
        self._birthdate_entry = None
        self._gender_var = None
        self._height_lbl_entry = None
        self._frame = None
        self._title_lbl = None
        self._new_win = None
        
        self._register_screen()
        
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _getDate(self):
        self._birthdate_entry = self._cal.get_date()
        
    def _destroyDateScreen(self):
        self._new_win.destroy()
        self._date_btn["state"] = "active"
        
    def _fetchDate(self):
        self._date_btn["state"] = "disabled"
        date_of_birth_lbl = tk.Label(self._frame,text="Date of Birth")
        date_of_birth_lbl.grid(row=8, column=0, sticky="nsew")
        
        self._new_win = Toplevel()
        self._new_win.title("Date of Birth")
        self._new_win.geometry("400x400")
        self._cal = Calendar(self._new_win, selectmode="day", date_patern="dd-mm-y")
        self._cal.grid(row=0, column=0)
        
        
        self._chooseBtn = tk.Button(self._new_win, text="Choose", command=self._getDate).grid(row=1, column=0)
        self._exitBtn = tk.Button(self._new_win, text="Exit", command=self._destroyDateScreen).grid(row=1, column=1)
        
    def _fetchName(self):
        name_lbl = tk.Label(self._frame,text="First name")
        name_lbl.grid(row=2, column=0, sticky="nsew")
        
        self._name_entry = tk.StringVar()
        name_ent = tk.Entry(self._frame, textvariable=self._name_entry)
        name_ent.grid(row=2, column=1)
    
    def _fetchSurname(self):   
        surname_lbl = tk.Label(self._frame, text="Last name")
        surname_lbl.grid(row=4, column=0, sticky="nsew")

        self._surname_entry = tk.StringVar()
        surname_ent = tk.Entry(self._frame, textvariable=self._surname_entry)
        surname_ent.grid(row=4, column=1)
        
    def _fetchEmail(self):
        email_lbl = tk.Label(self._frame, text="Enter Email Address")
        email_lbl.grid(row=5, column=0, sticky="nsew")

        self._email_entry = tk.StringVar()
        email_ent = tk.Entry(self._frame, textvariable=self._email_entry)
        email_ent.grid(row=5, column=1)
    
    def _fetchPasswords(self):
          
        password1_lbl = tk.Label(self._frame, text="Enter Password")
        password1_lbl.grid(row=6, column=0, sticky="nsew")

        self._password1_entry = tk.StringVar()
        password1_ent = tk.Entry(self._frame, textvariable=self._password1_entry, show="*")
        password1_ent.grid(row=6, column=1)
        
        password2_lbl = tk.Label(self._frame,text="Enter Password")
        password2_lbl.grid(row=7, column=0, sticky="nsew")

        self._password2_entry = tk.StringVar()
        password2_ent = tk.Entry(self._frame, textvariable=self._password2_entry, show="*")
        password2_ent.grid(row=7, column=1)
    
    def _fetchHeight(self):
        height_lbl = tk.Label(self._frame,text="Height (cm)")
        height_lbl.grid(row=11, column=0, sticky="nsew")

        self._height_lbl_entry = tk.StringVar()
        height_lbl_ent = tk.Entry(self._frame, textvariable=self._height_lbl_entry)
        height_lbl_ent.grid(row=11, column=1)
    
    def _fetchGender(self):   
        
        gender_lbl = tk.Label(self._frame,text="Select Gender")
        gender_lbl.grid(row=9, column=0, sticky="nsew")
        self._gender_var = tk.StringVar()
        radio_btn_male = tk.Radiobutton(self._frame, text="Male", value="Male" , variable=self._gender_var, activeforeground="green")
        radio_btn_female = tk.Radiobutton(self._frame, text="Female", value="Female", variable=self._gender_var, activeforeground="green")
        radio_btn_male.grid(row=9, column=1, columnspan=3)
        radio_btn_female.grid(row=10, column=1, columnspan=3)
        
    def _register_screen(self):
        self._frame = tk.Frame(master=self._root) 
        
        self._title_lbl = tk.Label(self._frame, text="Registration")
        self._title_lbl.grid(row=0, column=0, columnspan=3)
        self._space = tk.Label(self._frame, text="     ")
        self._space.grid(row=1, column=0, columnspan=2)
        
        self._fetchName()
        self._fetchSurname()
        self._fetchEmail()
        self._fetchPasswords()
        self._fetchGender()
        self._fetchHeight()
        
        self._date_btn = tk.Button(self._frame, text="Choose Date of Birth", command=self._fetchDate)
        self._date_btn.grid(row=8, column=1)
        
        _login_btn = tk.Button(self._frame, text="Change to login Screen", command =self._loginScreen)
        _login_btn.grid(row=12, column=0)
        _register_btn = tk.Button(self._frame, text="Register", command=self._savedata)
        _register_btn.grid(row=12, column=1)
  
    
    def _errorWindow(self, message):
        messagebox.showinfo("Error:", message)
    
    def _savedata(self):
        name = self._name_entry.get()
        surname = self._surname_entry.get()
        email = self._email_entry.get().lower()
        password1 = self._password1_entry.get()
        password2 = self._password2_entry.get()
        birthdate = self._birthdate_entry
        gender = self._gender_var.get().lower()
        height = self._height_lbl_entry.get()
  
        try:    
            if self._userServ._nameCheck(name):
                if self._userServ._nameCheck(surname):
                    if self._userServ._emailCheck(email):
                        if self._userServ._passwordCheck(password1, password2):
                            if self._userServ._checkHeightIsDigits(height):
                                self._datatools._create_userSTR(name, surname, email, password1, birthdate, gender, height)
                                messagebox.showinfo("Hurray!", "Registration Succesful!")
                                self._loginScreen()
                                
        except Exception as e:
            self._errorWindow(f"There's something wrong with registration, Error: {e}")
        
            
        