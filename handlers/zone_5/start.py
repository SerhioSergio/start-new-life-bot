from aiogram.types import Message
from aiogram.dispatcher import Dispatcher

ZONE_NAME = "Зона 5: Уверенность и речь"

async def start_zone(message: Message):
    await message.answer(f"Добро пожаловать в {ZONE_NAME}!\nСегодня работаем с голосом и внутренней силой.")

def register_zone_5_handlers(dp: Dispatcher):
    dp.register_message_handler(start_zone, lambda msg: msg.text.lower() == "зона 5")
