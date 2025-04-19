import telebot
from telebot.types import (Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery)
from config import EGE
bot = telebot.TeleBot(EGE)
points = 0
#мемы = порода шлепы, имя шлепы, улетаю куда? на гаити, шайлушай, доктор ливси, этот *** просто имба,
# что делает мага (сияет), кот на чем? (арбузе), когда ходилки бродилки захватит планету, мем из 2027
floppa = "https://static.wikia.nocookie.net/fnaf-fanon-animatronics/images/b/b6/Big-floppa.png/revision/latest?cb=20210920154944&path-prefix=ru"
haity = ""

nach = InlineKeyboardMarkup()
nach.row(InlineKeyboardButton("Начать", callback_data="starts"))

flops = InlineKeyboardMarkup()
flops.row(InlineKeyboardButton("Гера", callback_data="мем гера"),
          InlineKeyboardButton("Коржик", callback_data="мем коржик"))
flops.row(InlineKeyboardButton("Шлёпа", callback_data="мем шлепа"),
          InlineKeyboardButton("Бингус", callback_data="мем бингус"))

haiti = InlineKeyboardMarkup()
haiti.row(InlineKeyboardButton("Гаити", callback_data="мем гаити"),
          InlineKeyboardButton("Море", callback_data="мем море"))
haiti.row(InlineKeyboardButton("Родину", callback_data="мем родина"),
          InlineKeyboardButton("Мальдивы", callback_data="мем мальдивы"))

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
def callback1(call: CallbackQuery):
    global points
    ans = call.data.split()[1]
    if ans == "шлепа":
        points += 1
        print(points)
    bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id, caption=call.message.caption)
    bot.send_photo(chat_id=call.message.chat.id, caption="Вопрос №2:\nПродолжите "
                            "фразу: Уууууулетаю на...", reply_markup=haiti, photo=haity)
#ДАТУ ПОМЕНЯЙ ОБРЫГАН!!!!!!!!!!!!!


bot.infinity_polling()