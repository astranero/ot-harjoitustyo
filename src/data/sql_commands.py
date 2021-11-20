create_userTable = """CREATE TABLE IF NOT EXISTS Users (
                    id INT PRIMARY KEY,
                    firstName TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    dateOfBirth date NOT NULL,
                    sex NOT NULL,
                    height REAL
                    
                    )"""

create_weightTable = """CREATE TABLE IF NOT EXISTS Weights (
    
                    id integer PRIMARY KEY,
                    user.id INT,
                    weight REAL,
                    time DATE
                    FOREING KEY (user.id) REFERENCES Users (id)
    
                    )"""
                    


create_postTable = """CREATE TABLE IF NOT EXISTS Posts (
                    id INT PRIMARY KEY,
                    user.id INT,
                    post TEXT,
                    time DATE,
                    FOREING KEY (user.id) REFERENCES Users (id)"""
                    
def deleteTable(table:str):
    return "DROP TABLE ?", (table)
                    
def delete_user(email, password):
    return "DELETE Users WHERE email=? AND password=?", (email, password)
                
def check_user(email, password):                
    return "SELECT email FROM Users WHERE email=? AND password=?", (email, password)

def check_email_available(email):
    return "SELECT email FROM Users Where email=?", (email)

def update_password(email, password, newPassword):
    return "UPDATE Users SET password=? WHERE email=? AND password=?", (newPassword, email, password)

def update_weight(email, weight):
    return "UPDATE Users SET weight=? WHERE email=?", (weight, email)

def update_height(email, height):
    return "UPDATE Users SET height=? WHERE email=?", (height, email)

def delete_user(email, password):
    return "DELETE FROM Users WHERE email=? AND password=?", (email, password)