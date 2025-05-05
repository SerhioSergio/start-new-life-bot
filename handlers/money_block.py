
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import json
import os

# Путь к JSON-файлу с пользователями
USER_DATA_PATH = "users.json"
TEXTS_PATH = "content/money_selfworth_full_week"
AUDIO_PATH = "content/money_selfworth_full_week"

# Загрузка данных пользователя
def load_users():
    if not os.path.exists(USER_DATA_PATH):
        return {}
    with open(USER_DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(data):
    with open(USER_DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Обработчик команды /start_zone1
async def start_zone1(message: types.Message):
    users = load_users()
    user_id = str(message.from_user.id)
    users[user_id] = {"zone": 1, "day": 1, "part": "morning"}
    save_users(users)
    await send_day_part(message, 1, "morning")

# Отправка текста и аудио на текущий этап
async def send_day_part(message, day, part):
    day_key = f"day{day}_{part}"
    text_file = os.path.join(TEXTS_PATH, f"{day_key}.txt")
    audio_file = os.path.join(AUDIO_PATH, f"{day_key}.mp3")

    if os.path.exists(text_file):
        with open(text_file, "r", encoding="utf-8") as f:
            await message.answer(f.read())
    if os.path.exists(audio_file):
        with open(audio_file, "rb") as audio:
            await message.answer_voice(audio)

    if part == "morning":
        kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Ответить на вечерний вопрос"))
        await message.answer("Вечером вернись, чтобы продолжить день.", reply_markup=kb)
    else:
        kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Следующий день"))
        await message.answer("Молодец. Продолжим завтра.", reply_markup=kb)

# Обработка вечернего вопроса
async def handle_evening(message: types.Message):
    users = load_users()
    user_id = str(message.from_user.id)
    if user_id not in users:
        await message.answer("Сначала начни зону командой /start_zone1")
        return

    users[user_id]["part"] = "evening"
    day = users[user_id]["day"]
    save_users(users)
    await send_day_part(message, day, "evening")

# Обработка перехода к следующему дню
async def next_day(message: types.Message):
    users = load_users()
    user_id = str(message.from_user.id)
    if user_id not in users:
        await message.answer("Сначала начни зону командой /start_zone1")
        return

    if users[user_id]["day"] >= 7:
        await message.answer("Ты прошёл всю зону «Деньги и самооценка».")
        return

    users[user_id]["day"] += 1
    users[user_id]["part"] = "morning"
    save_users(users)
    await send_day_part(message, users[user_id]["day"], "morning")

def register_handlers_money(dp: Dispatcher):
    dp.register_message_handler(start_zone1, commands=["start_zone1"])
    dp.register_message_handler(handle_evening, Text(equals="Ответить на вечерний вопрос"))
    dp.register_message_handler(next_day, Text(equals="Следующий день"))
