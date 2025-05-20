from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN
from handlers.register_handlers import register_handlers

import os
print("DEBUG: Текущая директория =", os.getcwd())
print("DEBUG: Содержимое =", os.listdir())

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

register_handlers(dp)

if name == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
