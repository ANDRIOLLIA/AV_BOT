from telebot import *
import sqlite3

current_product_id = 1

token = '7674116155:AAHi_bfHnnmjho00x_Df1LsU3kMNu-kdTeE'
bot = telebot.TeleBot(token)

def get_product_by_id(product_id):
    conn = sqlite3.connect('products.sql')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products WHERE id = ?", (product_id,))
    product = cursor.fetchone()

    cursor.close()
    conn.close()
    return product

def send_product(message):
    global current_product_id
    product = get_product_by_id(current_product_id)

    if product:
        response = f"ID продукта: {product[0]}\n" \
                   f"Название продукта: {product[1]}\n" \
                   f"Описание: {product[2]}\n" \
                   f"Цена: {product[3]}"
    else:
        response = "Список товаров закончился, нажмите кнопку '️⬅️Назад'"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('⬅️Назад')
    next_prod = types.KeyboardButton('Следующий товар➡️')

    markup.add(back).add(next_prod)
    bot.send_message(message.chat.id, response, reply_markup=markup)

def next_product(message):
    global current_product_id
    product = get_product_by_id(current_product_id)

    if product:
        response = f"ID продукта: {product[0]}\n" \
                   f"Название продукта: {product[1]}\n" \
                   f"Описание: {product[2]}\n" \
                   f"Цена: {product[3]}"
    else:
        response = "Список товаров закончился, нажмите кнопку '️⬅️Назад'"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('⬅️Назад')
    next_prod = types.KeyboardButton('Следующий товар➡️')

    markup.add(back).add(next_prod)
    bot.send_message(message.chat.id, response, reply_markup=markup)