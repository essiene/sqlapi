import sqlapi.connection
import MySQLdb as mysql

class Connection(sqlapi.connection.Connection):
    def __init__(self, username, password, host, database):
        sqlapi.connection.Connection.__init__(self, username, password, host, database)
        self.conn = mysql.connect(user=username, passwd=password, host=host)
        self.conn.select_db(database)
