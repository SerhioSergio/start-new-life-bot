from aiogram.types import Message
from handlers.user_progress import save_user_step
from handlers.a_module import analyze_and_reply

ZONE_NAME = "Зона 1 — Деньги и самооценка"
STEPS = [
    "День 1_утро", "День 1_вечер",
    "День 2_утро", "День 2_вечер",
    "День 3_утро", "День 3_вечер",
    "День 4_утро", "День 4_вечер",
    "День 5_утро", "День 5_вечер",
    "День 6_утро", "День 6_вечер",
    "День 7_утро", "День 7_вечер"
]

# Запуск первого шага зоны
async def start_day_for_zone1(message: Message, context: dict):
    user_id = message.from_user.id
    step = STEPS[0]  # "День 1_утро"
    await save_user_step(user_id, step)

    await message.answer(
        f"Ты начал работу в *{ZONE_NAME}*.\n\n"
        "День 1 — Утро.\n"
        "Сегодня мы заложим основу уверенности и ценности себя.\n\n"
        "Когда будешь готов — напиши: «Продолжить»."
    )

# Утренний промпт
async def send_morning_prompt(context, user_id, day):
    await context.bot.send_message(
        chat_id=user_id,
        text=(
            f"*{ZONE_NAME}* — День {day} Утро\n\n"
            "Сегодня ты начинаешь с основ. Ответь честно:\n"
            "*Что для тебя деньги?*\n"
            "Просто цифры? Безопасность? Способ признания?\n\n"
            "Напиши, не думая долго — и отправь, как есть."
        ),
        parse_mode="Markdown"
    )

# Вечерний промпт
async def send_evening_prompt(context, user_id, day):
    await context.bot.send_message(
        chat_id=user_id,
        text=(
            f"*{ZONE_NAME}* — День {day} Вечер\n\n"
            "Вспомни, как прошёл день. Ответь:\n"
            "*Что ты понял о своей ценности?*\n"
            "Есть ли связь между самооценкой и деньгами в твоей жизни?"
        ),
        parse_mode="Markdown"
    )

# Анализ ответа (опционально)
async def analyze_user_reply(message: Message):
    user_id = message.from_user.id
    user_text = message.text
    feedback = await analyze_and_reply(user_text, zone="zone_1")
    
    await message.answer(feedback)
