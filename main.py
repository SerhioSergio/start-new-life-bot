from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

print("Бот запущен")

# Здесь можно подключить хендлеры, если они есть
# from handlers import register_handlers
# register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
