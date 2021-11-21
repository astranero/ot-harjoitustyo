import database_connection as connection


con = connection.return_db_connection()
cur = con.cursor()
                   
def delete_userSTR(email, password):
    cur.execute("DELETE Users WHERE email=? AND password=?", (email, password))

def delete_all_usersSTR():
    cur.execute("DELETE Users")

def delete_all_weightsSTR():
    cur.execute("DELETE Weights")

def delete_all_postsSTR():
    cur.execute("DELETE Posts")
                
def check_userSTR(email, password):                
    cur.execute("SELECT email FROM Users WHERE email=? AND password=?", (email, password))

def check_email_availableSTR(email):
    cur.execute("SELECT email FROM Users Where email=?", (email))

def update_passwordSTR(email, password, newPassword):
    cur.execute("UPDATE Users SET password=? WHERE email=? AND password=?", (newPassword, email, password))

def update_weightSTR(email, weight):
    cur.execute("UPDATE Users SET weight=? WHERE email=?", (weight, email))

def update_heighSTR(email, height):
    cur.execute("UPDATE Users SET height=? WHERE email=?", (height, email))

def delete_userSTR(email, password):
    cur.execute("DELETE FROM Users WHERE email=? AND password=?", (email, password))

def create_userSTR(firstName, surname, email, password, dateOfBirth, sex, height):
    cur.execute("INSERT INTO Users (firstName, surname, email, password, dateOfBirth, sex, height) VALUES (?, ?, ?, ?, ?, ?)", (firstName, surname, email, password, dateOfBirth, sex, height))
    
  