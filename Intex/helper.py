import telebot
from telebot.types import (Message, InlineKeyboardMarkup, InlineKeyboardButton as IB, CallbackQuery)
from database import Stockings
#from config import INTEX
#from data_intex import Women, session
bot = telebot.TeleBot("8166283094:AAHT9WuPORydyj90123EB_inv7dXC0mYQhY")
back = InlineKeyboardMarkup()
back.row(IB(text="Назад к меню⬅", callback_data="back norm"))

back_photo = InlineKeyboardMarkup()
back_photo.row(IB(text="Назад к меню⬅", callback_data="back foto"))

#Клавиатура для меню
main = InlineKeyboardMarkup()
main.row(IB(text="Посмотреть ссылки⚙", callback_data="main links"))
main.row(IB(text="Посмотреть размерные таблицы📃", callback_data="main tabs"))
main.row(IB(text="Помощь в выбором размера👨‍💻", callback_data="main help"))

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
                                    f"боте-помошнике Интекс, выберите нужное вам действие:\nДля того чтобы вернуться"
                        f" в главное меню, используйте кнопку НАЗАД, либо нажмите на /start",
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
        text="Выберите нужное вам изделие👇\n👩‍🏫Чтобы правильно определить нужный вид чулков, сверьтесь с таблицами, или "
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
def handler(call: CallbackQuery):
    #пошаговый сбор информации
    action = call.data.split()[1]
    print(action)
    if action == "golfm":
        gend = "male"
    elif action == "golff":
        gend = "female"
    global prodata
    prodata = gend
    print(prodata)
    bot.edit_message_text(message_id=call.message.id, chat_id=call.message.chat.id, text="Укажите длину окружности вашей лодыжки")
    bot.register_next_step_handler(call.message, handler2, gend)
def handler2(message: Message, gend):
    ankle = message.text
    if ankle.isdigit():
        bot.send_message(chat_id=message.chat.id, text="Укажите длину окружности вашей голени")
        bot.register_next_step_handler(message, handler3, ankle, gend)
    else:
        bot.send_message(chat_id=message.chat.id, text="Укажите в сообщении целое число без пробелов!")
        bot.register_next_step_handler(message, handler2, gend)
def handler3(message: Message, ankle, gend):
    shin = message.text
    if shin.isdigit():
        bot.send_message(chat_id=message.chat.id, text="Укажите длину окружности вашей стопы")
        bot.register_next_step_handler(message, handler4, ankle, shin, gend)
    else:
        bot.send_message(chat_id=message.chat.id, text="Укажите в сообщении целое число без пробелов!")
        bot.register_next_step_handler(message, handler3, ankle, gend)

def handler4(message: Message, ankle, shin, gend):
    feet = message.text
    if feet.isdigit():
        #проблемное место
        #int(shin), int(feet), int(ankle)
        resi = Stockings.get_size(gend, int(ankle), int(shin), int(feet))
        print(resi)
        if resi[0] == resi[1] == resi[2]:
            if prodata == "male":
                bot.send_message(chat_id=message.chat.id, text=f"📚Результаты подсчитаны!\nНаиболее подходящий для Вас размер"
                f" под мужские гольфы - {resi[0]}.\nЗаказать их можно по ссылке:\nhttps://bint.ru/shop/golfy/muzhskie/")
            elif prodata == "female":
                bot.send_message(chat_id=message.chat.id,
                                 text=f"📚Результаты подсчитаны!\nНаиболее подходящий для Вас размер"
                                      f" под женские гольфы - {resi[0]}.\nЗаказать их можно по ссылке:\nhttps://bint.ru/shop/golfy/zhenskie-s-zakrytym-noskom/")
    else:
        bot.send_message(chat_id=message.chat.id, text="Укажите в сообщении целое число без пробелов!")
        bot.register_next_step_handler(message, handler4, ankle, shin, gend)


bot.infinity_polling()