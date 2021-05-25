import sqlite3

connection = sqlite3.connect('flask_tut.db', check_same_thread= False)
cursor= connection.cursor()

cursor.execute(
    """Create table todolist(
    pk INTEGER PRIMARY KEY Autoincrement,
    tasks VARCHAR(100),
    );"""
)
cursor.execute(
    """Create table users(
    pk INTEGER PRIMARY KEY Autoincrement,
    username VARCHAR(32),
    password VARCHAR(16)
    );"""
)
connection.commit()
cursor.close()
connection.close()
