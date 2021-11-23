import database_connection as conn

class DatabaseTools:
    def __init__(self):
        self.cur = conn.return_connection().cursor()
        self.connection = conn.return_connection()
        
    def delete_userSTR(self, email, password):
        self.cur.execute("DELETE Users WHERE email=? AND password=?", (email, password))
        self.connection.commit()

    def delete_all(self):
       self.cur.execute("DELETE Users")
       self.cur.execute("DELETE Posts")
       self.cur.execute("DELETE Weights")
       self.connection.commit()
                  
    def check_userStr(self,email, password):                
        self.cur.execute("SELECT email FROM Users WHERE email=? AND password=?", (email, password))

    def check_email_availableSTR(self, email):
        return self.cur.execute("SELECT email FROM Users Where email=?",(email,)).fetchone()

    def update_passwordSTR(self, email, password, newPassword):
        self.cur.execute("UPDATE Users SET password=? WHERE email=? AND password=?", (newPassword, email, password))
        self.connection.commit()

    def update_weightSTR(self, email, weight):
        self.cur.execute("UPDATE Users SET weight=? WHERE email=?", (weight, email))
        self.connection.commit()
        
    def update_heighSTR(self, email, height):
        self.cur.execute("UPDATE Users SET height=? WHERE email=?", (height, email))
        self.connection.commit()
        
    def delete_userSTR(self, email, password):
        self.cur.execute("DELETE FROM Users WHERE email=? AND password=?", (email, password))
        self.connection.commit()
        
    def create_userSTR(self, firstName, surname, email, password, dateOfBirth, sex=None, height=None):
        self.cur.execute("INSERT INTO Users (firstName, surname, email, password, dateOfBirth, sex, height) VALUES (?, ?, ?, ?, ?, ?,?)", (firstName, surname, email, password, dateOfBirth, sex, height))
        self.connection.commit()
     
  