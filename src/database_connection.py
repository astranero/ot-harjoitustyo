import sqlite3
import os
CONN = None
try:
    directory_name = os.path.dirname(__file__)
    CONN = sqlite3.connect(os.path.join(
        directory_name, "database", "Softfit.db"))
    CONN.row_factory = sqlite3.Row
except sqlite3.Error as e:
    if CONN is not None:
        CONN.close()
    print("Error has occured:", e)


def return_connection():
    try:
        if CONN is not None:
            return CONN
            raise sqlite3.Error
    except sqlite3.Error:
        print("Database connection error occured!")
