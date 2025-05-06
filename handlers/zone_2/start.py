from aiogram.types import Message
from aiogram.dispatcher import Dispatcher

ZONE_NAME = "Зона 2: Самооценка и уверенность"

async def start_zone(message: Message):
    await message.answer(f"Добро пожаловать в {ZONE_NAME}!\nГотов двигаться дальше?")

def register_zone_2_handlers(dp: Dispatcher):
    dp.register_message_handler(start_zone, lambda msg: msg.text.lower() == "зона 2")
