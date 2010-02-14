from sqlapi.exceptions import *
import sqlapi.util as s_util
import sys

__all__ = ['Result', 'Table', 'connect', 'nocolumns', 'columns', 'singlerow']

_DEBUG = False

class Result(object):
    pass

class Table(object):
    def __init__(self, sqlapi_conn=None, dbapi_conn=None):
        if sqlapi_conn:
            self.conn = sqlapi_conn.conn
        elif dbapi_conn:
            self.conn = conn

        self.cur = self.conn.cursor()
        self.sqlapi_connection = sqlapi_conn
        self.dbapi_connection = dbapi_conn
    

def setdebug(debug=True):
    global _DEBUG
    _DEBUG=debug

def connect(dburl, pool=False):
    module, username, password, host, database = s_util.get_connection_properties(dburl)

    Connection = None

    if pool:
        from sqlapi.db.pool import Connection
        return Connection(username, password, host, database, module)
    else:
        if module == 'mysql':
            from sqlapi.db.mysql import Connection
            return Connection(username, password, host, database)
        elif module == 'sqlite':
            from sqlapi.db.sqlite import Connection
            return Connection(database)


def query(resulttype='columns'):
    def wrapper(func):
        def inner(*args, **kw):
            kw['resulttype'] = resulttype
            kw['func'] = func
            return _process(*args, **kw)

        inner.__name__ == func.__name__
        inner.__dict__ == func.__dict__
        inner.__doc__ == func.__doc__ 
        
        return inner

    return wrapper

singlerow = query('singlerow')
columns = query('columns')
nocolumns = query('nocolumns')

def _itercolumns(cur):
    desc = cur.description
    for row in cur.fetchall():
        r = Result()
        for i in xrange(0, len(row)):
            setattr(r, desc[i][0], row[i])

        yield r

def _process(*args, **kw):
    resulttype = kw['resulttype']
    del kw['resulttype']

    func = kw['func']
    del kw['func']

    self = args[0]
    params = args[1:] #jump over 'self'

    query_str = func.__doc__ % params


    if _DEBUG: print >>sys.stderr, query_str

    if resulttype == 'columns':
        self.cur.execute(query_str)
        return _itercolumns(self.cur)
    elif resulttype == 'nocolumns':
        return self.cur.execute(query_str)
    elif resulttype == 'singlerow':
        self.cur.execute(query_str)
        gen = _itercolumns(self.cur)
        try:
            return gen.next()
        except StopIteration:
            raise SqlApiException('Query has no result')
