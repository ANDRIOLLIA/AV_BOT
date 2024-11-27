from telebot import *
import sqlite3
current_product_id = 1

token = '7674116155:AAHi_bfHnnmjho00x_Df1LsU3kMNu-kdTeE'
bot = telebot.TeleBot(token)

def get_product_by_id(product_id):
    conn = sqlite3.connect('products.sql')
    cursor = conn.cursor()

    # SQL-запрос для получения продукта по id
    cursor.execute("SELECT * FROM Products WHERE id = ?", (product_id,))

    # Получаем результат
    product = cursor.fetchone()

    cursor.close()
    conn.close()
    return product



def send_product(message):
    global current_product_id  # Используем глобальную переменную

    # Получаем информацию о продукте из базы данных
    product = get_product_by_id(current_product_id)

    if product:
        # Отправляем пользователю информацию о продукте
        response = f"ID продукта: {product[0]}\n" \
                   f"Название продукта: {product[1]}\n" \
                   f"Описание: {product[2]}\n" \
                   f"Цена: {product[3]}"
    else:
        response = f"Продукт с id {current_product_id} не найден."

    # Создаем клавиатуру с кнопками
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('⬅️Назад')
    next_prod = types.KeyboardButton('Следующий товар➡️')

    markup.add(back).add(next_prod)

    # Отправляем ответ с клавиатурой
    bot.send_message(message.chat.id, response, reply_markup=markup)


# Обработчик нажатия на кнопку "Следующий товар"
@bot.message_handler(func=lambda message: message.text == 'Следующий товар➡️')
def next_product(message):
    global current_product_id

    # Увеличиваем ID для следующего товара
    current_product_id += 1

    # Получаем информацию о следующем продукте
    product = get_product_by_id(current_product_id)

    if product:
        # Отправляем информацию о следующем продукте
        response = f"ID продукта: {product[0]}\n" \
                   f"Название продукта: {product[1]}\n" \
                   f"Описание: {product[2]}\n" \
                   f"Цена: {product[3]}"
    else:
        response = f"Продукт с id {current_product_id} не найден."

    # Создаем клавиатуру для следующего товара
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('⬅️Назад')
    next_prod = types.KeyboardButton('Следующий товар➡️')

    markup.add(back).add(next_prod)

    # Отправляем информацию с клавиатурой
    bot.send_message(message.chat.id, response, reply_markup=markup)