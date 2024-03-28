import asyncio
import aiosqlite

async def create_db():
    async with aiosqlite.connect("quiz.db") as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS questions
                            (id INTEGER PRIMARY KEY, question TEXT, answer TEXT)''')
        await db.commit()

asyncio.run(create_db())


async def add_question(question, answer):
    async with aiosqlite.connect("quiz.db") as db:
        await db.execute("INSERT INTO questions (question, answer) VALUES (?, ?)", (question, answer,))
        await db.commit()

async def create_questions_table():
    async with aiosqlite.connect("quiz.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY,
                question TEXT NOT NULL,
                answer TEXT NOT NULL
            )
        """)
        await db.commit()
        print("Таблица вопросов создана.")


async def create_participants_table():
    async with aiosqlite.connect("quiz.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS participants (
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                chat_id INTEGER NOT NULL,
                username TEXT,
                wins INTEGER DEFAULT 0
            )
        """)
        await db.commit()
        print("Таблица участников создана.")

asyncio.run(create_questions_table())
asyncio.run(create_participants_table())
