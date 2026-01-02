import telebot
from telebot.types import (Message, InlineKeyboardMarkup, InlineKeyboardButton as IB, CallbackQuery)
from database import *
#from config import INTEX
bot = telebot.TeleBot("8166283094:AAHT9WuPORydyj90123EB_inv7dXC0mYQhY")
back = InlineKeyboardMarkup()
back.row(IB(text="Назад к меню⬅", callback_data="back norm"))

back_photo = InlineKeyboardMarkup()
back_photo.row(IB(text="Назад к меню⬅", callback_data="back foto"))

#Клавиатура для меню
main = InlineKeyboardMarkup()
main.row(IB(text="Инструкция по пользованию🔖", callback_data="main noobs"))
main.row(IB(text="Помощь с выбором размера👨‍💻", callback_data="main help"))
main.row(IB(text="Посмотреть размерные таблицы📃", callback_data="main tabs"))
main.row(IB(text="Посмотреть ссылки⚙", callback_data="main links"))

#Клавиатуры с продукцией
prod = InlineKeyboardMarkup()
prod.row(IB(text="Мужские гольфы", callback_data="prod muzh"), IB(text="Женские гольфы", callback_data="prod zhen"))
prod.row(IB(text="Чулки повседневные", callback_data="prod normis"))
prod.row(IB(text="Чулки для широкого бедра", callback_data="prod fat"))
prod.row(IB(text="Чулки для операций/родов", callback_data="prod born"))
prod.row(IB(text="Колготки", callback_data="prod kolgotki"))
prod.row(IB(text="Назад к меню⬅", callback_data="back norm"))

prod2 = InlineKeyboardMarkup()
prod2.row(IB(text="Мужские гольфы", callback_data="prod2 golfm"), IB(text="Женские гольфы", callback_data="prod2 golff"))
prod2.row(IB(text="Чулки повседневные", callback_data="prod2 normis"))
prod2.row(IB(text="Чулки для широкого бедра", callback_data="prod2 fat"))
prod2.row(IB(text="Чулки для операций/родов", callback_data="prod2 born"))
prod2.row(IB(text="Колготки", callback_data="prod2 kolgotki"))
prod2.row(IB(text="Назад к меню⬅", callback_data="back norm"))
prodata = ""


@bot.message_handler(commands=["start"])
def start(message: Message):
    #меню
    bot.send_message(chat_id=message.chat.id, text=f"{message.from_user.first_name}👋, приветствуем вас в "
                                    f"боте-помощнике Интекс, выберите нужное вам действие:\n\n"
    f"Перед началом настоятельно рекомендуем прочитать инструкцию по пользованию😉",
                     reply_markup=main)

@bot.callback_query_handler(func=lambda call:call.data.startswith("back norm"))
def handler(call: CallbackQuery):
    #меню для кнопки назад
    bot.edit_message_text(chat_id=call.message.chat.id, text=f"👇Вы находитесь в главном меню бота, "
                                    f"выберите нужное вам действие:",
                     reply_markup=main, message_id=call.message.id)

@bot.callback_query_handler(func=lambda call:call.data.startswith("back foto"))
def handler_for_photos(call: CallbackQuery):
    bot.send_message(chat_id=call.message.chat.id, text=f"👇Вы находитесь в главном меню бота, "
                                    f"выберите нужное вам действие:", reply_markup=main)


#инструкция
@bot.callback_query_handler(func=lambda call:call.data.startswith("main noobs"))
def handler(call: CallbackQuery):
    bot.send_message(chat_id=call.message.chat.id, reply_markup=back, text=f"👩‍🏫Основная инструкция по пользованию ботом:\n\n1️⃣ Как управлять ботом?"
    f"\nДля перемещения по разделам нажимайте на кнопки под сообщениями, а для вызова меню - нажмите на /start, эта команда также выделена синим цветом.\n"
    f"\n2️⃣ Как использовать помощника по выбору размеров?\nСперва выберите нужный вам товар, а затем после сообщения бота напишите в чат нужный атрибут"
    f" в сантиметрах. Чтобы ваше сообщение распозналось, нужно вводить целое число без пробелов и других символов. Если ваши данные окажутся дробными - округлите их. Во время процесса ввода атрибутов в чат команды не работают."
    f"\n\n3️⃣ Что если бот мне не отвечает?\nЕсть три варианта решения проблемы:\n 1. Ввести команду /start\n 2. Очистить чат и перезапустить бота"
    f"\n 3. Подождать. Проблемы иногда бывают со стороны мессенджера или провайдера, тут вам поможет ожидание.\n\nНадеюсь что данная инструкция ответила на все ваши вопросы😊")

@bot.callback_query_handler(func=lambda call:call.data.startswith("main links"))
def handler(call: CallbackQuery):
    #ссылки
    bot.edit_message_text(chat_id=call.message.chat.id, reply_markup=back, message_id=call.message.id,
        text="⚡Основные ссылки:\nОфициальный сайт: https://bint.ru\nКанал Интекс: https://t.me/tm_intex\n"
             "Менеджер: @alena_intex\nТехподдержка: @Openok89")

@bot.callback_query_handler(func=lambda call:call.data.startswith("main tabs"))
def handler(call: CallbackQuery):
    #выбор изделия для просмотра
    bot.edit_message_text(chat_id=call.message.chat.id, reply_markup=prod, message_id=call.message.id,
        text="Выберите нужное вам изделие👇\n👩‍🏫Чтобы правильно определить нужный размер изделия, сверьтесь с таблицами или "
             "перейдите в раздел помощи в главном меню")

@bot.callback_query_handler(func=lambda call:call.data.startswith("prod "))
def handler(call: CallbackQuery):
    #предоставление самого фото
    action = call.data.split()[1]
    if action == "muzh":
        bot.send_photo(photo=open("man_chulok.jpg", "rb"), chat_id=call.message.chat.id, reply_markup=back_photo,
                       caption="Размерная таблица для мужских гольфов👆")
    elif action == "zhen":
        bot.send_photo(photo=open("woman_chulok.jpg", "rb"), chat_id=call.message.chat.id, reply_markup=back_photo,
                       caption="Размерная таблица для женских гольфов👆")
    elif action == "normis":
        bot.send_photo(photo=open("golf_default.jpg", "rb"), chat_id=call.message.chat.id, reply_markup=back_photo,
                       caption="Размерная таблица для повседневных чулок👆")
    elif action == "fat":
        bot.send_photo(photo=open("golf_thick.jpg", "rb"), chat_id=call.message.chat.id, reply_markup=back_photo,
                       caption="Размерная таблица для чулок c широкой бедренной частью👆")
    elif action == "kolgotki":
        bot.send_photo(photo=open("kolgotki.jpg", "rb"), chat_id=call.message.chat.id, reply_markup=back_photo,
                       caption="Размерная таблица для колготок👆")
    elif action == "born":
        bot.send_photo(photo=open("rodi.jpg", "rb"), chat_id=call.message.chat.id, reply_markup=back_photo,
                       caption="Размерная таблица для чулок для операций/родов👆")



@bot.callback_query_handler(func=lambda call:call.data.startswith("main help"))
def handler(call: CallbackQuery):
    #выбор изделия для подбора размера
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=prod2,
                          text="Выберите нужное вам изделие👇")


#   \\\\\\\\Гольфы/////////
@bot.callback_query_handler(func=lambda call:call.data.startswith("prod2 golf"))
def handlerer(call: CallbackQuery):
    #пошаговый сбор информации
    action = call.data.split()[1]
    if action == "golfm":
        gend = "male"
    elif action == "golff":
        gend = "female"
    global prodata
    prodata = gend
    bot.edit_message_text(message_id=call.message.id, chat_id=call.message.chat.id, text="👩‍🏫Укажите длину окружности вашей лодыжки")
    bot.register_next_step_handler(call.message, handlerer2, gend)
def handlerer2(message: Message, gend):
    ankle = message.text
    if ankle.isdigit():
        bot.send_message(chat_id=message.chat.id, text="👩‍🏫Укажите длину окружности вашей голени")
        bot.register_next_step_handler(message, handlerer3, ankle, gend)
    else:
        bot.send_message(chat_id=message.chat.id, text="Укажите в сообщении целое число без пробелов!")
        bot.register_next_step_handler(message, handlerer2, gend)
def handlerer3(message: Message, ankle, gend):
    shin = message.text
    if shin.isdigit():
        bot.send_message(chat_id=message.chat.id, text="👩‍🏫Укажите размер вашей стопы")
        bot.register_next_step_handler(message, handlerer4, ankle, shin, gend)
    else:
        bot.send_message(chat_id=message.chat.id, text="Укажите в сообщении целое число без пробелов!")
        bot.register_next_step_handler(message, handlerer3, ankle, gend)

def handlerer4(message: Message, ankle, shin, gend):
    feet = message.text
    if feet.isdigit():
        #проблемное место
        #int(shin), int(feet), int(ankle)
        resi = Stockings.get_size(gend, ankle_size=int(ankle), shin_size=int(shin), feet_size=int(feet))
        print(resi)
        if resi[0] == resi[1] == resi[2] and resi[0]:
            if prodata == "male":
                bot.send_message(chat_id=message.chat.id, text=f"📚Результаты подсчитаны!\nНаиболее подходящий для Вас размер"
                f" под мужские гольфы - {resi[0]}.\n🧦Заказать их можно по ссылке:\nhttps://bint.ru/shop/golfy/muzhskie/\nНажмите /start или введите эту команду для вызова меню")
            elif prodata == "female":
                bot.send_message(chat_id=message.chat.id,
                                 text=f"📚Результаты подсчитаны!\nНаиболее подходящий для Вас размер"
                                      f" под женские гольфы - {resi[0]}.\n🧦Заказать их можно по ссылке:\nhttps://bint.ru/shop/golfy/zhenskie-s-zakrytym-noskom/\nНажмите /start или введите эту команду для вызова меню")
        elif resi[0] and resi[1] and resi[2]:
            bot.send_message(chat_id=message.chat.id, text=f"☝️Видимо не все атрибуты попали под один размер, результаты ниже:\n"
            f"1. Размер лодыжки: {resi[0]}\n2. Размер голени: {resi[1]}\n3. Размер стопы: {resi[2]}\nРекомендуем вам взять наименьший размер из предложенных,"
            f" либо безразмерную версию изделия.", reply_markup=back)
        elif not resi[0] or not resi[1] or not resi[2]:
            bot.send_message(chat_id=message.chat.id, reply_markup=back, text="☝️Некоторые из результатов не совпали с размерами, что делать?"
            "\n1. Перепроверить введенные данные, вдруг вы опечатались.\n2. Если данные введены корректно, то можно заказать изделие на заказ, за этим можно"
            " обратиться к менеджеру: @alena_intex; либо можно заказать безразмерную версию изделия на сайте: https://bint.ru/shop/chulki/"
            "\n\n❓Почему так происходит? Числа что вы ввели, либо меньше чем S, либо больше чем XL")
    else:
        bot.send_message(chat_id=message.chat.id, text="Укажите в сообщении целое число без пробелов!")
        bot.register_next_step_handler(message, handler4, ankle, shin, gend)



#   \\\\\\\\Колготки/////////
@bot.callback_query_handler(func=lambda call:call.data.startswith("prod2 kolgotki"))
def handler(call: CallbackQuery):
    #пошаговый сбор информации
    bot.edit_message_text(message_id=call.message.id, chat_id=call.message.chat.id, text="👩‍🏫Укажите длину окружности вашей лодыжки")
    bot.register_next_step_handler(call.message, handler2)
def handler2(message: Message):
    ankle = message.text
    if ankle.isdigit():
        bot.send_message(chat_id=message.chat.id, text="👩‍🏫Укажите длину окружности вашей голени")
        bot.register_next_step_handler(message, handler3, ankle)
    else:
        bot.send_message(chat_id=message.chat.id, text="Укажите в сообщении целое число без пробелов!")
        bot.register_next_step_handler(message, handler2)
def handler3(message: Message, ankle):
    shin = message.text
    if shin.isdigit():
        bot.send_message(chat_id=message.chat.id, text="👩‍🏫Укажите размер вашей стопы")
        bot.register_next_step_handler(message, handler4, ankle, shin)
    else:
        bot.send_message(chat_id=message.chat.id, text="Укажите в сообщении целое число без пробелов!")
        bot.register_next_step_handler(message, handler3, ankle)

def handler4(message: Message, ankle, shin):
    feet = message.text
    if feet.isdigit():
        bot.send_message(chat_id=message.chat.id, text="👩‍🏫Укажите длину окружности верхней части бедра")
        bot.register_next_step_handler(message, handler5, ankle, shin, feet)
    else:
        bot.send_message(chat_id=message.chat.id, text="Укажите в сообщении целое число без пробелов!")
        bot.register_next_step_handler(message, handler4, ankle, shin)

def handler5(message: Message, ankle, shin, feet):
    okr_b = message.text
    if okr_b.isdigit():
        bot.send_message(chat_id=message.chat.id, text="👩‍🏫Укажите длину обхвата бедер")
        bot.register_next_step_handler(message, handler6, ankle, shin, feet, okr_b)
    else:
        bot.send_message(chat_id=message.chat.id, text="Укажите в сообщении целое число без пробелов!")
        bot.register_next_step_handler(message, handler5, ankle, shin, feet)

def handler6(message: Message, ankle, shin, feet, okr_b):
    obhvat_b = message.text
    if obhvat_b.isdigit():
        bot.send_message(chat_id=message.chat.id, text="👩‍🏫Укажите длину обхвата талии")
        bot.register_next_step_handler(message, handler7, ankle, shin, feet, okr_b, obhvat_b)
    else:
        bot.send_message(chat_id=message.chat.id, text="Укажите в сообщении целое число без пробелов!")
        bot.register_next_step_handler(message, handler6, ankle, shin, feet, okr_b)

def handler7(message: Message, ankle, shin, feet, okr_b, obhvat_b):
    obhvat_t = message.text
    if obhvat_t.isdigit():
        gend = "male"
        print(ankle, shin, feet, okr_b, obhvat_b, obhvat_t)
        resi = Tights.getting_size("male",  ankle_size=int(ankle), shin_size=int(shin), feet_size=int(feet), okr_b_size=int(okr_b), obhv_b_size=int(obhvat_b), obhvt_size=int(obhvat_t))
        print(resi)
        print(resi[0], resi[1], resi[2], resi[3], resi[4], resi[5])
        if resi[0] == resi[1] == resi[2] == resi[3] == resi[4] == resi[5] and resi[0]:
            bot.send_message(chat_id=message.chat.id,
                             text=f"📚Результаты подсчитаны!\nНаиболее подходящий для Вас размер"
                                  f" под колготки - {resi[0]}.\n🧦Заказать их можно по ссылке:\nhttps://bint.ru/shop/kolgotki/\nНажмите /start или введите эту команду для вызова меню")
        elif resi[0] and resi[1] and resi[2] and resi[3] and resi[4] and resi[5]:
            bot.send_message(chat_id=message.chat.id,
                             text=f"☝️Видимо не все атрибуты попали под один размер, результаты ниже:\n"
                                  f"1. Размер лодыжки: {resi[0]}\n2. Размер голени: {resi[1]}\n3. Размер стопы: {resi[2]}\n"
            f" 4. Размер окружности бедра: {resi[3]}\n 5. Размер обхвата бедер: {resi[4]}\n"
            f" 6. Размер окружности талии: {resi[5]}\nРекомендуем вам взять наименьший размер из предложенных,"
                                  f" либо безразмерную версию изделия",
                             reply_markup=back)
        elif not resi[0] or not resi[1] or not resi[2] or not resi[3] or not resi[4] or not resi[5]:
            bot.send_message(chat_id=message.chat.id, reply_markup=back,
                             text="☝️Некоторые из результатов не совпали с размерами, что делать?"
            "\n1. Перепроверить введенные данные, вдруг вы опечатались.\n2. Если данные введены корректно, то можно заказать изделие на заказ, за этим можно"
            " обратиться к менеджеру: @alena_intex; либо заказать безразмерную версию изделия на сайте: https://bint.ru/shop/chulki/"
            "\n\n❓Почему так происходит? Числа что вы ввели, либо меньше чем S, либо больше чем XL")
    else:
        bot.send_message(chat_id=message.chat.id, text="Укажите в сообщении целое число без пробелов!")
        bot.register_next_step_handler(message, handler7, ankle, shin, feet, okr_b, obhvat_b)


bot.infinity_polling()