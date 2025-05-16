import asyncio
import logging
import os

from aiogram import Bot, Dispatcher

from handlers.message import register_message
from sheets.watcher import watch_google_form  # фоновый цикл

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
if TOKEN is None:
    raise ValueError("BOT_TOKEN not set")

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(TOKEN)
    dp = Dispatcher()

    # Регистрируем хендлеры
    register_message(dp)

    # Запускаем отслеживание Google Таблицы как фоновую задачу
    asyncio.create_task(watch_google_form(bot, CHAT_ID))

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
