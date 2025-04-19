import telebot
from telebot.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from config import TOKEN, CHANNEL_ID
from Matematik import solve
import time
bot = telebot.TeleBot(TOKEN)
true = "https://w7.pngwing.com/pngs/259/59/png-transparent-computer-icons-encapsulated-postscript-educational-icon-miscellaneous-cdr-text.png"
error = "https://cdn-icons-png.flaticon.com/512/258/258393.png"


@bot.inline_handler(func=lambda query: True)
def x(query: InlineQuery):
    mathem = solve(query.query)
    mathem = str(mathem)[1: -1]
    mess = InlineQueryResultArticle(id="1", title="Ответ:", description=f"{mathem}", thumbnail_url=true,
                                    input_message_content=InputTextMessageContent(f"{query.query}\nx = {mathem}"))
    bot.answer_inline_query(query.id, results=[mess])

@bot.inline_handler(func=lambda query: len(query.query.split()) == 5)
def equation(query: InlineQuery):
    link = true
    if "x" in query.query:
        lis = query.query.split()
        if lis[1] == "+":
            result = eval(f"{lis[-1]} - {lis[2]}")
        if lis[1] == "-":
            result = eval(f"{lis[-1]} + {lis[2]}")
        if lis[1] == "*":
            if lis[2] == "0" and lis[-1] != "0":
                result = (f"Неверное выражение!")
                link = error
            elif lis[2] == "0":
                result = (f"Х может быть любым числом")
                link = error
            else:
                result = eval(f"{lis[-1]} / {lis[2]}")
        if lis[1] == "/":
            if lis[2] != "0":
                 result = eval(f"{lis[-1]} * {lis[2]}")
            else:
                result = "На ноль делить нельзя!"
                link = error
        if lis[1] == "**":
            result = eval(f"{lis[-1]} ** (1/{lis[2]})")
        print(result)
        mess = InlineQueryResultArticle(id="1", title="Ответ:", description=f"{result}", thumbnail_url = link,
                                        input_message_content=InputTextMessageContent(f"{query.query}\nx = {result}"))
        bot.answer_inline_query(query.id, results=[mess])

@bot.inline_handler(func=lambda query: len(query.query.split())%2 == 1)
def inline(query: InlineQuery):
    print(query.query)
    split = query.query.split()
    math = ["/", "*", "-", "+"]
    result = ""
    for i in range(len(split)):
        if i % 2 == 0:
            if split[i].isdigit():
                continue
        else:
            if split[i] in math:
                continue
        result = "Неправильное выражение!"
        break
    if not result == "Неправильное выражение!":
        try:
            result = eval(query.query)
        except ZeroDivisionError:
            result = "На ноль делить нельзя!"
    print(result)
    mess = InlineQueryResultArticle(id="1", title="Ответ:", description=f"{result}",
                                    input_message_content=InputTextMessageContent(f"{query.query} = {result}"))
    bot.answer_inline_query(query.id, results=[mess])

bot.infinity_polling()