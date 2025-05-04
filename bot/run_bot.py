from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

def start(update: Update, context: CallbackContext):
    main_menu_keyboard = [['Начать Зону 1 — Деньги и Самооценка']]
    main_menu_markup = ReplyKeyboardMarkup(main_menu_keyboard, resize_keyboard=True)
    update.message.reply_text(
        "Добро пожаловать в Start a New Life!",
        reply_markup=main_menu_markup
    )

def handle_main_menu(update: Update, context: CallbackContext):
    text = update.message.text
    if text == 'Начать Зону 1 — Деньги и Самооценка':
        update.message.reply_text(
            "🚀 Отлично! Начинаем Зону 1 — *Деньги и Самооценка*.

"
            "*День 1. Утро:*

"
            "_«Я достоин жить достойно. Деньги — это инструмент моей свободы, а не доказательство моей ценности.»_

"
            "👉 Что ты выбираешь чувствовать, когда думаешь о деньгах?

"
            "(Напиши прямо сюда — бот сохранит твой ответ и вечером продолжит работу.)",
            parse_mode="Markdown"
        )

def run_bot():
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text('Начать Зону 1 — Деньги и Самооценка'), handle_main_menu))

    updater.start_polling()
    updater.idle()
