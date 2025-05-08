
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

async def transcribe_voice(file_path):
    try:
        with open(file_path, "rb") as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript["text"]
    except Exception as e:
        return f"[Ошибка расшифровки голоса: {e}]"
