import sqlite3

def get_db_connection():
    conn = sqlite3.connect('instance/site.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with conn:
        conn.executescript('''
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS blog (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                date_posted TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES user (id)
            );
        ''')
    conn.close()