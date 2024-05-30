from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, LabeledPrice
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, CallbackContext, MessageHandler, filters, PreCheckoutQueryHandler
from db_operations import create_pool, process_words, get_correct_option_for_word, get_or_create_user_word_status, update_user_word_status, update_learned_status, check_all_words_learned, \
get_daily_words, register_learned_word, update_user_score, check_level_up, update_word_progress, is_word_learned, get_user_level, get_correct_option_for_word

import urllib.parse
from uuid import uuid4
import asyncio
import asyncpg
import random
import logging
from localization import localization

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_callback_data(prefix, option_key, word_id):
    callback_data = f"{prefix}|{option_key}|{word_id}"
    logger.info(f"Callback data: {callback_data} (length: {len(callback_data)})")
    return callback_data

# Function to create a unique key for each option
def generate_option_key():
    return str(uuid4())[:8]  # Generate a short unique key



async def start_daily_learning(update, context):
    logger.info('start_daily_learning called')
    user_id = update.effective_user.id
    try:
        pool = context.bot_data['db_pool']
        words = await get_daily_words(pool, user_id, lesson_id=1, count=10)
        if not words:
            await update.message.reply_text('No new words to learn today.')
            return

        processed_words, all_words = await process_words(words, pool)
        context.user_data['learning_words'] = processed_words
        context.user_data['words_to_learn'] = processed_words[:]  # Копия списка слов
        context.user_data['correct_answers'] = 0
        context.user_data['learned_words'] = []  # Очистка списка выученных слов
        context.user_data['all_words'] = all_words  # Сохранение all_words в user_data

        # Отправляем новое сообщение при начале новой сессии
        context.user_data.pop('message_id', None)
        await send_random_learning_word(update, context)
    except Exception as e:
        logger.error(f'Exception in start_daily_learning: {e}')
        await update.message.reply_text('An error occurred while starting your daily learning session.')


def create_progress_bar(current, total, length=5):
    filled_length = int(length * current // total)
    bar = '🟩' * filled_length + '⬜' * (length - filled_length)
    return bar


async def send_random_learning_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    words_status = context.user_data.get('words_to_learn', [])
    learned_words = context.user_data.get('learned_words', [])
    all_words = context.user_data.get('all_words', [])

    if not words_status:
        await finish_daily_learning(update, context, learned_words)
        return

    current_word = context.user_data.get('current_word')
    if current_word and current_word['correct_count'] >= current_word['required_correct']:
        words_status = [word for word in words_status if word['word_id'] != current_word['word_id']]
        learned_words.append(current_word)
        context.user_data['words_to_learn'] = words_status
        context.user_data['learned_words'] = learned_words

    if not words_status:
        await finish_daily_learning(update, context, learned_words)
        return

    last_word_id = context.user_data.get('last_word_id')
    available_words = [word for word in words_status if word['word_id'] != last_word_id] or words_status
    random_word = random.choice(available_words)
    context.user_data['current_word'] = random_word
    context.user_data['last_word_id'] = random_word['word_id']

    # Track the types of questions asked for each word
    if 'asked_question_types' not in random_word:
        random_word['asked_question_types'] = []

    if 'en_word' not in random_word['asked_question_types']:
        question_type = 'en_word'
        random_word['asked_question_types'].append('en_word')
    elif 'sentence_1' not in random_word['asked_question_types']:
        question_type = 'en_sentence'
        random_word['asked_question_types'].append('sentence_1')
    elif 'sentence_2' not in random_word['asked_question_types']:
        question_type = 'en_sentence'
        random_word['asked_question_types'].append('sentence_2')
    elif 'ru_word' not in random_word['asked_question_types']:
        question_type = 'ru_word'
        random_word['asked_question_types'].append('ru_word')
    else:
        question_type = random.choice(['en_word', 'ru_word', 'en_sentence'])

    if question_type == 'ru_word':
        question_text = f"'{random_word['text_ru']}' это?\n\n"
        correct_option = random_word['text_en']
        options = [w['text_en'] for w in all_words if w['word_id'] != random_word['word_id']]
    elif question_type == 'en_sentence':
        if 'sentence_1' in random_word['asked_question_types'] and 'sentence_2' not in random_word[
            'asked_question_types']:
            sentence_index = 2
        else:
            sentence_index = 1
        sentence = random_word[f'sentence_{sentence_index}'].replace(random_word['text_en'], '_____')
        sentence_ru = random_word[f'sentence_{sentence_index}_ru']
        question_text = f"{sentence}\n\n{sentence_ru}\n\n"
        correct_option = random_word['text_en']
        options = [w['text_en'] for w in all_words if w['word_id'] != random_word['word_id']]
    else:
        question_text = f"'{random_word['text_en']}' это?\n\n"
        correct_option = random_word['text_ru']
        options = [w['text_ru'] for w in all_words if w['word_id'] != random_word['word_id']]

    if len(options) < 3:
        options = options + random.sample([opt for opt in options if opt != correct_option], 3 - len(options))
    else:
        options = random.sample(options, 3)

    all_options = options + [correct_option]
    random.shuffle(all_options)

    display_correct_count = random_word['correct_count'] + 1
    progress_bar = create_progress_bar(display_correct_count, random_word['required_correct'])
    progress_text = f"[{progress_bar}] {display_correct_count}/{random_word['required_correct']}"

    question_text += progress_text

    options_mapping = {}
    options_buttons = []
    for i, option in enumerate(all_options):
        option_key = generate_option_key()
        options_mapping[option_key] = option
        options_buttons.append([InlineKeyboardButton(f"{i + 1}️⃣ {option}",
                                                     callback_data=create_callback_data("learning_answer", option_key,
                                                                                        random_word['word_id']))])

    context.user_data['options_mapping'] = options_mapping
    reply_markup = InlineKeyboardMarkup(options_buttons)

    if 'message_id' in context.user_data:
        message_id = context.user_data['message_id']
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
        except Exception as e:
            logger.error(f"Error deleting message: {e}")

    try:
        if question_type == 'en_word':
            audio_file_id = random_word['audio_url']
            if audio_file_id:
                message = await context.bot.send_audio(chat_id=chat_id, audio=audio_file_id, caption=question_text,
                                                       reply_markup=reply_markup)
            else:
                message = await context.bot.send_message(chat_id=chat_id, text=question_text, reply_markup=reply_markup)
        else:
            message = await context.bot.send_message(chat_id=chat_id, text=question_text, reply_markup=reply_markup)

        context.user_data['message_id'] = message.message_id
    except Exception as e:
        logger.error(f"Error sending question: {e}")
        message = await context.bot.send_message(chat_id=chat_id, text=question_text, reply_markup=reply_markup)
        context.user_data['message_id'] = message.message_id



async def handle_learning_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    logger.info(f"Received callback data: {query.data}")

    try:
        data_parts = query.data.split('|')

        if len(data_parts) != 3:
            logger.error(f"Invalid callback data format: {query.data}")
            return

        option_key = data_parts[1]
        word_id = int(data_parts[2])

        options_mapping = context.user_data.get('options_mapping', {})
        chosen_option = options_mapping.get(option_key, None)

        if chosen_option is None:
            logger.error(f"Invalid option key: {option_key}")
            await query.answer("Invalid option selected.")
            return

        logger.info(f"User {query.from_user.id} chose option {chosen_option} for word ID {word_id}")

        pool = context.bot_data.get('db_pool')
        user_id = update.effective_user.id

        # Получаем текущее слово
        current_word = context.user_data.get('current_word')
        if not current_word or current_word['word_id'] != word_id:
            logger.error(f"Current word does not match word_id: {word_id}")
            await query.answer("Error processing your answer.")
            return

        # Определяем правильный вариант ответа в зависимости от типа вопроса
        if query.message.caption:
            question_type = 'en_word'  # если есть аудио, то значит английский
        elif '_____' in query.message.text:
            question_type = 'en_sentence'
        else:
            question_type = 'ru_word'

        correct_option = current_word['text_en'] if question_type in ['ru_word', 'en_sentence'] else current_word['text_ru']

        user_word_status = await get_or_create_user_word_status(pool, user_id, word_id)

        if chosen_option == correct_option:
            user_word_status['correct_count'] += 1
            if user_word_status['correct_count'] >= user_word_status['required_correct']:
                user_word_status['learned'] = True
                context.user_data['words_to_learn'] = [word for word in context.user_data['words_to_learn'] if word['word_id'] != word_id]
        else:
            user_word_status['correct_count'] = max(0, user_word_status['correct_count'] - 1)

        await update_user_word_status(pool, user_word_status)

        context.user_data['current_word']['correct_count'] = user_word_status['correct_count']

        new_buttons = []
        for key, option in options_mapping.items():
            if option == correct_option:
                label = f"✅ {option}"
            elif key == option_key:
                label = f"❌ {option}"
            else:
                label = option
            new_buttons.append([InlineKeyboardButton(label, callback_data="none")])

        reply_markup = InlineKeyboardMarkup(new_buttons)
        await query.edit_message_reply_markup(reply_markup=reply_markup)

        await asyncio.sleep(1)
        await send_random_learning_word(update, context)
    except Exception as e:
        logger.error(f"Error in handle_learning_answer: {e}")

async def finish_daily_learning(update: Update, context: ContextTypes.DEFAULT_TYPE, learned_words):
    chat_id = update.effective_chat.id

    if 'message_id' in context.user_data:
        message_id = context.user_data['message_id']
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
        except Exception as e:
            logger.error(f"Error deleting message: {e}")

    if not learned_words:
        message = "Урок завершён! 🎉\nСегодня не было выучено ни одного слова."
    else:
        message = "Урок завершён! 🎉\n\nВы выучили следующие слова:\n"
        for word in learned_words:
            message += f"- {word['text_en']} ([{word['transcription']}]) - {word['text_ru']}\n"

    final_message = await context.bot.send_message(chat_id=chat_id, text=message)
    context.user_data['message_id'] = final_message.message_id


    # Регистрация обработчиков
def register_handlers(application):
    logger.info('Registering handlers')
    application.add_handler(CommandHandler('start_daily_learning', start_daily_learning))
    application.add_handler(CallbackQueryHandler(handle_learning_answer, pattern=r'^learning_answer\|'))
