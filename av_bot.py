import telebot
from telebot import types
# import sqlite3

import dbs
from dbs import *

import administrator
from administrator import *

import next_button

token = '7674116155:AAHi_bfHnnmjho00x_Df1LsU3kMNu-kdTeE'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['admin_panel'])
def admin(message):
    if message.chat.id in ADMIN_IDS:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        adm = types.KeyboardButton('AdM PaNeI_❌')
        markup.add(adm)
        bot.send_message(message.chat.id, 'Вы Админ!', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Вы не Админ!')
        start(message)

@bot.message_handler(func=lambda message: message.text == 'Добавить товар🛍️')
def new_item(message):
    if message.chat.id in ADMIN_IDS:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('⬅️Назад')
        markup.add(back)
        bot.send_message(message.chat.id, 'Добавление товара🛍️')
        init_product_db()
        start_creation_product(message)
    else:
        bot.send_message(message.chat.id, 'Ошибка❌')
        start(message)

def start_creation_product(message):
    bot.send_message(message.chat.id, 'Введите название товара!')
    bot.register_next_step_handler(message, add_product_name)

def add_product_name(message):
    administrator.product_name = message.text.strip()
    administrator.full_product += 'Название: ' + administrator.product_name + '\n'
    bot.send_message(message.chat.id, 'Введите описание товара!')
    bot.register_next_step_handler(message, add_product_description)

def add_product_description(message):
    administrator.product_description = message.text.strip()
    administrator.full_product += 'Описание: ' + administrator.product_description + '\n'
    bot.send_message(message.chat.id, 'Введите цену товара')
    bot.register_next_step_handler(message, add_product_price)

def add_product_price(message):
    administrator.product_price = message.text.strip()
    administrator.full_product += 'Цена: ' + administrator.product_price + '\n'
    conn = sqlite3.connect('products.sql')
    cur = conn.cursor()
    cur.execute('INSERT INTO Products '
                '(prod_name, '
                'description,'
                'price) '
                'VALUES (?, ?, ?)',
                (administrator.product_name,
                administrator.product_description,
                administrator.product_price))
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Товар добавлен!')
    bot.send_message(message.chat.id, administrator.full_product)


user_states = {}


@bot.message_handler(commands=['delete'])
def start_delete(message):
    user_states[message.chat.id] = 'awaiting_id'
    bot.send_message(message.chat.id, 'Введите артикул товара (Столбец ID в базе данных):')


@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'awaiting_id')
def delete_product(message):
    delete_id = message.text.strip()
    conn = sqlite3.connect('products.sql')
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM products WHERE id = ?", (delete_id,))
        conn.commit()
        bot.send_message(message.chat.id, 'Товар удален!')
    except sqlite3.Error as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")
    finally:
        cur.close()
        conn.close()

    # Убираем состояние пользователя после обработки запроса
    del user_states[message.chat.id]


@bot.message_handler(func=lambda message: message.text == 'Да✅')
def yes(message):
    start_order(message)

@bot.message_handler(func=lambda message: message.text == 'Следующий товар➡️')
def next_product_button(message):
    next_button.current_product_id += 1
    next_button.next_product(message)

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

    bot.send_message(message.chat.id, 'Здравствуйте, рады вас приветствовать в нашем магазине!\nНадеемся, вы подберете что-то для себя!', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        administrator.user_id = message.from_user.username  # username - то, что идет после "@"
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
                markup.add(add_goods, delete_goods).add(back)
                bot.send_message(message.chat.id, 'AdM PaNeI_❌', reply_markup=markup)

            else:
                bot.send_message(message.chat.id, 'Ошибка!')
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                goods = types.KeyboardButton('Наши товары🛍️')
                feedback = types.KeyboardButton('Обратная связь☎️')
                order1 = types.KeyboardButton('Сделать заказ📦')
                markup.add(goods, feedback, order1)

        elif message.text == 'Добавить товар🛍️':
            new_item(message)

        elif message.text == 'Обратная связь☎️':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅️Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Если у вас есть вопросы или предложения, то вы можете обратиться к ним:\n1.@sddmnx', reply_markup=markup)

        elif message.text == 'Наши товары🛍️':
            next_button.send_product(message)

        elif message.text == '⬅️Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            goods = types.KeyboardButton('Наши товары🛍️')
            feedback = types.KeyboardButton('Обратная связь☎️')
            order1 = types.KeyboardButton('Сделать заказ📦')
            markup.add(goods, feedback, order1)
            if message.chat.id in ADMIN_IDS:
                adm = types.KeyboardButton('AdM PaNeI_❌')
                markup.add(adm)
            bot.send_message(message.chat.id, '⬅️Назад', reply_markup=markup)

        elif message.text == 'Сделать заказ📦':
            bot.send_message(message.chat.id, 'Сделать заказ📦')
            start_order(message)

        elif administrator.is_ordering and message.text == '🛑 Отмена':
            cancel(message)

# НАЧАЛО СОЗДАНИЯ ЗАКАЗА
def start_order(message):
    administrator.is_ordering = True

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cancel_button = types.KeyboardButton('🛑 Отмена')
    markup.add(cancel_button)

    bot.send_message(message.chat.id, 'Введите ваше ФИО!', reply_markup=markup)
    administrator.full_user_order += 'Ваше ФИО: \n'
    bot.register_next_step_handler(message, add_user_name)

def cancel(message):
    administrator.is_ordering = False
    bot.send_message(message.chat.id, 'Отменено!')
    start(message)

def add_user_name(message):
    if not administrator.is_ordering:
        return

    if message.text == '🛑 Отмена':
        cancel(message)
        return

    administrator.user_name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите ваш номер телефона!')
    administrator.full_user_order = 'Ваше ФИО: ' + administrator.user_name + '\n'
    bot.register_next_step_handler(message, add_user_phone)

def add_user_phone(message):
    if not administrator.is_ordering:
        return

    if message.text == '🛑 Отмена':
        cancel(message)
        return

    administrator.user_phone = message.text.strip()
    administrator.full_user_order += 'Ваш номер телефона: ' + administrator.user_phone + '\n'
    bot.send_message(message.chat.id, 'Введите ваш адрес!')
    bot.register_next_step_handler(message, add_user_address)

def add_user_address(message):
    if not administrator.is_ordering:
        return

    if message.text == '🛑 Отмена':
        cancel(message)
        return

    administrator.user_address = message.text.strip()
    administrator.full_user_order += 'Ваш адрес: ' + administrator.user_address + '\n'
    bot.send_message(message.chat.id, 'Введите адрес ближайшего почтового отделения!')
    bot.register_next_step_handler(message, add_user_post_address)

def add_user_post_address(message):
    if not administrator.is_ordering:
        return

    if message.text == '🛑 Отмена':
        cancel(message)
        return

    administrator.user_post_address = message.text.strip()
    administrator.full_user_order += 'Адрес ближайшего почтового отделения: ' + administrator.user_post_address + '\n'

    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()
    cur.execute('INSERT INTO userOrder (full_name, phone_number, address, post_address) VALUES (?, ?, ?, ?)',(administrator.user_name, administrator.user_phone, administrator.user_address, administrator.user_post_address))
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, administrator.full_user_order)
    bot.send_message('@AndreyTestChat', 'Тег пользователя: @' + administrator.user_id + '\n' + administrator.full_user_order)
    bot.send_message(message.chat.id, 'Ваш заказ успешно оформлен!')
    administrator.is_ordering = False
    start(message)

dbs.init_user_order_db()
bot.polling(none_stop=True)