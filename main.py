from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN
from handlers.register_handlers import register_handlers

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

print("Бот запущен")

register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
