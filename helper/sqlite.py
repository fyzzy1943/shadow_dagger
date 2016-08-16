import sqlite3, os

db_file = os.path.join(os.path.abspath('.'), 'torrent.db')

def test():
    conn = sqlite3.connect('torrent.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM hdsky')

    values = cursor.fetchall()

    print(values)
    cursor.close()
    conn.close()

def init():
    if os.path.exists(db_file):
        return

    conn = sqlite3.connect(db_file)
    cursor=conn.cursor()
    cursor.execute(
        r'CREATE TABLE sky(id INT PRIMARY KEY,title VARCHAR(255),link VARCHAR(255),author VARCHAR(255),category VARCHAR(255),enclosure VARCHAR(255),date VARCHAR(255))')
    cursor.close()
    conn.commit()
    conn.close()

    print('init successful, db file at', db_file)

def insert():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(
        r'CREATE TABLE sky(id INT PRIMARY KEY,title VARCHAR(255),link VARCHAR(255),author VARCHAR(255),category VARCHAR(255),enclosure VARCHAR(255),date VARCHAR(255))')
    cursor.close()
    conn.commit()
    conn.close()
