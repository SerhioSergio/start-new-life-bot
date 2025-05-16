from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import Dispatcher
from handlers.zone_1.start import register_zone_1_handlers, process_zone as zone_1_process
from handlers.zone_2.start import register_zone_2_handlers, process_zone as zone_2_process
from handlers.zone_3.start import register_zone_3_handlers, process_zone as zone_3_process
from handlers.zone_4.start import register_zone_4_handlers, process_zone as zone_4_process
from handlers.zone_5.start import register_zone_5_handlers, process_zone as zone_5_process
from handlers.zone_6.start import register_zone_6_handlers, process_zone as zone_6_process
from handlers.zone_7.start import register_zone_7_handlers, process_zone as zone_7_process
from handlers.zone_8.start import register_zone_8_handlers, process_zone as zone_8_process

# Главное меню
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

# Обработчик выбора зоны
async def handle_zone_selection(message: Message):
    text = message.text.strip().lower()
    if text == "зона 1":
        await zone_1_process(message)
    elif text == "зона 2":
        await zone_2_process(message)
    elif text == "зона 3":
        await zone_3_process(message)
    elif text == "зона 4":
        await zone_4_process(message)
    elif text == "зона 5":
        await zone_5_process(message)
    elif text == "зона 6":
        await zone_6_process(message)
    elif text == "зона 7":
        await zone_7_process(message)
    elif text == "зона 8":
        await zone_8_process(message)
    else:
        await message.answer("Я не понял, какую зону ты выбрал. Попробуй снова.")

# Регистрация
def register_money_block_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_money_block_start, commands=["start"])
    dp.register_message_handler(handle_zone_selection, lambda msg: msg.text.lower().startswith("зона"))
