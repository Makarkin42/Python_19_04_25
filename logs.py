from loguru import logger
logger.add("logi.logs", level="ERROR")

logger.debug("Отладка: ...")
logger.info("Button_1: pressed")
logger.success("Успешно!")   #Для loguru
logger.warning("Предупреждение!")
logger.error("Тревога!!")
logger.critical("ОСТАНОВКА!!!")