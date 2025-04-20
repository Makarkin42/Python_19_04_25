import telebot
from telebot.types import (Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery)
from config import EGE
bot = telebot.TeleBot(EGE)
points = 0
#мемы = гигачад, имя шлепы, улетаю куда? на гаити, шайлушай, wojak, этот *** просто имба,
# что делает мага (сияет), кот на чем? (арбузе), когда ходилки бродилки захватит планету, мем из 2027
floppa = "https://static.wikia.nocookie.net/fnaf-fanon-animatronics/images/b/b6/Big-floppa.png/revision/latest?cb=20210920154944&path-prefix=ru"
shailushai = "https://s0.rbk.ru/v6_top_pics/media/img/2/33/347018703159332.webp"
maga = "https://icdn.lenta.ru/images/2025/02/18/14/20250218142101075/square_1280_bda036fb1cb4f2a41c1d14e0f358276d.jpg"
giga = "https://upload.wikimedia.org/wikipedia/ru/9/94/%D0%93%D0%B8%D0%B3%D0%B0%D1%87%D0%B0%D0%B4.jpg"

nach = InlineKeyboardMarkup()
nach.row(InlineKeyboardButton("Начать", callback_data="starts"))

flops = InlineKeyboardMarkup()
flops.row(InlineKeyboardButton("Гера", callback_data="мем 1 гера"),
          InlineKeyboardButton("Коржик", callback_data="мем 1 коржик"))
flops.row(InlineKeyboardButton("Шлёпа", callback_data="мем 1 шлепа"),
          InlineKeyboardButton("Бингус", callback_data="мем 1 бингус"))

haiti = InlineKeyboardMarkup()
haiti.row(InlineKeyboardButton("Гаити", callback_data="мем 2 гаити"),
          InlineKeyboardButton("Море", callback_data="мем 2 море"))
haiti.row(InlineKeyboardButton("Родину", callback_data="мем 2 родина"),
          InlineKeyboardButton("Мальдивы", callback_data="мем 2 мальдивы"))

shailu = InlineKeyboardMarkup()
shailu.row(InlineKeyboardButton("Лесничок", callback_data="мем 3 лесничок"),
          InlineKeyboardButton("Грибной", callback_data="мем 3 грибной"))
shailu.row(InlineKeyboardButton("Смурф", callback_data="мем 3 смурф"),
          InlineKeyboardButton("Шайлушай", callback_data="мем 3 шайлушай"))

shine = InlineKeyboardMarkup()
shine.row(InlineKeyboardButton("Поёт", callback_data="мем 4 поет"),
          InlineKeyboardButton("Сияет", callback_data="мем 4 сияет"))
shine.row(InlineKeyboardButton("Танцует", callback_data="мем 4 танц"),
          InlineKeyboardButton("Празднует", callback_data="мем 4 празд"))

melon = InlineKeyboardMarkup()
melon.row(InlineKeyboardButton("Тыкве", callback_data="мем 5 тыва"),
          InlineKeyboardButton("Яблоке", callback_data="мем 5 эпл"))
melon.row(InlineKeyboardButton("Арбузе", callback_data="мем 5 арбуз"),
          InlineKeyboardButton("Мяче", callback_data="мем 5 мяч"))

aim = InlineKeyboardMarkup()
aim.row(InlineKeyboardButton("Аим", callback_data="мем 6 аим"),
          InlineKeyboardButton("Игра", callback_data="мем 6 игра"))
aim.row(InlineKeyboardButton("Прицел", callback_data="мем 6 прицел"),
          InlineKeyboardButton("Тима", callback_data="мем 6 тима"))

chad = InlineKeyboardMarkup()
chad.row(InlineKeyboardButton("Гигачад", callback_data="мем 7 чад"))
chad.row(InlineKeyboardButton("Гурам Мецхарвешвили", callback_data="мем 7 гурам"))
chad.row(InlineKeyboardButton("Крис Судмалис", callback_data="мем 7 крис"))
chad.row(InlineKeyboardButton("Эрнест Халимов", callback_data="мем 7 эрнест"))


@bot.message_handler(commands=["start"])
def start(message: Message):
    bot.send_message(chat_id=message.chat.id, reply_markup=nach, text=f"Привет, {message.from_user.first_name}👋!\n"
                                f"Ты попал на экзамен по мемам, где вопросы будут постепенно усложняться.\n"
                                        f"Если ты готов, то нажимай НАЧАТЬ")

@bot.callback_query_handler(func=lambda call:call.data.startswith("starts"))
def callback1(call: CallbackQuery):
    global points
    bot.send_photo(photo=floppa, caption=f"Вопрос №1:\nКак зовут этого кота?",chat_id=call.message.chat.id,
                          reply_markup=flops)

@bot.callback_query_handler(func=lambda call:call.data.startswith("мем"))
def handler(call: CallbackQuery):
    global points
    que = call.data.split()[1]
    if que == "1":
        ans = call.data.split()[2]
        if ans == "шлепа":
            points += 1
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption=call.message.caption)
        bot.send_photo(chat_id=call.message.chat.id, caption="Вопрос №2:\nПродолжите "
                                "фразу: Уууууулетаю на...", reply_markup=haiti, photo=open("pirojki.jpg", "rb"))
    if que == "2":
        ans = call.data.split()[2]
        if ans == "гаити":
            points += 1
            print(points)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption=call.message.caption)
        bot.send_photo(chat_id=call.message.chat.id, caption="Вопрос №3:\nКак зовут это существо?",
                       reply_markup=shailu, photo=shailushai)
    if que == "3":
        ans = call.data.split()[2]
        if ans == "шайлушай":
            points += 1
            print(points)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption=call.message.caption)
        bot.send_photo(chat_id=call.message.chat.id, caption="Вопрос №4:\nЧто делает этот человек?",
                       reply_markup=shine, photo=maga)

    if que == "4":
        ans = call.data.split()[2]
        if ans == "сияет":
            points += 1
            print(points)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption=call.message.caption)
        bot.send_photo(chat_id=call.message.chat.id, caption="Вопрос №5:\nНа чём сидит этот кот?",
                       reply_markup=melon, photo=open("melon.jpg", "rb"))
    if que == "5":
        ans = call.data.split()[2]
        if ans == "арбуз":
            points += 1
            print(points)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption=call.message.caption)
        bot.send_photo(chat_id=call.message.chat.id, caption="Вопрос №6:\nЧто говорит этот человек?",
                       reply_markup=aim, photo=open("aim.jpg", "rb"))
    if que == "6":
        ans = call.data.split()[2]
        if ans == "прицел":
            points += 1
            print(points)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption=call.message.caption)
        bot.send_photo(chat_id=call.message.chat.id, caption="Вопрос №6:\nКак зовут гигачада в реальной жизни?",
                       reply_markup=chad, photo=giga)

bot.infinity_polling()