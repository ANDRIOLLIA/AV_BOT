import telebot
from telebot import types
import sqlite3

token = '7674116155:AAHi_bfHnnmjho00x_Df1LsU3kMNu-kdTeE'

bot = telebot.TeleBot(token)

user_name = None
user_phone = None
user_address = None
user_post_address = None

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    goods = types.KeyboardButton('Наши товары🛍️')
    feedback = types.KeyboardButton('Обратная связь☎️')
    order1 = types.KeyboardButton('Сделать заказ📦')
    markup.add(goods, feedback,order1)
    bot.send_message(message.chat.id, 'Здравствуйте, рады вас приветствовать в нашем магазине!\nНадеемся, вы подберете что-то для себя!', reply_markup = markup)

@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Обратная связь☎️':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅️Назад')

            markup.add(back)
            bot.send_message(message.chat.id, 'Если у вас есть вопросы или предложения, то вы можете обратиться к ним:\n1.@sddmnx', reply_markup = markup)

        elif message.text == 'Наши товары🛍️':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅️Назад')

            markup.add(back)
            bot.send_message(message.chat.id, 'Наши товары🛍️', reply_markup = markup)

        elif message.text == '⬅️Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            goods = types.KeyboardButton('Наши товары🛍️')
            feedback = types.KeyboardButton('Обратная связь☎️')
            order1 = types.KeyboardButton('Сделать заказ📦')

            markup.add(goods, feedback, order1)
            bot.send_message(message.chat.id,'⬅️Назад',reply_markup=markup)

        if message.text == 'Сделать заказ📦':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Заполните заявку по примеру ниже, указывая свои данные',reply_markup=markup)
            bot.register_next_step_handler(message, start_order)

def start_order(message):
    conn = sqlite3.connect('database.sql')
    cursor = conn.cursor()
    cursor.execute(f'CREATE TABLE IF NOT EXISTS userOrder (id int auto_increment primary key, full_name VARCHAR(50), phone_number VARCHAR(20), address VARCHAR(30), post_address VARCHAR(30))')
    conn.commit()
    cursor.close()
    conn.close()
    global user_name
    bot.send_message(message.chat.id, 'Введите ваше ФИО!')
    user_name = message.text.strip()
    bot.register_next_step_handler(message, phone_usernumber)

def phone_usernumber(message):
    global user_phone
    bot.send_message(message.chat.id, 'Введите ваш номер телефона!')
    user_phone = message.text.strip()
    bot.register_next_step_handler(message, useraddress)

def useraddress(message):
    global user_address
    bot.send_message(message.chat.id, 'Введите ваш адрес!')
    user_address = message.text.strip()
    bot.register_next_step_handler(message, post_useraddress)

def post_useraddress(message):
    global user_post_address
    bot.send_message(message.chat.id, 'Введите адрес ближайшего почтового отделения!')
    user_post_address = message.text.strip()
    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()
    cur.execute(f'INSERT INTO userOrder (full_username, phone_usernumber, useraddress, post_useradress) VALUES ("%s", "%s", "%s", "%s") % (user_name, user_phone, user_address, user_post_address)')
    conn.commit()
    cur.close()
    conn.close()
    start()

        # elif message.text != all_names.all_list:
        #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #     bot.forward_message(chat_id='@AndreyTestChat', from_chat_id=message.chat.id, message_id=message.id)
        #     bot.send_message(message.chat.id, 'Спасибо за заказ! Скоро с вами свяжется администратор магазина!', reply_markup=markup)


bot.polling(none_stop = True)