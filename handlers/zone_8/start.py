from aiogram.types import Message
from aiogram.dispatcher import Dispatcher
from handlers.zone_8.zone8 import start_day_for_zone8

async def start_zone_8(message: Message, context):
    await start_day_for_zone8(message, context)

def register_zone_8(dp: Dispatcher):
    pass
