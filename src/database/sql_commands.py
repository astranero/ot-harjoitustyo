def create_user_table():
    return """CREATE TABLE IF NOT EXISTS Users (
                    id INTEGER PRIMARY KEY,
                    firstName TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    dateOfBirth date NOT NULL,
                    sex NOT NULL,
                    height NOT NULL
                    )"""


def create_weight_table():
    return """CREATE TABLE IF NOT EXISTS Weights (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    weight REAL,
                    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES Users (id) 
                    )"""


def create_post_table():
    return """CREATE TABLE IF NOT EXISTS Posts (
                    id INTEGER PRIMARY KEY,
                    user_id INT,
                    post TEXT,
                    image DATA,
                    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES Users (id))"""
