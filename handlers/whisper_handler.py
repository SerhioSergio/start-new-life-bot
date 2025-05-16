import os
import whisper
from uuid import uuid4
from aiogram.types import Message
from aiogram.dispatcher import Dispatcher

model = whisper.load_model("base")  # Можно заменить на "small", "medium", "large"

async def transcribe_voice(voice_bytes: bytes, extension: str = ".ogg") -> str:
    filename = f"temp_audio_{uuid4().hex}{extension}"

    # Сохраняем аудио во временный файл
    with open(filename, "wb") as f:
        f.write(voice_bytes)

    try:
        # Распознаём речь
        result = model.transcribe(filename)
        text = result.get("text", "").strip()
    except Exception as e:
        text = f"(Ошибка распознавания голоса: {e})"
    finally:
        os.remove(filename)

    return text

async def handle_voice(message: Message):
    voice = await message.voice.download()
    file_bytes = await voice.read()
    text = await transcribe_voice(file_bytes)
    await message.answer(f"Распознано: {text}")

def register_voice_handler(dp: Dispatcher):
    dp.register_message_handler(handle_voice, content_types=["voice"])
