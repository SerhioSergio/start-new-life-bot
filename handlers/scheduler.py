
import asyncio
from datetime import datetime, timedelta
from aiogram import Bot
from handlers.user_progress import get_current_day
import json

async def send_morning_message(bot: Bot, user_id: int):
    with open('content/week1.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    day = get_current_day(user_id)
    if day <= len(data):
        message = data[day-1]['morning']
        await bot.send_message(user_id, f"Доброе утро! {message}")

async def send_evening_message(bot: Bot, user_id: int):
    with open('content/week1.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    day = get_current_day(user_id)
    if day <= len(data):
        message = data[day-1]['evening']
        await bot.send_message(user_id, f"Добрый вечер! {message}")

async def schedule_daily_messages(bot: Bot):
    user_ids = []  # сюда нужно будет добавить ID пользователей

    while True:
        now = datetime.utcnow()
        morning = now.replace(hour=8, minute=0, second=0, microsecond=0)
        evening = now.replace(hour=22, minute=0, second=0, microsecond=0)

        if now >= morning and now < morning + timedelta(minutes=1):
            for user_id in user_ids:
                await send_morning_message(bot, user_id)

        if now >= evening and now < evening + timedelta(minutes=1):
            for user_id in user_ids:
                await send_evening_message(bot, user_id)

        await asyncio.sleep(60)
