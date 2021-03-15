from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

import random


cf = CallbackData('post', 'id', 'action')


def inline_for_number(number_url, number_id):
    keyboard = InlineKeyboardMarkup()

    but_open_in_web = InlineKeyboardButton("Відкрити в 🌐", url=number_url)
    but_add_comment = InlineKeyboardButton("Добавити 💬", callback_data=cf.new(id=number_id, action="comment"))

    keyboard.add(but_open_in_web, but_add_comment)
    return keyboard


def inline_for_number_with_comment(markup):
    keyboard = markup
    number = random.randint(0, 100)
    but_1 = InlineKeyboardButton("Небезпечний 🔴", callback_data=cf.new(id=f"{number}.1", action="comment_add"))
    but_2 = InlineKeyboardButton("Надокучливий 🟠", callback_data=cf.new(id=f"{number}.2", action="comment_add"))
    but_3 = InlineKeyboardButton("Нейтральний 🟡", callback_data=cf.new(id=f"{number}.3", action="comment_add"))
    but_4 = InlineKeyboardButton("Безпечний 🟢", callback_data=cf.new(id=f"{number}.4", action="comment_add"))

    keyboard.add(but_1)
    keyboard.add(but_2)
    keyboard.add(but_3)
    keyboard.add(but_4)
    return keyboard

