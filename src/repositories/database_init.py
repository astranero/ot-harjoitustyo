import database_connection as connection
import database.sql_commands as command

con = connection.return_connection()

def database_drop_it(con):
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Users")
    cur.execute("DROP TABLE IF EXISTS Weights")
    cur.execute("DROP TABLE IF EXISTS Posts")
    con.commit()


def database_create_tables(con):
    cur = con.cursor()
    cur.execute(command.create_user_table())
    cur.execute(command.create_weight_table())
    cur.execute(command.create_post_table())
    con.commit()


def database_init():
    database_drop_it(con)
    database_create_tables(con)
