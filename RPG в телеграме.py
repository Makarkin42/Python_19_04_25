import telebot
from telebot.types import (Message, ReplyKeyboardMarkup, ReplyKeyboardRemove,
                           InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery)
from config import TOKEN
import random
import s_taper
from s_taper.consts import *
scheme = {"user_id": INT+KEY, "nick": TEXT, "race": TEXT, "hp": INT, "dmg": INT, "armor": INT,"money": INT, "max": INT}
users = s_taper.Taper("users", "rpg.db").create_table(scheme)
bot = telebot.TeleBot(TOKEN)
races = ["Зомби", "Робот", "Человек"]
enemies = {"Огр": (150, 9), "Крыса": (60, 15), "Титан": (200, 7),
           "Мутант": (90, 13), "Киборг": (120, 11)}
alls = {}
choose = InlineKeyboardMarkup()
choose.row(InlineKeyboardButton("Атаковать", callback_data="forest Атака"),
           InlineKeyboardButton("Убежать", callback_data="forest Побег"))
townb = InlineKeyboardMarkup()
townb.row(InlineKeyboardButton("Таверна", callback_data="town Таверна"),
                     InlineKeyboardButton("Лавка", callback_data="town Лавка"))
townb.row(InlineKeyboardButton("Мои показатели", callback_data="town Показ"))
battles = {}

@bot.message_handler(commands=["start"])
def handler(message: Message):
    alls[message.from_user.id] = [message.from_user.id]
    bot.send_message(chat_id=message.chat.id, text=f"Привет, {message.from_user.first_name}!"
                                                f" Как будут звать твоего персонажа?")
    bot.register_next_step_handler(message,register1)

def register1(message: Message):
    name = message.text
    print(name)
    alls[message.from_user.id].append(name)
    keyb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    keyb.row(*races)
    bot.send_message(chat_id=message.chat.id, text="Какой расы твой персонаж?", reply_markup=keyb)
    bot.register_next_step_handler(message, register2)

def register2(message: Message):
    race = message.text.capitalize()
    print(race)
    if race in races:
        alls[message.from_user.id].append(race)
        battles[message.from_user.id] = []
        if race == "Человек":
            users.write(alls[message.from_user.id] + [100, 15, 2, 30, 100])
        if race == "Зомби":
            users.write(alls[message.from_user.id]+[100, 20, 0, 10, 100])
        if race == "Робот":
            users.write(alls[message.from_user.id] + [100, 10, 5, 10, 100])
        bot.send_message(chat_id=message.chat.id, text = "Приключение начинается!", reply_markup=ReplyKeyboardRemove())
        bot.send_message(chat_id=message.chat.id, text="Если ты хочешь попасть в Тёмный лес - то используй"
                                                       " /forest, а если в Городок торговцев - /town")
    else:
        bot.send_message(chat_id=message.chat.id, text="Выбери расу из списка!")
        bot.register_next_step_handler(message, register2)

@bot.message_handler(commands=["forest"])
def handler(message: Message):
    userid = message.from_user.id
    if userid not in battles or not battles[userid]:
        bot.send_message(chat_id=message.chat.id, text="Ты попал в Тёмный лес! Здесь ты сможешь сражаться с разными"
                                                       " врагами и боссами, а также подзаработать денег!")
        victim = random.choice(tuple(enemies))
        hp, dmg = enemies[victim]
        battles[message.from_user.id] = [victim, hp, dmg]
        bot.send_message(chat_id=message.chat.id, text=f"На тебя напал {victim}! У него {hp}❤ и {dmg}⚔",
                         reply_markup=choose)

@bot.callback_query_handler(func=lambda call:call.data.startswith("forest"))
def callback(call: CallbackQuery):
    player = users.read("user_id", call.from_user.id)
    print(call.data)
    action = call.data.split()[1]
    text = call.message.text.split("\n")[0]
    if action == "Атака":
        battles[call.from_user.id][1] -= player[4]
        text += f"\n\nТы ударил врага! У него осталось {battles[call.from_user.id][1]}🖤"
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=choose)
        if battles[call.from_user.id][1] >= 1:
            player[3] -= battles[call.from_user.id][2] - player[5]
            text += f"\nВраг ударил тебя! У тебя осталось {player[3]}❤"
            bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=choose)
            if player[3] <= 0:
                bot.send_message(chat_id=call.message.chat.id, text=f"{player[1]} погиб в этом бою! /start для новой игры")
                bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.id)
        else:
            prize = random.randint(12, 38)
            bot.edit_message_text(chat_id=call.message.chat.id, text=text+f"\n\nВраг побеждён!\n В его карманах оказалось"
                                                                f" {prize} монет!\n/town для перехода в город\n"
                                                                          f"/forest для новой битвы", message_id=call.message.id)
            player[6] += prize
            battles[call.from_user.id].clear()
    elif action == "Побег":
        luck = random.random()
        if luck >= 0.70:
            bot.edit_message_text(text=text + "\n\nПобег удался! /town для перехода в город \n/forest для новой битвы", chat_id=call.message.chat.id,
                                  message_id=call.message.id)
            battles[call.from_user.id].clear()
        else:
            text += "\n\nПобег не удался!"
            bot.edit_message_text(text,chat_id=call.message.chat.id,
                                 message_id=call.message.id, reply_markup=choose)
            player[3] -= battles[call.from_user.id][2] - player[5]
            text += f"\nВраг ударил тебя! У тебя осталось {player[3]}❤"
            bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=choose)
    users.write(player)

@bot.callback_query_handler(func=lambda call:call.data.startswith("town"))
def callback(call: CallbackQuery):
    player = users.read("user_id", call.from_user.id)
    action = call.data.split()[1]
    if action == "Таверна":
        keyb = InlineKeyboardMarkup()
        keyb.row(InlineKeyboardButton("Перекус (5©, 25❤)", callback_data="Таверна перекус 5 30"))
        keyb.row(InlineKeyboardButton("Лекарство (18©, 100❤)", callback_data="Таверна лекарство 18 100"))
        keyb.row(InlineKeyboardButton("Вернуться в город", callback_data="Таверна назад 0 0"))
        bot.edit_message_text(text="Приветствую тебя в таверне! Тут ты сможешь подлечиться и отдохнуть от боёв",
                              chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=keyb)
    if action == "Лавка":
        keyb = InlineKeyboardMarkup()
        keyb.row(InlineKeyboardButton("+20 здоровья (25©)", callback_data="Лавка здоровье 20 20"))
        keyb.row(InlineKeyboardButton("+2 урона (25©)", callback_data="Лавка урон 25 2"))
        keyb.row(InlineKeyboardButton("+1 броня (40©)", callback_data="Лавка броня 40 1"))
        keyb.row(InlineKeyboardButton("Вернуться в город", callback_data="Лавка назад 0 0"))
        bot.edit_message_text(text="Приветствую тебя в лавке! Тут ты сможешь прокачать свои боевые параметры",
                              chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=keyb)
    if action == "Показ":
        keyb = InlineKeyboardMarkup()
        keyb.row(InlineKeyboardButton("Вернуться в город", callback_data="Лавка назад 0 0"))
        bot.edit_message_text(text=f"Текущее здоровье: {player[3]}\n"
                                   f"Максимальное здоровье: {player[7]}\nУрон: {player[4]}\nБроня: {player[5]}\n"
                                   f"Деньги: {player[6]}", chat_id=call.message.chat.id,
                              message_id=call.message.id, reply_markup=keyb)

@bot.callback_query_handler(func=lambda call:call.data.startswith("Таверна"))
def taver(call: CallbackQuery):
    player = users.read("user_id", call.from_user.id)
    tag, price, res = call.data.split()[1:]
    price = int(price)
    res = int(res)
    if price == 0:
        bot.edit_message_text(text="Ты попал в Городок торговцев! Здесь ты можешь отдохнуть после"
                                   " битвы, восполнить здоровье и улучшить свои показатели!\n"
                                   "Если ты готов ко встрече с врагом - жми /forest", chat_id=call.message.chat.id,
                              message_id=call.message.id, reply_markup=townb)
    elif player[6] >= price:
        player[6] -= price
        player[3] += res
        keyb = call.message.reply_markup
        bot.edit_message_text(text=f"Ты купил {tag}! Теперь у тебя {player[6]} денег и {player[3]} здоровья!",
                              chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=keyb)
    else:
        bot.answer_callback_query(call.id,text="Слишком мало денег!")
    users.write(player)

@bot.callback_query_handler(func=lambda call:call.data.startswith("Лавка"))
def upd(call: CallbackQuery):
    player = users.read("user_id", call.from_user.id)
    tag, price, res = call.data.split()[1:]
    price = int(price)
    res = int(res)
    if price == 0:
        bot.edit_message_text(text="Ты попал в Городок торговцев! Здесь ты можешь отдохнуть после"
                                " битвы, восполнить здоровье и улучшить свои показатели!\n"
                        "Если ты готов ко встрече с врагом - жми /forest",chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=townb)
    elif price <= player[6]:
        keyb = call.message.reply_markup
        player[6] -= price
        if tag == "здоровье":
            player[7] += res
            bot.edit_message_text(text=f"Ты купил {tag}! Теперь у тебя {player[6]} денег и {player[7]} "
                                       f"максимального здоровья!",
                                  chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=keyb)
        elif tag == "урон":
            player[4] += res
            bot.edit_message_text(text=f"Ты купил {tag}! Теперь у тебя {player[6]} денег и {player[4]} урона!",
                                  chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=keyb)
        elif tag == "броня":
            player[5] += res
            bot.edit_message_text(text=f"Ты купил {tag}! Теперь у тебя {player[6]} денег и {player[5]} брони!",
                                  chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=keyb)
    else:
        bot.answer_callback_query(call.id, text="Слишком мало денег!")
    users.write(player)

@bot.message_handler(commands=["town"])
def town(message: Message):
    userid = message.from_user.id
    if userid not in battles or not battles[userid]:
        player = users.read("user_id",userid)
        print(player)
        if player and player[3] > 0:
            bot.send_message(chat_id=message.chat.id, text="Ты попал в Городок торговцев! Здесь ты можешь отдохнуть после"
                                                       " битвы, восполнить здоровье и улучшить свои показатели!\n"
                                                           "Если ты готов ко встрече с врагом - жми /forest",
                             reply_markup=townb)

@bot.message_handler(content_types=["text", "sticker"])
def handler(message: Message):
    emo = random.choice(["🤡", "🤑", "🏀", "😎", "🥵","👶🏿"])
    print(message)
    bot.send_message(chat_id=message.chat.id, text="Дальше ничего нет!!!")
    bot.send_message(chat_id=message.chat.id, text=f"{emo}")

bot.infinity_polling()
#Content types: 'audio', 'photo', 'voice', 'video', 'document', 'text', 'location', 'contact', 'sticker'