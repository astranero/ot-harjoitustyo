create_userTableSTR = """CREATE TABLE IF NOT EXISTS Users (
                    id INT PRIMARY KEY,
                    firstName TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    dateOfBirth date NOT NULL,
                    sex NOT NULL,
                    height REAL
                    
                    )"""

create_weightTableSTR = """CREATE TABLE IF NOT EXISTS Weights (
    
                    id integer PRIMARY KEY,
                    user.id INT,
                    weight REAL,
                    time DATE
                    FOREING KEY (user.id) REFERENCES Users (id)
    
                    )"""
                    


create_postTableSTR = """CREATE TABLE IF NOT EXISTS Posts (
                    id INT PRIMARY KEY,
                    user.id INT,
                    post TEXT,
                    time DATE,
                    FOREING KEY (user.id) REFERENCES Users (id)"""
                    
def deleteTableSTR(table:str):
    return "DROP TABLE ?", (table)
                    
def delete_userSTR(email, password):
    return "DELETE Users WHERE email=? AND password=?", (email, password)
                
def check_userSTR(email, password):                
    return "SELECT email FROM Users WHERE email=? AND password=?", (email, password)

def check_email_availableSTR(email):
    return "SELECT email FROM Users Where email=?", (email)

def update_passwordSTR(email, password, newPassword):
    return "UPDATE Users SET password=? WHERE email=? AND password=?", (newPassword, email, password)

def update_weightSTR(email, weight):
    return "UPDATE Users SET weight=? WHERE email=?", (weight, email)

def update_heighSTR(email, height):
    return "UPDATE Users SET height=? WHERE email=?", (height, email)

def delete_userSTR(email, password):
    return "DELETE FROM Users WHERE email=? AND password=?", (email, password)

def create_userSTR(firstName, surname, email, password, dateOfBirth, sex, height):
    return "INSERT INTO Users (firstName, surname, email, password, dateOfBirth, sex, height) VALUES (?, ?, ?, ?, ?, ?)", (firstName, surname, email, password, dateOfBirth, sex, height)
