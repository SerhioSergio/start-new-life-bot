from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import Dispatcher

# Импорты всех зон
from handlers.zone_1.start import process_zone_1_process
from handlers.zone_2.start import process_zone_2_process
from handlers.zone_3.start import process_zone_3_process
from handlers.zone_4.start import process_zone_4_process
from handlers.zone_5.start import process_zone_5_process
from handlers.zone_6.start import process_zone_6_process
from handlers.zone_7.start import process_zone_7_process
from handlers.zone_8.start import process_zone_8_process

# Команда /start
async def handle_money_block_start(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(1, 9):
        keyboard.add(KeyboardButton(f"Зона {i}"))

    await message.answer(
        "Добро пожаловать в трансформационную программу *Start a New Life*!\n\n"
        "Выбери, с какой зоны ты хочешь начать:",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

# Выбор зоны
async def handle_zone_selection(message: Message):
    text = message.text.strip().lower()

    zone_map = {
        "зона 1": process_zone_1_process,
        "зона 2": process_zone_2_process,
        "зона 3": process_zone_3_process,
        "зона 4": process_zone_4_process,
        "зона 5": process_zone_5_process,
        "зона 6": process_zone_6_process,
        "зона 7": process_zone_7_process,
        "зона 8": process_zone_8_process,
    }

    if text in zone_map:
        await zone_map[text](message)
    else:
        await message.answer("Кажется, ты выбрал зону неправильно. Попробуй ещё раз.")

# Регистрация хендлеров
def register_money_block_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_money_block_start, commands=["start"])
    dp.register_message_handler(handle_zone_selection, lambda msg: msg.text.lower().startswith("зона"))
