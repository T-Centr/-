import sqlite3
import numpy as np
import pandas as pd

conn = sqlite3.connect("sqlite/data.db3")
db = conn.cursor()
'''
db.execute("""CREATE TABLE films
                 (id INTEGER PRIMARY KEY AUTOINCREMENT not null,
                 url text,
                 title text default '',
                 budget INTEGER default 0,
                 sales_www INTEGER default 0)""")
conn.commit()

films = np.loadtxt("films.txt", dtype="str")
for film in films:
    db.execute("INSERT INTO films (url) VALUES (?)", (film,))
conn.commit()
'''
data = np.array(db.execute("SELECT * FROM films").fetchall())
data = pd.read_sql_query("SELECT * FROM films", conn)
print(data)
