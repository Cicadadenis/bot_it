# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from data.config import adm


def check_user_out_func(user_id):
    menu_default = ReplyKeyboardMarkup(resize_keyboard=True)
    menu_default.row("🔐 Акаунты", "📱 Профиль", "ℹ FAQ")
    menu_default.row("📯 Функции", "📦 Анонимный Файлообменик", "📶 virtualSim")#📲 ProtonMail")
    menu_default.row("📸 Штамп на фото")
    if str(user_id) in adm:
        menu_default.row("🔐 Управление  🖍", "📰 Информация о боте")
        menu_default.row("⚙ Настройки", "🔆 Общие функции", "👤 Добавление Администраторов ⚜️")
        menu_default.row("🔗 Одн. ссылка для входа")
    return menu_default


all_back_to_main_default = ReplyKeyboardMarkup(resize_keyboard=True)
all_back_to_main_default.row("⬅ На главную")

ssaa = InlineKeyboardMarkup(row_width=2)
ssaa.add(
    InlineKeyboardButton("✅ Добавить ", callback_data='yes_add')
)

lic = InlineKeyboardMarkup()
lic.add(
    InlineKeyboardButton('✅ Начать', callback_data='pr')
)

reg_back = InlineKeyboardMarkup()
reg_back.add(
    InlineKeyboardButton('❌ Отмена', callback_data='otm')
)

virtualsim = InlineKeyboardMarkup(row_width=2)
virtualsim.add(
    InlineKeyboardButton('📲 ProtonMail',callback_data='proton'),
    InlineKeyboardButton('📲 Signal', callback_data='sig')
)