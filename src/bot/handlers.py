import telebot
from loguru import logger
from src.bot.bot_instance import bot
from src.utils.extensions import CryptoConverter, ConvertionException
from src.models.data import notice, keys, valid_commands

@bot.message_handler(commands=[valid_commands['start'], valid_commands['help']])
def get_describe(message):
    bot.reply_to(message, notice['describe'])

@bot.message_handler(commands=[valid_commands['values']])
def get_currencies(message):
    text = notice['using_currency']
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

# Fallback-обработчик для ЛЮБОЙ команды, которая НЕ совпадает с разрешёнными
@bot.message_handler(func=lambda message: message.text and message.text.startswith('/'))
def unknown_command(message):
    # Извлекаем команду (без аргументов и без /)
    command = message.text.split()[0][1:].lower()
    #получаем вывод валидных команд каждая с новой строки
    valid_cmd = '\n'.join(f'/{cmd}' for cmd in valid_commands.values())
    bot.reply_to(
        message,
        f"{notice['unknown']} /{command}.\n"
        f"{notice['valid_comm']} \n{valid_cmd}"
    )

@bot.message_handler(content_types=['text', ])
def convert_message(message: telebot.types.Message):
    user = f"@{message.from_user.username}" if message.from_user.username else f"ID{message.from_user.id}"
    logger.info(f"Получено сообщение от {user}: {message.text!r}")
    try:
        text = CryptoConverter.valid_data(message.text)
        bot.send_message(message.chat.id, text)
        logger.success(f"Успешный расчёт для {user}: {message.text!r} → {text}")
    except ConvertionException as e:
        bot.reply_to(message, f'{notice['user_err']}\n{e}')
        logger.warning(f"Ошибка пользователя {user}: {e} (ввод: {message.text!r})")
    except Exception as e:
        bot.reply_to(message, f'{notice['server_err']}\n{e}')
        logger.exception(f"Критическая ошибка при обработке сообщения от {user}: {message.text!r}")


