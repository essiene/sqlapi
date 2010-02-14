import sqlapi.connection
from sqlapi.extlib import antipool

class Connection(sqlapi.connection.Connection):
    def __init__(self, username, password, host, database, module):
        sqlapi.connection.Connection.__init__(self, username, password, host, database)
        self.module = module

        # TODO: Catch import errors and report on 
        # non support
        if self.module == 'mysql':
            import MySQLdb
            dbpool = antipool.ConnectionPool(MySQLdb, user=self.username, passwd=self.password, host=self.host, db=self.database)
        elif module_name == 'sqlite':
            import pysqlite2.dbapi2
            dbpool = antipool.ConnectionPool(pysqlite2.dbapi2, database=self.database)

        antipool.initpool(dbpool)
        

    def __get_conn(self):
        return antipool.dbpool().connection()

    conn = property(__get_conn, None, None, "A connection Object")

    
