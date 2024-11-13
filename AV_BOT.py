from telebot import types
import telebot

import all_names

token = '7522613800:AAEqiD1x5eL1XwI2zhIzAU4_VlRoW5CvsmE'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Наши товары🧣')
    item2 = types.KeyboardButton('Обратная связь☎️')
    item3 = types.KeyboardButton('Мы во ВКонтакте💬')
    item4 = types.KeyboardButton('Оставить отзыв📝')
    item5 = types.KeyboardButton('Задонатить нам💵')

    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, 'Здравствуйте, рады вас приветствовать в нашем магазине!\nНадеемся, вы подберете что-то для себя!', reply_markup = markup)
    bot.send_message(message.chat.id, '❗️Предупреждение❗️\nПеред покупкой советуем ознакомиться с нашими правилами сообщества, найти их вы можете по кнопке "Мы во ВКонтакте💬"\nВ боте представлены не все цвета одежды, которые есть в нашем каталоге.\n Так же важно отметить, что бот находится на стадии разработки, и в нем возможны баги =)')

@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Обратная связь☎️':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅️Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Если у вас есть вопросы или предложения, то вы можете обратиться к ним:\n1.@sddmnx\n2.@Prince_of_halfblood', reply_markup = markup)

        elif message.text == 'Мы во ВКонтакте💬':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅️Назад')
            markup.add(back)

            bot.send_message(message.chat.id,'Наше сообщество во Вконтакте:\nhttps://vk.com/affordableandvaluable',reply_markup=markup)

        elif message.text == 'Оставить отзыв📝':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅️Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Отзывы пока в разработке', reply_markup=markup)

        elif message.text == 'Задонатить нам💵':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅️Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Большое спасибо! Можете скинуть нам любую сумму, мы будем очень рады вашей поддержке!\n2202 2067 8753 2618 - Сбер =)', reply_markup=markup)

        elif message.text == 'Наши товары🧣':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Женская одежда👗')
            # item2 = types.KeyboardButton('Мужская одежда👔')
            # item3 = types.KeyboardButton('Обувь👟')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(item1).add(back)
            # Добавить в markup item2, item3 после того, как появится обувь и мужская одежда
            bot.send_message(message.chat.id, 'Наши товары🧣', reply_markup = markup)

        elif message.text == 'Женская одежда👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Платья👗')
            item2 = types.KeyboardButton('Юбки👗')
            item3 = types.KeyboardButton('Рубашки и блузки👔')
            item4 = types.KeyboardButton('Костюмы и пиджаки👔')
            item5 = types.KeyboardButton('Брюки👖')
            item6 = types.KeyboardButton('Свитеры и кардиганы🧥')
            item7 = types.KeyboardButton('Прочее🔄')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, back)

            bot.send_message(message.chat.id, 'Женская одежда👗', reply_markup=markup)

        # elif message.text == 'Мужская одежда👔':
        #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #     back = types.KeyboardButton('⬅️Назад')
        #     markup.add(back)
        #
        #     bot.send_message(message.chat.id, 'К сожалению в каталоге мужской одежды пока нет =(', reply_markup=markup)
        #
        # elif message.text == 'Обувь👟':
        #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #     back = types.KeyboardButton('⬅️Назад')
        #     markup.add(back)
        #
        #     bot.send_message(message.chat.id,'К сожалению в каталоге обуви пока нет =(', reply_markup=markup)

        elif message.text == '⬅️Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Наши товары🧣')
            item2 = types.KeyboardButton('Обратная связь☎️')
            item3 = types.KeyboardButton('Мы во ВКонтакте💬')
            item4 = types.KeyboardButton('Оставить отзыв📝')
            item5 = types.KeyboardButton('Задонатить нам💵')

            markup.add(item1, item2, item3, item4, item5)
            bot.send_message(message.chat.id,'⬅️Назад',reply_markup=markup)

        elif message.text == 'Платья👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Второе платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Первое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/1.jpg', 'rb')
            bot.send_photo(message.chat.id, photo,caption='Платье\n4 390 ₽\nАртикул 631\nОписание\n-Цвета: голубой, бежевый\n-Размеры: XS, S, M, L, XL\n-Ткань: 20% вискоза, 80% полиэстер')

        elif message.text == 'Второе платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Третье платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Второе платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/2.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='уооууоуоуоуо')

        elif message.text == 'Третье платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Четвертое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Третье платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/3.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='ахпахпахпахпапх')

        elif message.text == 'Четвертое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Пятое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Четвертое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/4.jpg', 'rb')
            bot.send_photo(message.chat.id, photo,caption='въахпъвахпъвапхваъпхваъпхвап')

        elif message.text == 'Пятое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Шестое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Пятое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/5.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='уооууоуоуоуо')

        elif message.text == 'Шестое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Седьмое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Шестое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/6.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='ахпахпахпахпапх')

        elif message.text == 'Седьмое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Восьмое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Седьмое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/7.jpg', 'rb')
            bot.send_photo(message.chat.id, photo,caption='въахпъвахпъвапхваъпхваъпхвап')

        elif message.text == 'Восьмое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Девятое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Восьмое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/8.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='уооууоуоуоуо')

        elif message.text == 'Девятое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Десятое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Девятое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/9.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='ахпахпахпахпапх')

        elif message.text == 'Десятое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Одиннадцатое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Десятое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/10.jpg', 'rb')
            bot.send_photo(message.chat.id, photo,caption='въахпъвахпъвапхваъпхваъпхвап')

        elif message.text == 'Одиннадцатое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Двенадцатое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Одиннадцатое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/11.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='уооууоуоуоуо')

        elif message.text == 'Двенадцатое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Тринадцатое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Двенадцатое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/12.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='ахпахпахпахпапх')

        elif message.text == 'Тринадцатое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Четырнадцатое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Тринадцатое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/13.jpg', 'rb')
            bot.send_photo(message.chat.id, photo,caption='въахпъвахпъвапхваъпхваъпхвап')

        elif message.text == 'Четырнадцатое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Пятнадцатое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Четырнадцатое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/14.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='уооууоуоуоуо')

        elif message.text == 'Пятнадцатое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Шестнадцатое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Пятнадцатое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/15.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='ахпахпахпахпапх')

        elif message.text == 'Шестнадцатое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Семнадцатое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Шестнадцатое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/16.jpg', 'rb')
            bot.send_photo(message.chat.id, photo,caption='въахпъвахпъвапхваъпхваъпхвап')

        elif message.text == 'Семнадцатое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Восемнадцатое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Семнадцатое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/17.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='уооууоуоуоуо')

        elif message.text == 'Восемнадцатое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Девятнадцатое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Восемнадцатое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/18.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='ахпахпахпахпапх')

        elif message.text == 'Девятнадцатое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Двадцатое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Девятнадцатое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/19.jpg', 'rb')
            bot.send_photo(message.chat.id, photo,caption='въахпъвахпъвапхваъпхваъпхвап')

        elif message.text == 'Двадцатое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Двадцать первое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Двадцатое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/20.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='уооууоуоуоуо')

        elif message.text == 'Двадцать первое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Двадцать второе платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Двадцать первое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/21.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='ахпахпахпахпапх')

        elif message.text == 'Двадцать второе платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Двадцать третье платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Двадцать второе платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/22.jpg', 'rb')
            bot.send_photo(message.chat.id, photo,caption='въахпъвахпъвапхваъпхваъпхвап')

        elif message.text == 'Двадцать третье платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Двадцать четвертое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Двадцать третье платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/23.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='уооууоуоуоуо')

        elif message.text == 'Двадцать четвертое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Двадцать пятое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Двадцать четвертое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/24.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='ахпахпахпахпапх')

        elif message.text == 'Двадцать пятое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Двадцать шестое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Двадцать пятое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/25.jpg', 'rb')
            bot.send_photo(message.chat.id, photo,caption='въахпъвахпъвапхваъпхваъпхвап')

        elif message.text == 'Двадцать шестое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Двадцать седьмое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Двадцать шестое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/26.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='уооууоуоуоуо')

        elif message.text == 'Двадцать седьмое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Двадцать восьмое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Двадцать седьмое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/27.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='ахпахпахпахпапх')

        elif message.text == 'Двадцать восьмое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Двадцать девятое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Двадцать восьмое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/28.jpg', 'rb')
            bot.send_photo(message.chat.id, photo,caption='въахпъвахпъвапхваъпхваъпхвап')

        elif message.text == 'Двадцать девятое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Тридцатое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Двадцать девятое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/29.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='уооууоуоуоуо')

        elif message.text == 'Тридцатое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Тридцать первое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Тридцатое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/30.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='ахпахпахпахпапх')

        elif message.text == 'Тридцать первое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Тридцать второе платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Тридцать первое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/31.jpg', 'rb')
            bot.send_photo(message.chat.id, photo,caption='въахпъвахпъвапхваъпхваъпхвап')

        elif message.text == 'Тридцать второе платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Тридцать третье платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Тридцать второе платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/32.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='уооууоуоуоуо')

        elif message.text == 'Тридцать третье платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Тридцать четвертое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Тридцать третье платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/33.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='ахпахпахпахпапх')

        elif message.text == 'Тридцать четвертое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Тридцать пятое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Тридцать четвертое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/34.jpg', 'rb')
            bot.send_photo(message.chat.id, photo,caption='въахпъвахпъвапхваъпхваъпхвап')

        elif message.text == 'Тридцать пятое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Тридцать шестое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Тридцать пятое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/35.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='уооууоуоуоуо')

        elif message.text == 'Тридцать шестое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Тридцать седьмое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Тридцать шестое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/36.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='ахпахпахпахпапх')

        elif message.text == 'Тридцать седьмое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Тридцать восьмое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Тридцать седьмое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/37.jpg', 'rb')
            bot.send_photo(message.chat.id, photo,caption='въахпъвахпъвапхваъпхваъпхвап')

        elif message.text == 'Тридцать восьмое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Тридцать девятое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Тридцать восьмое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/38.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='уооууоуоуоуо')

        elif message.text == 'Тридцать девятое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Сороковое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Тридцать девятое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/39.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='ахпахпахпахпапх')

        elif message.text == 'Сороковое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Сорок первое платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Сороковое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/40.jpg', 'rb')
            bot.send_photo(message.chat.id, photo,caption='въахпъвахпъвапхваъпхваъпхвап')

        elif message.text == 'Сорок первое платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            skip_prod = types.KeyboardButton('Сорок второе платье👗')
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(skip_prod).add(order, back)
            bot.send_message(message.chat.id, 'Сорок первое платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/41.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='уооууоуоуоуо')

        elif message.text == 'Сорок второе платье👗':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            order = types.KeyboardButton('Сделать заказ📦')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(order, back)
            bot.send_message(message.chat.id, 'Сорок второе платье👗', reply_markup=markup)
            photo = open('E:/AV_BOT/photos/dress/42.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption='уооууоуоуоуо')

        elif message.text == 'Сделать заказ📦':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            mes = 'Заполните заявку по примеу ниже, указывая свои данные\n1.Ваш юзернейм в телеграм\номер телефона\n2.Артикул товара\n3.Цвет\n4.Размер\n5.Количество товара\n6.Ваш адрес'
            bot.send_message(message.chat.id, mes,reply_markup=markup)

        elif message.text != all_names.all_list:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.forward_message(chat_id='@avshopadmins', from_chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, 'Спасибо за заказ! Скоро с вами свяжется администратор магазина!', reply_markup=markup)


bot.polling(none_stop = True)