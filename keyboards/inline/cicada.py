# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


cicada = InlineKeyboardMarkup(row_width=1)
cicada.add(
    InlineKeyboardButton('🔗 Зашифр. Ссылку', callback_data='uurl'),
    InlineKeyboardButton('☑️ Пробив по IP', callback_data='ip'),
    InlineKeyboardButton('🔐 Генератор паролей', callback_data='gen_pass'),
    InlineKeyboardButton('🧰 Генератор ников', callback_data='gen_nick'),
    InlineKeyboardButton('🔝 user!! agent!!', callback_data='gen_agent'),
    InlineKeyboardButton(text='🌐 Генератор прокси', callback_data='gen_proxy')
)

uss = InlineKeyboardMarkup(row_width=1)
uss.add(
    InlineKeyboardButton(text='1️⃣  ANDROID ✅', callback_data='uss_android'),
    InlineKeyboardButton(text='2️⃣  IOS ✅', callback_data='uss_ios'),
    InlineKeyboardButton(text='3️⃣   Linux  ✅', callback_data='uss_linux'),
    InlineKeyboardButton(text='4️⃣    windows   ✅', callback_data='uss_windows'),
)

soglasie = InlineKeyboardMarkup()
soglasie.add(
    InlineKeyboardButton("✅ Да", callback_data="dada"),
    InlineKeyboardButton("❌ Нет", callback_data='nene')
)



gen_ent = InlineKeyboardMarkup(row_width=1)
gen_ent.add(
    InlineKeyboardButton(text='🧬 Сгенерировать', callback_data='gen_agnt'),
    InlineKeyboardButton(text='⚙️ Параметры', callback_data='settings_pass'),
    InlineKeyboardButton(text='◀️ Назад', callback_data='back_gen'),
)
gen_pass = InlineKeyboardMarkup(row_width=1)
gen_pass.add(
    InlineKeyboardButton(text='🧬 Сгенерировать', callback_data='generate_pass'),
    InlineKeyboardButton(text='⚙️ Параметры', callback_data='settings_pass'),
    InlineKeyboardButton(text='◀️ Назад', callback_data='back_gen'),
)


 
gen_pro = InlineKeyboardMarkup(row_width=1)
gen_pro.add(
    InlineKeyboardButton(text='🔄 Сгенерировать', callback_data='generate_proxy'),
    InlineKeyboardButton(text='◀️ Назад', callback_data='back_gen'),
)


cicada3301 = InlineKeyboardMarkup()

cicada3301.row(
    InlineKeyboardButton(text='🏞 Получить id фото:', callback_data='id_foto')
)