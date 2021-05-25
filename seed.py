import sqlite3

connection = sqlite3.connect('flask_tut.db', check_same_thread= False)
cursor= connection.cursor()

cursor.execute(
    """INSERT INTO users(
    username,
    password
    )
    VALUES(
    'Ashka',
    'ashka2000'
    );"""
)

cursor.execute(
    """INSERT INTO users(
    username,
    password
    )
    VALUES(
    'Drashti',
    'drashti2001'
);"""
)
cursor.execute(
    """INSERT INTO todolist
    (tasks)
    VALUES
    ('call aashka');"""
)

connection.commit()
cursor.close()
connection.close()
