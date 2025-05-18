from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN
from handlers.register_handlers import register_handlers

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

print("Инициализация бота...")

register_handlers(dp)

print("Хендлеры зарегистрированы")
print("Запуск polling...")

executor.start_polling(dp, skip_updates=True)
