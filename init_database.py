import sqlite3

database = sqlite3.connect("peers.db")
c = database.cursor()
c.execute("""
    CREATE TABLE peers (
        ip text,
        uuid text
    )""")

database.commit()
database.close()