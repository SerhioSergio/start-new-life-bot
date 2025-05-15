# Logic for zone_2
from aiogram.types import Message
from handlers.user_progress import save_user_step
from handlers.ai_module import analyze_and_reply

ZONE_NAME = "Зона 2: Энергия и восстановление"
STEPS = [
    "День_1_утро", "День_1_вечер",
    "День_2_утро", "День_2_вечер",
    "День_3_утро", "День_3_вечер",
    "День_4_утро", "День_4_вечер",
    "День_5_утро", "День_5_вечер",
    "День_6_утро", "День_6_вечер",
    "День_7_утро", "День_7_вечер",
]

async def start_day_for_zone2(message: Message, context):
    user_id = message.from_user.id
    await save_user_step(user_id, "zone_2", "День_1_утро")

    await message.answer(f"Ты начал работу с {ZONE_NAME}")
    await message.answer("День 1. Утро. Готов вернуть себе энергию? Начнём с осознания, куда она уходит.")

async def send_morning_prompt(context, user_id, day):
    await context.bot.send_message(user_id, f"{ZONE_NAME} — День {day} утро. Где ты теряешь энергию чаще всего?")

async def send_evening_prompt(context, user_id, day):
    await context.bot.send_message(user_id, f"{ZONE_NAME} — День {day} вечер. Что сегодня наполнило тебя силой?")
