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
    oprosi = session.query(Questions).all()
    names = [opros.title for opros in oprosi]
    names = "\n".join(names)
    bot.send_message(chat_id=message.chat.id, text=f"👋{message.from_user.first_name}, здравствуйте, выберите нужный"
                                    f" опрос из списка ниже, напечатав его в чат без ошибок👇")
    bot.send_message(chat_id=message.chat.id, text=f"Список опросов:\n{names}")
    bot.register_next_step_handler(message, front)

def front(message: Message):
    text = message.text
    opros = session.query(Questions).filter(text==Questions.title).all()
    if opros:
        ask(message, opros[0].list, [], opros[0].id)
    else:
        bot.send_message(chat_id=message.chat.id, text="Выбранный опрос не найден в базе данных!")
        bot.register_next_step_handler(message, front)

def ask(message: Message, que: list, ans: list, que_id: int):
    answer = message.text
    ans.append(answer)
    if len(que) > len(ans):
        question = que[len(ans)]
        bot.send_message(chat_id=message.chat.id, text=f"{question}")
        bot.register_next_step_handler(message, ask, que, ans, que_id)


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
    logger.info("Админ нажал на 'Добавить опрос'")
    bot.send_message(chat_id=call.message.chat.id, text="Введите название опроса:")
    bot.register_next_step_handler(call.message, add2)

def add2(message: Message):
    pull_name = message.text
    logger.info(f"Админ ввел {pull_name}")
    bot.send_message(chat_id=message.chat.id, text="Введите вопросы:")
    bot.register_next_step_handler(message, add3, pull_name)
def add3(message: Message, pull_name):
    pull_quests = message.text.split("\n")
    logger.info(f"Были введены вопросы: {pull_quests}")
    copy = Questions()
    copy.title = pull_name
    copy.list = pull_quests
    session.merge(copy)
    session.commit()
    bot.send_message(chat_id=message.chat.id, text=f"Опрос был добавлен!")
    logger.success("Успешное сохранение данных в таблицу")

@bot.callback_query_handler(func=lambda call:call.data.startswith("admin list"))
def vision(call: CallbackQuery):
    logger.info("Админ нажал на кнопку просмотра")
    bot.answer_callback_query(call.id) #Удаление мерцания кнопки
    oprosi = session.query(Questions).all()
    names = [opros.title for opros in oprosi]
    names = "\n".join(names)  #Делаем из списка строку
    if names:
        bot.send_message(chat_id=call.message.chat.id, text=f"Выберите нужный опрос:\n{names}")
        bot.register_next_step_handler(call.message, vision2)
    else:
        logger.warning("В таблице нет опросов!")
        bot.send_message(chat_id=call.message.chat.id, text="Опросы ещё не добавлены!")

def vision2(message: Message):
    res = message.text
    opros = session.query(Questions).filter(res==Questions.title).all()
    if not opros:
        logger.warning(f"Админ ввел {res}, но в таблице такого опроса нет!")
        bot.send_message(chat_id=message.chat.id, text="Указнного списка не существует! Проверьте "
                                                       "правильность написания")
        bot.register_next_step_handler(message, vision2)
    else:
        ques_old = opros[0].list
        ques = "\n".join(ques_old)
        bot.send_message(chat_id=message.chat.id, text=f"Вопросы по запросу {res}:\n{ques}")
        logger.success(f"Получено {len(ques_old)} опросов!")

@bot.callback_query_handler(func=lambda call:call.data.startswith("admin delete"))
def removing(call: CallbackQuery):
    logger.info("Админ нажал на кнопку удаления")
    oprosi = session.query(Questions).all()
    names = [opros.title for opros in oprosi]
    names = "\n".join(names)
    bot.send_message(chat_id=call.message.chat.id, text=f"Выберите нужный для удаления список:\n{names}")
    bot.register_next_step_handler(call.message, remove2)
def remove2(message: Message):
    res = message.text
    opros = session.query(Questions).filter(res == Questions.title).all()
    if not opros:
        logger.warning(f"Админ ввел {res}, но в таблице такого опроса нет!")
        bot.send_message(chat_id=message.chat.id, text="Указнного опроса не существует! Проверьте "
                                                       "правильность написания")
    else:
        session.query(Questions).filter(res == Questions.title).delete()
        bot.send_message(chat_id=message.chat.id, text=f"Опрос '{res}' был удален!")
        logger.success(f"Опрос {res} был удален!")



bot.infinity_polling()