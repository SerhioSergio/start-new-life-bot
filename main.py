from aiogram import Bot, Dispatcher, executor, types
from handlers.money_block import register_handlers_money
import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

# Регистрируем обработчики первой зоны
register_handlers_money(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
