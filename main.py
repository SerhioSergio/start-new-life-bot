from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN
from handlers import register_handlers  # <- без отступов слева!

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

print("Бот запущен")

register_handlers(dp)

if name == "__main__":
    executor.start_polling(dp, skip_updates=True)
