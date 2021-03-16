from aiogram import types
from babel.dates import format_datetime
import datetime

from app.Core import dp, bot
from app.Menu import inline_for_number
from app.Helper import number_with_character, is_phone_number
from app.Db.commands import select_number_info, update_number_activity


@dp.message_handler(content_types=['text'])
async def main_text_handler(message: types.Message):
    if is_phone_number(message.text):
        data = select_number_info(message.text)
        update_number_activity(data[0])
        result = f"`Номер телефону:` {number_with_character(data[1])}\n\n" \
                 f"`Рейтинг:` 🔴🔴🔴🔴🔴🔴🟢🟢🟢🟢\n" \
                 f"`Дата останнього перегляду:`  _{format_datetime(data[2], 'd MMMM Y', locale='uk_UA')}_\n" \
                 f"`Кількість переглядів:`  _{data[3]}_"
        keyboard = inline_for_number("https://google.com/", data[0])
        await message.answer(result, reply_markup=keyboard, parse_mode=types.ParseMode.MARKDOWN_V2)
    else:
        await message.answer("Номер телефону введено не коректно")
