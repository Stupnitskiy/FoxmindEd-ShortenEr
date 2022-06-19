import sqlite3

from src import app


def get_db_connection():
    db_name = app.config['DB_NAME']
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row

    return conn
