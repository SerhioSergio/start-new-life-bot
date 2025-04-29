
import json
import os
from datetime import datetime

USERS_FILE = 'users.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

def get_current_day(user_id):
    users = load_users()
    user = users.get(str(user_id), {"day": 1})
    return user.get("day", 1)

def save_user_answer(user_id, text):
    users = load_users()
    today = datetime.utcnow().strftime('%Y-%m-%d')
    if str(user_id) not in users:
        users[str(user_id)] = {"day": 1, "answers": {}}
    users[str(user_id)]["answers"][today] = text
    save_users(users)

def increment_day(user_id):
    users = load_users()
    if str(user_id) not in users:
        users[str(user_id)] = {"day": 1, "answers": {}}
    users[str(user_id)]["day"] += 1
    save_users(users)
