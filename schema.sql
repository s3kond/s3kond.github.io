-- schema.sql

-- Создание таблицы пользователей
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    coins INTEGER
);

-- Вставка начальных данных
INSERT INTO users (id, coins) VALUES (1, 0);
