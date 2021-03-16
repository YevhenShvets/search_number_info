from aiogram import types
import aiogram.utils.markdown as md
from aiogram.types import ParseMode
import typing

from app.Core import dp, bot
from app.Menu import cf, inline_for_number_with_comment, inline_for_view_comment
from app.Commands.comment import Form
from app.Db import select_comment, select_comment_len
from app.Helper import create_beautiful_comment


@dp.callback_query_handler(cf.filter(action='comment'))
async def callback_handler_comment(callback_query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    number_id = callback_data['id']
    if len(callback_query.message.reply_markup.inline_keyboard) == 2:
        keyboard = inline_for_number_with_comment(number_id, callback_query.message.reply_markup)

        await bot.edit_message_reply_markup(callback_query.message.chat.id,
                                            callback_query.message.message_id,
                                            reply_markup=keyboard)
    else:
        keyboard = callback_query.message.reply_markup
        for i in range(len(callback_query.message.reply_markup.inline_keyboard), 2, -1):
            keyboard.inline_keyboard.pop()
        await bot.edit_message_reply_markup(callback_query.message.chat.id,
                                            callback_query.message.message_id,
                                            reply_markup=keyboard)


@dp.callback_query_handler(cf.filter(action='comment_add'))
async def callback_handler_add_comment(callback_query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    data = callback_data["id"].split('.')
    number_id = data[0]
    type_c = int(data[1])
    if type_c == 1:
        await Form.Dangerous.set()
    elif type_c == 2:
        await Form.Tiresome.set()
    elif type_c == 3:
        await Form.Neutral.set()
    else:
        await Form.Safe.set()

    state = dp.get_current().current_state()
    async with state.proxy() as data:
        data['id'] = number_id

    await bot.send_message(callback_query.message.chat.id,
                           "<b>Введіть будь ласка відгук:</b>\n<code>cancel - зупинити.</code>",
                           parse_mode=ParseMode.HTML
                           )


@dp.callback_query_handler(cf.filter(action='comment_view'))
async def callback_handler_view_comments(callback_query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    number_id = callback_data["id"]
    count_comments = select_comment_len(number_id)
    if count_comments == 0:
        await bot.send_message(callback_query.message.chat.id,
                               "Відгуки відсутні(")
    else:
        keyboard = inline_for_view_comment(number_id, 0, count_comments)
        comment = select_comment(number_id, 0)
        b_comment = create_beautiful_comment(comment)
        await bot.send_message(callback_query.message.chat.id,
                               b_comment,
                               reply_markup=keyboard,
                               parse_mode=ParseMode.MARKDOWN)


@dp.callback_query_handler(cf.filter(action='comment_view_back'))
async def callback_handler_view_next_comments(callback_query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    data = callback_data['id'].split('.')
    number_id = data[0]
    offset = int(data[1]) - 1
    count_comment = select_comment_len(number_id)
    if offset >= 0:
        keyboard = inline_for_view_comment(number_id, offset, count_comment)
        comment = select_comment(number_id, offset)
        b_comment = create_beautiful_comment(comment)
        await bot.edit_message_text(text=b_comment,
                                    chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    reply_markup=keyboard,
                                    parse_mode=ParseMode.MARKDOWN)


@dp.callback_query_handler(cf.filter(action='comment_view_next'))
async def callback_handler_view_back_comments(callback_query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    data = callback_data['id'].split('.')
    number_id = data[0]
    offset = int(data[1])+1
    count_comment = select_comment_len(number_id)
    if offset < count_comment:
        keyboard = inline_for_view_comment(number_id, offset, count_comment)
        comment = select_comment(number_id, offset)
        b_comment = create_beautiful_comment(comment)
        await bot.edit_message_text(text=b_comment,
                                    chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    reply_markup=keyboard,
                                    parse_mode=ParseMode.MARKDOWN)

