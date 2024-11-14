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

ADMIN_IDS = [5242512520]

full_user_order = ''

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

        if message.text == 'Обратная связь☎️':
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

def start_order(message):


    bot.send_message(message.chat.id, 'Введите ваше ФИО!')
    global full_user_order
    full_user_order = 'Ваше ФИО: \n'

    conn = sqlite3.connect('database.sql')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS userOrder (id INTEGER PRIMARY KEY AUTOINCREMENT, full_name TEXT, phone_number TEXT, address TEXT, post_address TEXT)')
    conn.commit()
    cursor.execute('CREATE TABLE IF NOT EXISTS userOrder (id INTEGER PRIMARY KEY AUTOINCREMENT, full_name TEXT, phone_number TEXT, address TEXT, post_address TEXT)')
    conn.commit()
    cursor.close()
    conn.close()

    bot.register_next_step_handler(message, phone_usernumber)

def phone_usernumber(message):
    global user_name
    user_name = message.text.strip()  # Сохраняем ФИО
    bot.send_message(message.chat.id, 'Введите ваш номер телефона!')
    global full_user_order
    full_user_order = 'Ваше ФИО: ' + user_name + '\n'  # Добавляем ФИО в заказ
    bot.register_next_step_handler(message, useraddress)

def useraddress(message):
    global user_phone
    user_phone = message.text.strip()  # Сохраняем номер телефона
    bot.send_message(message.chat.id, 'Введите ваш адрес!')
    global full_user_order
    full_user_order += 'Ваш номер телефона: ' + user_phone + '\n'  # Добавляем номер телефона в заказ
    bot.register_next_step_handler(message, post_useraddress)

def post_useraddress(message):
    global user_address
    user_address = message.text.strip()  # Сохраняем адрес
    bot.send_message(message.chat.id, 'Введите адрес ближайшего почтового отделения!')
    global full_user_order
    full_user_order += 'Ваш адрес: ' + user_address + '\n'  # Добавляем адрес в заказ
    bot.register_next_step_handler(message, final_post_useraddress)

def final_post_useraddress(message):
    global user_post_address
    user_post_address = message.text.strip()  # Сохраняем адрес ближайшего почтового отделения
    global full_user_order
    full_user_order += 'Адрес ближайшего почтового отделения: ' + user_post_address + '\n'  # Добавляем полный заказ

    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()
    cur.execute('INSERT INTO userOrder (full_name, phone_number, address, post_address) VALUES (?, ?, ?, ?)',(user_name, user_phone, user_address, user_post_address))
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, full_user_order)
    bot.send_message('@AndreyTestChat', full_user_order)
    bot.send_message(message.chat.id, 'Ваш заказ успешно оформлен!')
    start(message)


bot.polling(none_stop = True)