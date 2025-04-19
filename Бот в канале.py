import telebot
from telebot.types import (Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, Poll,
                           InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery)
from config import TOKEN, CHANNEL_ID
import time
bot = telebot.TeleBot(TOKEN)
results = ""

@bot.message_handler(commands=["hello"])
def hello(message: Message):
    bot.send_message(text="Привет воображаемым подписчикам!", chat_id=CHANNEL_ID)

@bot.message_handler(commands=["poll"])
def poll(message: Message):
    #bot.send_poll(chat_id=CHANNEL_ID, question="Сколько ног у паука?", options=["2", "4", "6", "8", "10"])
    bot.send_message(text="Какой будет вопрос?", chat_id=message.chat.id)
    bot.register_next_step_handler(message, ques1)

def ques1(message: Message):
    global ans1
    ans1 = message.text
    bot.send_message(text="Какие будут варианты ответов?", chat_id=message.chat.id)
    bot.register_next_step_handler(message, ques2)
def ques2(message: Message):
    ans2 = message.text
    answ = ans2.split(",")
    bot.send_poll(chat_id=CHANNEL_ID, question=ans1, options=answ)

@bot.poll_handler(func=lambda poll: True)
def answers(poll: Poll):
    global results
    results = poll.question
    for option in poll.options:
        results += f"\n{option.text} - {option.voter_count} голосов"

@bot.message_handler(commands=["result"])
def handler(message: Message):
    bot.send_message(chat_id=message.chat.id, text=results)

@bot.message_handler(content_types=["text"])
@bot.channel_post_handler(content_types=["text", "photo"])
def handler(message: Message):
    print(message.text, message.chat.id)

bot.infinity_polling()