import telebot
from telebot.types import (Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, Poll,
                           InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery)
from config import TOKEN, CHANNEL_ID
import time
import random
import requests
from bs4 import BeautifulSoup
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["photo"])
def handler(message: Message):
    bot.send_message(text="нармальна", chat_id=message.chat.id)
    for i in range(10):
        photo, desc = pars.urls()
        print(photo)
        '''pic = random.choice(["https://cs13.pikabu.ru/post_img/2023/09/10/6/1694334404138966000.webp",
                             "https://i.namu.wiki/i/kJjmUmfROsSy6VaoDpyIJ9THJTqQcICD7pOnOqfTeWKCQa39SIlbxRTJLSckyfzU80EGblaHtLkDCzlt7CT38A.png",
                             "https://www.bethowen.ru/upload/medialibrary/52e/52ec4a031f14527c423b18aac9cca6cc.jpg"])'''
        time.sleep(3)
        bot.send_photo(photo=photo, caption=desc,chat_id=message.chat.id)

class Parser():
    def __init__(self, url):
        req = requests.get(url).text
        self.soup = BeautifulSoup(req, "html.parser")
    def urls(self):
        alls = self.soup.find_all("img", {"class": "story-image__image"})
        pic = random.choice(alls)
        if pic.has_attr("data-src"):
            img = pic["data-src"]
        else:
            img = pic["src"]
        desc = pic["alt"]
        return img, desc


pars = Parser(url="https://pikabu.ru/tag/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D0%B8%D0%B5%20%D0%B6%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5%2C%D0%9C%D0%B5%D0%BC%D1%8B%2C%D0%AE%D0%BC%D0%BE%D1%80/hot?et=%D0%9C%D0%B0%D1%82&n=4")

bot.infinity_polling()