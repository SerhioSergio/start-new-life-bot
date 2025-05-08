
import json
from pathlib import Path

progress_file = Path("user_data.json")

def load_progress():
    if progress_file.exists():
        with open(progress_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_progress(data):
    with open(progress_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_user_step(user_id, zone):
    data = load_progress()
    return data.get(str(user_id), {}).get(zone)

def save_user_step(user_id, zone, step):
    data = load_progress()
    user_data = data.get(str(user_id), {})
    user_data[zone] = step
    data[str(user_id)] = user_data
    save_progress(data)
