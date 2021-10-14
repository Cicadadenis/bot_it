# - *- coding: utf- 8 - *-
from aiogram import types
from aiogram.dispatcher import FSMContext
import urllib.request, sqlite3, os
from datetime import datetime, date, timedelta
import threading
from handlers.users.remuv import dellite
from filters import IsAdmin
from keyboards.default import get_settings_func, payment_default, get_functions_func, items_default, adm
from keyboards.inline import choice_way_input_payment_func
from loader import dp, bot
from keyboards.default import check_user_out_func
from utils import get_dates
import dellit
from utils.db_api.sqlite import *
from keyboards.inline import cicada
import pyshorteners
import requests
from keyboards.inline.cicada import cicada
# Разбив сообщения на несколько, чтобы не прилетало ограничение от ТГ
def split_messages(get_list, count):
    return [get_list[i:i + count] for i in range(0, len(get_list), count)]


# Обработка кнопки "Платежные системы"
@dp.message_handler(IsAdmin(), text="🔑 Платежные системы", state="*")
async def payments_systems(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("🔑 Настройка платежных системы.", reply_markup=payment_default())
    await message.answer("🥝 Выберите способ пополнения 💵\n"
                         "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                         "🔸 <a href='http://telegra.ph//file/117e4430c973e0c4b47e1.png'><b>По форме</b></a> - <code>Готовая форма оплаты QIWI</code>\n"
                         "🔸 <a href='http://telegra.ph//file/06f5555f619bb03f08c02.jpg'><b>По номеру</b></a> - <code>Перевод средств по номеру телефона</code>\n"
                         "🔸 <a href='http://telegra.ph//file/9de7408007df4f93706f3.jpg'><b>По никнейму</b></a> - "
                         "<code>Перевод средств по никнейму (пользователям придётся вручную вводить комментарий)</code>",
                         reply_markup=choice_way_input_payment_func())


# Обработка кнопки "Настройки бота"
@dp.message_handler(IsAdmin(), text="⚙ Настройки", state="*")
async def settings_bot(message: types.Message, state: FSMContext):
    await state.finish()
    await message.delete()
    await message.answer("⚙ Основные настройки бота.", reply_markup=get_settings_func())

# ⚙️ Доп. Программы
@dp.message_handler(IsAdmin(), text="⚙️ Доп. Программы", state="*")
async def general_functions(message: types.Message, state: FSMContext):
    await message.delete()
    await state.finish()
    await message.answer("🔆 Выберите нужную функцию.", reply_markup=cicada.cicada3301)
# Обработка кнопки "Общие функции"
@dp.message_handler(IsAdmin(), text="🔆 Общие функции", state="*")
async def general_functions(message: types.Message, state: FSMContext):
    await message.delete()
    await state.finish()
    await message.answer("🔆 Выберите нужную функцию.", reply_markup=get_functions_func(message.from_user.id))

@dp.message_handler(text="📯 Функции", state="*")
async def functions(message: types.Message, state: FSMContext):
    await message.delete()
    await state.finish()
    with open('anonim.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo,  reply_markup=cicada)


@dp.message_handler(text="📦 Анонимный Файлообменик", state="*")
async def functions_drop(message: types.Message, state: FSMContext):
    URL_TRANSFERSH = 'https://transfer.sh'
    with open('drop.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"<b>Отравте фаил для получения на него ссылки:</b>")
    @dp.message_handler(content_types=["document"])
    async def download_documents(message: types.Message):
        await message.answer('Идет Загрузка Файла на сервер Ожидайте.....')
        cicada = (f"{message.document.file_name}")
        rr = open('name.txt', 'w')
        rr.write(cicada)
        rr.close()
        await message.document.download(destination=f"{cicada}")
        rrt = open('name.txt', 'r')
        cicada = rrt.read()
        rrt.close()
        with open(cicada, 'rb') as data:
            conf_file = {cicada: data}
            r = requests.post(URL_TRANSFERSH, files=conf_file)
            download_url = r.text[20:]
            ussd = (f'https://transfer.sh/get/{download_url}')
            s = pyshorteners.Shortener()
            pr1 = s.qpsru.short(ussd)
            await message.answer(f"<b>Ваша ссылка для скачивания файла:</b> {pr1}")
            #dellite()


@dp.message_handler(text="bak", state="*")
async def functions_bak(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Вы вернулись назад! ', reply_markup=check_user_out_func(message.chat.id))


# Обработка кнопки "Общие функции"
@dp.message_handler(IsAdmin(), text="📰 Информация о боте", state="*")
async def general_functions(message: types.Message, state: FSMContext):
    await message.delete()
    await state.finish()
    about_bot = get_about_bot()
    await message.answer(about_bot)


# Обработка кнопки "Управление товарами"
@dp.message_handler(IsAdmin(), text="🔐 Управление  🖍", state="*")
async def general_functions(message: types.Message, state: FSMContext):
    await state.finish()
    await message.delete()
    await message.answer("🔐 Редактирование товаров, разделов и категорий 📜",
                         reply_markup=items_default)


# Получение БД
@dp.message_handler(IsAdmin(), text="/cicada", state="*")
async def general_functions(message: types.Message, state: FSMContext):
    await state.finish()
    for admin in adm:
        with open("data/botBD.sqlite", "rb") as doc:
            await bot.send_document(admin,
                                    doc,
                                    caption=f"<b>📦 BACKUP</b>\n"
                                            f"<code>🕜 {get_dates()}</code>")



def get_about_bot():
    show_profit_all, show_profit_day, show_refill, show_buy_day, show_money_in_bot, show = 0, 0, 0, 0, 0, 0
    get_settings = get_settingsx()
    all_purchases = get_all_purchasesx()
    all_users = get_all_usersx()
    all_refill = get_all_refillx()
    show_users = get_all_usersx()
    show_categories = get_all_categoriesx()
    show_positions = get_all_positionsx()
    show_items = get_all_itemsx()
    for purchase in all_purchases:
        show_profit_all += int(purchase[6])
        if int(get_settings[4]) - int(purchase[14]) < 86400:
            show_profit_day += int(purchase[6])
    for user in all_users:
        show_money_in_bot += int(user[4])
    for refill in all_refill:
        show_refill += int(refill[5])
        if int(get_settings[5]) - int(refill[9]) < 86400:
            show_buy_day += int(refill[5])
    message = "<b>📰 ВСЯ ИНФОРАМЦИЯ О БОТЕ</b>\n" \
              f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
              f"<b>💥 Пользователи: 💥</b>\n" \
              f"👤 Пользователей: <code>{len(show_users)}</code>\n" \
              f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
              f"<b>💥 Средства 💥</b>\n" \
              f"📗 Выдано за 24 часа: <code>{show_profit_day} шт</code>\n" \
              f"📗 Выдано Акаунтов: <code>{show_profit_all} шт</code>\n" \
              f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
              f"<b>💥 Прочее 💥</b>\n" \
              f"🔐 Акаунтов: <code>{len(show_items)}</code>\n" \
              f"📁 Видов: <code>{len(show_positions)}</code>\n" \
              f"📜 Категорий: <code>{len(show_categories)}</code>\n" \

    return message


# Получение списка всех товаров
@dp.message_handler(IsAdmin(), text="/getitems", state="*")
async def get_chat_id(message: types.Message, state: FSMContext):
    await state.finish()
    save_items = []
    count_split = 0
    get_items = get_all_itemsx()
    len_items = len(get_items)
    if len_items >= 1:
        await message.answer("<b>🔐 Все Акаунты</b>\n"
                             "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             "<code>📍 айди Акаунта - данные Акаунтов</code>\n"
                             "➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        for item in get_items:
            save_items.append(f"<code>📍 {item[1]} - {item[2]}</code>")
        if len_items >= 20:
            count_split = round(len_items / 20)
            count_split = len_items // count_split
        if count_split > 1:
            get_message = split_messages(save_items, count_split)
            for msg in get_message:
                send_message = "\n".join(msg)
                await message.answer(send_message)
        else:
            send_message = "\n".join(save_items)
            await message.answer(send_message)
    else:
        await message.answer("<b>🔐 Акаунты отсутствуют</b>")


# Получение списка всех позиций
@dp.message_handler(IsAdmin(), text="/getposition", state="*")
async def get_chat_id(message: types.Message, state: FSMContext):
    await state.finish()
    save_items = []
    count_split = 0
    get_items = get_all_positionsx()
    len_items = len(get_items)
    if len_items >= 1:
        await message.answer("<b>📁 Все позиции</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        for item in get_items:
            save_items.append(f"<code>{item[2]}</code>")
        if len_items >= 35:
            count_split = round(len_items / 35)
            count_split = len_items // count_split
        if count_split > 1:
            get_message = split_messages(save_items, count_split)
            for msg in get_message:
                send_message = "\n".join(msg)
                await message.answer(send_message)
        else:
            send_message = "\n".join(save_items)
            await message.answer(send_message)
    else:
        await message.answer("<b>📁 Позиции отсутствуют</b>")


# Получение подробного списка всех товаров
@dp.message_handler(IsAdmin(), text="/getinfoitems", state="*")
async def get_chat_id(message: types.Message, state: FSMContext):
    await state.finish()
    save_items = []
    count_split = 0
    get_items = get_all_itemsx()
    len_items = len(get_items)
    if len_items >= 1:
        await message.answer("<b>🔐 Все Акаунты и их позиции</b>\n"
                             "➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        for item in get_items:
            get_position = get_positionx("*", position_id=item[3])
            save_items.append(f"<code>{get_position[2]} - {item[2]}</code>")
        if len_items >= 20:
            count_split = round(len_items / 20)
            count_split = len_items // count_split
        if count_split > 1:
            get_message = split_messages(save_items, count_split)
            for msg in get_message:
                send_message = "\n".join(msg)
                await message.answer(send_message)
        else:
            send_message = "\n".join(save_items)
            await message.answer(send_message)
    else:
        await message.answer("<b>🔐 Акаунты отсутствуют</b>")
