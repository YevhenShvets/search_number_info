from aiogram import types
from babel.dates import format_datetime
import datetime

from app.Core import dp, bot
from app.Menu import inline_for_number
from app.Helper import number_with_character


@dp.message_handler(content_types=['text'])
async def main_text_handler(message: types.Message):
    last_date = format_datetime(datetime.date.today(), 'd MMMM Y', locale='uk_UA')
    number = number_with_character(message.text)
    result = f"`Номер телефону:` {number}\n\n\n" \
             f"`Рейтинг:` 🔴🔴🔴🔴🔴🔴🟢🟢🟢🟢\n" \
             f"`Дата останнього візиту:`  _{last_date}_"
    keyboard = inline_for_number("https://google.com/", 1)
    await message.answer(result, reply_markup=keyboard, parse_mode=types.ParseMode.MARKDOWN_V2)
