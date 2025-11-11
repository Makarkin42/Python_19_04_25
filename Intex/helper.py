import telebot
from telebot.types import (Message, InlineKeyboardMarkup, InlineKeyboardButton as IB, CallbackQuery)
from config import INTEX
bot = telebot.TeleBot(INTEX)
back = InlineKeyboardMarkup()
back.row(IB(text="Назад к меню⬅", callback_data="back"))

main = InlineKeyboardMarkup()
main.row(IB(text="Посмотреть ссылки⚙", callback_data="main links"))
main.row(IB(text="Посмотреть размерные таблицы📃", callback_data="main tabs"))
main.row(IB(text="Помощь в выбором размера👨‍💻", callback_data="main help"))

prod = InlineKeyboardMarkup()
prod.row(IB(text="Мужские гольфы", callback_data="prod muzh"), IB(text="Женские гольфы", callback_data="prod zhen"))
prod.row(IB(text="Чулки обыкновенные", callback_data="prod normis"))
prod.row(IB(text="Чулки для широкого бедра", callback_data="prod zhirni"))
prod.row(IB(text="Назад к меню⬅", callback_data="back"))
@bot.message_handler(commands=["start"])
def start(message: Message):
    bot.send_message(chat_id=message.chat.id, text=f"{message.from_user.first_name}👋, приветствуем вас в "
                                    f"боте-помошнике Интекс, выберите нужное вам действие:",
                     reply_markup=main)

@bot.callback_query_handler(func=lambda call:call.data.startswith("back"))
def handler(call: CallbackQuery):
    bot.edit_message_text(chat_id=call.message.chat.id, text=f"👇Вы находитесь в главном меню бота, "
                                    f"выберите нужное вам действие:",
                     reply_markup=main, message_id=call.message.id)


@bot.callback_query_handler(func=lambda call:call.data.startswith("main links"))
def handler(call: CallbackQuery):
    bot.edit_message_text(chat_id=call.message.chat.id, reply_markup=back, message_id=call.message.id,
        text="⚡Основные ссылки:\nОфициальный сайт: https://bint.ru\nКанал Интекс: https://t.me/tm_intex\n"
             "Менеджер: @alena_intex\nТехподдержка: @Openok89")

@bot.callback_query_handler(func=lambda call:call.data.startswith("main tabs"))
def handler(call: CallbackQuery):
    bot.edit_message_text(chat_id=call.message.chat.id, reply_markup=prod, message_id=call.message.id,
        text="Выберите нужное вам изделие👇\n👩‍🏫Чтобы правильно определить нужный вид чулков, сверьтесь с таблицами, или "
             "перейдите в раздел помощи в главном меню")

@bot.callback_query_handler(func=lambda call:call.data.startswith("prod"))
def handler(call: CallbackQuery):
    action = call.data.split()[1]
    if action == "muzh":
        bot.send_photo(photo=open("man_chulok.jpg", "rb"), chat_id=call.message.chat.id, reply_markup=back,
                       caption="Размерная таблица для мужских гольфов👆")


bot.infinity_polling()