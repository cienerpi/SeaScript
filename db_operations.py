import asyncpg
import logging
import random
from sshtunnel import SSHTunnelForwarder
import paramiko

# Настройка базового конфига логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

SSH_HOST = '128.199.4.131'
SSH_PORT = 22
SSH_USER = 'root'
SSH_KEY_PATH = 'C:\\Users\\ciene\\.ssh\\id_rsa'
SSH_KEY_PASSWORD = '123456789'  # Замените на ваш пароль для SSH-ключа

DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'maindb'
DB_USER = 'bot'
DB_PASSWORD = '123456789'


async def create_pool():
    try:
        mykey = paramiko.RSAKey.from_private_key_file(SSH_KEY_PATH, password=SSH_KEY_PASSWORD)

        tunnel = SSHTunnelForwarder(
            (SSH_HOST, SSH_PORT),
            ssh_username=SSH_USER,
            ssh_pkey=mykey,
            remote_bind_address=(DB_HOST, DB_PORT)
        )
        tunnel.start()

        local_bind_host = '127.0.0.1'  # Изменение с '0.0.0.0' на '127.0.0.1'
        local_bind_port = tunnel.local_bind_port
        print(f"SSH tunnel established: {local_bind_host}:{local_bind_port}")

        connection_string = f'postgresql://{DB_USER}:{DB_PASSWORD}@{local_bind_host}:{local_bind_port}/{DB_NAME}'
        print(f"Connection string: {connection_string}")

        pool = await asyncpg.create_pool(dsn=connection_string)
        return tunnel, pool
    except Exception as e:
        print(f"Ошибка создания пула подключений: {e}")
        return None, None


async def add_test(name, department, pool):
    async with pool.acquire() as conn:
        test_id = await conn.fetchval(
            'INSERT INTO tests (name, department) VALUES ($1, $2) RETURNING id',
            name, department
        )
    return test_id

async def add_question(test_id, question, image_url, options, correct_option, pool):
    async with pool.acquire() as conn:
        await conn.execute(
            '''
            INSERT INTO questions (test_id, question, image_url, option_1, option_2, option_3, option_4, correct_option)
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
            ''',
            test_id, question, image_url, options[0], options[1], options[2], options[3], correct_option
        )

async def get_questions_for_test(test_id, pool):
    async with pool.acquire() as conn:
        questions = await conn.fetch(
            """
            SELECT id, question, image_url, option_1, option_2, option_3, option_4, correct_option
            FROM questions
            WHERE test_id = $1
            ORDER BY RANDOM()
            LIMIT 5
            """,
            test_id
        )
    return questions

async def get_tests_by_department(department, pool):
    async with pool.acquire() as conn:
        tests = await conn.fetch(
            "SELECT id, name FROM tests WHERE department = $1",
            department
        )
    return tests

async def get_all_tests(pool):
    async with pool.acquire() as conn:
        tests = await conn.fetch("SELECT id, name FROM tests")
    return tests


async def register_new_user(user_id, pool, referrer_user_id=None):
    try:
        async with pool.acquire() as conn:
            # Check if the user already exists
            exists = await conn.fetchval("SELECT 1 FROM users WHERE user_id = $1", user_id)
            if exists:
                return user_id

            referrer_id = None
            if referrer_user_id:
                # Fetch the referrer's ID from the database
                referrer_id = await conn.fetchval("SELECT user_id FROM users WHERE user_id = $1", referrer_user_id)

            # Insert the new user and return the new user_id
            new_user_id = await conn.fetchval(
                "INSERT INTO users (user_id, referred_by, balance, level_id) VALUES ($1, $2, 20, 1) RETURNING user_id",
                user_id, referrer_id
            )

            if referrer_id:
                # Update referrer's balance
                await conn.execute("UPDATE users SET balance = balance + 5 WHERE user_id = $1", referrer_id)

            return new_user_id

    except Exception as e:
        return None





async def get_user_balance(user_id, pool):
    async with pool.acquire() as conn:
        balance = await conn.fetchval(
            "SELECT balance FROM users WHERE user_id = $1",
            user_id
        )
        return balance if balance is not None else 0


async def update_user_balance(user_id, amount, pool):
    async with pool.acquire() as conn:
        current_balance = await conn.fetchval(
            "SELECT balance FROM users WHERE user_id = $1",
            user_id
        )
        if current_balance is not None:
            new_balance = current_balance + amount
            await conn.execute(
                "UPDATE users SET balance = $1 WHERE user_id = $2",
                new_balance, user_id
            )

async def get_all_user_ids(pool):
    async with pool.acquire() as conn:
        rows = await conn.fetch("SELECT user_id FROM users")
        return [row['user_id'] for row in rows]

async def add_test_result(user_id, test_id, score_percentage, correct_answers, incorrect_answers, pool):
    async with pool.acquire() as conn:
        await conn.execute(
            """INSERT INTO test_results (user_id, test_id, score_percentage, correct_answers, incorrect_answers)
               VALUES ($1, $2, $3, $4, $5)""",
            user_id, test_id, score_percentage, ",".join(map(str, correct_answers)), ",".join(map(str, incorrect_answers))
        )

async def get_user_test_statistics(user_id, pool):
    async with pool.acquire() as conn:
        test_results = await conn.fetch(
            "SELECT test_id, completion_date, score_percentage, correct_answers, incorrect_answers FROM test_results WHERE user_id = $1",
            user_id
        )
    return test_results

async def get_incorrect_questions_for_user(user_id, pool):
    async with pool.acquire() as conn:
        rows = await conn.fetch(
            """
            SELECT incorrect_answers FROM test_results
            WHERE user_id = $1 AND incorrect_answers IS NOT NULL
            """,
            user_id
        )
        incorrect_questions = set()
        for row in rows:
            incorrect_questions.update(row['incorrect_answers'].split(','))
    return list(incorrect_questions)

async def fetch_questions_by_ids(question_ids, pool):
    if not question_ids:
        return []

    async with pool.acquire() as conn:
        # Используем ANY для списка ID
        questions = await conn.fetch(
            """
            SELECT id, question, image_url, option_1, option_2, option_3, option_4, correct_option
            FROM questions WHERE id = ANY($1)
            """,
            question_ids
        )
    return questions

async def update_correct_answers(user_id, correct_answers_ids, pool):
    async with pool.acquire() as conn:
        for question_id in correct_answers_ids:
            # Проверяем, существует ли уже запись для данного вопроса и пользователя
            exists = await conn.fetchval(
                "SELECT EXISTS(SELECT 1 FROM question_user_status WHERE user_id = $1 AND question_id = $2)",
                user_id, question_id
            )
            if not exists:
                # Если записи нет, создаем новую
                await conn.execute(
                    "INSERT INTO question_user_status (user_id, question_id, is_correct) VALUES ($1, $2, TRUE)",
                    user_id, question_id
                )
            else:
                # Если запись есть, обновляем ее
                await conn.execute(
                    "UPDATE question_user_status SET is_correct = TRUE WHERE user_id = $1 AND question_id = $2",
                    user_id, question_id
                )



async def get_incorrect_questions_for_retry(user_id, pool):
    incorrect_questions = []
    async with pool.acquire() as conn:
        rows = await conn.fetch(
            "SELECT question_id FROM question_user_status WHERE user_id=$1 AND is_correct=False",
            user_id
        )
        incorrect_questions = [row['question_id'] for row in rows]
    return incorrect_questions

async def get_incorrect_questions_for_combined_approach(user_id, pool):
    incorrect_questions = set()
    correct_questions = set()

    async with pool.acquire() as conn:
        # Получаем неправильные вопросы из test_results
        rows = await conn.fetch(
            "SELECT incorrect_answers FROM test_results WHERE user_id=$1",
            user_id
        )
        for row in rows:
            incorrect_questions.update(set(row['incorrect_answers'].split(',')))

        # Исключаем вопросы, на которые уже дан правильный ответ
        correct_answers = await conn.fetch(
            "SELECT question_id FROM question_user_status WHERE user_id=$1 AND is_correct=True",
            user_id
        )
        correct_questions = {str(row['question_id']) for row in correct_answers}  # Приведение к строке, если необходимо

    return list(incorrect_questions - correct_questions)

async def get_subscribers_count(pool):
    async with pool.acquire() as conn:
        count = await conn.fetchval("SELECT COUNT(*) FROM users")
        return count if count else 0

async def get_random_question_for_test(test_id, pool):
    async with pool.acquire() as conn:
        row = await conn.fetchrow(
            """
            SELECT id, question, image_url, correct_option 
            FROM questions 
            WHERE test_id = $1 
            ORDER BY RANDOM() 
            LIMIT 1
            """,
            test_id
        )
        if row:
            return {
                "id": row['id'],
                "question": row['question'],
                "image_url": row['image_url'],
                "correct_option": row['correct_option']
            }
        return None




#new


import logging

logger = logging.getLogger(__name__)


async def get_daily_words(pool, user_id, lesson_id, count=10):
    async with pool.acquire() as conn:
        query = '''
            SELECT w.word_id, w.text_en, w.text_ru, w.transcription, w.audio_url,
                   COALESCE(uws.correct_count, 0) AS correct_count, 
                   COALESCE(uws.required_correct, 5) AS required_correct,
                   w.sentence_1, w.sentence_2, w.sentence_1_ru, w.sentence_2_ru
            FROM words w
            LEFT JOIN user_words_status uws ON w.word_id = uws.word_id AND uws.user_id = $1
            WHERE w.lesson_id = $2 AND (uws.learned IS NULL OR uws.learned = FALSE)
            ORDER BY RANDOM()
            LIMIT $3
        '''
        words = await conn.fetch(query, user_id, lesson_id, count)
        return [dict(word) for word in words]


async def process_words(words, pool, total_options=4):
    word_ids = [word['word_id'] for word in words]
    async with pool.acquire() as conn:
        all_words = await conn.fetch('SELECT word_id, text_en, text_ru FROM words WHERE word_id != ALL($1)', word_ids)
        all_words = [dict(word) for word in all_words]

    processed_words = []
    for word in words:
        word_dict = dict(word)
        word_dict['asked_question_types'] = []  # Инициализация списка типов вопросов
        word_dict['sentence_1'] = word.get('sentence_1', '').replace(word['text_en'], '_____')
        word_dict['sentence_2'] = word.get('sentence_2', '').replace(word['text_en'], '_____')
        word_dict['sentence_1_ru'] = word.get('sentence_1_ru', '')
        word_dict['sentence_2_ru'] = word.get('sentence_2_ru', '')
        processed_words.append(word_dict)
    return processed_words, all_words

async def update_word_progress(pool, user_id, word_id, is_correct):
    async with pool.acquire() as conn:
        if is_correct:
            await conn.execute('''
                INSERT INTO user_word_progress (user_id, word_id, correct_count)
                VALUES ($1, $2, 1)
                ON CONFLICT (user_id, word_id) DO UPDATE SET correct_count = user_word_progress.correct_count + 1
            ''', user_id, word_id)
        else:
            await conn.execute('''
                INSERT INTO user_word_progress (user_id, word_id, correct_count)
                VALUES ($1, $2, 0)
                ON CONFLICT (user_id, word_id) DO NOTHING
            ''', user_id, word_id)


async def is_word_learned(pool, user_id, word_id):
    async with pool.acquire() as conn:
        correct_count = await conn.fetchval('''
            SELECT correct_count FROM user_word_progress WHERE user_id = $1 AND word_id = $2
        ''', user_id, word_id)
    if correct_count is None:
        return False  # Если correct_count равен None, возвращаем False
    return correct_count >= 5  # Считаем слово выученным после 5 правильных ответов




async def register_learned_word(pool, user_id, word_id):
    async with pool.acquire() as conn:
        await conn.execute('''
            INSERT INTO user_words (user_id, word_id)
            VALUES ($1, $2)
            ON CONFLICT (user_id, word_id) DO NOTHING
        ''', user_id, word_id)


async def update_user_score(pool, user_id, score):
    async with pool.acquire() as conn:
        await conn.execute('''
            UPDATE users SET balance = balance + $1 WHERE user_id = $2
        ''', score, user_id)

async def check_level_up(pool, user_id):
    async with pool.acquire() as conn:
        user_score = await conn.fetchval('SELECT balance FROM users WHERE user_id = $1', user_id)
        if user_score is None:
            # Log an error or handle the situation appropriately
            print(f"No score found for user {user_id}")
            return None
        new_level = None

        if user_score >= 100:
            new_level = 'Third Officer'
        elif user_score >= 200:
            new_level = 'Second Officer'
        elif user_score >= 300:
            new_level = 'Chief Officer'
        elif user_score >= 400:
            new_level = 'Captain'

        if new_level:
            await conn.execute('''
                UPDATE users SET level_id = (SELECT level_id FROM levels WHERE description = $1) WHERE user_id = $2
            ''', new_level, user_id)
            return new_level
    return None


async def get_user_level(pool, user_id):
    async with pool.acquire() as conn:
        level_id = await conn.fetchval('SELECT level_id FROM users WHERE user_id = $1', user_id)
        logger.info(f"Retrieved level_id: {level_id} for user_id: {user_id}")
        return level_id


async def get_correct_option_for_word(pool, word_id):
    async with pool.acquire() as conn:
        correct_option = await conn.fetchval('SELECT text_ru FROM words WHERE word_id = $1', word_id)
    return correct_option



async def get_or_create_user_word_status(pool, user_id, word_id):
    async with pool.acquire() as conn:
        status = await conn.fetchrow(
            'SELECT * FROM user_words_status WHERE user_id = $1 AND word_id = $2', user_id, word_id
        )
        if status is None:
            await conn.execute(
                'INSERT INTO user_words_status (user_id, word_id, correct_count, required_correct, learned) VALUES ($1, $2, 0, 5, FALSE)',
                user_id, word_id
            )
            logger.info(f"Created new word status for user_id={user_id}, word_id={word_id}")
            return {'user_id': user_id, 'word_id': word_id, 'correct_count': 0, 'required_correct': 5, 'learned': False}
        return dict(status)

async def update_user_word_status(pool, status):
    logger.info(f'Updating word status for user_id={status["user_id"]}, word_id={status["word_id"]}')
    async with pool.acquire() as conn:
        try:
            await conn.execute(
                'UPDATE user_words_status SET correct_count = $1, required_correct = $2, learned = $3 WHERE user_id = $4 AND word_id = $5',
                status['correct_count'], status['required_correct'], status['learned'], status['user_id'], status['word_id']
            )
            logger.info(f'Successfully updated word status for user_id={status["user_id"]}, word_id={status["word_id"]}')
        except Exception as e:
            logger.error(f'Error updating word status for user_id={status["user_id"]}, word_id={status["word_id"]}: {e}')

async def update_learned_status(pool, user_id, word_id, learned):
    async with pool.acquire() as conn:
        await conn.execute(
            'UPDATE user_words_status SET learned = $1 WHERE user_id = $2 AND word_id = $3',
            learned, user_id, word_id)


def check_all_words_learned(context):
    words_status = context.user_data.get('learning_words', [])
    return all(word.get('learned', False) for word in words_status)
