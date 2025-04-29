from aiogram import types, Dispatcher

def register_zone_1_handlers(dp: Dispatcher):
    @dp.message_handler(lambda message: message.text.lower() == 'деньги')
    async def money_zone(message: types.Message):
        await message.answer('Зона 1: Деньги и самооценка — начинаем!')