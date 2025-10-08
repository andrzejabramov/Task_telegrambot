crypto-compare-bot/
├── .env                           # Переменные окружения (токен бота)
├── .gitignore                     # Игнорируем .env, __pycache__ и т.д.
├── README.md                      # Описание проекта (будет ТЗ)
├── requirements.txt               # Зависимости
├── src/
|   |--- main.py                   # Точка входа
|   |--- config/
│        └── settings.py           # Загрузка настроек из .env
|   |----api/
│        └── crypto_compare.py     # Работа с API CryptoCompare
|   |---- bot/
│        ├── __init__.py
│        ├── handlers.py           # Обработчики команд Telegram
│        └── bot_instance.py       # Инициализация бота
|   |----utils/
         └── schemas.py            # Валидация ввода (опционально)
         |-- currency.py           # словарь валют
         |-- extentions.py         # классы (исключения)


# Бот сравнения криптовалют

Простой Telegram-бот для получения текущего курса криптовалюты к фиатной или другой криптовалюте с использованием [CryptoCompare API](https://min-api.cryptocompare.com/).

## 📌 Функционал

- Поддержка команды `/start` — приветствие и инструкция.
- Поддержка команды `/price <FROM> <TO>` — получение курса, например:  
  `/price BTC USD` → `1 BTC = 61234.56 USD`
- Обработка ошибок: неверный формат, неизвестная валюта и т.д.
- Поддержка нескольких валют одновременно (опционально): `/price BTC,ETH USD`

## 🛠 Технологии

- Python 3.8+
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- [CryptoCompare Public API](https://min-api.cryptocompare.com/)
- `python-dotenv` для управления секретами
- `requests` для HTTP-запросов

## 📁 Структура проекта

См. дерево файлов выше.

## ⚙️ Установка

1. Клонируйте репозиторий
2. Создайте `.env` файл:
   ```env
   TELEGRAM_BOT_TOKEN=ваш_токен_от_BotFather
   
## Результат работы:

![page1](https://github.com/andrzejabramov/Task_telegrambot/blob/master/img/Снимок%20экрана%202025—10—08%20в%2017.34.13.jpeg.png)
![page2](https://github.com/andrzejabramov/Task_telegrambot/blob/master/img/Снимок%20экрана%202025—10—08%20в%2017.35.48.jpeg.png)
![page3](https://github.com/andrzejabramov/Task_telegrambot/blob/master/img/Снимок%20экрана%202025—10—08%20в%2017.36.21.jpeg.png)
