from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

from config import BOT_TOKEN
from handlers.money_block import start_zone
from handlers import (
    zone_1, zone_2, zone_3, zone_4, zone_5, zone_6, zone_7
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
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выбери зону, с которой хочешь начать:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    zone_name = query.data
    await start_zone(zone_name, query, context)

if name == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()
