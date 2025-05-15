import os
import whisper
from uuid import uuid4

model = whisper.load_model("base")  # Можно заменить на "small", "medium", "large" при необходимости

async def transcribe_voice(voice: bytes, extension: str = ".ogg") -> str:
    filename = f"temp_audio_{uuid4().hex}{extension}"
    
    # Сохраняем аудиофайл
    with open(filename, "wb") as f:
        f.write(voice)

    try:
        # Расшифровываем
        result = model.transcribe(filename)
        text = result.get("text", "").strip()
    except Exception as e:
        text = f"[Ошибка распознавания голоса: {e}]"
    finally:
        os.remove(filename)

    return text
