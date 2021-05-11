from aiogram import types
from app.Core import dp
from app.Db.commands import select_qa_len, select_qa
from app.Menu import inline_for_view_qa, inline_for_view_categories
from app.Helper import create_beautiful_qa


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await message.answer("напишіть номер 👇👇👇", parse_mode=types.ParseMode.MARKDOWN)


@dp.message_handler(commands='help')
async def help_command(message: types.Message):
    result = f"Вітаю 🖐🖐🖐\n\n" \
             f"Цей бот призначений для перегляду відгуків номерів телефонів 🙀\n\n" \
             f"Щоб переглянути відгуки та інформації про номер просто відправте його мені\n\n" \
             f"Доступні формати🖊🖋🖌:\n" \
             f"0xxxxxxxxx, 380xxxxxxxxx, +380xxxxxxxxx, (0xx) xxx-xx-xx, +38(0xx) xxx-xx-xx"
    await message.answer(result, parse_mode=types.ParseMode.MARKDOWN)


@dp.message_handler(commands='about')
async def about_command(message: types.Message):
    await message.answer('Бота створив - <a href="tg://user?id=684734168">Євген Швець</a>\n\n/start - Розпочати роботу\n/help - Допомога', parse_mode=types.ParseMode.HTML)


@dp.message_handler(commands='site')
async def site_command(message: types.Message):
    await message.answer('<a href="http://127.0.0.1:8000/">Перейти на сайт⤴️</a>', parse_mode=types.ParseMode.HTML)


@dp.message_handler(commands='qa')
async def qa_command(message: types.Message):
    count_qa = select_qa_len()
    keyboard = inline_for_view_qa(0, count_qa)
    qa = select_qa(0)
    qa_data = create_beautiful_qa(qa)
    await message.answer(qa_data,
                        reply_markup=keyboard,
                        parse_mode=types.ParseMode.MARKDOWN)

@dp.message_handler(commands='categories')
async def categories_command(message: types.Message):
    result = f"*Категорії:*\n" \
             f"➖➖➖➖➖➖➖➖➖"
    keyboard = inline_for_view_categories()
    await message.answer(result,
                        reply_markup=keyboard,
                        parse_mode=types.ParseMode.MARKDOWN)
