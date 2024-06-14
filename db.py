import sqlite3

def get_db_connection():
    connection = sqlite3.connect('game.db')
    return connection

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS player (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vehicle (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            player_id INTEGER,
            FOREIGN KEY (player_id) REFERENCES player(id)
        )
    ''')
    conn.commit()
    conn.close()
