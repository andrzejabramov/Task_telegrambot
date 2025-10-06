from telebot import types
from bot_instance import bot
from src.api.crypto_compare import get_price

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Используй /price <FROM> <TO>, например: /price BTC USD")

@bot.message_handler(commands=['price'])
def handle_price(message):
    try:
        parts = message.text.split()
        if len(parts) != 3:
            raise ValueError("Неверный формат. Используй: /price BTC USD")
        _, from_cur, to_cur = parts
        price = get_price(from_cur, to_cur)
        bot.reply_to(message, f"1 {from_cur.upper()} = {price:.2f} {to_cur.upper()}")
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")