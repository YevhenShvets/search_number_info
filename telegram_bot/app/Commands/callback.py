from aiogram import types
import aiogram.utils.markdown as md
from aiogram.types import ParseMode
import typing

from app.Core import dp, bot
from app.Menu import cf, inline_for_number_with_comment
from app.Commands.comment import Form


@dp.callback_query_handler(cf.filter(action='comment'))
async def callback_handler_add_comment(callback_query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    if len(callback_query.message.reply_markup.inline_keyboard) == 1:
        keyboard = inline_for_number_with_comment(callback_query.message.reply_markup)

        await bot.edit_message_reply_markup(callback_query.message.chat.id,
                                            callback_query.message.message_id,
                                            reply_markup=keyboard)
    else:
        keyboard = callback_query.message.reply_markup
        for i in range(len(callback_query.message.reply_markup.inline_keyboard), 1, -1):
            keyboard.inline_keyboard.pop()
        await bot.edit_message_reply_markup(callback_query.message.chat.id,
                                            callback_query.message.message_id,
                                            reply_markup=keyboard)


@dp.callback_query_handler(cf.filter(action='comment_add'))
async def callback_handler_add_comment_add(callback_query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
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
                           "<b>Введіть будь ласка коментар:</b>\n<code>cancel - зупинити.</code>",
                           parse_mode=ParseMode.HTML
                           )
