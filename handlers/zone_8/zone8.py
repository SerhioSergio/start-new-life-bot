from aiogram.types import Message
from handlers.user_progress import update_user_progress, get_user_zone_progress
from ai_module import analyze_and_reply

ZONE_NAME = "Зона 8: Разрыв с тенью"
STEPS = [
    "День_1_утро", "День_1_вечер",
    "День_2_утро", "День_2_вечер",
    "День_3_утро", "День_3_вечер",
    "День_4_утро", "День_4_вечер",
    "День_5_утро", "День_5_вечер",
    "День_6_утро", "День_6_вечер",
    "День_7_утро", "День_7_вечер"
]

async def start_day_for_zone8(message: Message, context):
    await message.answer(f"Ты начал работу с {ZONE_NAME}.")
    await message.answer("День 1 — Утро. Готов разрушать страхи?")

async def send_morning_prompt(context, user_id, day):
    await context.bot.send_message(user_id, f"{ZONE_NAME} — День {day} утро. Пора разрушать старое.")

async def send_evening_prompt(context, user_id, day):
    await context.bot.send_message(user_id, f"{ZONE_NAME} — День {day} вечер. Подведи итоги.")
