#TODO: use pyprotocols for making this an interface.
class Connection(object):
    def __init__(self, username, password, host, database):
         self.username = username
         self.password = password
         self.host = host
         self.database = database

