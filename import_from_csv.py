import sqlite3

# Create the db file and table
conn = sqlite3.connect('books.db')
cur = conn.cursor()

# Create a table: specify column names and data types
sql = """ CREATE TABLE Bookshelf (
            Title TEXT,
            Author TEXT,
            Genre TEXT,
            Height INTEGER,
            Publisher TEXT
            ) """

cur.execute(sql)

conn.commit()
conn.close()


