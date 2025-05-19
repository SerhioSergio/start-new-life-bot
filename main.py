from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN
from handlers.register_handlers import register_handlers

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

print("Запуск бота...")
register_handlers(dp)
print("Хендлеры подключены, начинаем polling...")

if name == "__main__":
    executor.start_polling(dp, skip_updates=True)
