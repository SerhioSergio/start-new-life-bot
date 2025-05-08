from dotenv import load_dotenv
import os

# Загружаем переменные из .env или из окружения (Render и т.д.)
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")