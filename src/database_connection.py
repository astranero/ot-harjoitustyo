import sqlite3
import os

conn = None
try:
    
    directory_name = os.path.dirname(__file__)
    con = sqlite3.connect(os.path.join(directory_name,"data", "database.sqlite"))
    con.row_factory = sqlite3.Row
    
  
except sqlite3.Error as e:
    print("Error has occured:", e)
finally:
    if conn:
        conn.close()
        
def return_db_connection():
    return con