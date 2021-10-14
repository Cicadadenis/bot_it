# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Кнопки при поиске профиля через админ-меню
open_profile_inl = InlineKeyboardMarkup()
mybuy_kb = InlineKeyboardButton(text="ℹ️ Мои кабинет", callback_data="my_buy")
open_profile_inl.add(mybuy_kb)

# Кнопка с возвратом к профилю
to_profile_inl = InlineKeyboardMarkup()
to_profile_inl.add(InlineKeyboardButton(text="📱 Профиль", callback_data="user_profile"))
