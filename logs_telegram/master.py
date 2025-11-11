import telebot
from telebot.types import (Message, ReplyKeyboardMarkup, ReplyKeyboardRemove,
                           InlineKeyboardMarkup, InlineKeyboardButton as IB, CallbackQuery)
from config import PULL
from loguru import logger
from pulls_data import session, Answers, Questions
logger.add("tg_logi.logs")
bot = telebot.TeleBot(PULL)
logger.info("Успешный запуск")
admins = [5070171003]

@bot.message_handler(commands=["start"])
def handler(message: Message):
    print(message.from_user.id)
    logger.info(f"{message.from_user.id} подал /start")
    bot.send_message(chat_id=message.chat.id, text="Используйте /pull, чтобы начать опрос")

@bot.message_handler(commands=["admin"])
def admin_panel(message: Message):
    if message.from_user.id in admins:
        choose = InlineKeyboardMarkup()
        choose.row(IB(text="Создать опрос", callback_data="admin pull"))
        choose.row(IB(text="Посмотреть опросы", callback_data="admin list"))
        choose.row(IB(text="Удалить опрос", callback_data="admin delete"))
        bot.send_message(chat_id=message.chat.id, reply_markup=choose, text="АДМИН ПАНЕЛЬ")
        logger.info(f"{message.from_user.id} включил админ панель")
    else:
        logger.warning(f"{message.from_user.id} пытается получить доступ к панели!")
        bot.send_message(chat_id=message.chat.id, text="Нет прав на команду!")

@bot.callback_query_handler(func=lambda call:call.data.startswith("admin pull"))
def appending(call: CallbackQuery):
    bot.answer_callback_query(call.id)
    bot.send_message(chat_id=call.message.chat.id, text="Введите название опроса:")
    bot.register_next_step_handler(call.message, add2)

def add2(message: Message):
    pull_name = message.text
    bot.send_message(chat_id=message.chat.id, text="Введите вопросы:")
    bot.register_next_step_handler(message, add3, pull_name)
def add3(message: Message, pull_name):
    pull_quests = message.text.split("\n")
    copy = Questions()
    copy.title = pull_name
    copy.list = pull_quests
    session.merge(copy)
    session.commit()
    logger.success("Успешное сохранение данных в таблицу")

@bot.callback_query_handler(func=lambda call:call.data.startswith("admin list"))
def vision(call: CallbackQuery):
    bot.answer_callback_query(call.id)
    oprosi = session.query(Questions).all()
    names = [opros.title for opros in oprosi]
    names = "\n".join(names)  #Делаем из списка строку
    bot.send_message(chat_id=call.message.chat.id, text=f"Выберите нужный опрос:\n{names}")
    bot.register_next_step_handler(call.message, vision2)

def vision2(message: Message):
    res = message.text
    opros = session.query(Questions).filter(res==Questions.title).all()
    if not opros:
        bot.send_message(chat_id=message.chat.id, text="Указнного списка не существует! Проверьте "
                                                       "правильность написания")
        bot.register_next_step_handler(message, vision2)
    else:
        ques = opros[0].list
        ques = "\n".join(ques)
        bot.send_message(chat_id=message.chat.id, text=f"Вопросы по запросу {res}:\n{ques}")


bot.infinity_polling()