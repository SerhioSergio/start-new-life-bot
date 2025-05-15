import whisper

model = whisper.load_model("base")  # Можно "small", "medium", "large" — base быстрее

def transcribe_voice(file_path):
    try:
        result = model.transcribe(file_path)
        return result["text"]
    except Exception as e:
        return f"[Ошибка расшифровки: {e}]"
