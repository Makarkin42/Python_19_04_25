import telebot
from telebot.types import (Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery)
from config import GIFT
bot = telebot.TeleBot(GIFT)
points = 0

#1 - год рождения 69, 2 - год свадьбы 88, город детства, девичья фамилия, любимый внук!!!!!!

nach = InlineKeyboardMarkup()
nach.row(InlineKeyboardButton("Начать", callback_data="starts"))

one = InlineKeyboardMarkup()
one.row(InlineKeyboardButton("1966", callback_data="мем 1 66"),
        InlineKeyboardButton("1969", callback_data="мем 1 69"))
one.row(InlineKeyboardButton("1971", callback_data="мем 1 71"),
        InlineKeyboardButton("1974", callback_data="мем 1 74"))

two = InlineKeyboardMarkup()
two.row(InlineKeyboardButton("1988", callback_data="мем 2 88"),
        InlineKeyboardButton("1990", callback_data="мем 2 69"))
two.row(InlineKeyboardButton("1991", callback_data="мем 2 71"),
        InlineKeyboardButton("1993", callback_data="мем 2 74"))

tre = InlineKeyboardMarkup()
tre.row(InlineKeyboardButton("Волгоград", callback_data="мем 3 волг"),
        InlineKeyboardButton("Ростов-на-Дону", callback_data="мем 3 рост"))
tre.row(InlineKeyboardButton("Ставрополь", callback_data="мем 3 став"),
        InlineKeyboardButton("Таганрог", callback_data="мем 3 таган"))

four = InlineKeyboardMarkup()
four.row(InlineKeyboardButton("Балашова", callback_data="мем 4 66"),
        InlineKeyboardButton("Велигжанина", callback_data="мем 4 69"))
four.row(InlineKeyboardButton("Коптева", callback_data="мем 4 коптева"),
        InlineKeyboardButton("Прокофьева", callback_data="мем 4 74"))

five = InlineKeyboardMarkup()
five.row(InlineKeyboardButton("Федя", callback_data="конец 4 yup"),
        InlineKeyboardButton("Федор", callback_data="конец 4 yup"))
five.row(InlineKeyboardButton("Федор Степанович", callback_data="конец 4 yup"))
five.row(InlineKeyboardButton("Велигжанин Федя", callback_data="конец 4 yup"))

dipl = InlineKeyboardMarkup()
dipl.row(InlineKeyboardButton("ЗАБРАТЬ", callback_data="diplom"))

@bot.message_handler(commands=["start"])
def start(message: Message):
    bot.send_message(chat_id=message.chat.id, reply_markup=nach, text=f"Привет, {message.from_user.first_name}👋!\n\n"
                                f"Ты попал(а) на тематическую викторину по теме 'День рождения бабушки🎉'.\n"
           f"Викторина будет состоять из 5 вопросов, правильно ответив на которые ты получишь секретный приз!\n\n"
            f"Если ты готов(а), то скорее нажимай НАЧАТЬ!")

@bot.callback_query_handler(func=lambda call:call.data.startswith("starts"))
def callback1(call: CallbackQuery):
    global points
    points = 0
    bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text, message_id=call.message.id)
    bot.send_message(chat_id=call.message.chat.id, reply_markup=one, text=f"Вопрос №1📆:\nВ каком году родилась Людмила?")

@bot.callback_query_handler(func=lambda call:call.data.startswith("мем"))
def callback1(call: CallbackQuery):
    global points
    que = call.data.split()[1]
    if que == "1":
        ans = call.data.split()[2]
        if ans == "69":
            points += 1
        bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text, message_id=call.message.id)
        bot.send_message(chat_id=call.message.chat.id, reply_markup=two,
                         text=f"Вопрос №2💍:\nВ каком году Людмила вышла замуж?")
    if que == "2":
        ans = call.data.split()[2]
        if ans == "88":
            points += 1
        bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text, message_id=call.message.id)
        bot.send_message(chat_id=call.message.chat.id, reply_markup=tre,
                         text=f"Вопрос №3🎡:\nКакой город для Людмилы наиболее родной?")
    if que == "3":
        ans = call.data.split()[2]
        if ans == "таган":
            points += 1
        bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text, message_id=call.message.id)
        bot.send_message(chat_id=call.message.chat.id, reply_markup=four,
                         text=f"Вопрос №4👩:\nКакая у Людмилы девичья фамилия?")
    if que == "4":
        ans = call.data.split()[2]
        if ans == "коптева":
            points += 1
        bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text, message_id=call.message.id)
        bot.send_message(chat_id=call.message.chat.id, reply_markup=five,
                         text=f"Бонусный вопрос!✨\nКакой любимый внук Людмилы?")

@bot.callback_query_handler(func=lambda call:call.data.startswith("конец"))
def callback1(call: CallbackQuery):
    global points
    ans = call.data.split()[2]
    if ans == "yup":
        points += 1
    bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text, message_id=call.message.id)
    bot.send_message(chat_id=call.message.chat.id, text=f"Викторина завершена! Результаты ниже👇👇👇")
    if points <= 4:
        bot.send_message(chat_id=call.message.chat.id, text=f"К сожалению, вы ответили правильно не на все вопросы,"
                f" поэтому не получаете приз. Вы можете попробовать снова, нажав на команду /start")
    if points == 5:
        bot.send_message(chat_id=call.message.chat.id, text=f"Вы ответили правильно на все вопросы, поэтому получаете"
        f" приз:\nДиплом лучшей бабушки!\nЧтобы забрать его, жми на кнопку снизу.", reply_markup=dipl)

@bot.callback_query_handler(func=lambda call:call.data.startswith("diplom"))
def callback1(call: CallbackQuery):
    bot.send_photo(chat_id=call.message.chat.id, caption="С ДНЕМ РОЖДЕНИЯ!🎉🎉🎉", photo=open("diplom.jpg", "rb"))

bot.infinity_polling()