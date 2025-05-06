from aiogram.types import Message
from aiogram.dispatcher import Dispatcher

ZONE_NAME = "Зона 6: Самоценность и смысл"

async def start_zone(message: Message):
    await message.answer(f"Добро пожаловать в {ZONE_NAME}!\nНайдём опору в себе и в своём пути.")

def register_zone_6_handlers(dp: Dispatcher):
    dp.register_message_handler(start_zone, lambda msg: msg.text.lower() == "зона 6")
