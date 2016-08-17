import sqlite3, os

db_file = os.path.join(os.path.abspath('.'), 'torrent.db')

def init():
    if os.path.exists(db_file):
        return

    conn = sqlite3.connect(db_file)
    cursor=conn.cursor()
    cursor.execute(
        r'CREATE TABLE torrent(title VARCHAR(255),link VARCHAR(255),section VARCHAR(255),enclosure VARCHAR(255))')
    cursor.close()
    conn.commit()
    conn.close()

    print('init successful, db file at', db_file)

def insert(title, link, section, enclosure):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(
        r'INSERT INTO torrent VALUES (?,?,?,?)', (title, link, section, enclosure))
    row = cursor.rowcount
    cursor.close()
    conn.commit()
    conn.close()

    return row

def has(title):
    if title=='' or title is None:
        return False

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(r'SELECT rowid FROM torrent WHERE title=?', (title,))
    value = cursor.fetchall()
    cursor.close()
    conn.close()

    if len(value)>0:
        return True
    else:
        return False

def getID(title):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(r'SELECT rowid FROM torrent WHERE title=?', (title,))
    value = cursor.fetchall()
    cursor.close()
    conn.close()

    if len(value)>0:
        return value[0][0]
    else:
        return False
