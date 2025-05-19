from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from handlers.zone_1.zone_1 import start_day_for_zone1
from handlers.zone_2.zone_2 import start_day_for_zone2
from handlers.zone_3.zone_3 import start_day_for_zone3
from handlers.zone_4.zone_4 import start_day_for_zone4
from handlers.zone_5.zone_5 import start_day_for_zone5
from handlers.zone_6.zone_6 import start_day_for_zone6
from handlers.zone_7.zone_7 import start_day_for_zone7
from handlers.zone_8.zone_8 import start_day_for_zone8

# Кнопки для выбора зоны
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(
    KeyboardButton("Зона 1"), KeyboardButton("Зона 2"),
    KeyboardButton("Зона 3"), KeyboardButton("Зона 4"),
    KeyboardButton("Зона 5"), KeyboardButton("Зона 6"),
    KeyboardButton("Зона 7"), KeyboardButton("Зона 8")
)

# Обработка команды /start
async def start_command(message: types.Message):
    await message.answer(
        "Привет! Это бот *Start New Life*.\n\n"
        "Здесь начинается твоя трансформация.\n"
        "Выбери зону, с которой хочешь начать:",
        reply_markup=keyboard
    )

# Обработка кнопок выбора зоны
async def handle_zone_selection(message: types.Message):
    text = message.text.lower()

    if text == "зона 1":
        await start_day_for_zone1(message, context={})
    elif text == "зона 2":
        await start_day_for_zone2(message, context={})
    elif text == "зона 3":
        await start_day_for_zone3(message, context={})
    elif text == "зона 4":
        await start_day_for_zone4(message, context={})
    elif text == "зона 5":
        await start_day_for_zone5(message, context={})
    elif text == "зона 6":
        await start_day_for_zone6(message, context={})
    elif text == "зона 7":
        await start_day_for_zone7(message, context={})
    elif text == "зона 8":
        await start_day_for_zone8(message, context={})
    else:
        await message.answer("Пожалуйста, выбери одну из доступных зон.")

# Регистрация хендлеров
def register_money_block_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=["start"])
    dp.register_message_handler(handle_zone_selection)
