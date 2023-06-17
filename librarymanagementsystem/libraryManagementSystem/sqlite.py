import sqlite3
from sqlite3 import Error

def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def doTask(conn):

    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS library_librarian")

def main():
    database = r"/home/aftab37/Documents/learnCode/github/webdev/librarymanagementsystem/db.sqlite3"

    # create a database connection
    conn = create_connection(database)
    with conn:
        doTask(conn)
        
if __name__ == '__main__':
    main()