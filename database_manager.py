#database_manager.py

import logging
import sqlite3
import aiosqlite


def init_db():
    conn = sqlite3.connect('tests_db.sqlite')
    cursor = conn.cursor()

    # Создание таблицы тестов
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT NOT NULL
    )''')

    # Создание таблицы вопросов
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        test_id INTEGER NOT NULL,
        question TEXT NOT NULL,
        image_url TEXT,
        option_1 TEXT NOT NULL,
        option_2 TEXT NOT NULL,
        option_3 TEXT NOT NULL,
        option_4 TEXT NOT NULL,
        correct_option INTEGER NOT NULL,
        FOREIGN KEY (test_id) REFERENCES tests(id)
    )''')

    # Создание таблицы пользователей
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE NOT NULL,
        balance INTEGER DEFAULT 0,
        referred_by INTEGER,
        FOREIGN KEY (referred_by) REFERENCES users(id)
    )''')

    # Создание таблицы транзакций
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        amount INTEGER NOT NULL,
        type TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )''')

    # Новая таблица для результатов тестов
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS test_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        test_id INTEGER NOT NULL,
        completion_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        score_percentage INTEGER NOT NULL,
        correct_answers TEXT,
        incorrect_answers TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (test_id) REFERENCES tests(id)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS question_user_status (
        user_id INTEGER NOT NULL,
        question_id INTEGER NOT NULL,
        is_correct BOOLEAN NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (question_id) REFERENCES questions(id),
        PRIMARY KEY (user_id, question_id)
    )''')

    conn.commit()
    conn.close()

# Добавление нового теста и возврат его ID
def connect_db():
    return sqlite3.connect("tests_db.sqlite")

async def add_test(name, department):
    async with aiosqlite.connect('tests_db.sqlite') as db:
        cursor = await db.execute("INSERT INTO tests (name, department) VALUES (?, ?)", (name, department))
        await db.commit()
        return cursor.lastrowid


async def add_question(test_id, question, image_url, options, correct_option):
    async with aiosqlite.connect('tests_db.sqlite') as db:
        await db.execute("""INSERT INTO questions (test_id, question, image_url, option_1, option_2, option_3, option_4, correct_option) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                         (test_id, question, image_url, options[0], options[1], options[2], options[3], correct_option))
        await db.commit()


async def get_questions_for_test(test_id):
    async with aiosqlite.connect('tests_db.sqlite') as db:
        async with db.execute("""
            SELECT id, question, image_url, option_1, option_2, option_3, option_4, correct_option 
            FROM questions 
            WHERE test_id=? 
            ORDER BY RANDOM() 
            LIMIT 5
        """, (test_id,)) as cursor:
            questions = await cursor.fetchall()
    return questions




async def get_tests_by_department(department):
    async with aiosqlite.connect('tests_db.sqlite') as db:
        async with db.execute("SELECT id, name FROM tests WHERE department = ?", (department,)) as cursor:
            tests = await cursor.fetchall()
    return tests


def register_new_user(telegram_id, referrer_telegram_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    # Проверка, существует ли уже пользователь с таким telegram_id
    cursor.execute("SELECT id FROM users WHERE telegram_id = ?", (telegram_id,))
    user = cursor.fetchone()

    if user is None:
        # Регистрация нового пользователя
        if referrer_telegram_id:
            # Поиск referrer_id по его telegram_id
            cursor.execute("SELECT id FROM users WHERE telegram_id = ?", (referrer_telegram_id,))
            referrer = cursor.fetchone()
            referrer_id = referrer[0] if referrer else None
        else:
            referrer_id = None

        cursor.execute("INSERT INTO users (telegram_id, referred_by, balance) VALUES (?, ?, 200)", (telegram_id, referrer_id))
        conn.commit()

        # Если referrer_id найден, обновляем его баланс
        if referrer_id:
            cursor.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (100, referrer_id))  # Например, начисляем 100 единиц валюты
            conn.commit()

    conn.close()


async def get_user_balance(user_telegram_id):
    async with aiosqlite.connect('tests_db.sqlite') as db:
        async with db.execute("SELECT balance FROM users WHERE telegram_id = ?", (user_telegram_id,)) as cursor:
            row = await cursor.fetchone()
            if row:
                return row[0]
            return 0


async def update_user_balance(user_telegram_id, amount):
    async with aiosqlite.connect('tests_db.sqlite') as db:
        # Сначала получаем текущий баланс пользователя
        async with db.execute("SELECT balance FROM users WHERE telegram_id = ?", (user_telegram_id,)) as cursor:
            row = await cursor.fetchone()
            if row:
                new_balance = row[0] + amount
                # Обновляем баланс пользователя
                await db.execute("UPDATE users SET balance = ? WHERE telegram_id = ?", (new_balance, user_telegram_id))
                await db.commit()


async def get_all_user_ids():
    user_ids = []
    async with aiosqlite.connect('tests_db.sqlite') as db:
        async with db.execute("SELECT telegram_id FROM users") as cursor:
            async for row in cursor:
                user_ids.append(row[0])
    return user_ids


async def add_test_result(user_id, test_id, score_percentage, correct_answers, incorrect_answers):
    async with aiosqlite.connect('tests_db.sqlite') as db:
        await db.execute("""INSERT INTO test_results (user_id, test_id, score_percentage, correct_answers, incorrect_answers) 
                            VALUES (?, ?, ?, ?, ?)""",
                         (user_id, test_id, score_percentage, ",".join(map(str, correct_answers)), ",".join(map(str, incorrect_answers))))
        await db.commit()


async def get_user_test_statistics(user_id):
    async with aiosqlite.connect('tests_db.sqlite') as db:
        async with db.execute("SELECT test_id, completion_date, score_percentage, correct_answers, incorrect_answers FROM test_results WHERE user_id = ?",
                              (user_id,)) as cursor:
            test_results = await cursor.fetchall()
    return test_results

async def get_incorrect_questions_for_user(user_id):
    async with aiosqlite.connect('tests_db.sqlite') as db:
        # Предполагается, что incorrect_answers хранит ID вопросов через запятую
        async with db.execute("""
            SELECT incorrect_answers FROM test_results
            WHERE user_id = ? AND incorrect_answers IS NOT NULL
        """, (user_id,)) as cursor:
            rows = await cursor.fetchall()
            # Объединяем все неправильные ответы в один список, избегая дубликатов
            incorrect_questions = set()
            for row in rows:
                incorrect_questions.update(row[0].split(','))
    return list(incorrect_questions)


async def fetch_questions_by_ids(question_ids):
    question_ids_str = ','.join(str(id) for id in question_ids)
    async with aiosqlite.connect('tests_db.sqlite') as db:
        query = f"SELECT id, question, image_url, option_1, option_2, option_3, option_4, correct_option FROM questions WHERE id IN ({question_ids_str})"
        async with db.execute(query) as cursor:
            questions = await cursor.fetchall()
    print(questions)  # Для отладки
    return questions


async def update_correct_answers(user_id, correct_answers_ids):
    async with aiosqlite.connect('tests_db.sqlite') as db:
        for question_id in correct_answers_ids:
            # Проверка, существует ли запись
            async with db.execute("SELECT * FROM question_user_status WHERE user_id=? AND question_id=?", (user_id, question_id)) as cursor:
                if await cursor.fetchone() is None:
                    # Если запись не существует, создаем ее
                    await db.execute("INSERT INTO question_user_status (user_id, question_id, is_correct) VALUES (?, ?, ?)", (user_id, question_id, True))
                else:
                    # Если запись существует, обновляем ее
                    await db.execute("UPDATE question_user_status SET is_correct = ? WHERE user_id = ? AND question_id = ?", (True, user_id, question_id))
        await db.commit()


async def get_incorrect_questions_for_retry(user_id):
    incorrect_questions = []
    async with aiosqlite.connect('tests_db.sqlite') as db:
        async with db.execute(
            "SELECT question_id FROM question_user_status WHERE user_id=? AND is_correct=False",
            (user_id,)
        ) as cursor:
            async for row in cursor:
                incorrect_questions.append(row[0])
    return incorrect_questions


async def get_incorrect_questions_for_combined_approach(user_id):
    incorrect_questions = set()
    correct_questions = set()

    async with aiosqlite.connect('tests_db.sqlite') as db:
        # Получаем неправильные вопросы из test_results
        async with db.execute("SELECT incorrect_answers FROM test_results WHERE user_id=?", (user_id,)) as cursor:
            rows = await cursor.fetchall()
            for row in rows:
                incorrect_questions.update(set(row[0].split(',')))

    async with aiosqlite.connect('tests_db.sqlite') as db:
        # Исключаем вопросы, на которые уже дан правильный ответ
        async with db.execute("SELECT question_id FROM question_user_status WHERE user_id=? AND is_correct=True", (user_id,)) as cursor:
            rows = await cursor.fetchall()
            for row in rows:
                correct_questions.add(str(row[0]))  # Убедитесь, что question_id приведены к строке, если необходимо

    # Возвращаем разницу между ними
    return list(incorrect_questions - correct_questions)


async def get_subscribers_count():
    async with aiosqlite.connect('tests_db.sqlite') as db:
        async with db.execute("SELECT COUNT(*) FROM users") as cursor:
            row = await cursor.fetchone()
            if row:
                return row[0]
            return 0


if __name__ == '__main__':
    init_db()
    print("База данных инициализирована.")
