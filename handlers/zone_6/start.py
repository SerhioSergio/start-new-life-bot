from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import Dispatcher
from handlers.user_progress import get_user_step, save_user_step

ZONE_NAME = "Зона 6"

steps = [
    "Утро 1", "Вечер 1",
    "Утро 2", "Вечер 2",
    "Утро 3", "Вечер 3",
    "Утро 4", "Вечер 4",
    "Утро 5", "Вечер 5",
    "Утро 6", "Вечер 6",
    "Утро 7", "Вечер 7"
]
steps = [f"{step} ({ZONE_NAME})" for step in steps]

def get_step_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Продолжить"))
    keyboard.add(KeyboardButton("Назад"))
    keyboard.add(KeyboardButton("Выйти"))
    return keyboard

async def process_zone_6(message: Message):
    user_id = message.from_user.id
    step = get_user_step(user_id, "zone_6") or 0

    if message.text.lower() in ["продолжить", "назад", "выйти"] and step > 0:
        if message.text.lower() == "продолжить" and step < len(steps) - 1:
            step += 1
        elif message.text.lower() == "назад" and step > 0:
            step -= 1
        elif message.text.lower() == "выйти":
            await message.answer("Ты вышел из зоны. Возвращайся, когда будешь готов.")
            return
        save_user_step(user_id, "zone_6", step)

    await message.answer(steps[step], reply_markup=get_step_keyboard())
    save_user_step(user_id, "zone_6", step)

def register_zone_6_handlers(dp: Dispatcher):
    dp.register_message_handler(process_zone_6, lambda msg: msg.text.lower() in ["продолжить", "назад", "выйти"])
