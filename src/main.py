from bot import handlers  # импортируем, чтобы зарегистрировать обработчики
from bot.bot_instance import bot

if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()