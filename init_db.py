import sqlite3

from src import app

db_name = app.config['DB_NAME']
connection = sqlite3.connect(db_name)

with open('schema.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()
