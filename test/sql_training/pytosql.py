import sqlite3

"""
CREATING AND ACCESSING 
"""

# https://docs.python.org/3/library/sqlite3.html
# tutorial, create Monthy Python database 

# let's create a new database in format .db
# this is basicly a reference to the on-disk database
con = sqlite3.connect('tutorial.db')

# Let's create a abstract cursor to execute, fetch, etc our database
cur = con.cursor()

# we can execute then, a command to create a table with it's columns
cur.execute("CREATE TABLE movie (title, year, score)")

# right now the .db has been created and so on, anything we introduced will 
# be added to the database

# we can use fetch to get a copy of the tables that we have created so far
# this to confirm evertthing has worked accordingly
# sqlite_master references the biggest most outer table in our database
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())

# if we query for a non-existent table res.fetchone is None
# i.e.
# res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam' ")
# res.fetchone() --> None

cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And now something completely different', 1971, 7.5)
""")

# after insertion, we need to commit the changes
con.commit()
# or we can erase changes made with
# con.rollback()

# we can confirm that the data was correctly submitted using
res = cur.execute("SELECT score FROM movie")
print(res.fetchall()) # will print [(score1,), (score2,), ...]

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0)
    ]

cur.executemany("INSERT INTO movie VALUES (?, ?, ?)", data)
con.commit() # Remember to commit the transaction after executing INSERT.

# to access rows in the table movies we can simply use cur.execute as an iterable
for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row) # --> (year, title) is tuple type

# finally we end all of our changes using con.close()
con.close()

# and to access the database again, after all changes has been made and we consider it
# complete and/or usable
new_con = sqlite3.connect("tutorial.db")
new_cur = new_con.cursor()
# we want to access title and year, but from the better rated to the worst
# so the order the table in descendent order top to bottom
res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
title, year = res.fetchone() # we fetch the first one in our ordered database
# where the !r just preserves the quotes in the moment of printing
print(f"The highest scoring Monty Python movie is {title!r}, released in {year}")
# print(f"Hola {'Byron'}")   # Hola Byron
# print(f"Hola {'Byron'!r}") # Hola 'Byron'
