import database_connection as conn

class DatabaseTools:
    def __init__(self):
        self.cur = conn.return_connection().cursor()
        self.connection = conn.return_connection()
                  
    def _check_Email(self,email, password):                
        return self.cur.execute("SELECT email FROM Users WHERE email=? AND password=?", (email, password)).fetchone()
    
    def _check_Password(self, email, password):
        return self.cur.execute("SELECT password FROM Users WHERE email=? AND password=?", (email, password)).fetchone()
    
    def _check_email_availableSTR(self, email):
        return self.cur.execute("SELECT email FROM Users Where email=?",(email,)).fetchone()

    def _update_passwordSTR(self, email, password, newPassword):
        self.cur.execute("UPDATE Users SET password=? WHERE email=? AND password=?", (newPassword, email, password))
        self.connection.commit()
        
    def _update_heighSTR(self, email, height):
        self.cur.execute("UPDATE Users SET height=? WHERE email=?", (height, email))
        self.connection.commit()
        
    def _delete_userSTR(self, email, password):
        self.cur.execute("DELETE FROM Users WHERE email=? AND password=?", (email, password))
        self.connection.commit()
        
    def _create_userSTR(self, firstName, surname, email, password, dateOfBirth, sex=None, height=None):
        self.cur.execute("INSERT INTO Users (firstName, surname, email, password, dateOfBirth, sex, height) VALUES (?, ?, ?, ?, ?, ?,?)", (firstName, surname, email, password, dateOfBirth, sex, height))
        self.connection.commit()
     
  