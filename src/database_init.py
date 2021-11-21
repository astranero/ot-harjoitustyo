import database_connection as connection
import database.sql_commands as command

con = connection.return_connection()
def database_DropIt(con):
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Users")
    cur.execute("DROP TABLE IF EXISTS Weights")
    cur.execute("DROP TABLE IF EXISTS Posts")
    con.commit()
    
def database_createTables(con):
    cur = con.cursor()
    cur.execute(command.createUserTableSTR())
    cur.execute(command.createWeightTableSTR())
    cur.execute(command.createPostTableSTR())
    con.commit()


def database_init():
    database_DropIt(con)
    database_createTables(con)