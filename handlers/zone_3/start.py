from aiogram.types import Message
from aiogram.dispatcher import Dispatcher

ZONE_NAME = "Зона 3: Отношения и границы"

async def start_zone(message: Message):
    await message.answer(f"Добро пожаловать в {ZONE_NAME}!\nПоговорим о твоих границах и близости.")

def register_zone_3_handlers(dp: Dispatcher):
    dp.register_message_handler(start_zone, lambda msg: msg.text.lower() == "зона 3")
