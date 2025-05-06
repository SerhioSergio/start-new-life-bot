from aiogram.types import Message
from aiogram.dispatcher import Dispatcher

# Уникальное приветствие для каждой зоны (можешь изменить)
ZONE_NAME = "Зона 1: Деньги и самооценка"

async def start_zone(message: Message):
    await message.answer(f"Добро пожаловать в {ZONE_NAME}!\nДавай начнём работу.")

def register_zone_1_handlers(dp: Dispatcher):
    dp.register_message_handler(start_zone, lambda msg: msg.text.lower() == "зона 1")
