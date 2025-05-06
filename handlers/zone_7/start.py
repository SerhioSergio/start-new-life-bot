from aiogram.types import Message
from aiogram.dispatcher import Dispatcher

ZONE_NAME = "Зона 7: Выход из выгорания"

async def start_zone(message: Message):
    await message.answer(f"Добро пожаловать в {ZONE_NAME}!\nБудем восстанавливаться — мягко, но мощно.")

def register_zone_7_handlers(dp: Dispatcher):
    dp.register_message_handler(start_zone, lambda msg: msg.text.lower() == "зона 7")
