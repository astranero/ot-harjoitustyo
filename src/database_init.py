import database_connection as connection
import data.sql_commands as command

con = connection.return_db_connection()
cur = con.cursor()

def database_init():
    cur.execute("DROP TABLE Users")
    cur.execute("DROP TABLE Weights")
    cur.execute("DROP TABLE Posts")
    
def createTables(con):
    
    cur.execute(command.createUserTableSTR())
    cur.execute(command.createWeightTableSTR())
    cur.execute(command.createPostTableSTR())
    con.commit()


if __name__ == "__main__":
    createTables()
    database_init()