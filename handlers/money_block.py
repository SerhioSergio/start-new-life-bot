from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import Dispatcher

from handlers.zone_1.start import register_zone_1_handlers, process_zone
from handlers.zone_2.start import register_zone_2_handlers, process_zone_2
from handlers.zone_3.start import register_zone_3_handlers, process_zone_3
from handlers.zone_4.start import register_zone_4_handlers, process_zone_4
from handlers.zone_5.start import register_zone_5_handlers, process_zone_5
from handlers.zone_6.start import register_zone_6_handlers, process_zone_6
from handlers.zone_7.start import register_zone_7_handlers, process_zone_7
from handlers.zone_8.start import register_zone_8_handlers, process_zone_8

async def handle_money_block_start(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(1, 9):
        keyboard.add(KeyboardButton(f"Зона {i}"))

    await message.answer(
        "Добро пожаловать в программу 'Start a New Life'\n\nС какой зоны ты хочешь начать?",
        reply_markup=keyboard
    )

async def handle_zone_selection(message: Message):
    text = message.text.strip().lower()
    if text == "зона 1":
        await process_zone(message)
    elif text == "зона 2":
        await process_zone_2(message)
    elif text == "зона 3":
        await process_zone_3(message)
    elif text == "зона 4":
        await process_zone_4(message)
    elif text == "зона 5":
        await process_zone_5(message)
    elif text == "зона 6":
        await process_zone_6(message)
    elif text == "зона 7":
        await process_zone_7(message)
    elif text == "зона 8":
        await process_zone_8(message)
    else:
        await message.answer("Такой зоны нет. Попробуй снова.")

def register_money_block_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_money_block_start, commands=["start"])
    dp.register_message_handler(handle_zone_selection, lambda msg: msg.text.lower().startswith("зона"))
