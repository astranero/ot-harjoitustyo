import sqlite3
import os

conn = None
try:    
    directory_name = os.path.dirname(__file__)    
    conn = sqlite3.connect(os.path.join(directory_name,"database", "Softfit.db"))    
    conn.row_factory = sqlite3.Row    

except sqlite3.Error as e:    
    if conn!=None:    
        conn.close()    
    print("Error has occured:", e)      

def return_connection():
    try:
        if conn!=None:
            return conn
        else:
            raise Exception("There's no connection")
    except:
        print("Database connection error occured!")    
        raise

    
    
    
    
    

