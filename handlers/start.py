# Стартовая логика зоны 8
from aiogram.types import Message
from aiogram.dispatcher import Dispatcher

from handlers.zone_8.zone8 import start_day_for_zone8
from whisper_handler import transcribe_voice  # <== импорт из whisper_handler.py

from io import BytesIO

# Обработка текстового старта зоны
async def start_zone_8(message: Message):
    await start_day_for_zone8(message)

# Обработка голосового сообщения
async def handle_voice_message(message: Message):
    voice_file = await message.voice.get_file()
    voice_bytes = await voice_file.download(destination=BytesIO())
    transcript = await transcribe_voice(voice_bytes.getvalue(), extension=".ogg")

    await message.answer(f"Расшифровка голоса:\n{transcript}")

# Регистрация хендлеров
def register_zone_8_handlers(dp: Dispatcher):
    dp.register_message_handler(start_zone_8, commands=["zone_8"])
    dp.register_message_handler(handle_voice_message, content_types=["voice"])
