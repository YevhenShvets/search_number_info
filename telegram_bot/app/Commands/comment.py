import logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from app.Core import dp, bot
from app.Helper import create_comment_data
from app.Db.commands import insert_comment


class Form(StatesGroup):
    id = State()
    Dangerous = State()
    Tiresome = State()
    Neutral = State()
    Safe = State()


@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)

    await state.finish()

    await message.reply('Дію відмінено', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=Form.Dangerous)
async def process_dangerous(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Dangerous'] = message.text
    await stop_handler(message, state)


@dp.message_handler(state=Form.Tiresome)
async def process_tiresome(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Tiresome'] = message.text
    await stop_handler(message, state)


@dp.message_handler(state=Form.Neutral)
async def process_neutral(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Neutral'] = message.text
    await stop_handler(message, state)


@dp.message_handler(state=Form.Safe)
async def process_safe(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Safe'] = message.text
    await stop_handler(message, state)


async def stop_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    comment_data = create_comment_data(data)
    insert_comment(comment_data)
    await message.reply("_Дякую за ваш відгук_👍", parse_mode=ParseMode.MARKDOWN_V2)
    # Finish conversation
    await state.finish()

# Check age. Age gotta be digit
# @dp.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
# async def process_age_invalid(message: types.Message):
#     """
#     If age is invalid
#     """
#     return await message.reply("Age gotta be a number.\nHow old are you? (digits only)")


# @dp.message_handler(lambda message: message.text.isdigit(), state=Form.age)
# async def process_age(message: types.Message, state: FSMContext):
#     # Update state and data
#     await Form.next()
#     await state.update_data(age=int(message.text))
#
#     # Configure ReplyKeyboardMarkup
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
#     markup.add("Male", "Female")
#     markup.add("Other")
#
#     await message.reply("What is your gender?", reply_markup=markup)
#
#
# @dp.message_handler(lambda message: message.text not in ["Male", "Female", "Other"], state=Form.gender)
# async def process_gender_invalid(message: types.Message):
#     """
#     In this example gender has to be one of: Male, Female, Other.
#     """
#     return await message.reply("Bad gender name. Choose your gender from the keyboard.")

