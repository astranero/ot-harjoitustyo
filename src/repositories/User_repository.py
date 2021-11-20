from database_connection import return_db_connection
con = return_db_connection
c = con.cursor()
def CreateTable():
    c.execute('''CREATE TABLE main.userData (

                    email UNIQUE TEXT,
                    password TEXT,
                    weight INT,
                    height INT,
                    
                    
                    
                    )''')