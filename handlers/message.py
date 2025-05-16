from aiogram import Dispatcher, types
async def echo(msg: types.Message):
    await msg.answer("Привет! Я бот для Google Форм.")




def register_message(dp: Dispatcher):
    dp.message.register(echo)

