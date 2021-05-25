import sqlite3

def check_pw(username):
    connection= sqlite3.connect('flask_tut.db', check_same_thread= False)
    cursor=connection.cursor()
    cursor.execute(""" SELECT password FROM users WHERE username='{username}' ORDER BY pk DESC;""".format(username=username))
    password=cursor.fetchone()[0]

    connection.commit()
    connection.cursor()
    connection.close()
    return password

def check_user(username):
    connection= sqlite3.connect('flask_tut.db', check_same_thread= False)
    cursor=connection.cursor()
    cursor.execute(""" SELECT username FROM users ORDER BY pk DESC;""")
    db_users=cursor.fetchall()
    users=[]

    for i in range(len(db_users)):
        person=db_users[i][0]
        users.append(person)

    connection.commit()
    connection.cursor()
    connection.close()
    return users

def signup(username,password):
        connection= sqlite3.connect('flask_tut.db', check_same_thread= False)
        cursor=connection.cursor()
        cursor.execute(""" SELECT password FROM users WHERE username='{username}';""".format(username=username))
        exist=cursor.fetchone()

        if exist is None:
            cursor.execute(""" INSERT INTO users(username, password)VALUES('{username}', '{password}');""".format(username=username, password=password))
            connection.commit()
            connection.cursor()
            connection.close()

        else:
            return('You are already a member.')

        return'You are successfully signed in'

def speak():
    import speech_recognition as sr
    recognizer = sr.Recognizer()

    with sr.Microphone() as inputs:
        print("Please speak now")
        listening = recognizer.listen(inputs)

    try:
        str= recognizer.recognize_google(listening)
        return print(str)
    except:
        return("please speak again")


def insert(task):
    connection= sqlite3.connect('flask_tut.db', check_same_thread= False)
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO todolist(tasks) VALUES('{task}');""".format(task=task))
    return 'Task added!'

def show():
    connection= sqlite3.connect('flask_tut.db', check_same_thread= False)
    cursor=connection.cursor()
    cursor.execute("""SELECT tasks FROM todolist ORDER BY pk DESC;""")
    tasks=cursor.fetchall()
    list = []
    for i in range(len(tasks)):
        taskn=tasks[i][0]
        list.append(taskn)
    connection.commit()
    connection.cursor()
    connection.close()
    return list
