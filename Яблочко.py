import telebot
from config import PROMO
from telebot.types import (Message, ReplyKeyboardMarkup)
import random

bot = telebot.TeleBot(PROMO)
res = ["алмаз💎", "цветное стеклышко", "древнюю вазу⚱", "золотую монетку📀", "серебряную монетку💿", "кость🦴",
       "украшение царицы💍", "древнюю кисть для росписи🖌", "пустой мешочек🎒", "мешочек, заполненый монетами💰",
       "древнюю шкатулку🗃", "глиняную фигурку♟", "гигантский сундук🧰", "одежду предков👘" "палку🦯",
       "топаз", "позолоченую цепь", "осколок плиты", "драгоценную серьгу", "древнюй топор🪓", "древний серп",
       "осколок аметиста", "шкатулку с рубинами🗃", "каменный молот⚒", "чей-то череп💀", "древнюю плиту с рисунками🀄"]
promos = []


@bot.message_handler(commands=["start"])
def handler(message: Message):
    keyb = ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=False)
    keyb.row("💎КОПАТЬ⛏")
    bot.send_message(chat_id=message.chat.id, reply_markup=keyb,
                     text="Привет👋\n\nТы попал на экспедицию по раскопкам древнего города, "
                          "где можно выкопать ценные предметы⚱\n\n"
                          "Также, местные говорят, что тут можно найти секретный промокод для "
                          "магазина Яблочко, дающий огромную скидку🏷\n\n"
                          "Если ты готов - то смело жми кнопку 💎КОПАТЬ⛏!")


@bot.message_handler(content_types=["text"])
def mine(message: Message):
    if message.text == "💎КОПАТЬ⛏":
        luck = random.random()
        if luck <= 0.05 and message.from_user.id not in promos:
            bot.send_message(chat_id=message.chat.id, message_effect_id="5046509860389126442",
                             text="Поздравляю! Ты смог выкопать секретный промокод - Super_Promo2023")
            promos.append(message.from_user.id)
        else:
            miner = random.choice(res)
            bot.send_message(chat_id=message.chat.id, text=f"Ого!😮 Ты выкопал {miner}!")
    else:
        bot.send_message(chat_id=message.chat.id, text="Скорее нажимай кнопку 💎КОПАТЬ!⛏")


bot.infinity_polling()
