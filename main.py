from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN
import handlers.register_handlers as register_handlers

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

print("Бот запущен")

if __name__ == "__main__":
    import asyncio
    from telegram.ext import ApplicationBuilder

    register_handlers.register_handlers(dp)

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.run_polling()
