import os
import whisper
from uuid import uuid4
from aiogram.types import Message
from aiogram.dispatcher import Dispatcher

# Загружаем модель
model = whisper.load_model("small")  # можно заменить на "base", "medium", "large"

# Распознавание
async def transcribe_voice(voice_bytes: bytes, extension: str = ".ogg") -> str:
    filename = f"temp_audio_{uuid4().hex}{extension}"

    with open(filename, "wb") as f:
        f.write(voice_bytes)

    try:
        result = model.transcribe(filename)
        text = result.get("text", "").strip()
    except Exception as e:
        text = f"(Ошибка распознавания голоса: {e})"
    finally:
        os.remove(filename)

    return text

# Обработка голосового сообщения
async def handle_voice(message: Message):
    voice = await message.voice.download()
    file_bytes = await voice.read()

    # HWLOG: вывод в консоль Render
    print(f"[HWLOG] Получено голосовое. Размер: {len(file_bytes)} байт")

    # Проверка на длину аудио
    if len(file_bytes) > 25_000_000:
        await message.answer("Голосовое слишком длинное. Пожалуйста, до 60 секунд.")
        return

    await message.answer("Распознаю голос...")

    text = await transcribe_voice(file_bytes)
    await message.answer(f"Распознано: {text}")

# Регистрация обработчика
def register_voice_handler(dp: Dispatcher):
    dp.register_message_handler(handle_voice, content_types=["voice"])
