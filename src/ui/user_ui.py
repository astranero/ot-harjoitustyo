from tkinter import  Frame, StringVar, Toplevel, constants, Button, Label, Entry, Tk
from services.calculator_service import *
from tkinter.messagebox import askyesno, showinfo
from database.database_tools import DatabaseTools

class User:
    def __init__(self, root, email, password, login_view):
        self._root = root
        self._frame = None
        self._calculator = Calculator()
        self._DataTools = DatabaseTools()
        self._loginView = login_view
        self._email = email
        self._password = password
        self._passwordVar1 = None
        self._passwordVar2 = None
        self._UserScreenInit()
        
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
        
    def _userDelete(self):
        answer= self._popAskWin()
        if answer:
            try:
                self._DataTools._delete_userSTR(self._email, self._password) 
                self._loginView()
            except Exception as e:
                showinfo("Error", "Error:" + f"{e}")    
           
                
    def _popAskWin(self):
        return askyesno("Confirmation", "Are you sure that you want to continue?")
    
    def _calculateHandling(self):
        self._calButton = Button(self._frame, text="Calculate", command=lambda: print("pöö"))
        self._calButton.grid(row=10, column=1)
    
    def _trackHandling(self):
         self._weightButton = Button(self._frame, text="Track", command=lambda: print("pöö")) 
         self._updateWeight = Button(self._frame, text="Add weight", command=None)
         self._weightButton.grid(row=1, column=2)
    
    def _pictureHandling(self):
        self._picButton = Button(self._frame, text="Pictures", command=None)
        self._picButton.grid(row=1, column=3)   
    
    def _deleteHandling(self):
        self._deleteAccButton = Button(self._frame, text="Delete Account", command=self._userDelete)      
        self._deleteAccButton.grid(row=1, column=1)     
    
    def _passwordHandling(self):
        self._passwordButton = Button(self._frame, text="Change password", command=self._passwordChange)    
        self._passwordButton.grid(row=5, column=5)
    
    def _logOutHandling(self):
        self._logoutButton = Button(self._frame, text="LogOut", command=self._logOut)
        self._logoutButton.grid(row=1,column=5)

    def _logOut(self):
        self._loginView()
            
    def _UserScreenInit(self):
        
        self._frame = Frame(self._root)
        self._calculateHandling()
        self._deleteHandling()
        self._pictureHandling()
        self._passwordHandling()
        self._trackHandling()
        self._logOutHandling()
    
    def _passwordChange(self):
        self._passwordButton["state"] = "disabled"
        answer = self._popAskWin()
        
        if answer:
            self._win = Toplevel(self._frame)
            self._win.title("Password Change")
                
            self._password1_lbl = Label(self._win, text="Enter password: ").grid(row=1, column=1)
            self._passwordVar1 = StringVar(self._win)
            self._passwordEntry = Entry(self._win, textvariable=self._passwordVar1, show="*")
            self._passwordEntry.grid(row=1, column=2)
            
            self._password2_lbl = Label(self._win, text="Re-enter password: ").grid(row=2, column=1)
            self._passwordVar2 = StringVar(self._win)
            self._passwordEntry2 = Entry(self._win, textvariable=self._passwordVar2, show="*")
            self._passwordEntry2.grid(row=2, column=2)

            self._passDoneBtn = Button(self._win, text="Done", command=self._passwordFinalization).grid(row=3, column=1)

    def _passwordFinalization(self):
        self._password1 = self._passwordVar1.get()
        self._password2 = self._passwordVar2.get()
        print(f"a:{self._password1} , {self._password}")
        try:
            if self._password1 == self._password2:
                self._DataTools._update_passwordSTR(self._email, self._password,self._password2)
                showinfo("Done", "Password has been changed!")
                
        except Exception as e:
            showinfo(f"Error", {e})    
        self._win.destroy()    
        self._passwordButton["state"] = "active" 