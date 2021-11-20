import database_connection as connection
import data.sql_commands as command


con = connection.return_db_connection()
def database_init():
    
    cur = con.cursor()
    print(command.deleteTableSTR("Users"))
    cur.execute(command.deleteTableSTR("Users"))
    cur.execute(command.deleteTableSTR("Posts"))
    cur.execute(command.deleteTableSTR("Weights"))
    
    
def createTables(con):
    cur = con.cursor()
    cur.execute(command.createUserTableSTR)
    cur.execute(command.createWeightTableSTR)
    cur.execute(command.createPostTableSTR)
    con.commit()

if __name__ == "__main__":
    database_init()