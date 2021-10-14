from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


menu_default = InlineKeyboardMarkup(row_width=2)
menu_default.add(
    InlineKeyboardButton('⚙️ Настройки', callback_data='seting'),
    InlineKeyboardButton('🔧 По умолчанию', callback_data='rem')
)
menu_setings = InlineKeyboardMarkup(row_width=1)
menu_setings.add(
    InlineKeyboardButton('®️ Штамп', callback_data='t1'),
    InlineKeyboardButton('🖌 Размер', callback_data='t2'),
    InlineKeyboardButton('Отступ 🔼 Y 🔽', callback_data='t3'),
    InlineKeyboardButton('Отступ ◀️ X ▶️', callback_data='t4'),
    InlineKeyboardButton('📊 Настройка цвета', callback_data='t5'),
    InlineKeyboardButton('🔙 Назад', callback_data='back')
)


menu__color = InlineKeyboardMarkup(row_width=2)
menu__color.add(
    InlineKeyboardButton('🌫 Свой Цвет', callback_data='color'),
    InlineKeyboardButton('🔴 Red', callback_data='red'),
    InlineKeyboardButton('🟢 Green', callback_data='green'),
    InlineKeyboardButton('🟢 Green', callback_data='green'),
    InlineKeyboardButton('🟢 Green', callback_data='green'),
    InlineKeyboardButton('🟢 Green', callback_data='green'),
    InlineKeyboardButton('🟢 Green', callback_data='green'),
    InlineKeyboardButton('🟢 Green', callback_data='green'),
    InlineKeyboardButton('🟢 Green', callback_data='green'),
    InlineKeyboardButton('🟢 Green', callback_data='green'),
    InlineKeyboardButton('🟢 Green', callback_data='green'),
    InlineKeyboardButton('🟢 Green', callback_data='green'),
    InlineKeyboardButton('🔵 Blue', callback_data='blue'),
    InlineKeyboardButton('🔙 Назад', callback_data='back')
)


nazad = InlineKeyboardMarkup()
nazad.add(
    InlineKeyboardButton('🔙 Назад', callback_data='back')
)