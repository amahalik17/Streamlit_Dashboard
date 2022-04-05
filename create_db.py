import sqlite3
from config import db_path


connection = sqlite3.connect(db_path)

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock (
        id INTEGER PRIMARY KEY, 
        symbol VARCHAR(50) NOT NULL UNIQUE, 
        name VARCHAR(500) NOT NULL,
        exchange VARCHAR(50) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_price (
        id INTEGER PRIMARY KEY, 
        stock_id INTEGER,
        date TEXT NOT NULL,
        open TEXT NOT NULL, 
        high TEXT NOT NULL, 
        low TEXT NOT NULL, 
        close TEXT NOT NULL, 
        volume TEXT NOT NULL,
        FOREIGN KEY (stock_id) REFERENCES stock (id)
    )
""")

connection.commit()