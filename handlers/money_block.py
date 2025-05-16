from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import Dispatcher

# Простой стартовый обработчик
async def handle_money_block_start(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Зона 1"), KeyboardButton("Зона 2"))
    keyboard.add(KeyboardButton("Зона 3"), KeyboardButton("Зона 4"))
    keyboard.add(KeyboardButton("Зона 5"), KeyboardButton("Зона 6"))
    keyboard.add(KeyboardButton("Зона 7"), KeyboardButton("Зона 8"))

    await message.answer(
        "Добро пожаловать в программу 'Start a New Life'.\n\n"
        "С какой зоны ты хочешь начать?",
        reply_markup=keyboard
    )

# Регистрация обработчика
def register_money_block_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_money_block_start, commands=["start"])
