from aiogram.types import Message
from aiogram.dispatcher import Dispatcher

from handlers.zone_1.start import register_zone_1_handlers
from handlers.zone_2.start import register_zone_2_handlers
from handlers.zone_3.start import register_zone_3_handlers
from handlers.zone_4.start import register_zone_4_handlers
from handlers.zone_5.start import register_zone_5_handlers
from handlers.zone_6.start import register_zone_6_handlers
from handlers.zone_7.start import register_zone_7_handlers


async def start_block_command(message: Message):
    await message.answer("Добро пожаловать! Напиши, какую зону хочешь начать: Зона 1 … Зона 7")


def register_money_block_handlers(dp: Dispatcher):
    dp.register_message_handler(start_block_command, commands=["start"])

    # Регистрируем все 7 зон
    register_zone_1_handlers(dp)
    register_zone_2_handlers(dp)
    register_zone_3_handlers(dp)
    register_zone_4_handlers(dp)
    register_zone_5_handlers(dp)
    register_zone_6_handlers(dp)
    register_zone_7_handlers(dp)
