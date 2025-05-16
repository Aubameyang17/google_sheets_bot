import json
import os
import gspread
import asyncio
from oauth2client.service_account import ServiceAccountCredentials

# Настройка доступа
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_json = os.getenv("GOOGLE_CREDENTIALS")
creds = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(creds_json), scope)
client = gspread.authorize(creds)

sheet = client.open("Тестовая форма (Ответы)").sheet1

last_row = len(sheet.get_all_values())

async def watch_google_form(bot, chat_id):
    global last_row
    while True:
        try:
            values = sheet.get_all_values()
            if len(values) > last_row:
                new_rows = values[last_row:]
                for row in new_rows:
                    text = "\n".join(row)
                    await bot.send_message(chat_id=chat_id, text=f"📥 Новый ответ:\n{text}")
                last_row = len(values)
        except Exception as e:
            print(f"[Sheets Error] {e}")
        await asyncio.sleep(20)  # Проверять каждые 20 секунд
