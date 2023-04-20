# let's create a git database
import sqlite3
import os


class dbManager:
    # __enter__ and __close__ can be used as context managers
    def __enter__(self):
        self.con = sqlite3.connect('..\..\.leni\db\dbleni.db')
    
    def __close__(self):
        self.con.close()


def main():
    con = sqlite3.connect('..\..\.leni\db\dbleni.db') # check, done succesfully
    cur = con.cursor() # manipulation instance

    cur.execute("CREATE TABLE GitObject(sha TEXT, type TEXT, size INT, Content BLOB)")
    cur.execute("CREATE TABLE Tree(name TEXT, type TEXT)")
    cur.execute("CREATE TABLE Tag(name TEXT, type TEXT)")
    cur.execute("CREATE TABLE Commit(message TEXT, type TEXT)")
    cur.execute("CREATE TABLE Blob (name TEXT, mode INT, type BLOB)")
    
    

    con.close()


if __name__ == '__main__':
    main()