from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, CallbackContext, MessageHandler, filters
import asyncio
from database_manager import add_test, add_question, get_incorrect_questions_for_combined_approach, get_questions_for_test, get_subscribers_count, update_correct_answers, fetch_questions_by_ids, get_tests_by_department, register_new_user, get_user_balance, update_user_balance, get_all_user_ids, add_test_result, get_user_test_statistics
from config import TOKEN
import aiosqlite, logging

ADMIN_USER_ID = 452181463  # Telegram ID администратора
ADMIN = [452181463]
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def start(update: Update, context: CallbackContext):
    referrer_id = context.args[0] if context.args else None
    new_user_telegram_id = update.effective_user.id
    # Вызываем функцию для регистрации нового пользователя и обработки реферального ID
    register_new_user(new_user_telegram_id, referrer_id)

    keyboard = [
        [InlineKeyboardButton("Personal Cabinet", callback_data='personal_account')],
        [InlineKeyboardButton("Deck Department", callback_data='deck_department')],
        [InlineKeyboardButton("Engine Department", callback_data='engine_department')],
        [InlineKeyboardButton("Take the test on incorrect questions", callback_data='retry_incorrect_questions')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Проверяем, вызвана ли функция из обновления сообщения или из обратного вызова
    if update.message:
        await update.message.reply_text('Please, choose:', reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.message.reply_text('Please, choose:', reply_markup=reply_markup)

async def start_callback(update: Update, context: CallbackContext) -> None:
    referrer_id = context.args[0] if context.args else None
    new_user_telegram_id = update.effective_user.id

    # Вызываем функцию для регистрации нового пользователя и обработки реферального ID
    register_new_user(new_user_telegram_id, referrer_id)

    keyboard = [
        [InlineKeyboardButton("Personal Cabinet", callback_data='personal_account')],
        [InlineKeyboardButton("Deck Department", callback_data='deck_department')],
        [InlineKeyboardButton("Engine Department", callback_data='engine_department')],q
        [InlineKeyboardButton("Take the test on incorrect questions", callback_data='retry_incorrect_questions')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Проверяем, вызвана ли функция из обновления сообщения или из обратного вызова
    if update.message:
        await update.message.reply_text('Please, choose:', reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.message.reply_text('Please, choose:', reply_markup=reply_markup)


async def deck_department_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Tests", callback_data='deck_tests')],
        [InlineKeyboardButton("Main Menu", callback_data='start')]  # Добавлена кнопка для возвращения в основное меню
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Choose option:", reply_markup=reply_markup)

async def deck_tests_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    tests = await get_tests_by_department("deck")
    keyboard = [[InlineKeyboardButton(text=name, callback_data=f"start_test_{test_id}")] for test_id, name in tests]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Выберите тест:", reply_markup=reply_markup)


async def engine_department_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Tests", callback_data='mechanics_tests')],
        [InlineKeyboardButton("Main Menu", callback_data='start')]  # Добавлена кнопка для возвращения в основное меню

    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Choose option:", reply_markup=reply_markup)


async def engine_tests_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    tests = await get_tests_by_department("mechanics")  # Убедитесь, что у вас есть функция для получения тестов по отделу
    keyboard = [[InlineKeyboardButton(text=name, callback_data=f"start_test_{test_id}")] for test_id, name in tests]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Выберите тест:", reply_markup=reply_markup)


async def start_test_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_telegram_id = query.from_user.id
    balance = await get_user_balance(user_telegram_id)

    if balance >= 100:  # Проверка баланса
        await update_user_balance(user_telegram_id, -100)  # Списание баланса за начало теста

        test_id = query.data.split('_')[-1]
        questions = await get_questions_for_test(test_id)  # Получаем список вопросов
        total_questions = len(questions)  # Общее количество вопросов

        # Сохраняем вопросы и индекс текущего вопроса
        context.user_data['current_test_questions'] = questions
        context.user_data['current_question_index'] = 0
        context.user_data['current_test_id'] = test_id  # Сохраняем ID текущего теста
        # Инициализация списков для правильных и неправильных ответов
        context.user_data['correct_answers_ids'] = []
        context.user_data['incorrect_answers_ids'] = []

        first_question = questions[0]
        first_question_number = context.user_data['current_question_index']  # Это будет 0

        # Отправляем первый вопрос с общим количеством вопросов
        await send_question(context, update.effective_chat.id, first_question, first_question_number, total_questions)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Недостаточно тугриков для начала теста. Ваш баланс: {balance} тугриков.")





async def send_question(context, chat_id, question_info, question_number, total_questions):
    # Добавляем нумерацию вопросов
    question_text = f"Вопрос {question_number + 1} из {total_questions}:\n\n{question_info[1]}"
    image_url = question_info[2]
    options = question_info[3:7]

    # Группируем кнопки горизонтально
    keyboard = [InlineKeyboardButton(str(i + 1), callback_data=f"answer_{i + 1}_{question_number}") for i, _ in enumerate(options)]
    reply_markup = InlineKeyboardMarkup([keyboard])  # Обёртываем в дополнительный список для горизонтального отображения

    # Отправляем вопрос как фото с подписью или как текст
    if image_url:
        try:
            await context.bot.send_photo(chat_id=chat_id, photo=image_url, caption=question_text, reply_markup=reply_markup)
        except Exception as e:
            print(f"Error sending photo: {e}")
            await context.bot.send_message(chat_id=chat_id, text=question_text, reply_markup=reply_markup)
    else:
        await context.bot.send_message(chat_id=chat_id, text=question_text, reply_markup=reply_markup)


async def handle_answer_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data_parts = query.data.split('_')
    answer_index = int(data_parts[1])
    question_number = int(data_parts[2])

    current_question_index = context.user_data.get('current_question_index', 0)
    questions = context.user_data.get('current_test_questions', [])
    total_questions = len(questions)

    question_id = questions[current_question_index][0]  # Assuming [0] is the question ID
    user_id = update.effective_user.id

    if question_number != current_question_index:
        await query.answer("This question has already been answered or is not the current question.", show_alert=True)
        return

    correct_option = questions[current_question_index][7]
    if answer_index == correct_option:
        response = "Correct! 🎉"
        if question_id not in context.user_data['correct_answers_ids']:
            context.user_data['correct_answers_ids'].append(question_id)
            if question_id in context.user_data['incorrect_answers_ids']:
                context.user_data['incorrect_answers_ids'].remove(question_id)
            # Update the question status in the database as correct
            await update_correct_answers(user_id, [question_id])
    else:
        response = f"Incorrect. 😭 The correct answer was option {correct_option}."
        if question_id not in context.user_data['incorrect_answers_ids']:
            context.user_data['incorrect_answers_ids'].append(question_id)
            if question_id in context.user_data['correct_answers_ids']:
                context.user_data['correct_answers_ids'].remove(question_id)
                # No need to update the database in this case as the answer remains incorrect

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

    # Logic to move to the next question or finish the test remains unchanged
    if current_question_index + 1 < total_questions:
        context.user_data['current_question_index'] += 1
        next_question = questions[current_question_index + 1]
        await send_question(context, update.effective_chat.id, next_question, context.user_data['current_question_index'], total_questions)
    else:
        correct_answers = len(context.user_data.get('correct_answers_ids', []))
        percentage = (correct_answers / total_questions) * 100
        await add_test_result(user_id, context.user_data['current_test_id'], percentage, context.user_data['correct_answers_ids'], context.user_data['incorrect_answers_ids'])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Test finished! You answered {correct_answers} out of {total_questions} questions correctly ({percentage:.0f}%).")
        await start(update, context)

        # Clearing the current test data from user context
        del context.user_data['current_test_questions']
        del context.user_data['current_question_index']
        del context.user_data['correct_answers_ids']
        del context.user_data['incorrect_answers_ids']





async def personal_account_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    balance = await get_user_balance(query.from_user.id)

    keyboard = [
        [InlineKeyboardButton("Get Referral Link", callback_data='get_referral_link')],
        [InlineKeyboardButton("Show Balance", callback_data='show_balance')],
        [InlineKeyboardButton("Show Test Statistics", callback_data='show_tests_stats')],
        [InlineKeyboardButton("Main Menu", callback_data='start')]  # Добавлена кнопка для возвращения в основное меню
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text=f"Personal Account:\nYour balance: {balance} Tugriks", reply_markup=reply_markup)




async def get_user_balance(user_telegram_id):
    async with aiosqlite.connect('tests_db.sqlite') as db:
        async with db.execute("SELECT balance FROM users WHERE telegram_id = ?", (user_telegram_id,)) as cursor:
            balance = await cursor.fetchone()
    return balance[0] if balance else 0


async def show_balance_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Повторно получаем баланс, если пользователь запросил обновление
    balance = await get_user_balance(query.from_user.id)
    await query.edit_message_text(text=f"Ваш баланс Тугриков: {balance}")



async def get_referral_link_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    user_telegram_id = query.from_user.id
    referral_link = generate_referral_link(
        user_telegram_id)  # Убедитесь, что функция generate_referral_link реализована

    await query.edit_message_text(text=f"Ваша реферальная ссылка: {referral_link}")


def generate_referral_link(user_id):
    bot_username = "educationpt_bot"
    return f"https://t.me/{bot_username}?start={user_id}"


def get_user_info(user_telegram_id):
    # Получение данных пользователя из базы данных по telegram_id
    # Генерация реферальной ссылки
    referral_link = generate_referral_link(user_telegram_id)
    # Возвращаем информацию о пользователе и реферальную ссылку в виде строки
    return f"Ваша реферальная ссылка: {referral_link}\nВаш баланс: ..."


async def broadcast_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # Проверка, является ли пользователь администратором
    if user_id not in ADMIN:
        await update.message.reply_text("You do not have permission to use this command.")
        return

    # Запрос фото для рассылки
    context.user_data['awaiting_photo'] = True
    await update.message.reply_text("Please send the photo for broadcasting.")


async def handle_photo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.pop('awaiting_photo', False):
        context.user_data['photo'] = update.message.photo[-1].file_id
        await update.message.reply_text("Фото успешно добавлено. Теперь отправьте текст для рассылки.")
        context.user_data['awaiting_text'] = True


async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.pop('awaiting_text', False):
        text = update.message.text
        photo = context.user_data.pop('photo', None)
        if photo:
            user_ids = await get_all_user_ids()  # Убедитесь, что у вас есть эта функция
            for user_id in user_ids:
                try:
                    await context.bot.send_photo(chat_id=user_id, photo=photo, caption=text)
                    await update.message.reply_text(f"Сообщение отправлено пользователю с ID: {user_id}")
                except Exception as e:
                    print(f"Ошибка при отправке пользователю {user_id}: {e}")
            await update.message.reply_text("Рассылка выполнена.")


async def add_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Проверяем, является ли пользователь администратором
    if update.effective_user.id != ADMIN_USER_ID:
        await update.message.reply_text("У вас нет прав для использования этой команды.")
        return

    # Проверяем, что команда содержит необходимые аргументы
    if not context.args or len(context.args) < 2:
        await update.message.reply_text("Используйте команду в формате: /add_balance user_id amount")
        return

    try:
        user_id = int(context.args[0])
        amount = int(context.args[1])
    except ValueError:
        await update.message.reply_text("Некорректный формат команды. Убедитесь, что ID пользователя и сумма - числа.")
        return

    # Вызываем функцию для обновления баланса пользователя
    await update_user_balance(user_id, amount)
    await update.message.reply_text(f"Баланс пользователя {user_id} успешно обновлён на {amount} тугриков.")


async def show_tests_stats_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    test_results = await get_user_test_statistics(user_id)

    # Using sets to store unique IDs
    unique_correct_answers = set()
    unique_incorrect_answers = set()

    detailed_stats = ""

    for result in test_results:
        test_id, completion_date, score_percentage, correct_answers, incorrect_answers = result

        # Adding IDs to the respective sets
        if correct_answers:
            unique_correct_answers.update(correct_answers.split(','))
        if incorrect_answers:
            unique_incorrect_answers.update(incorrect_answers.split(','))

        correct_count = len(correct_answers.split(',')) if correct_answers else 0
        incorrect_count = len(incorrect_answers.split(',')) if incorrect_answers else 0

        detailed_stats += f"Test {test_id} (Date: {completion_date}): Correct - {correct_count}, Incorrect - {incorrect_count}, Success rate - {score_percentage}%\n"

    # Calculating the total number of unique correct and incorrect answers
    total_correct = len(unique_correct_answers)
    total_incorrect = len(unique_incorrect_answers)

    stats_message = f"Overall statistics: Correct answers - {total_correct}, Incorrect answers - {total_incorrect}\n\nDetailed test statistics:\n{detailed_stats}"

    await context.bot.send_message(chat_id=update.effective_chat.id, text=stats_message)



async def start_test_with_questions(update: Update, context: ContextTypes.DEFAULT_TYPE, incorrect_question_ids):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    # Проверяем, есть ли неправильные вопросы для повторения
    if not incorrect_question_ids:
        await context.bot.send_message(chat_id=chat_id, text="You have no questions to repeat.")
        return

    # Получаем вопросы из базы данных по их ID
    questions = await fetch_questions_by_ids(incorrect_question_ids)

    if questions:
        # Сохраняем вопросы и индекс текущего вопроса
        context.user_data['current_test_questions'] = questions
        context.user_data['current_question_index'] = 0

        # Инициализация списков для правильных и неправильных ответов
        context.user_data['correct_answers_ids'] = []
        context.user_data['incorrect_answers_ids'] = []

        # Отправляем первый вопрос
        first_question = questions[0]
        await send_question(context, chat_id, first_question, 0, len(questions))
    else:
        await context.bot.send_message(chat_id=chat_id, text="Произошла ошибка при загрузке вопросов.")


async def retry_incorrect_questions_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    incorrect_questions_ids = await get_incorrect_questions_for_combined_approach(user_id)

    if incorrect_questions_ids:
        await start_test_with_questions(update, context, incorrect_questions_ids)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="You have no questions to repeat.")



async def send_question_for_retry_incorrect_question(context, chat_id, question_info, question_number, total_questions):
    # Добавляем нумерацию вопросов
    question_text = f"Вопрос {question_number + 1} из {total_questions} (повторение неправильных ответов):\n\n{question_info[1]}"
    image_url = question_info[2]
    options = question_info[3:7]

    # Группируем кнопки горизонтально
    keyboard = [InlineKeyboardButton(str(i + 1), callback_data=f"retry_answer_{i + 1}_{question_number}") for i, _ in enumerate(options)]
    reply_markup = InlineKeyboardMarkup([keyboard])  # Обёртываем в дополнительный список для горизонтального отображения

    # Отправляем вопрос как фото с подписью или как текст
    if image_url:
        try:
            await context.bot.send_photo(chat_id=chat_id, photo=image_url, caption=question_text, reply_markup=reply_markup)
        except Exception as e:
            print(f"Error sending photo: {e}")
            await context.bot.send_message(chat_id=chat_id, text=question_text, reply_markup=reply_markup)
    else:
        await context.bot.send_message(chat_id=chat_id, text=question_text, reply_markup=reply_markup)


async def check_subscribers(update: Update, context: CallbackContext) -> None:
    if update.effective_user.id in ADMIN_USER_ID:
        # Запрос к базе данных для получения количества подписчиков
        subscribers_count = await get_subscribers_count()
        await update.message.reply_text(f"Current number of subscribers: {subscribers_count}")
    else:
        await update.message.reply_text("You do not have permission to use this command.")



def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("add_balance", add_balance))
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(deck_department_callback, pattern='^deck_department$'))
    application.add_handler(CallbackQueryHandler(deck_tests_callback, pattern='^deck_tests$'))
    application.add_handler(CallbackQueryHandler(engine_department_callback, pattern='^engine_department$'))
    application.add_handler(CallbackQueryHandler(engine_tests_callback, pattern='^mechanics_tests$'))
    application.add_handler(CallbackQueryHandler(start_test_callback, pattern='^start_test_'))
    application.add_handler(CallbackQueryHandler(handle_answer_callback, pattern='^answer_'))
    application.add_handler(CallbackQueryHandler(personal_account_callback, pattern='^personal_account$'))
    application.add_handler(CallbackQueryHandler(get_referral_link_callback, pattern='^get_referral_link$'))
    application.add_handler(CallbackQueryHandler(show_balance_callback, pattern='^show_balance$'))
    application.add_handler(CallbackQueryHandler(show_tests_stats_callback, pattern='^show_tests_stats$'))
    application.add_handler(CallbackQueryHandler(retry_incorrect_questions_callback, pattern='^retry_incorrect_questions$'))
    application.add_handler(CallbackQueryHandler(start_callback, pattern='^start$'))
    application.add_handler(CommandHandler("check_subscribers", check_subscribers))

    application.add_handler(CommandHandler("broadcast", broadcast_command))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo_message))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))
    application.add_handler(CommandHandler("add_balance", add_balance))


    application.run_polling()

if __name__ == '__main__':
    main()