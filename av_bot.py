import telebot
from telebot import types
import sqlite3

token = '7674116155:AAHi_bfHnnmjho00x_Df1LsU3kMNu-kdTeE'
bot = telebot.TeleBot(token)

user_name = None
user_phone = None
user_address = None
user_post_address = None
ordi = None
is_ordering = False


user_id = None

ADMIN_IDS = [5242512520]

DEFAULT_BUTTONS = ['Наши товары🛍️','Обратная связь☎️','Сделать заказ📦','⬅️Назад', 'Ошибка❌']

ADM_BUTTONS = ['Наши товары🛍️','Обратная связь☎️','Сделать заказ📦','⬅️Назад', 'AdM PaNeI_❌', 'Добавить товар🛍️', 'Удалить товар❌', 'Ошибка❌']

full_user_order = ''

@bot.message_handler(commands = ['admin_panel'])
def admin(message):
    if message.chat.id in ADMIN_IDS:
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        adm = types.KeyboardButton('AdM PaNeI_❌')
        markup.add(adm)
        bot.send_message(message.chat.id, 'You are admin!', reply_markup = markup)
    else:
        bot.send_message(message.chat.id, "You aren't admin")
        start(message)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    goods = types.KeyboardButton('Наши товары🛍️')
    feedback = types.KeyboardButton('Обратная связь☎️')
    order1 = types.KeyboardButton('Сделать заказ📦')
    adm = types.KeyboardButton('AdM PaNeI_❌')
    if message.chat.id in ADMIN_IDS:
        markup.add(goods, feedback, order1, adm)
    else:
        markup.add(goods, feedback, order1)

    bot.send_message(message.chat.id,'Здравствуйте, рады вас приветствовать в нашем магазине!\nНадеемся, вы подберете что-то для себя!',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        global user_id
        user_id = message.from_user.username #username - то, что идет после "@"
        if message.text not in DEFAULT_BUTTONS:
            if message.chat.id not in ADMIN_IDS:
                bot.send_message(message.chat.id, 'Ошибка❌')

        if message.text not in ADM_BUTTONS:
            if message.chat.id in ADMIN_IDS:
                bot.send_message(message.chat.id, 'Ошибка❌')

        if message.text == 'AdM PaNeI_❌':
            if message.chat.id in ADMIN_IDS:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                add_goods = types.KeyboardButton('Добавить товар🛍️')
                delete_goods = types.KeyboardButton('Удалить товар❌')
                back = types.KeyboardButton('⬅️Назад')
                markup.add(add_goods).add(delete_goods).add(back)
                bot.send_message(message.chat.id, 'AdM PaNeI_❌', reply_markup=markup)

            else:
                bot.send_message(message.chat.id, 'Ошибка!')
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                goods = types.KeyboardButton('Наши товары🛍️')
                feedback = types.KeyboardButton('Обратная связь☎️')
                order1 = types.KeyboardButton('Сделать заказ📦')
                markup.add(goods, feedback, order1)

        elif message.text == 'Обратная связь☎️':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅️Назад')
            markup.add(back)
            bot.send_message(message.chat.id,'Если у вас есть вопросы или предложения, то вы можете обратиться к ним:\n1.@sddmnx',reply_markup=markup)

        elif message.text == 'Наши товары🛍️':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅️Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Наши товары🛍️', reply_markup=markup)

        elif message.text == '⬅️Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            goods = types.KeyboardButton('Наши товары🛍️')
            feedback = types.KeyboardButton('Обратная связь☎️')
            order1 = types.KeyboardButton('Сделать заказ📦')
            markup.add(goods, feedback, order1)
            bot.send_message(message.chat.id, '⬅️Назад', reply_markup = markup)

        elif message.text == 'AdM PaNeI_❌':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            add_goods = types.KeyboardButton('Добавить товар🛍️')
            delete_goods = types.KeyboardButton('Удалить товар❌')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(add_goods).add(delete_goods).add(back)
            bot.send_message(message.chat.id, 'AdM PaNeI_❌', reply_markup = markup)

        elif message.text == 'Сделать заказ📦':
            bot.send_message(message.chat.id, 'Сделать заказ📦')
            start_order(message)
        elif is_ordering and message.text == '🛑 Отмена':
            cancel_order(message)

# НАЧАЛО СОЗДАНИЯ ЗАКАЗА
def start_order(message):
    global is_ordering
    is_ordering = True

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cancel_button = types.KeyboardButton('🛑 Отмена')
    markup.add(cancel_button)

    bot.send_message(message.chat.id, 'Введите ваше ФИО!', reply_markup=markup)
    global full_user_order
    full_user_order = 'Ваше ФИО: \n'
    bot.register_next_step_handler(message, add_user_name)

def cancel_order(message):
    global is_ordering
    is_ordering = False
    bot.send_message(message.chat.id,'Создание заказа отменено!')
    start(message)

def add_user_name(message):
    global user_name
    if not is_ordering:
        return

    if message.text == '🛑 Отмена':
        cancel_order(message)
        return

    user_name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите ваш номер телефона!')
    global full_user_order
    full_user_order = 'Ваше ФИО: ' + user_name + '\n'
    bot.register_next_step_handler(message, add_user_phone)


def add_user_phone(message):
    if not is_ordering:
        return

    if message.text == '🛑 Отмена':
        cancel_order(message)
        return

    global user_phone
    user_phone = message.text.strip()
    global full_user_order
    full_user_order += 'Ваш номер телефона: ' + user_phone + '\n'
    bot.send_message(message.chat.id, 'Введите ваш адрес!')
    bot.register_next_step_handler(message, add_user_address)

def add_user_address(message):
    if not is_ordering:
        return

    if message.text == '🛑 Отмена':
        cancel_order(message)
        return

    global user_address
    user_address = message.text.strip()
    global full_user_order
    full_user_order += 'Ваш адрес: ' + user_address + '\n'
    bot.send_message(message.chat.id, 'Введите адрес ближайшего почтового отделения!')
    bot.register_next_step_handler(message, add_user_post_address)

def add_user_post_address(message):
    global is_ordering
    if not is_ordering:
        return

    if message.text == '🛑 Отмена':
        cancel_order(message)
        return

    global user_post_address
    user_post_address = message.text.strip()
    global full_user_order
    full_user_order += 'Адрес ближайшего почтового отделения: ' + user_post_address + '\n'

    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()
    cur.execute('INSERT INTO userOrder (full_name, phone_number, address, post_address) VALUES (?, ?, ?, ?)',
                (user_name, user_phone, user_address, user_post_address))
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, full_user_order)
    bot.send_message(message.chat.id, 'Ваш заказ успешно оформлен!')
    is_ordering = False
    start(message)

bot.polling(none_stop=True)