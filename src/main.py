from src.bot import handlers  # импортируем, чтобы зарегистрировать обработчики
from src.bot.bot_instance import bot


if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling() #for dev
    #bot.infinity_polling() #for prod (with restart server)
