from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from handlers.register_handlers import register_handlers

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Добро пожаловать в Start New Life Bot!')

def run_bot():
    register_handlers(dp)
    executor.start_polling(dp, skip_updates=True)
