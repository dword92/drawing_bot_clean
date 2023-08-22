import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY,
                   user_id INTEGER,
                   request_count INTEGER DEFAULT 0)''')
conn.commit()


def add_user_to_database(user_id: int):
    # Добавление пользователя в базу данных
    cursor.execute("INSERT OR REPLACE INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()


def increment_request_count(user_id: int):
    # Увеличение значения request_count для пользователя
    cursor.execute("UPDATE users SET request_count = request_count + 1 WHERE user_id = ?", (user_id,))
    conn.commit()


def get_request_count(user_id: int) -> int:
    # Получение значения request_count для пользователя
    cursor.execute("SELECT request_count FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return 0


def close_database_connection():
    conn.close()  # Закрываем соединение с базой данных
