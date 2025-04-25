from aiogram import Dispatcher
from handlers.zone_1.zone_1 import register_zone_1_handlers

def register_handlers(dp: Dispatcher):
    register_zone_1_handlers(dp)
