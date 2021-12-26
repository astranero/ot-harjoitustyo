import sqlite3
import os
CONN = None


def return_connection(database_name):
    try:
        directory_name = os.path.dirname(__file__)
        CONN = sqlite3.connect(os.path.join(
            directory_name, "database", database_name))
        CONN.row_factory = sqlite3.Row
    except sqlite3.Error as e:
        if CONN is not None:
            CONN.close()
        print("Error has occured:", e)
    try:
        if CONN is not None:
            return CONN
        return None
    except sqlite3.Error as error:
        return error


def return_file_path(file_name):
    directory_name = os.path.dirname(__file__)
    try:
        csv_file = os.path.join(directory_name, "database", file_name)
    except FileNotFoundError:
        pass
    return csv_file
