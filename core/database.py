import sqlite3

conn = sqlite3.connect('users2.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NULL,
    first_name TEXT NULL
    
)
''')

conn.commit()

