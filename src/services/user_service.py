from tkinter.messagebox import askyesno, showinfo
from database.database_tools import DatabaseTools
import string
import re

class UserService:
    
    def __init__(self):
        self._datatools = DatabaseTools()
    
    def _errorWindow(self, message):
        showinfo("Error:", message)
        
    def _userDelete(self, email, password):
        self._email = email
        self._password = password
        answer = askyesno("Confirmation", "Are you sure that you want to continue?")
        if answer:
            try:
                self._datatools._delete_userSTR(self._email, self._password) 
                
            except Exception as e:
                showinfo("Error", "Error:" + f"{e}")   
                 
    def _changePassword(self, email, password1, password2):
        self._password1 = password1
        self._password2 = password2
        
        try:
            if self._password1 == self._password2:
                self._dataTools._update_passwordSTR(self._email, self._password,self._password2)
                showinfo("Done", "Password has been changed!")
        except Exception as e:
            showinfo(f"Error", {e}) 
    
    def _nameCheck(self, name):
        
        error = True
        letters = string.ascii_letters + " " 
        for i in name:
            if (i not in letters):
                error = False
        if name == None:
            error = False
        if error == False:
            self._errorWindow("Name fields should contain letters.")
        return error
        
    def _emailCheck(self, email):
        error = False
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (re.fullmatch(regex, email))!=None:
            try:
                email_available = self._datatools._check_email_availableSTR(email)
                if email_available != None:
                    self._errorWindow("Email is already in use!")
                error=True
            except Exception as e:
                self._errorWindow(f"Error: {e}")
        else:
            self._errorWindow("Incorrect Email Address.")
        return error
    
           
    def _passwordCheck(self,password1, password2):
        error=False
        if (password1 == password2 == ""):
            self._errorWindow("Password can't be null.")
            return error
        if password1 == password2 and not (password1 == password2 == ""):
            error=True
        else:
            self._errorWindow("Passwords don't match!")    
        return error
            
    
    def _checkHeightIsDigits(self, height):
        error=True
        new_height = height
        dig = string.digits + "."
        for i in height:
            if i not in (dig):
                error = False

        if error==False or new_height==None or new_height=="":   
            self._errorWindow("Please insert height as centimeters in digits and dots, please.")
            return False
        try:
            new_heigh = int(height)
            if new_heigh < 0 and new_heigh > 300:
                error = False
        except Exception as e:
            pass 
        
        try:    
            new_heigh = float(height)
            if new_heigh < 0.0 and new_heigh > 300.0: 
                error = False
        except Exception as e:
            pass 
        
        return error