
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import Dispatcher
from handlers.user_progress import get_user_step, save_user_step

ZONE_NAME = "Зона 7: Выход из выгорания"

steps = [
    "день_1_утро", "день_1_вечер",
    "день_2_утро", "день_2_вечер",
    "день_3_утро", "день_3_вечер",
    "день_4_утро", "день_4_вечер",
    "день_5_утро", "день_5_вечер",
    "день_6_утро", "день_6_вечер",
    "день_7_утро", "день_7_вечер"
]

messages = {
    step: f"Это {step.replace('_', ' ')} в {ZONE_NAME}." for step in steps
}

def get_step_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Продолжить"))
    keyboard.add(KeyboardButton("Назад"))
    keyboard.add(KeyboardButton("Выйти"))
    return keyboard

async def process_zone(message: Message):
    user_id = message.from_user.id
    step = get_user_step(user_id, "zone_7")
    if step is None:
        step = 0
    await message.answer(messages[steps[step]], reply_markup=get_step_keyboard())
    save_user_step(user_id, "zone_7", step)

async def handle_buttons(message: Message):
    user_id = message.from_user.id
    step = get_user_step(user_id, "zone_7")
    if step is None:
        step = 0

    if message.text == "Продолжить" and step < len(steps) - 1:
        step += 1
    elif message.text == "Назад" and step > 0:
        step -= 1
    elif message.text == "Выйти":
        await message.answer("Вы вышли в главное меню.", reply_markup=None)
        save_user_step(user_id, "zone_7", 0)
        return

    await message.answer(messages[steps[step]], reply_markup=get_step_keyboard())
    save_user_step(user_id, "zone_7", step)

def register_zone_7_handlers(dp: Dispatcher):
    dp.register_message_handler(process_zone, lambda msg: msg.text.lower() == "зона 7")
    dp.register_message_handler(handle_buttons, lambda msg: msg.text in ["Продолжить", "Назад", "Выйти"])
