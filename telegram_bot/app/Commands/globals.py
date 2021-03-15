from aiogram import types
from app.Core import dp


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await message.answer("start command", parse_mode=types.ParseMode.MARKDOWN)


@dp.message_handler(commands='help')
async def help_command(message: types.Message):
    await message.answer("help command", parse_mode=types.ParseMode.MARKDOWN)
