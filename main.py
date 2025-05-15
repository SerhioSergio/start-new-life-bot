from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN
from handlers.register_handlers import register_handlers

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

print("Бот запущен")

register_handlers(dp)

if __name__ == "__main__":
    import asyncio
    from handlers import register_handlers  # замени на свой модуль
    from telegram.ext import ApplicationBuilder

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    register_handlers(app)
    app.run_polling()  # именно polling, не webhook!
