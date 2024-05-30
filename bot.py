from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, LabeledPrice, BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, CallbackContext, MessageHandler, filters, PreCheckoutQueryHandler
from db_operations import get_incorrect_questions_for_combined_approach, get_questions_for_test, \
     get_subscribers_count,  update_correct_answers, fetch_questions_by_ids, get_tests_by_department, register_new_user,\
     get_user_balance, update_user_balance, get_all_user_ids, add_test_result, get_user_test_statistics, get_all_tests, \
     get_random_question_for_test, create_pool
from config import TOKEN, STRIPE_TOKEN
import logging, asyncpg, random, asyncio, db_operations
from localization import localization
from englishlessons import register_handlers
from quiz_module import register_quiz_handlers



ALLOWED_CHAT_IDS = [-4129260987]
ADMIN_USER_ID = 452181463
ADMIN = [452181463]
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



async def start(update: Update, context: CallbackContext):
    if update.message.chat.type != 'private':
        await update.message.reply_text("This command can only be used in private chats.")
        return

    user_id = update.effective_user.id
    referrer_id = context.args[0] if context.args else None
    if referrer_id:
        try:
            referrer_id = int(referrer_id)
        except ValueError:
            referrer_id = None

    keyboard = [
        [InlineKeyboardButton(" Українська", callback_data='set_lang_ua'),
         InlineKeyboardButton(" English", callback_data='set_lang_en'),
         InlineKeyboardButton(" Русский", callback_data='set_lang_ru')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Please choose your language / Пожалуйста, выберите ваш язык / Будь ласка, оберіть вашу мову:",
        reply_markup=reply_markup
    )

    pool = context.bot_data.get('db_pool')
    if not pool:
        pool = await create_pool()
        context.bot_data['db_pool'] = pool

    if pool:
        registered_user_id = await register_new_user(user_id, pool, referrer_user_id=referrer_id)
        if registered_user_id is None:
            await update.message.reply_text("Ошибка регистрации.")
    else:
        await update.message.reply_text("Не удалось подключиться к базе данных.")

async def language_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    language = query.data.split('_')[-1]
    context.user_data['language'] = language
    user_id = query.from_user.id
    chat_id = "@seascript"
    referrer_id = context.args[0] if context.args else None
    if referrer_id:
        try:
            referrer_id = int(referrer_id)
        except ValueError:
            referrer_id = None

    pool = context.bot_data.get('db_pool')
    if not pool:
        pool = await create_pool()
        context.bot_data['db_pool'] = pool

    registered_user_id = await register_new_user(user_id, pool, referrer_user_id=referrer_id)
    if registered_user_id is None:
        await query.edit_message_text("Registration error.")
        return

    try:
        member = await context.bot.get_chat_member(chat_id=chat_id, user_id=user_id)
        if member.status in ['left', 'kicked']:
            keyboard = [
                [InlineKeyboardButton("Subscribe", url="https://t.me/seascript")],
                [InlineKeyboardButton("Check Subscription", callback_data='verify_subscription')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_text("Please subscribe to the channel to continue.", reply_markup=reply_markup)
        else:
            await show_main_menu(update, context)
    except Exception as e:
        await query.edit_message_text("Failed to check subscription status.")



async def verify_subscription_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    chat_id = "@seascript"
    language = context.user_data.get('language', 'en')  # Значение по умолчанию - английский

    try:
        member = await context.bot.get_chat_member(chat_id=chat_id, user_id=user_id)
        if member.status not in ['left', 'kicked']:
            await query.answer(localization[language]['thanks_for_subscribing'], show_alert=True)
            await show_main_menu(query, context, edit=True)  # Установите edit=True, если хотите редактировать сообщение
        else:
            await query.answer(localization[language]['please_subscribe'], show_alert=True)
    except Exception as e:
        await query.answer(localization[language]['subscription_error'], show_alert=True)
        print(e)


async def show_main_menu(update_or_query, context: CallbackContext, edit=False):
    language = context.user_data.get('language', 'en')  # Default language

    keyboard = [
        [InlineKeyboardButton(localization[language]['personal_cabinet'], callback_data='personal_account')],
        [InlineKeyboardButton("CES 6", callback_data='ces_6_menu')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    prompt_text = localization[language]['main_menu_prompt']  # Localized text prompt

    try:
        if edit:
            if hasattr(update_or_query, 'edit_message_text'):
                await update_or_query.edit_message_text(text=prompt_text, reply_markup=reply_markup)
            elif hasattr(update_or_query, 'callback_query') and hasattr(update_or_query.callback_query, 'edit_message_text'):
                await update_or_query.callback_query.edit_message_text(text=prompt_text, reply_markup=reply_markup)
        else:
            chat_id = (update_or_query.effective_chat.id if isinstance(update_or_query, Update)
                       else update_or_query.message.chat.id)
            await context.bot.send_message(chat_id=chat_id, text=prompt_text, reply_markup=reply_markup)
    except Exception as e:
        if hasattr(update_or_query, 'message'):
            await update_or_query.message.reply_text(f"Error: {str(e)}")


async def ces_6_menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    language = context.user_data.get('language', 'en')  # Default language

    keyboard = [
        [InlineKeyboardButton(localization[language]['deck_department'], callback_data='deck_department')],
        [InlineKeyboardButton(localization[language]['engine_department'], callback_data='engine_department')],
        [InlineKeyboardButton(localization[language]['main_menu'], callback_data='main_menu')]  # Back to main menu button
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    prompt_text = localization[language]['choose_option']  # Assuming there is a 'choose_option' in localization

    await query.edit_message_text(text=localization[language]['ces_6_guide'] + "\n\n" + prompt_text, reply_markup=reply_markup)




async def menu_command(update: Update, context: CallbackContext):
    await show_main_menu(update, context, edit=True)

async def start_callback(update: Update, context: CallbackContext) -> None:
    language = context.user_data.get('language', 'en')  # Default to English

    referrer_id = context.args[0] if context.args else None
    new_user_id = update.effective_user.id
    # Assuming 'pool' is available here as a part of context or globally
    await register_new_user(new_user_id, referrer_user_id=referrer_id)

    keyboard = [
        [InlineKeyboardButton(localization[language]['personal_cabinet'], callback_data='personal_account')],
        [InlineKeyboardButton(localization[language]['deck_department'], callback_data='deck_department')],
        [InlineKeyboardButton(localization[language]['engine_department'], callback_data='engine_department')],
        [InlineKeyboardButton(localization[language]['retry_incorrect_questions'], callback_data='retry_incorrect_questions')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    prompt_text = localization[language]['main_menu_prompt']

    if update.message:
        await update.message.reply_text(prompt_text, reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.message.reply_text(prompt_text, reply_markup=reply_markup)



async def deck_department_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    language = context.user_data.get('language', 'en')  # Default to English if not set

    pool = context.bot_data.get('db_pool')
    if not pool:
        await query.edit_message_text(text=localization[language]['database_error'])
        return

    tests = await get_tests_by_department("deck", pool)  # Pass the pool to the function
    test_buttons = [[InlineKeyboardButton(text=name, callback_data=f"start_test_{test_id}")] for test_id, name in tests]
    retry_button = [InlineKeyboardButton(localization[language]['retry_incorrect_questions'], callback_data='retry_incorrect_questions')]
    main_menu_button = [InlineKeyboardButton(localization[language]['main_menu'], callback_data='main_menu')]

    keyboard = test_buttons + [retry_button, main_menu_button]
    reply_markup = InlineKeyboardMarkup(keyboard)
    prompt_text = localization[language]['choose_test']  # Localized prompt text

    await query.edit_message_text(text=prompt_text, reply_markup=reply_markup)


async def deck_tests_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    language = context.user_data.get('language', 'en')  # Значение по умолчанию - английский

    pool = context.bot_data.get('db_pool')
    if not pool:
        await query.edit_message_text(text=localization[language]['database_error'])
        return

    tests = await get_tests_by_department("deck", pool)  # Теперь передаем пул в функцию
    test_buttons = [[InlineKeyboardButton(text=name, callback_data=f"start_test_{test_id}")] for test_id, name in tests]
    main_menu_button = [InlineKeyboardButton(localization[language]['main_menu'], callback_data='main_menu')]

    keyboard = test_buttons + [main_menu_button]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(text=localization[language]['choose_test'], reply_markup=reply_markup)


async def engine_department_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Получаем язык пользователя из сохраненных данных
    language = context.user_data.get('language', 'en')  # Значение по умолчанию - английский

    # Получение пула соединений
    pool = context.bot_data.get('db_pool')
    if not pool:
        await query.edit_message_text(text=localization[language]['database_error'])
        return

    # Извлечение данных о тестах из базы данных
    tests = await get_tests_by_department("mechanics", pool)  # Теперь передаем пул в функцию
    test_buttons = [[InlineKeyboardButton(text=name, callback_data=f"start_test_{test_id}")] for test_id, name in tests]
    retry_button = [InlineKeyboardButton(localization[language]['retry_incorrect_questions'],
                                         callback_data='retry_incorrect_questions')]
    main_menu_button = [InlineKeyboardButton(localization[language]['main_menu'], callback_data='main_menu')]

    # Составление клавиатуры
    keyboard = test_buttons + [retry_button, main_menu_button]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отображение сообщения с выбором тестов
    await query.edit_message_text(text=localization[language]['choose_test'], reply_markup=reply_markup)


async def engine_tests_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Получаем язык пользователя из сохраненных данных
    language = context.user_data.get('language', 'en')  # Значение по умолчанию - английский

    # Получение пула соединений
    pool = context.bot_data.get('db_pool')
    if not pool:
        await query.edit_message_text(text=localization[language]['database_error'])
        return

    # Извлечение данных о тестах из базы данных
    tests = await get_tests_by_department("mechanics", pool)  # Теперь передаем пул в функцию
    test_buttons = [[InlineKeyboardButton(text=name, callback_data=f"start_test_{test_id}")] for test_id, name in tests]
    main_menu_button = [InlineKeyboardButton(localization[language]['main_menu'], callback_data='main_menu')]

    # Составление клавиатуры
    keyboard = test_buttons + [main_menu_button]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отображение сообщения с выбором тестов
    await query.edit_message_text(text=localization[language]['choose_test'], reply_markup=reply_markup)



async def start_test_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    language = context.user_data.get('language', 'en')  # Default to English

    pool = context.bot_data.get('db_pool')
    if not pool:
        await query.edit_message_text(text=localization[language]['database_error'])
        return

    user_id = query.from_user.id

    balance = await get_user_balance(user_id, pool)
    if balance >= 1:
        await update_user_balance(user_id, -1, pool)

        test_id_str = query.data.split('_')[-1]
        try:
            test_id = int(test_id_str)
        except ValueError:
            await query.edit_message_text(text=localization[language]['invalid_test_id'])
            return

        questions = await get_questions_for_test(test_id, pool)
        total_questions = len(questions)

        context.user_data['current_test_questions'] = questions
        context.user_data['current_question_index'] = 0
        context.user_data['current_test_id'] = test_id
        context.user_data['correct_answers_ids'] = []
        context.user_data['incorrect_answers_ids'] = []

        first_question = questions[0]
        first_question_number = context.user_data['current_question_index']
        await send_question(context, update.effective_chat.id, first_question, first_question_number, total_questions)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=localization[language]['insufficient_funds'].format(balance=balance))



async def send_question(context, chat_id, question_info, question_number, total_questions):
    language = context.user_data.get('language', 'en')  # Значение по умолчанию - английский

    question_text = localization[language]['question_prompt'].format(
        number=question_number + 1,
        total=total_questions,
        question=question_info[1]
    )
    image_url = question_info[2]
    options = question_info[3:7]

    keyboard = [InlineKeyboardButton(str(i + 1), callback_data=f"answer_{i + 1}_{question_number}") for i, _ in enumerate(options)]
    reply_markup = InlineKeyboardMarkup([keyboard])

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

    language = context.user_data.get('language', 'en')  # Default to English
    data_parts = query.data.split('_')
    answer_index = int(data_parts[1])
    question_number = int(data_parts[2])
    user_id = update.effective_user.id

    pool = context.bot_data.get('db_pool')
    if not pool:
        pool = await create_pool()
        context.bot_data['db_pool'] = pool

    current_question_index = context.user_data.get('current_question_index', 0)
    questions = context.user_data.get('current_test_questions', [])
    total_questions = len(questions)

    if not questions:
        await query.message.reply_text("Error: No question data available.")
        return

    if question_number != current_question_index:
        await query.answer("This question has already been answered or is not the current question.", show_alert=True)
        return

    question_id = questions[current_question_index][0]
    correct_option = questions[current_question_index][7]
    is_correct = answer_index == correct_option

    if is_correct:
        response = "Correct! 🎉"
        if question_id not in context.user_data['correct_answers_ids']:
            context.user_data['correct_answers_ids'].append(question_id)
            if question_id in context.user_data['incorrect_answers_ids']:
                context.user_data['incorrect_answers_ids'].remove(question_id)
            await update_correct_answers(user_id, [question_id], pool)
    else:
        response = f"Incorrect. 😭 The correct answer was option {correct_option}."
        if question_id not in context.user_data['incorrect_answers_ids']:
            context.user_data['incorrect_answers_ids'].append(question_id)
            if question_id in context.user_data['correct_answers_ids']:
                context.user_data['correct_answers_ids'].remove(question_id)

    if query.message.text:
        await query.edit_message_text(response)
    else:
        await query.message.reply_text(response)

    if current_question_index + 1 < total_questions:
        context.user_data['current_question_index'] += 1
        next_question = questions[current_question_index + 1]
        await send_question(context, update.effective_chat.id, next_question, context.user_data['current_question_index'], total_questions)
    else:
        correct_answers = len(context.user_data.get('correct_answers_ids', []))
        incorrect_answers = len(context.user_data.get('incorrect_answers_ids', []))
        percentage = (correct_answers / total_questions) * 100
        await add_test_result(user_id, context.user_data.get('current_test_id'), percentage, context.user_data['correct_answers_ids'], context.user_data['incorrect_answers_ids'], pool)
        final_message = f"Test finished! You answered {correct_answers} out of {total_questions} questions correctly ({percentage:.0f}%)."
        await query.message.reply_text(final_message)
        # Call show_main_menu after the final message
        await show_main_menu(update, context, edit=False)
        # Clear the test data from user context after the test is completed
        del context.user_data['current_test_questions']
        del context.user_data['current_question_index']
        del context.user_data['correct_answers_ids']
        del context.user_data['incorrect_answers_ids']






async def personal_account_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    language = context.user_data.get('language', 'en')  # Значение по умолчанию - английский

    balance = await get_user_balance(query.from_user.id, context.bot_data['db_pool'])

    keyboard = [
        [InlineKeyboardButton(localization[language]['get_referral_link'], callback_data='get_referral_link')],
        [InlineKeyboardButton(localization[language]['buy_tugriks'], callback_data='buy_tugriks')],
        [InlineKeyboardButton(localization[language]['show_balance'], callback_data='show_balance')],
        [InlineKeyboardButton(localization[language]['show_tests_stats'], callback_data='show_tests_stats')],
        [InlineKeyboardButton(localization[language]['main_menu'], callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    account_text = localization[language]['personal_account'].format(balance=balance)
    await query.edit_message_text(text=account_text, reply_markup=reply_markup)




async def show_balance_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    language = context.user_data.get('language', 'en')  # Значение по умолчанию - английский

    pool = context.bot_data.get('db_pool')
    if not pool:
        pool = await create_pool()  # Создаем пул, если он еще не создан
        context.bot_data['db_pool'] = pool

    balance = await get_user_balance(query.from_user.id, pool)

    keyboard = [[InlineKeyboardButton(localization[language]['main_menu'], callback_data='main_menu')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    balance_text = localization[language]['your_balance'].format(balance=balance)
    await query.edit_message_text(text=balance_text, reply_markup=reply_markup)



async def get_referral_link_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    language = context.user_data.get('language', 'en')  # Default to English

    user_id = query.from_user.id
    referral_link = generate_referral_link(user_id)

    keyboard = [[InlineKeyboardButton(localization[language]['main_menu'], callback_data='main_menu')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    referral_text = localization[language]['your_referral_link'].format(referral_link=referral_link)
    await query.edit_message_text(text=referral_text, reply_markup=reply_markup)



def generate_referral_link(user_id):
    bot_username = "educationpt_bot"
    return f"https://t.me/{bot_username}?start={user_id}"


def get_user_info(user_id, language='en'):
    referral_link = generate_referral_link(user_id)
    referral_text = localization[language]['your_referral_link'].format(referral_link=referral_link)
    balance_text = localization[language]['your_balance']
    return f"{referral_text}\n{balance_text}"


async def broadcast_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN:
        await update.message.reply_text("You do not have permission to use this command.")
        return
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
            user_ids = await get_all_user_ids()
            for user_id in user_ids:
                try:
                    await context.bot.send_photo(chat_id=user_id, photo=photo, caption=text)
                    await update.message.reply_text(f"Сообщение отправлено пользователю с ID: {user_id}")
                except Exception as e:
                    print(f"Ошибка при отправке пользователю {user_id}: {e}")
            await update.message.reply_text("Рассылка выполнена.")


async def add_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_USER_ID:
        await update.message.reply_text("У вас нет прав для использования этой команды.")
        return

    if not context.args or len(context.args) < 2:
        await update.message.reply_text("Используйте команду в формате: /add_balance user_id amount")
        return
    try:
        user_id = int(context.args[0])
        amount = int(context.args[1])
    except ValueError:
        await update.message.reply_text("Некорректный формат команды. Убедитесь, что ID пользователя и сумма - числа.")
        return

    await update_user_balance(user_id, amount)
    await update.message.reply_text(f"Баланс пользователя {user_id} успешно обновлён на {amount} тугриков.")


async def show_tests_stats_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    language = context.user_data.get('language', 'en')  # Assuming default language is English

    # Retrieve connection pool and check if it's available
    pool = context.bot_data.get('db_pool')
    if not pool:
        await query.edit_message_text(text=localization[language]['database_unavailable'])
        return

    test_results = await get_user_test_statistics(user_id, pool)

    unique_correct_answers = set()
    unique_incorrect_answers = set()

    detailed_stats = ""
    for result in test_results:
        test_id, completion_date, score_percentage, correct_answers, incorrect_answers = result
        correct_answers_list = correct_answers.split(',') if correct_answers else []
        incorrect_answers_list = incorrect_answers.split(',') if incorrect_answers else []

        unique_correct_answers.update(correct_answers_list)
        unique_incorrect_answers.update(incorrect_answers_list)

        detailed_stats += localization[language]['test_details'].format(
            test_id=test_id, date=completion_date, correct=len(correct_answers_list), incorrect=len(incorrect_answers_list), rate=score_percentage)

    total_correct = len(unique_correct_answers)
    total_incorrect = len(unique_incorrect_answers)

    stats_message = localization[language]['overall_statistics'].format(total_correct=total_correct, total_incorrect=total_incorrect) + "\n\n" + localization[language]['detailed_statistics'].format(details=detailed_stats)

    keyboard = [[InlineKeyboardButton(localization[language]['main_menu'], callback_data='main_menu')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if query.message:
        await query.edit_message_text(text=stats_message, reply_markup=reply_markup)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=stats_message, reply_markup=reply_markup)



async def start_test_with_questions(update: Update, context: ContextTypes.DEFAULT_TYPE, incorrect_question_ids):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    language = context.user_data.get('language', 'en')  # Defaulting to English

    pool = context.bot_data.get('db_pool')
    if not pool:
        pool = await create_pool()
        context.bot_data['db_pool'] = pool

    if not incorrect_question_ids:
        await context.bot.send_message(chat_id=chat_id, text=localization[language]['no_questions_to_repeat'])
        return

    incorrect_question_ids = [int(id) for id in incorrect_question_ids if id.isdigit()]
    questions = await fetch_questions_by_ids(incorrect_question_ids, pool)

    if questions:
        context.user_data['current_test_questions'] = questions
        context.user_data['current_question_index'] = 0
        context.user_data['correct_answers_ids'] = []
        context.user_data['incorrect_answers_ids'] = []
        context.user_data['current_test_id'] = None  # Special identifier if needed

        first_question = questions[0]
        await send_question(context, chat_id, first_question, 0, len(questions))
    else:
        await context.bot.send_message(chat_id=chat_id, text=localization[language]['error_loading_questions'])
        logging.info(f"Test started with questions for user {user_id}. No questions fetched with IDs {incorrect_question_ids}")





async def retry_incorrect_questions_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Assume default language is English, retrieve user's preferred language
    language = context.user_data.get('language', 'en')

    # Retrieve or create a connection pool
    pool = context.bot_data.get('db_pool')
    if not pool:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=localization[language]['database_unavailable'])
        pool = await create_pool()
        context.bot_data['db_pool'] = pool

    user_id = query.from_user.id
    incorrect_questions_ids = await get_incorrect_questions_for_combined_approach(user_id, pool)

    if incorrect_questions_ids:
        await start_test_with_questions(update, context, incorrect_questions_ids)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=localization[language]['no_questions_to_repeat'])




async def send_question_for_retry_incorrect_question(context, chat_id, question_info, question_number, total_questions):
    language = context.user_data.get('language', 'en')

    question_text = localization[language]['retry_question_prompt'].format(
        number=question_number + 1,
        total=total_questions,
        question=question_info[1]
    )

    image_url = question_info[2]
    options = question_info[3:7]

    keyboard = [InlineKeyboardButton(str(i + 1), callback_data=f"retry_answer_{i + 1}_{question_number}") for i, _ in enumerate(options)]
    reply_markup = InlineKeyboardMarkup([keyboard])

    if image_url:
        try:
            await context.bot.send_photo(chat_id=chat_id, photo=image_url, caption=question_text, reply_markup=reply_markup)
        except Exception as e:
            error_message = localization[language]['error_sending_photo'].format(error=e)
            print(error_message)  # Or log the error using logging framework
            await context.bot.send_message(chat_id=chat_id, text=question_text, reply_markup=reply_markup)
    else:
        await context.bot.send_message(chat_id=chat_id, text=question_text, reply_markup=reply_markup)



async def check_subscribers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Предполагаем, что ADMIN_USER_ID это список ID администраторов
    if update.effective_user.id in ADMIN:
        # Получение пула соединений
        pool = context.bot_data.get('db_pool')
        if not pool:
            pool = await create_pool()
            context.bot_data['db_pool'] = pool

        # Получение количества подписчиков (пример функции, требует реализации)
        subscribers_count = await get_subscribers_count(pool)
        await update.message.reply_text(f"Current number of subscribers: {subscribers_count}")
    else:
        await update.message.reply_text("You do not have permission to use this command.")


async def buy_tugriks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    if query:
        message = query.message
        chat_id = message.chat.id
        message_id = message.message_id
        language = context.user_data.get('language', 'en')  # Defaulting to English

        keyboard = [
            [InlineKeyboardButton("3 Tugrik - $1.00", callback_data='buy_3_1')],
            [InlineKeyboardButton("6 Tugriks - $2.00", callback_data='buy_6_2')],
            [InlineKeyboardButton("12 Tugriks - $3.00", callback_data='buy_12_3')],
            [InlineKeyboardButton(localization[language]['main_menu'], callback_data='main_menu')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=localization[language]['choose_tugriks'],
            reply_markup=reply_markup
        )



async def handle_buy_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    chat_id = query.message.chat_id
    data = query.data.split('_')
    quantity = int(data[1])
    amount_dollars = int(data[2])
    amount_cents = amount_dollars * 100

    language = context.user_data.get('language', 'en')

    title = localization[language]['invoice_title'].format(quantity=quantity)
    description = localization[language]['invoice_description'].format(quantity=quantity, amount=amount_dollars)
    tugrik_label = localization[language]['tugriks_label'].format(quantity=quantity)

    prices = [LabeledPrice(tugrik_label, amount_cents)]

    await context.bot.send_invoice(
        chat_id=chat_id,
        title=title,
        description=description,
        payload="Custom-Payload",
        provider_token=STRIPE_TOKEN,  # Ensure STRIPE_TOKEN is defined somewhere in your settings
        currency="USD",
        prices=prices,
        start_parameter="time-machine-example"
    )


async def successful_payment_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    amount_cents = update.message.successful_payment.total_amount  # Получаем сумму в центах

    amounts_to_tugriks = {
        100: 3,  # $1.00 -> 3 тугрика
        200: 6,  # $2.00 -> 6 тугриков
        300: 12,  # $3.00 -> 12 тугриков
    }

    quantity = amounts_to_tugriks.get(amount_cents, 0)
    language = context.user_data.get('language', 'en')  # Defaulting to English

    if quantity > 0:
        pool = context.bot_data.get('db_pool')
        if not pool:
            pool = await create_pool()  # Создаем пул, если он еще не создан
            context.bot_data['db_pool'] = pool

        await update_user_balance(user_id, quantity, pool)
        thank_you_message = localization[language]['thank_you_purchase'].format(quantity=quantity)
        await context.bot.send_message(chat_id=chat_id, text=thank_you_message)
    else:
        error_message = localization[language]['error_processing_payment']
        await context.bot.send_message(chat_id=chat_id, text=error_message)


async def precheckout_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.pre_checkout_query
    # Здесь можно добавить дополнительные проверки
    await context.bot.answer_pre_checkout_query(pre_checkout_query_id=query.id, ok=True)






def main():
    # Create a connection pool
    pool = db_operations.create_pool()

    # Create the Telegram bot application
    application = Application.builder().token(TOKEN).build()

    application.bot_data['db_pool'] = None
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("add_balance", add_balance))
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(language_callback, pattern='^set_lang_'))
    application.add_handler(CallbackQueryHandler(ces_6_menu_callback, pattern='^ces_6_menu$'))
    register_quiz_handlers(application)

    application.add_handler(CallbackQueryHandler(verify_subscription_callback, pattern='^verify_subscription$'))
    application.add_handler(CallbackQueryHandler(menu_command, pattern='^main_menu$'))
    application.add_handler(CallbackQueryHandler(deck_department_callback, pattern='^deck_department$'))

    application.add_handler(CallbackQueryHandler(engine_department_callback, pattern='^engine_department$'))

    application.add_handler(CallbackQueryHandler(start_test_callback, pattern='^start_test_'))
    application.add_handler(CallbackQueryHandler(handle_answer_callback, pattern='^answer_'))
    application.add_handler(CallbackQueryHandler(personal_account_callback, pattern='^personal_account$'))
    application.add_handler(CallbackQueryHandler(get_referral_link_callback, pattern='^get_referral_link$'))
    application.add_handler(CallbackQueryHandler(buy_tugriks, pattern='^buy_tugriks$'))
    application.add_handler(CallbackQueryHandler(show_balance_callback, pattern='^show_balance$'))
    application.add_handler(CallbackQueryHandler(show_tests_stats_callback, pattern='^show_tests_stats$'))
    application.add_handler(CallbackQueryHandler(retry_incorrect_questions_callback, pattern='^retry_incorrect_questions$'))
    application.add_handler(CallbackQueryHandler(start_callback, pattern='^start$'))
    application.add_handler(CommandHandler("check_subscribers", check_subscribers))
    application.add_handler(CommandHandler('buy_tugriks', buy_tugriks))
    application.add_handler(CallbackQueryHandler(handle_buy_callback, pattern='^buy_'))
    application.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback))
    application.add_handler(PreCheckoutQueryHandler(precheckout_callback))

    application.add_handler(CommandHandler("broadcast", broadcast_command))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo_message))

    application.add_handler(CommandHandler("add_balance", add_balance))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))
    register_handlers(application)


    application.run_polling()

if __name__ == '__main__':
    main()