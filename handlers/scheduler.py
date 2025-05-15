# Планировщик утренних и вечерних сообщений
from handlers.user_progress import load_progress
import asyncio
from datetime import datetime
from aiogram import Bot
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)

async def schedule_zone_tasks(context):
    data = load_progress()
    for user_id, zones in data.items():
        for zone, progress in zones.items():
            day = int(progress.get("day", 1))
            if not progress.get("morning_done", False):
                await send_prompt(zone, user_id, day, is_morning=True)
            elif not progress.get("evening_done", False):
                await send_prompt(zone, user_id, day, is_morning=False)

async def send_prompt(zone, user_id, day, is_morning=True):
    if zone == "zone_1":
        from handlers.zone_1.zone1 import send_morning_prompt, send_evening_prompt
    elif zone == "zone_2":
        from handlers.zone_2.zone2 import send_morning_prompt, send_evening_prompt
    elif zone == "zone_3":
        from handlers.zone_3.zone3 import send_morning_prompt, send_evening_prompt
    elif zone == "zone_4":
        from handlers.zone_4.zone4 import send_morning_prompt, send_evening_prompt
    elif zone == "zone_5":
        from handlers.zone_5.zone5 import send_morning_prompt, send_evening_prompt
    elif zone == "zone_6":
        from handlers.zone_6.zone6 import send_morning_prompt, send_evening_prompt
    elif zone == "zone_7":
        from handlers.zone_7.zone7 import send_morning_prompt, send_evening_prompt
    elif zone == "zone_8":
        from handlers.zone_8.zone8 import send_morning_prompt, send_evening_prompt
    else:
        return

    if is_morning:
        await send_morning_prompt(context=None, user_id=user_id, day=day)
    else:
        await send_evening_prompt(context=None, user_id=user_id, day=day)

# Пример запуска
# asyncio.run(schedule_zone_tasks())
