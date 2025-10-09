# python-telegram-bot==13.7
import os
from datetime import datetime
import sqlite3
from telegram import Update, User, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, Filters, CallbackContext, CommandHandler, MessageHandler


# con = sqlite3.connect('telegram.db')
# cur = con.cursor()
# cur.execute('CREATE TABLE users(tgid, fullname, username)')
# cur.execute('CREATE TABLE logs(tgid, activity, datetime)')
# cur.execute('CREATE TABLE poll(tgid, answer_1, answer_2, answer_3)')
# con.commit()
# con.close()

TOKEN = '8313533739:AAGScIWHySnxNWtYDu8HOgQw863VmSTyQyQ'

poll_button_text = 'Пройти опрос'
poll_button = KeyboardButton(poll_button_text)
result_button_text = 'Мой результат'
result_button = KeyboardButton(result_button_text)
main_menu = ReplyKeyboardMarkup([[poll_button],
                                 [result_button]])
# main_menu_ot = ReplyKeyboardMarkup([[poll_button],
#                                  [result_button]], one_time_keyboard=True)
q1_button_text = 'Имя'
q2_button_text = 'Возраст'
q3_button_text = 'Место'
back_button_text = 'Назад'
poll_menu = ReplyKeyboardMarkup([
    [KeyboardButton(q1_button_text)],
    [KeyboardButton(q2_button_text)],
    [KeyboardButton(q3_button_text)],
    [KeyboardButton(back_button_text)]
], one_time_keyboard=True)

def save_answer(user, question, answer):
    con = sqlite3.connect('telegram.db')
    cur = con.cursor()
    sql = f"UPDATE poll SET answer_{question}='{answer}' WHERE tgid='{user.id}'"
    cur.execute(sql)
    con.commit()
    con.close()

def handle_user(user: User) -> None:
    con = sqlite3.connect('telegram.db')
    cur = con.cursor()
    result = cur.execute(f"SELECT * FROM users WHERE tgid='{user.id}'")
    db_user = result.fetchone()
    if db_user:
        pass
    else:
        cur.execute(f"INSERT INTO users VALUES ('{user.id}', '{user.full_name}', '{user.username}')")
        cur.execute(f"INSERT INTO poll VALUES ('{user.id}', NULL, NULL, NULL)")
        con.commit()
    con.close()

def log_activity(user: User, activity: str) -> None:
    con = sqlite3.connect('telegram.db')
    cur = con.cursor()
    cur.execute(f"INSERT INTO logs VALUES ('{user.id}', '{activity}', '{datetime.now().isoformat()}')")
    con.commit()
    con.close()

def start_command(update: Update, context: CallbackContext):
    user = update.effective_user
    context.user_data['is_polling'] = False
    handle_user(user)
    print(f'{user.full_name} - {user.username} - {user.id}')
    update.message.reply_text(f'Hello, {user.full_name}', reply_markup=main_menu)
    log_activity(user, 'start_command')

def help_command(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    print(f'{user.full_name} - {user.username} - {user.id}')
    log_activity(user, 'help_command')


question_map = {
    1: 'Как тебя зовут?',
    2: 'Сколько лет?',
    3: 'Где живешь?',
}


def poll_main(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    text = f'Давай пройдем опрос'
    update.message.reply_text(text, reply_markup=poll_menu)
    log_activity(user, 'poll started')


def poll_answer(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    q = update.effective_message.text

    context.user_data['is_polling'] = True
    if q == q1_button_text:
        context.user_data['answer_number'] = 1
        update.message.reply_text(question_map[1])
        log_activity(user, 'poll question 1')
    elif q == q2_button_text:
        context.user_data['answer_number'] = 2
        update.message.reply_text(question_map[2])
        log_activity(user, 'poll question 2')
    elif q == q3_button_text:
        context.user_data['answer_number'] = 3
        update.message.reply_text(question_map[3])
        log_activity(user, 'poll question 3')



def result_main(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    text = f'Вот результат твоего опроса'
    update.message.reply_text(text, reply_markup=main_menu)
    log_activity(user, 'poll results requested')

def handle_answer():
    pass

def text_handler(update: Update, context: CallbackContext) -> None:
    user = update.effective_user

    if context.user_data.get('is_polling') == True:
        q = context.user_data.get('answer_number')
        a = update.effective_message.text
        if q:
            save_answer(user, q, a)
            log_activity(user, f'poll answer {q}')
            update.message.reply_text('Ответ записал', reply_markup=poll_menu)
    else:
        text = f'Дорогой, {user.full_name}, я не понял тебя, используй кнопки в меню'
        update.message.reply_text(text, reply_markup=main_menu)
        log_activity(user, 'unknown action')


if __name__ == "__main__":
    updater = Updater(token=TOKEN, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(MessageHandler(Filters.regex(back_button_text) & ~Filters.command, poll_main))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.regex(poll_button_text) & ~Filters.command, poll_main))
    dispatcher.add_handler(MessageHandler(Filters.regex(q1_button_text) & ~Filters.command, poll_answer))
    dispatcher.add_handler(MessageHandler(Filters.regex(q2_button_text) & ~Filters.command, poll_answer))
    dispatcher.add_handler(MessageHandler(Filters.regex(q3_button_text) & ~Filters.command, poll_answer))
    dispatcher.add_handler(MessageHandler(Filters.regex(result_button_text) & ~Filters.command, result_main))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), text_handler))

    updater.start_polling()
    updater.idle()
