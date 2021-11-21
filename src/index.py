import database_init as dbase
import database_connection as connection

con = connection.conn

dbase.createTables(con)
dbase.database_init()
