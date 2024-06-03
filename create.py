import sqlite3

def create_db():
    conn = sqlite3.connect('coins.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            coins INTEGER DEFAULT 0,
            profit_per_tap INTEGER DEFAULT 1,
            energy INTEGER DEFAULT 1000
        )
    ''')

    cursor.execute('''
        INSERT INTO users (username, coins, profit_per_tap, energy) VALUES
        ('default_user', 0, 1, 1000)
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
