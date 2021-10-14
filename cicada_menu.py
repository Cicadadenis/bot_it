# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup


cicada = InlineKeyboardMarkup(row_width=2)
cicada.add(
    InlineKeyboardButton('🔗 Создать Шифрованую Ссылку', callback_data='uurl'),
    InlineKeyboardButton('☑️ Пробив по IP', callback_data='ip')
)