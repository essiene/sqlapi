import sqlapi.connection
import sqlite3 as sqlite


class Connection(sqlapi.connection.Connection):
    def __init__(self, database):
        print "database = '%s'" % (database)
        sqlapi.connection.Connection.__init__(self, username=None, password=None, host=None, database=database)
        self.conn = sqlite.connect(database)

