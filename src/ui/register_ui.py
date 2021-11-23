import tkinter as tk
from tkinter import constants
import database.database_tools as tools
import re

class Register:
    
    def __init__(self, root):
        self._root = root
        self._datatools = tools.DatabaseTools()
        self._name_entry = None
        self._surname_entry = None
        self._email_entry = None
        self._password1_entry = None
        self._password2_entry = None
        self._birthdate_entry = None
        self._sex_lbl_entry = None
        self._height_lbl_entry = None
        self._frame = None
        
        self._register_screen()
        
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
           
    def _register_screen(self):
        
        self._frame = tk.Frame(master=self._root)
        name_lbl = tk.Label(self._frame,text="Firstname*")
        name_lbl.grid(row=1, column=0, sticky="nsew")

        self._name_entry = tk.StringVar()
        name_ent = tk.Entry(self._frame, textvariable=self._name_entry)
        name_ent.grid(row=1, column=1)
        
        surname_lbl = tk.Label(self._frame, text="Surname*")
        surname_lbl.grid(row=2, column=0, sticky="nsew")

        self._surname_entry = tk.StringVar()
        surname_ent = tk.Entry(self._frame, textvariable=self._surname_entry)
        surname_ent.grid(row=2, column=1)
        
        email_lbl = tk.Label(self._frame, text="Email")
        email_lbl.grid(row=3, column=0, sticky="nsew")

        self._email_entry = tk.StringVar()
        email_ent = tk.Entry(self._frame, textvariable=self._email_entry)
        email_ent.grid(row=3, column=1)
        
        password1_lbl = tk.Label(self._frame, text="Password")
        password1_lbl.grid(row=4, column=0, sticky="nsew")

        self._password1_entry = tk.StringVar()
        password1_ent = tk.Entry(self._frame, textvariable=self._password1_entry)
        password1_ent.grid(row=4, column=1)
        
        password2_lbl = tk.Label(self._frame,text="Password")
        password2_lbl.grid(row=5, column=0, sticky="nsew")

        self._password2_entry = tk.StringVar()
        password2_ent = tk.Entry(self._frame, textvariable=self._password2_entry)
        password2_ent.grid(row=5, column=1)
        
        date_of_birth_lbl = tk.Label(self._frame,text="DateOfBirth")
        date_of_birth_lbl.grid(row=6, column=0, sticky="nsew")

        self.date_of_birth_lbl_entry = tk.StringVar()
        date_of_birth_lbl_ent = tk.Entry(self._frame, textvariable=self.date_of_birth_lbl_entry)
        date_of_birth_lbl_ent.grid(row=6, column=1)
        
        #Tämä olisi hyvä muuttaa on/off valinnaksi.
        sex_lbl = tk.Label(self._frame,text=" Sex* (Male/Female)")
        sex_lbl.grid(row=7, column=0, sticky="nsew")

        self._sex_lbl_entry = tk.StringVar()
        sex_lbl_ent = tk.Entry(self._frame, textvariable=self._sex_lbl_entry)
        sex_lbl_ent.grid(row=7, column=1)
        
        #Pitäisi varmistaa myöhemmin, että kyseessä on string. Ehkä myös asettaa raja, jonka ylittäminen ei onnistu. Pienin/Suurin painoennätys.
        height_lbl = tk.Label(self._frame,text="Height (kg)")
        height_lbl.grid(row=8, column=0, sticky="nsew")

        self._height_lbl_entry = tk.StringVar()
        height_lbl_ent = tk.Entry(self._frame, textvariable=self._height_lbl_entry)
        height_lbl_ent.grid(row=8, column=1)
        
        
        register_btn = tk.Button(self._frame, text="Done", command=self._savedata)
        register_btn.grid(row=9, column=1)
        
    def _savedata(self):
        
        name = self._name_entry.get()
        surname = self._surname_entry.get()
        email = self._email_entry.get()
        password1 = self._password1_entry.get()
        #password2 = self._password2_entry.get()
        birthdate = self.date_of_birth_lbl_entry.get()
        sex = self._sex_lbl_entry.get()
        height = self._sex_lbl_entry.get()
       
        """regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
        
        if password1 != password2:
            passworderror_lbl = tk.Label(master=self._frame, text="Passwords don't match!")
            passworderror_lbl.grid(row=4, column=4)
        elif sex.lower() != "male" and sex.lower() != "female" and sex.lower() != "":
            sexError = tk.Label(master=self._frame, text="Sex is incorrect.")
            sexError.grid(row=7,column=4)
            
        if (re.fullmatch(regex, email)) == False:
            email_used_lbl = tk.Label(master=self._frame, text="Email is incorrect.")
            email_used_lbl.grid(row=3, column=4) 
        
        email_available = self._datatools.check_email_availableSTR(email)
        if email_available == None:
            email_used_lbl = tk.Label(master=self._frame, text="Email is already in our database.")
            email_used_lbl.grid(row=3, column=5)"""
            
        self._datatools.create_userSTR(name, surname, email, password1, birthdate, sex, height)