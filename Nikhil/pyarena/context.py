"""
with is a context manager

1. Context manager is used to have functionality like try/finally
2. contextlib and function
3. Object oriented way by implementing __enter__ and __exit__ method in class
"""

from contextlib import contextmanager

class Connection:

    def close(self):
        print("closing Connection")

    def open(self):
        print("opening Connection")

    def execute(self, query):
        print(query)

@contextmanager
def db(hostname, username='root', password=None):
    # setup activitvities
    try:
        con = Connection()
        con.open()
        # end of setup activitvities
        yield con
    finally:
        # start of cleanup activitvities
        con.close()
        # end of cleanup activitvities

def db2(hostname, username='root', password=None):
    con = Connection()
    con.open()
    return con

# Normal
"""
con = None
try:
   con = db2('10.2.2.2', username='stc', password='stc')
   con.execute('select 2')
finally:
   if con:
       con.close()
"""

with db('10.2.2.2', username='stc', password='stc') as con:
    con.execute("select 1")
    #con.execute('selection')
####################################### \o/ ####################################################



class DB:

    def __init__(self, hostname, username=None, password=None):
        self.hostname = hostname
        self.username = username
        self.password = password
        self._con = Connection()

    def open(self):
        # self.con.open()
        self._con.open()

    def close(self):
        self._con.close()

    def __enter__(self):
        # Setup activitvities
        self.open()
        return self

    def __exit__(self, type, value, traceback):
        print(type)
        print(value)
        print(traceback)
        print("herererer")
        self.close()

    def me(self):
        raise Exception('')

    def execute(self, sql):
        raise Exception('test')

class Test:
    def test(self):
        raise Exception('Boom!')


print("#" * 80)
"""
db = DB(hostname='kuch bhi', username='koi bhi', password='')
db.open()
db.execute('selct 4')
db.close()
"""
print("#" * 80)

#db.__enter__()

with DB(hostname='kuch bhi', username='koi bhi', password='top secrete') as db:
    db.me()
    Test().test()
