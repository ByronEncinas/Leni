# f(U)isylK!uARt1eIamZ
# let's create a git database
import sqlite3
import os

# __enter__ and __close__ can be used as context managers
class dbManager:

    def __enter__(self):
        # creates/access
        self.con = sqlite3.connect('..\..\.leni\db\dbleni.db')
    
    def __close__(self):
        self.con.close()

def create_database():
    # con = sqlite3.connect('..\..\.leni\db\dbleni.db') # check, done succesfully
    con = sqlite3.connect('.\dbleni.db') # check, done succesfully
    cur = con.cursor() # manipulation instance

    cur.execute("DROP TABLE IF EXISTS 'Tree'")
    cur.execute("DROP TABLE IF EXISTS 'Tag'")
    cur.execute("DROP TABLE IF EXISTS 'Commit'")
    cur.execute("DROP TABLE IF EXISTS 'Blob'")

    cur.execute("CREATE TABLE 'GitObject'(sha TEXT, type TEXT, size INT, Content BLOB)")
    cur.execute("CREATE TABLE 'Tree'(name TEXT, type TEXT)")
    cur.execute("CREATE TABLE 'Tag'(name TEXT, type TEXT)")
    cur.execute("CREATE TABLE 'Commit'(message TEXT, type TEXT)")
    cur.execute("CREATE TABLE 'Blob' (name TEXT, mode INT, type BLOB);")
    
    con.close()

def enter_values():
    pass
def access_values():
    pass


if __name__ == '__main__':
    create_database()