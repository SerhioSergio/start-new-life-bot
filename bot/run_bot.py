from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

from config import BOT_TOKEN
from handlers.scheduler import send_prompt
from handlers.user_progress import load_progress
from handlers.money_block import start_zone
from handlers import (
    zone_1, zone_2, zone_3, zone_4, zone_5, zone_6, zone_7, zone_8
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
    [InlineKeyboardButton("Зона 1: Деньги и самооценка", callback_data="zone_1")],
    [InlineKeyboardButton("Зона 2: Энергия и восстановление", callback_data="zone_2")],
    [InlineKeyboardButton("Зона 3: Отношения и границы", callback_data="zone_3")],
    [InlineKeyboardButton("Зона 4: Цели и предназначение", callback_data="zone_4")],
    [InlineKeyboardButton("Зона 5: Осознанность и тело", callback_data="zone_5")],
    [InlineKeyboardButton("Зона 6: Перепрошивка и трансформация", callback_data="zone_6")],
    [InlineKeyboardButton("Зона 7: Выход из выгорания", callback_data="zone_7")],
    [InlineKeyboardButton("Зона 8: Разрыв с тенью. Перерождение", callback_data="zone_8")],
    [InlineKeyboardButton("Отправить утро", callback_data="send_morning")],
    [InlineKeyboardButton("Отправить вечер", callback_data="send_evening")]
]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выбери зону, с которой хочешь начать:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    zone_name = query.data
if zone_name == "send_morning":
        progress = load_progress()
        for user_id, zones in progress.items():
            for zone, zone_data in zones.items():
                day = int(zone_data.get("day", 1))
                await send_prompt(zone, user_id, day, is_morning=True)
        await query.edit_message_text("Утренние напоминания отправлены.")
        return

    elif zone_name == "send_evening":
        progress = load_progress()
        for user_id, zones in progress.items():
            for zone, zone_data in zones.items():
                day = int(zone_data.get("day", 1))
                await send_prompt(zone, user_id, day, is_morning=False)
        await query.edit_message_text("Вечерние напоминания отправлены.")
        return
        
    zone_map = {
        "zone_1": (zone_1, 1),
        "zone_2": (zone_2, 2),
        "zone_3": (zone_3, 3),
        "zone_4": (zone_4, 4),
        "zone_5": (zone_5, 5),
        "zone_6": (zone_6, 6),
        "zone_7": (zone_7, 7),
        "zone_8": (zone_8, 8),
    }

    if zone_name in zone_map:
        module, number = zone_map[zone_name]
        await start_zone(update, context, module, number)

if name == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()
