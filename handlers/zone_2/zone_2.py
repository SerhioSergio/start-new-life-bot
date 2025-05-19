from aiogram.types import Message
from handlers.user_progress import save_user_step
from handlers.a_module import analyze_and_reply

ZONE_NAME = "Зона 2 — Отношения и личные границы"
STEPS = [
    "День 1_утро", "День 1_вечер",
    "День 2_утро", "День 2_вечер",
    "День 3_утро", "День 3_вечер",
    "День 4_утро", "День 4_вечер",
    "День 5_утро", "День 5_вечер",
    "День 6_утро", "День 6_вечер",
    "День 7_утро", "День 7_вечер"
]

async def start_day_for_zone2(message: Message, context: dict):
    user_id = message.from_user.id
    step = STEPS[0]
    await save_user_step(user_id, step)
    await message.answer(
        f"Ты начал *{ZONE_NAME}*.\n\n"
        "День 1 — Утро.\n"
        "Сегодня мы посмотрим, как ты ставишь границы и что терпишь.\n\n"
        "Напиши «Продолжить», как будешь готов."
    )

async def send_morning_prompt(context, user_id, day):
    text = (
        f"*{ZONE_NAME}* — День {day} Утро\n\n"
        "Где ты чаще всего не говоришь «нет», когда хочешь?\n"
        "Почему тебе сложно отстоять себя?"
    )
    await context.bot.send_message(chat_id=user_id, text=text, parse_mode="Markdown")

async def send_evening_prompt(context, user_id, day):
    text = (
        f"*{ZONE_NAME}* — День {day} Вечер\n\n"
        "Подумай, где сегодня ты поступил не по своей воле?\n"
        "Что тебе мешает быть честным с собой?"
    )
    await context.bot.send_message(chat_id=user_id, text=text, parse_mode="Markdown")

async def analyze_user_reply(message: Message):
    user_text = message.text
    feedback = await analyze_and_reply(user_text, zone="zone_2")
    await message.answer(feedback)
