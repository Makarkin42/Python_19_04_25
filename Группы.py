import telebot
from telebot.types import (Message, ReplyKeyboardMarkup, ReplyKeyboardRemove,
                           InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery)
from config import TOKEN
import time
import random
bot = telebot.TeleBot(TOKEN)
players = []
alls = []
reps = []
blitz = time.time()

@bot.message_handler(content_types=["new_chat_members"])
def handler(message: Message):
    print(message.new_chat_members)
    for member in message.new_chat_members:
        bot.send_message(chat_id=message.chat.id, text=f"Привет, @{member.username}")

@bot.message_handler(commands=["play"])
def game(message: Message):
    keyb = InlineKeyboardMarkup()
    keyb.row(InlineKeyboardButton("Присоедениться", callback_data="play"))
    bot.send_message(chat_id=message.chat.id, text="Началась игра в слова", reply_markup=keyb)

@bot.callback_query_handler(func=lambda call:call.data.startswith("play"))
def callback(call: CallbackQuery):
    global mess, blitz
    if call.from_user.username not in players:
        players.append(call.from_user.username)
        bot.answer_callback_query(call.id, text="Ты присоеденился!")
        print(players)
        if len(players) == 1:
            mess = bot.send_message(chat_id=call.message.chat.id, text=f"Первый ходит @{players[0]}")
        elif len(players) == 2:
            blitz = time.time()
            bot.delete_message(chat_id=mess.chat.id, message_id=mess.id)
            mess = bot.send_message(chat_id=call.message.chat.id, text=f"Присоединился второй игрок, у тебя 15 секунд!")
    else:
        bot.answer_callback_query(call.id, text="Ты уже в игре!")

@bot.message_handler(commands=["report"])
def rep(message: Message):
    if alls:
        keyb = InlineKeyboardMarkup()
        keyb.row(InlineKeyboardButton(text="Проголосовать", callback_data="report"))
        bot.send_message(text="Считаете ли вы, что последний ход надо отменить?", chat_id=message.chat.id,
                         reply_markup=keyb)

@bot.callback_query_handler(func=lambda call:call.data.startswith("report"))
def callback(call: CallbackQuery):
    if call.from_user.username not in reps:
        reps.append(call.from_user.username)
        half = len(players) // 2
        if len(reps) > half:
            bot.edit_message_text(text="Ход был отменен!", chat_id=call.message.chat.id, message_id=call.message.id)
            alls.remove(alls[-1])
            pop = players.pop(-1)
            players.insert(0,pop)
            global mess
            bot.delete_message(chat_id=mess.chat.id, message_id=mess.id)
            mess = bot.send_message(chat_id=call.message.chat.id, text=f"Теперь ходит @{players[0]}")
            reps.clear()
    else:
        bot.answer_callback_query(call.id, text="Ты уже проголосовал!")

@bot.message_handler(content_types=["text", "sticker"])
def handler(message: Message):
    '''emo = random.choice(["🤡", "🤑", "🏀", "😎", "🥵","👶🏿"])
    print(message.chat.id, message.from_user.id)
    bot.send_message(chat_id=message.chat.id, text="Дальше ничего нет!!!")
    bot.send_message(chat_id=message.chat.id, text=f"{emo}")'''
    now = time.time()
    global mess
    global blitz
    print(now - blitz, blitz, now)
    if now - blitz >= 15 and len(players) > 1:
        pop = players.pop(0)
        bot.delete_message(chat_id=mess.chat.id, message_id=mess.id)
        mess = bot.send_message(chat_id=message.chat.id,
                                text=f"@{pop} слишком долго думает, за что был исключен!"
                                     f" Теперь ходит @{players[0]}")
        blitz = time.time()
        if len(players) == 1:
            bot.send_message(chat_id=message.chat.id, text=f"@{players[0]} победил в игре! Держи медальку🥇\n"
                            f"За всю игру было написано {len(alls)} слов и поучавствовало {len(players)} человек!")
            alls.clear()
            players.clear()
    if players and players[0] == message.from_user.username:
        word = message.text.lower()
        if alls and word[0] != alls[-1][-1]:
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
        elif word in alls:
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
        elif not word.isalpha():
            print(word.isalpha(), word)
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
        else:
            players.append(message.from_user.username)
            players.remove(message.from_user.username)
            alls.append(word)
            print(alls, players)
            bot.delete_message(chat_id=mess.chat.id, message_id=mess.id)
            mess = bot.send_message(chat_id=message.chat.id, text=f"Теперь ходит @{players[0]}, у тебя 15 секунд")
            blitz = time.time()

bot.infinity_polling()