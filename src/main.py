from loguru import logger
from src.bot import handlers  # импортируем, чтобы зарегистрировать обработчики
from src.bot.bot_instance import bot

logger.add(
    "logs/bot.log",
    rotation="10 MB",
    retention="7 days",
    compression="zip",
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    encoding="utf-8"
)



if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling() #for dev
    #bot.infinity_polling() #for prod (with restart server)
