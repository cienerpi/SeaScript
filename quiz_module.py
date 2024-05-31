from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, LabeledPrice
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, CallbackContext, MessageHandler, filters, PreCheckoutQueryHandler
import asyncio
import random
import logging
from db_operations import create_pool

ALLOWED_CHAT_IDS = [-1002214875727, -4129260987, -1001587110027]  # Replace with your chat IDs

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def get_random_question(pool):
    async with pool.acquire() as connection:
        row = await connection.fetchrow("SELECT id, question FROM quiz_questions ORDER BY RANDOM() LIMIT 1")
        if row:
            return {"id": row["id"], "question": row["question"]}
        return None

async def get_correct_answer(pool, question_id):
    async with pool.acquire() as connection:
        row = await connection.fetchrow("SELECT correct_answer FROM quiz_questions WHERE id=$1", question_id)
        if row:
            return row["correct_answer"]
        return None

async def update_user_stats(pool, user_id, chat_id):
    async with pool.acquire() as connection:
        await connection.execute("""
            INSERT INTO user_stats (user_id, chat_id, correct_answers)
            VALUES ($1, $2, 1)
            ON CONFLICT (user_id, chat_id) DO UPDATE 
            SET correct_answers = user_stats.correct_answers + 1
        """, user_id, chat_id)

async def get_chat_leaderboard(pool, chat_id):
    async with pool.acquire() as connection:
        rows = await connection.fetch("""
            SELECT user_id, correct_answers 
            FROM user_stats 
            WHERE chat_id = $1 
            ORDER BY correct_answers DESC 
            LIMIT 10
        """, chat_id)
        return rows

async def start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id not in ALLOWED_CHAT_IDS:
        await update.message.reply_text("This bot is not allowed in this chat.")
        return

    pool = context.bot_data.get("db_pool")
    if not pool:
        await update.message.reply_text("Database connection not available.")
        return

    question_info = await get_random_question(pool)
    if question_info:
        context.chat_data["question_id"] = question_info["id"]
        logger.info(f"Set question_id in chat_data: {context.chat_data['question_id']}")
        await update.message.reply_text(f"Question: {question_info['question']}")
    else:
        await update.message.reply_text("No questions available.")

async def check_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id not in ALLOWED_CHAT_IDS:
        logger.info(f"Chat ID {chat_id} is not allowed.")
        return  # Do not respond if the chat is not allowed

    pool = context.bot_data.get("db_pool")
    if not pool:
        logger.info("No database connection available.")
        return  # Do not respond if there is no database connection

    question_id = context.chat_data.get("question_id")
    logger.info(f"Retrieved question_id from chat_data: {question_id}")
    if not question_id:
        logger.info("No question_id found in chat_data.")
        return  # Do not respond if there is no question set

    user_answer = update.message.text.strip()
    logger.info(f"User answer: {user_answer}")
    correct_answer = await get_correct_answer(pool, question_id)
    logger.info(f"Correct answer: {correct_answer}")
    if user_answer.lower() == correct_answer.lower():
        await update.message.reply_text(f"Correct! 🎉 Answer: {correct_answer}.")
        # Update user stats
        user_id = update.effective_user.id
        await update_user_stats(pool, user_id, chat_id)
        # Reset the question after a correct answer
        context.chat_data["question_id"] = None
        logger.info(f"Reset question_id in chat_data")

async def show_leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id not in ALLOWED_CHAT_IDS:
        await update.message.reply_text("This bot is not allowed in this chat.")
        return

    pool = context.bot_data.get("db_pool")
    if not pool:
        await update.message.reply_text("Database connection not available.")
        return

    leaderboard = await get_chat_leaderboard(pool, chat_id)
    if not leaderboard:
        await update.message.reply_text("No leaderboard data available.")
        return

    leaderboard_text = "Chat leaderboard:\n"
    for rank, entry in enumerate(leaderboard, start=1):
        user = await context.bot.get_chat_member(chat_id, entry["user_id"])
        user_name = user.user.first_name
        leaderboard_text += f"{rank}. {user_name} - {entry['correct_answers']} correct answers\n"

    await update.message.reply_text(leaderboard_text)

def register_quiz_handlers(application):
    # Register quiz handlers
    application.add_handler(CommandHandler("start_quiz", start_quiz))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_answer))
    application.add_handler(CommandHandler("leaderboard", show_leaderboard))

# Initialize your application and register handlers as needed
