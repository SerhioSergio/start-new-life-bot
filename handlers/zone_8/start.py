from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import Dispatcher
from handlers.user_progress import get_user_step, save_user_step

ZONE_NAME = "Зона 8: Разрыв с тенью"

steps = [
    "День_1_утро", "День_1_вечер",
    "День_2_утро", "День_2_вечер",
    "День_3_утро", "День_3_вечер",
    "День_4_утро", "День_4_вечер",
    "День_5_утро", "День_5_вечер",
    "День_6_утро", "День_6_вечер",
    "День_7_утро", "День_7_вечер",
]

step_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
step_keyboard.add(KeyboardButton("Продолжить"))
step_keyboard.add(KeyboardButton("Назад"), KeyboardButton("Выйти"))

async def process_zone(message: Message):
    user_id = message.from_user.id
    step = get_user_step(user_id, "zone_8") or 0

    if step >= len(steps):
        await message.answer(f"{ZONE_NAME} завершена.")
        return

    await message.answer(f"{ZONE_NAME} — {steps[step]}", reply_markup=step_keyboard)
    save_user_step(user_id, "zone_8", step)

async def handle_buttons(message: Message):
    user_id = message.from_user.id
    step = get_user_step(user_id, "zone_8") or 0

    if message.text == "Продолжить":
        step += 1
    elif message.text == "Назад" and step > 0:
        step -= 1
    elif message.text == "Выйти":
        await message.answer("Вы вышли из зоны.")
        return

    if step >= len(steps):
        await message.answer(f"{ZONE_NAME} завершена.")
        return

    await message.answer(f"{ZONE_NAME} — {steps[step]}", reply_markup=step_keyboard)
    save_user_step(user_id, "zone_8", step)

def register_zone_8_handlers(dp: Dispatcher):
    dp.register_message_handler(process_zone, lambda msg: msg.text.lower() == "зона 8")
    dp.register_message_handler(handle_buttons, lambda msg: msg.text in ["Продолжить", "Назад", "Выйти"])
