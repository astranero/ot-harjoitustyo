
def createUserTableSTR():
    return """CREATE TABLE IF NOT EXISTS Users (
                    id INT PRIMARY KEY,
                    firstName TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    dateOfBirth date NOT NULL,
                    sex NOT NULL,
                    height REAL
                    
                    )"""

def createWeightTableSTR():
    return """CREATE TABLE IF NOT EXISTS Weights (
    
                    id integer PRIMARY KEY,
                    user.id INT,
                    weight REAL,
                    time DATE
                    FOREING KEY (user.id) REFERENCES Users (id)
    
                    )"""
                    


def createPostTableSTR():
    return """CREATE TABLE IF NOT EXISTS Posts (
                    id INT PRIMARY KEY,
                    user.id INT,
                    post TEXT,
                    time DATE,
                    FOREING KEY (user.id) REFERENCES Users (id)"""
     
