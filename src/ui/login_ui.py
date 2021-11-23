import tkinter as tk
from tkinter import constants


class LoginScreen:
    
    def __init__(self, root, show_register_view):
        self._root = root
        self._error_var = None
        self._error_lbl = None
        self._email_entry = None
        self._password_entry = None
        self._show_register_view = show_register_view
        self._frame = None
        
        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
        
    def _user_handling(self):
        pass
    def _initialize(self):
        
        self._frame = tk.Frame(master=self._root)
        self._error_var = tk.StringVar(master=self._frame)
        self._error_lbl = tk.Label(master=self._frame, textvariable=self._error_var, fg="#fcc002", bg="#afeeee")
        self._error_lbl.grid(padx=5, pady=5)
    
        heading_lbl = tk.Label(self._frame,text="Login Screen")
        heading_lbl.grid(row=1, column=1, sticky="nsew")

        email_lbl = tk.Label(self._frame,text="Email")
        email_lbl.grid(row=2, column=0, sticky="nsew")

        self._email_entry = tk.StringVar(self._frame)
        email_ent = tk.Entry(self._frame, textvariable=self._email_entry)
        email_ent.grid(row=2, column=1)

        password_lbl = tk.Label(self._frame, text="Password")
        password_lbl.grid(row=3, column=0, sticky="nsew")

        self._password_entry = tk.StringVar(self._frame)
        password_ent = tk.Entry(self._frame, textvariable=self._password_entry)
        password_ent.grid(row=3, column=1, sticky="nsew")
    
        btn_login = tk.Button(
            self._frame, 
            text="Login", 
            command=self._login_start)
        
        btn_login.grid(row=4, column=0, sticky="nsew")

        btn_register = tk.Button (
            master=self._frame, 
            text="Create User", 
            command=self._show_register_view)
        
        btn_register.grid(row=4, column=1, sticky="nsew")

        
    def _login_start(self):
        pass