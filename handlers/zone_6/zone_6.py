from aiogram.types import Message
from handlers.user_progress import save_user_step
from handlers.a_module import analyze_and_reply

ZONE_NAME = "Зона 5 — Тело, зажимы и внутренняя опора"
STEPS = [
    "День 1_утро", "День 1_вечер",
    "День 2_утро", "День 2_вечер",
    "День 3_утро", "День 3_вечер",
    "День 4_утро", "День 4_вечер",
    "День 5_утро", "День 5_вечер",
    "День 6_утро", "День 6_вечер",
    "День 7_утро", "День 7_вечер"
]

async def start_day_for_zone5(message: Message, context: dict):
    user_id = message.from_user.id
    step = STEPS[0]
    await save_user_step(user_id, step)
    await message.answer(
        f"Ты начал *{ZONE_NAME}*.\n\n"
        "День 1 — Утро.\n"
        "Сегодня ты начнёшь возвращаться в тело и чувствовать опору.\n\n"
        "Когда будешь готов — напиши «Продолжить»."
    )

async def send_morning_prompt(context, user_id, day):
    text = (
        f"*{ZONE_NAME}* — День {day} Утро\n\n"
        "Где в теле ты чувствуешь напряжение прямо сейчас?\n"
        "Опиши его. Что оно говорит тебе?"
    )
    await context.bot.send_message(chat_id=user_id, text=text, parse_mode="Markdown")

async def send_evening_prompt(context, user_id, day):
    text = (
        f"*{ZONE_NAME}* — День {day} Вечер\n\n"
        "Удалось ли тебе за день расслабиться?\n"
        "Как ты ощущаешь тело сейчас?"
    )
    await context.bot.send_message(chat_id=user_id, text=text, parse_mode="Markdown")

async def analyze_user_reply(message: Message):
    user_text = message.text
    feedback = await analyze_and_reply(user_text, zone="zone_5")
    await message.answer(feedback)
