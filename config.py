import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Токен Telegram-бота
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Проверка на случай, если токен не найден
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден. Убедись, что файл .env существует и переменная задана.")
