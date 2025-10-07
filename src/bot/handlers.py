from telebot import types
from src.bot.bot_instance import bot
from src.api.crypto_compare import get_price
from src.utils.data import notice, keys

@bot.message_handler(commands=['start', 'help'])
def get_describe(message):
    bot.reply_to(message, notice['describe'])

@bot.message_handler(commands=['values'])
def get_currencies(message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

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