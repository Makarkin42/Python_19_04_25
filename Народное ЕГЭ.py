import telebot
from telebot.types import (Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery)
from config import EGE
bot = telebot.TeleBot(EGE)
#мемы = гигачад, имя шлепы, улетаю куда? на гаити, шайлушай, wojak, этот *** просто имба,
# что делает мага (сияет), кот на чем? (арбузе), когда ходилки бродилки захватит планету, мем из 2027
floppa = "https://static.wikia.nocookie.net/fnaf-fanon-animatronics/images/b/b6/Big-floppa.png/revision/latest?cb=20210920154944&path-prefix=ru"
shailushai = "https://s0.rbk.ru/v6_top_pics/media/img/2/33/347018703159332.webp"
maga = "https://icdn.lenta.ru/images/2025/02/18/14/20250218142101075/square_1280_bda036fb1cb4f2a41c1d14e0f358276d.jpg"
giga = "https://upload.wikimedia.org/wikipedia/ru/9/94/%D0%93%D0%B8%D0%B3%D0%B0%D1%87%D0%B0%D0%B4.jpg"
meme = "https://avatars.mds.yandex.net/get-vthumb/3306004/16fc402869f115e5031302b5c6bdf2ce/800x450"
wojik = "https://i-enlisted.cdn.gaijin.net/original/3X/b/7/b7cf0143cafa3919bd2b924eeaace68fce41a5f5.jpeg"
hodil = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTd9ZF8o6bBUhbe411aEO7RZfJ2cJUD1bmyhg&s"
joe = "https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/04/62/e6/0462e6b9-45b0-f229-afc0-d2f79cce2cf4/artwork.jpg/600x600bf-60.jpg"
a, b, c, d, e, f, g, h, i, j, = "","","","","","","","","",""
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
          InlineKeyboardButton("Калаш", callback_data="мем 6 игра"))
aim.row(InlineKeyboardButton("Прицел", callback_data="мем 6 прицел"),
          InlineKeyboardButton("Тиммейт", callback_data="мем 6 тима"))

chad = InlineKeyboardMarkup()
chad.row(InlineKeyboardButton("Гигачад", callback_data="мем 7 чад"))
chad.row(InlineKeyboardButton("Гурам Мецхарвешвили", callback_data="мем 7 гурам"))
chad.row(InlineKeyboardButton("Крис Судмалис", callback_data="мем 7 крис"))
chad.row(InlineKeyboardButton("Эрнест Халимов", callback_data="мем 7 эрнест"))

mime = InlineKeyboardMarkup()
mime.row(InlineKeyboardButton("2026", callback_data="мем 8 2026"),
          InlineKeyboardButton("2027", callback_data="мем 8 два"))
mime.row(InlineKeyboardButton("2031", callback_data="мем 8 2031"),
          InlineKeyboardButton("2034", callback_data="мем 8 2034"))

brod = InlineKeyboardMarkup()
brod.row(InlineKeyboardButton("1 июня", callback_data="мем 9 2026"),
          InlineKeyboardButton("19 сентября", callback_data="мем 9 2027"))
brod.row(InlineKeyboardButton("31 декабря", callback_data="мем 9 2031"),
          InlineKeyboardButton("27 ноября", callback_data="мем 9 двасемь"))

wojak = InlineKeyboardMarkup()
wojak.row(InlineKeyboardButton("wojak", callback_data="sup 10 wojak"),
          InlineKeyboardButton("lorem ipsum", callback_data="sup 10 2027"))
wojak.row(InlineKeyboardButton("Думеры", callback_data="sup 10 2031"),
          InlineKeyboardButton("Зумеры", callback_data="sup 10 2034"))

@bot.message_handler(commands=["start"])
def start(message: Message):
    bot.send_message(chat_id=message.chat.id, reply_markup=nach, text=f"Привет, {message.from_user.first_name}👋!\n"
                                f"Ты попал на экзамен по мемам, где вопросы будут постепенно усложняться. Ответив"
                f" правильно на все вопросы, ты получишь СМЕШНЯВКУ😂\n"
                                        f"Если ты готов, то нажимай НАЧАТЬ")
points = 0

@bot.callback_query_handler(func=lambda call:call.data.startswith("starts"))
def callback1(call: CallbackQuery):
    global points
    bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text, message_id=call.message.id)
    bot.send_photo(photo=floppa, caption=f"Вопрос №1:\nКак зовут этого кота?",chat_id=call.message.chat.id,
                          reply_markup=flops)

@bot.callback_query_handler(func=lambda call:call.data.startswith("мем"))
def handler(call: CallbackQuery):
    global points,a,b,c,d,e,f,g,h,i
    que = call.data.split()[1]
    if que == "1":
        ans = call.data.split()[2]
        if ans == "шлепа":
            points += 1
            a = "✅"
        else:
            a = "❌"
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption=call.message.caption)
        bot.send_photo(chat_id=call.message.chat.id, caption="Вопрос №2:\nПродолжите "
                                "фразу: Уууууулетаю на...", reply_markup=haiti, photo=open("pirojki.jpg", "rb"))
    if que == "2":
        ans = call.data.split()[2]
        if ans == "гаити":
            points += 1
            print(points)
            b = "✅"
        else:
            b = "❌"
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption=call.message.caption)
        bot.send_photo(chat_id=call.message.chat.id, caption="Вопрос №3:\nКак зовут это существо?",
                       reply_markup=shailu, photo=shailushai)
    if que == "3":
        ans = call.data.split()[2]
        if ans == "шайлушай":
            points += 1
            print(points)
            c = "✅"
        else:
            c = "❌"
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption=call.message.caption)
        bot.send_photo(chat_id=call.message.chat.id, caption="Вопрос №4:\nЧто делает этот человек?",
                       reply_markup=shine, photo=maga)

    if que == "4":
        ans = call.data.split()[2]
        if ans == "сияет":
            points += 1
            print(points)
            d = "✅"
        else:
            d = "❌"
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption=call.message.caption)
        bot.send_photo(chat_id=call.message.chat.id, caption="Вопрос №5:\nНа чём сидит этот кот?",
                       reply_markup=melon, photo=open("melon.jpg", "rb"))
    if que == "5":
        ans = call.data.split()[2]
        if ans == "арбуз":
            points += 1
            print(points)
            e = "✅"
        else:
            e = "❌"
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption=call.message.caption)
        bot.send_photo(chat_id=call.message.chat.id, caption="Вопрос №6:\nЧто говорит этот человек?",
                       reply_markup=aim, photo=open("aim.jpg", "rb"))
    if que == "6":
        ans = call.data.split()[2]
        if ans == "прицел":
            points += 1
            print(points)
            f = "✅"
        else:
            f = "❌"
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption=call.message.caption)
        bot.send_photo(chat_id=call.message.chat.id, caption="Вопрос №7:\nКак зовут гигачада в реальной жизни?",
                       reply_markup=chad, photo=giga)
    if que == "7":
        ans = call.data.split()[2]
        if ans == "эрнест":
            points += 1
            print(points)
            g = "✅"
        else:
            g = "❌"
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption=call.message.caption)
        bot.send_photo(chat_id=call.message.chat.id, caption="Вопрос №8:\nИз какого года этот мем?",
                       reply_markup=mime, photo=meme)
    if que == "8":
        ans = call.data.split()[2]
        if ans == "два":
            points += 1
            print(points)
            h = "✅"
        else:
            h = "❌"
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption=call.message.caption)
        bot.send_photo(chat_id=call.message.chat.id, caption="Вопрос №9:\nКогда этот медведь хочет захватить планету?",
                       reply_markup=brod, photo=hodil)
    if que == "9":
        ans = call.data.split()[2]
        if ans == "двасемь":
            points += 1
            print(points)
            i = "✅"
        else:
            i = "❌"
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption=call.message.caption)
        bot.send_photo(chat_id=call.message.chat.id, caption="Вопрос №10: Финальный\nКак называются картинки такого типа?",
                       reply_markup=wojak, photo=wojik)

@bot.callback_query_handler(func=lambda call:call.data.startswith("sup"))
def handler(call: CallbackQuery):
    global points, j
    ans = call.data.split()[2]
    if ans == "wojak":
        points += 1
        print(points)
        j = "✅"
    else:
        j = "❌"
    bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption=call.message.caption)
    bot.send_message(chat_id=call.message.chat.id, text=f"Экзамен завершен! Результаты ниже👇👇👇")
    if points <= 9:
        bot.send_message(chat_id=call.message.chat.id, text=f"Вы ответили правильно не на все вопросы, из-за чего не"
        f" достойны СМЕШНЯВКИ. Результаты по вопросам снизу\nВопрос №1: {a}\nВопрос №2: {b}\nВопрос №3: {c}\nВопрос №4: {d}"
        f"\nВопрос №5: {e}\nВопрос №6: {f}\nВопрос №7: {g}\nВопрос №8: {h}\nВопрос №9: {i}\nВопрос №10: {j}\nВы можете"
                    f" попробовать снова командой /start")
    else:
        bot.send_message(chat_id=call.message.chat.id, text=f"Поразительно! {call.from_user.first_name},"
                f" вы ответили правильно на все вопросы! Чтож, думаю вы достойны СМЕШНЯВКИ. Используйте команду /fun "
                f"чтобы получить свою награду")

@bot.message_handler(commands=["fun"])
def funny(message: Message):
    bot.send_photo(chat_id=message.chat.id, photo=joe, caption="Вам звонит Джон Порк😂😂😂🧢🧢🧢")

bot.infinity_polling()