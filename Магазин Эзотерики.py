import telebot
from config import PROMO
from telebot.types import (Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery)
import random

bot = telebot.TeleBot(PROMO, parse_mode="html")
item = ""
gif = ""
magic = ["Да","Нет", "Будущее неясно","Переформулируй свой вопрос"]
book = ["Ваше будущее будет наполнено красками и яркими моментами...", "Будьте осторожны! Зимой на вас может упасть"
                                        " гора снега с крыши дома!", "В ближайшем будующем вы найдете хорошего друга, "
                        "который...", "Сегодня вы увидите улитку😮"]
hrust = ["Шар излучает светлую ауру, вы явно ему понравились.", "Шар излучает темную ауру, вы ему определённо не"
                            " понравились.", "Шар излучает нейтральную ауру, ему нечего сказать про вас."]
ruins = ["Будьте очень осторожны, ведь вы находитесь в точке выбора.", "Руна советует вам начать жизнь с чистого листа.",
         "Руна говорит вам, что надо найти партнера по деятельности."]

@bot.message_handler(commands=["start"])
def start(message: Message):
    choose = InlineKeyboardMarkup()
    choose.row(InlineKeyboardButton("Хрустальный шар", callback_data="товар хрустальный"))
    choose.row(InlineKeyboardButton("Магический шар", callback_data="товар магический"))
    choose.row(InlineKeyboardButton('Книга "Гадаем на кофейной гуще"', callback_data="товар книга"))
    choose.row(InlineKeyboardButton("Руны", callback_data="товар руны"))
    bot.send_message(chat_id=message.chat.id,  reply_markup=choose,
                     text="Добро пожаловать в магазин эзотерики!\n\nВыбери товар для демонстрации")

@bot.callback_query_handler(func=lambda call: call.data.startswith("товар"))
def handler(call: CallbackQuery):
    action = call.data.split()[1]
    future = InlineKeyboardMarkup()
    global item, gif
    future.row(InlineKeyboardButton("Узнать ответ", callback_data="ответ"))
    future.row(InlineKeyboardButton("Вернуться в магазин", callback_data="назад"))
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
    item = action
    if action == "магический":
        bot.send_message(chat_id=call.message.chat.id, reply_markup=future,
                                text="Ты выбрал Магический шар, задай вопрос, на который можно ответить Да или Нет\n"
                                                            "Если уверен в выборе - жми на кнопку!")
    elif action == "книга":
        mess = bot.send_animation(chat_id=call.message.chat.id, animation="https://i.pinimg.com/originals/3a/e8/d3/3ae8d37e96e203b9e2eaef6430942355.gif")
        gif = mess.id
        print(gif)
        bot.send_message(chat_id=call.message.chat.id, reply_markup=future,
                         text="Ты выбрал Книгу 'Гадаем на кофейной гуще'!\nЕсли ты готов узнать будущее - жми на кнопку!")
    elif action == "хрустальный":
        mess = bot.send_animation(chat_id=call.message.chat.id, animation="https://66.media.tumblr.com/e981de8b3ef14236b1b170406bdea3d9/tumblr_nrv9l92jQE1s7eez6o4_400.gif")
        gif = mess.id
        bot.send_message(chat_id=call.message.chat.id, reply_markup=future,
                         text="Ты выбрал Хрустальный шар! Чтобы узнать какого мнения о тебе шар - жми на кнопку!")
    elif action == "руны":
        bot.send_message(chat_id=call.message.chat.id, reply_markup=future,
                         text="Ты выбрал Руны! Если хочешь узнать предсказание предков - жми на кнопку!")

@bot.callback_query_handler(func=lambda call: call.data.startswith("ответ"))
def handler(call: CallbackQuery):
    if item == "магический":
        ans = random.choice(magic)
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=call.message.reply_markup,
                                 text=f"Магический шар дал ответ: {ans}\nМожешь задать следующий вопрос")
        except telebot.apihelper.ApiTelegramException:
            pass
    elif item == "книга":
        ans = random.choice(book)
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=call.message.reply_markup,
                                 text=f"Книга дала предсказание: &lt{ans}&gt\nМожешь ещё раз попытать удачу")
        except telebot.apihelper.ApiTelegramException:
            pass
    elif item == "хрустальный":
        ans = random.choice(hrust)
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=call.message.reply_markup,
                                 text=f"Хрустальный шар высказался: \n<tg-spoiler>{ans}</tg-spoiler>\nМожешь ещё раз попытать удачу")
        except telebot.apihelper.ApiTelegramException:
            pass
    elif item == "руны":
        ans = random.choice(ruins)
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=call.message.reply_markup,
                                 text=f"Руны складываются в предсказание: \n<blockquote>{ans}</blockquote>\nМожешь попытаться разгядеть ещё одно послание")
        except telebot.apihelper.ApiTelegramException:
            pass

@bot.callback_query_handler(func=lambda call: call.data.startswith("назад"))
def handler(call: CallbackQuery):
    print(call.message.id, gif)
    try:
        bot.delete_message(message_id=gif, chat_id=call.message.chat.id)
    except telebot.apihelper.ApiTelegramException:
        pass
    bot.delete_message(message_id=call.message.id, chat_id=call.message.chat.id)
    start(call.message)

bot.infinity_polling()