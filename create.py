import sqlite3

conn = sqlite3.connect('coins.db')
cursor = conn.cursor()

# Создаем таблицу пользователей
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        coins INTEGER DEFAULT 0
    )
''')

# Вставляем дефолтного пользователя для тестирования
cursor.execute('''
    INSERT OR IGNORE INTO users (username, coins) VALUES ('default_user', 0)
''')

conn.commit()
conn.close()
