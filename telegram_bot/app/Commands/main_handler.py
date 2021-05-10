from aiogram import types
from babel.dates import format_datetime
import datetime
import math

from app.Core import dp, bot
from app.Menu import inline_for_number
from app.Helper import number_with_character, is_phone_number
from app.Db.commands import select_number_info, update_number_activity, select_all_comments


@dp.message_handler(content_types=['text'])
async def main_text_handler(message: types.Message):
    isPhone, number = is_phone_number(message.text)
    if isPhone:
        data = select_number_info(number)
        update_number_activity(data[0])
        comments_stats = get_comments_stat(select_all_comments(data[0]))
        rating = ""
        for i in range(0, 100, 10):
            if i < comments_stats:
                rating+= "🔴"
            else:
                rating+="🟢"
        result = f"`Номер телефону:` {number_with_character(data[1])}\n\n" \
                 f"`Рейтинг:` {rating}\n" \
                 f"`Дата останнього перегляду:`  _{format_datetime(data[2], 'd MMMM Y', locale='uk_UA')}_\n" \
                 f"`Кількість переглядів:`  _{data[3]}_"
        keyboard = inline_for_number(f"http://127.0.0.1:8000/search/{number}", data[0])
        await message.answer(result, reply_markup=keyboard, parse_mode=types.ParseMode.MARKDOWN_V2)
    else:
        await message.answer("Номер телефону введено не коректно😞")



def get_comments_stat(comments):
    if len(comments) == 0:
        return 0
    comments_stat = 0
    levels = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0
    }
    for val in comments:
        levels[val[3].__str__()] += 1
    comments_stat = levels['1'] + levels['2']
    comments_stat = math.ceil(comments_stat * 100 / len(comments))
    return comments_stat