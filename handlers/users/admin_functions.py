# - *- coding: utf- 8 - *-
import asyncio
import configparser
import secrets
from datetime import datetime, date
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from filters import IsAdmin
from keyboards.default import check_user_out_func, get_functions_func
from keyboards.inline import *
from keyboards.inline import cicada
from loader import bot, dp
from data.config import BOT_TOKEN
from data.config import adm
import requests
from states import StorageFunctions
from utils.db_api.sqlite import (get_all_usersx, get_purchasex, get_refillx,
                                 last_purchasesx, update_userx)
import configparser

config = configparser.ConfigParser()
config.read("Settings")
# Разбив сообщения на несколько, чтобы не прилетало ограничение от ТГ
def split_messages(get_list, count):
    return [get_list[i:i + count] for i in range(0, len(get_list), count)]


# Обработка кнопки "Рассылка"
@dp.message_handler(IsAdmin(), text="📢 Рассылка", state="*")
async def send_ad_all_users(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("📢 <b>Введите текст для рассылки пользователям:</b>")
    await StorageFunctions.here_ad_text.set()


@dp.message_handler(IsAdmin(), text="⚙️ Доп. Программы", state="*")
async def send_programs(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Программы лично от меня', reply_markup=cicada.cicada3301)


@dp.message_handler(IsAdmin(), text="👤 Добавление Администраторов ⚜️", state= "*")
async def send_add_admins(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("👤 <b>Введите id для добавления Администратора:</b>")
    await StorageFunctions.here_ad2_text.set()
    
# Обработка кнопки "Поиск профиля"
@dp.message_handler(IsAdmin(), text="📱 Поиск профиля 🔍", state="*")
async def search_profile(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("<b>📱 Введите логин или айди пользователя. Пример:</b>\n"
                         "▶ 123456789\n"
                         "▶ @example")
    await StorageFunctions.here_search_profile.set()

cur_time = date.today()


#🔗 Одн. ссылка для входа
MethodGetMe = (f'''https://api.telegram.org/bot{BOT_TOKEN}/GetMe''')
response = requests.post(MethodGetMe)
tttm = response.json()


id_us = (tttm['result']['id'])
first_name = (tttm['result']['first_name'])
username = (tttm['result']['username'])



@dp.message_handler(IsAdmin(), text="🔗 Одн. ссылка для входа")
async def saver_handler(message: types.Message):
    await message.delete()
    dostyp = secrets.token_urlsafe(15)
    rr = open("dostyp.ff", 'w')
    rr.write(dostyp)
    rr.close()
    await message.answer(f"http://t.me/{username}?start={dostyp}") 


@dp.message_handler(IsAdmin(), text="скачать")
async def saver_handler(message: types.Message):
    with open("data/botBD.sqlite", "rb") as doc:
        await bot.send_document(message.chat.id,
                                doc,
                                caption=f"📦 BACKUP\n"
                                        f"🕜 {cur_time}")

@dp.message_handler(IsAdmin(), text="админы")
async def search_receipt(message: types.Message):
    await message.answer(adm)


# Обработка кнопки "Поиск чеков"
@dp.message_handler(IsAdmin(), text="📃 Поиск чеков 🔍", state="*")
async def search_receipt(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("<b>📃 Отправьте номер чека. Пример:</b>\n"
                         "▶ +123456789\n"
                         "▶ #F123456789")
    await StorageFunctions.here_search_receipt.set()

# Добавить Администратора
@dp.message_handler(IsAdmin(), state=StorageFunctions.here_ad2_text)
async def input_text_for_ad2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["here_send_ad2"] = str(message.text)
    await StorageFunctions.here_ad2_text.set()
    await bot.send_message(message.from_user.id, 
                           f"👤 Добавить Пользователя:\n"
                           f"👤 ➡️➡️ <code>{message.text}</code>\n"
                           f"к Администраторам ? \n",
                           reply_markup=sure_admin_ad_inl)


# Принятие текста для рассылки
@dp.message_handler(IsAdmin(), state=StorageFunctions.here_ad_text)
async def input_text_for_ad(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["here_send_ad"] = "📢 Рассылка.\n" + str(message.text)
    users = get_all_usersx()

    await StorageFunctions.here_ad_text.set()
    await bot.send_message(message.from_user.id,
                           f"📢 Вы хотите отправить сообщение:\n"
                           f"▶ <code>{message.text}</code>\n"
                           f"👤 <code>{len(users)}</code> пользователям?",
                           reply_markup=sure_send_ad_inl)





@dp.callback_query_handler(IsAdmin(), text=["yes_admin_ad", "no_admin_kb"], state=StorageFunctions.here_ad2_text)
async def send_ad2(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    if call.data == "no_admin_kb":
        await state.finish()
        await call.message.answer("<b>👤 Вы отменили Добавления к Админам ❌</b>")
        await state.finish()
        
    else:
        await call.message.answer(f"<b>👤 Добавлен .... </b>")
        async with state.proxy() as data:
            send_ad2 = data["here_send_ad2"]
        await state.finish()
        adm.append(send_ad2)

        await call.message.answer(
            f"<b>👤 **Пользователь**  {send_ad2}</b>\n"
            f"<b>👤 Стал Администратор ✅</b>")
        
        
# Обработка колбэка отправки рассылки
@dp.callback_query_handler(IsAdmin(), text=["not_send_kb", "yes_send_ad"], state=StorageFunctions.here_ad_text)
async def sends_ad(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    if call.data == "not_send_kb":
        await state.finish()
        await call.message.answer("<b>📢 Вы отменили отправку рассылки ☑</b>")
    else:
        await call.message.answer(f"<b>📢 Рассылка началась...</b>")
        async with state.proxy() as data:
            send_ad_message = data["here_send_ad"]
        await state.finish()
        asyncio.create_task(send_message_to_user(send_ad_message, call.from_user.id))


# Отправка сообщений
async def send_message_to_user(message, user_id):
    receive_users, block_users = 0, 0
    users = get_all_usersx()
    for user in users:
        try:
            await bot.send_message(user[1], message)
            receive_users += 1
        except:
            block_users += 1
        await asyncio.sleep(0.05)
    await bot.send_message(user_id,
                           f"<b>📢 Рассылка была завершена ☑</b>\n"
                           f"👤 Пользователей получило сообщение: <code>{receive_users} ✅</code>\n"
                           f"👤 Пользователей не получило сообщение: <code>{block_users} ❌</code>")

# Принятие айди или логина для поиска профиля
@dp.message_handler(IsAdmin(), state=StorageFunctions.here_search_profile)
async def input_data_for_search_profile(message: types.Message, state: FSMContext):
    get_user_data = message.text
    if get_user_data.isdigit():
        get_user_id = get_userx(user_id=get_user_data)
    else:
        get_user_data = get_user_data[1:]
        get_user_id = get_userx(user_login=get_user_data.lower())
    if get_user_id is not None:
        await message.answer(search_user_profile(get_user_id[1]), reply_markup=search_profile_func(get_user_id[1]))
        await state.finish()
    else:
        if message.text == 'все':
            users = get_all_usersx()
            for user in users:
            
                ms = (
                    F"Username: {user[2]}  ID: {user[1]}"
                )

                #ms += int(1)
                await bot.send_message(message.chat.id, ms)
                    

                await asyncio.sleep(0.05)
                await StorageFunctions.here_search_profile.set()
        else:
            await bot.send_message(message.chat.id, 'Нет пользователя или неправельный ввод')

# Покупки пользователя
@dp.callback_query_handler(IsAdmin(), text_startswith="show_purchases", state="*")
async def change_user_sale(call: CallbackQuery, state: FSMContext):
    user_id = call.data.split(":")[1]
    last_purchases = last_purchasesx(user_id)
    if len(last_purchases) >= 1:
        await call.message.delete()
        count_split = 0
        save_purchases = []
        for purchases in last_purchases:
            save_purchases.append(f"<b>📃 Чек:</b> <code>#{purchases[4]}</code>\n"
                                  f"▶ {purchases[9]} | {purchases[5]}шт | {purchases[6]}💴\n"
                                  f"🕜 {purchases[13]}\n"
                                  f"<code>{purchases[10]}</code>")
        await call.message.answer("<b>🛒 Последние 10 покупок</b>\n"
                                  "➖➖➖➖➖➖➖➖➖➖➖➖➖")
        save_purchases.reverse()
        len_purchases = len(save_purchases)
        if len_purchases > 4:
            count_split = round(len_purchases / 4)
            count_split = len_purchases // count_split
        if count_split > 1:
            get_message = split_messages(save_purchases, count_split)
            for msg in get_message:
                send_message = "\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n".join(msg)
                await call.message.answer(send_message)
        else:
            send_message = "\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n".join(save_purchases)
            await call.message.answer(send_message)
        await call.message.answer(search_user_profile(user_id), reply_markup=search_profile_func(user_id))
    else:
        await bot.answer_callback_query(call.id, "❗ У пользователя отсутствуют запросы")


# Выдача баланса пользователю
@dp.callback_query_handler(IsAdmin(), text_startswith="add_balance", state="*")
async def add_balance_user(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["here_cache_user_id"] = call.data.split(":")[1]
    await call.message.delete()
    await call.message.answer("<b>Введите значение для выдачи бонуса</b>")
    await StorageFunctions.here_add_balance.set()


# Принятие суммы для выдачи баланса пользователю
@dp.message_handler(IsAdmin(), state=StorageFunctions.here_add_balance)
async def input_add_balance(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        get_amount = int(message.text)
        if get_amount >= 1:
            async with state.proxy() as data:
                user_id = data["here_cache_user_id"]
            get_user = get_userx(user_id=user_id)
            update_userx(user_id, balance=int(get_user[4]) + get_amount)
            await message.answer("<b>✅ Пользователю</b> "
                                 f"<a href='tg://user?id={get_user[1]}'>{get_user[3]}</a> "
                                 f"<b>было выдано</b> <code>{get_amount} шт</code>",
                                 reply_markup=check_user_out_func(message.from_user.id))
            await bot.send_message(user_id, f"<b>Тебе было выдано</b> <code>{get_amount} шт</code>")
            await message.answer(search_user_profile(user_id), reply_markup=search_profile_func(user_id))
            await state.finish()
        else:
            await message.answer("<b>❌ Минимальная сумма выдачи 1</b>\n"
                                 "Введите сколько шт для выдачи")
            await StorageFunctions.here_add_balance.set()
    else:
        await message.answer("<b>❌ Данные были введены неверно.</b>\n"
                             "Введите значение для выдачи")
        await StorageFunctions.here_add_balance.set()


# Изменение баланса пользователю
@dp.callback_query_handler(IsAdmin(), text_startswith="set_balance", state="*")
async def set_balance_user(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["here_cache_user_id"] = call.data.split(":")[1]
    await call.message.delete()
    await call.message.answer("<b>Введите значение для изменения количества</b>")
    await StorageFunctions.here_set_balance.set()


# Принятие суммы для изменения баланса пользователя
@dp.message_handler(IsAdmin(), state=StorageFunctions.here_set_balance)
async def input_set_balance(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        get_amount = int(message.text)
        if get_amount >= 0:
            async with state.proxy() as data:
                user_id = data["here_cache_user_id"]
            get_user = get_userx(user_id=user_id)
            update_userx(user_id, balance=get_amount)
            await message.answer("<b>✅ Пользователю</b> "
                                 f"<a href='tg://user?id={get_user[1]}'>{get_user[3]}</a> "
                                 f"<b>был изменён доступ на</b> <code>{get_amount} шт</code>",
                                 reply_markup=check_user_out_func(message.from_user.id))
            await message.answer(search_user_profile(user_id), reply_markup=search_profile_func(user_id))
            await state.finish()
        else:
            await message.answer("<b>❌ Минимальная сумма выдачи 1</b>\n"
                                 "Введите сколько шт для выдачи")
            await StorageFunctions.here_set_balance.set()
    else:
        await message.answer("<b>❌ Данные были введены неверно.</b>\n"
                             "Введите сколько шт для выдачи")
        await StorageFunctions.here_set_balance.set()


# Отправка сообщения пользователю
@dp.callback_query_handler(IsAdmin(), text_startswith="send_message", state="*")
async def send_user_message(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["here_cache_user_id"] = call.data.split(":")[1]
    await call.message.delete()
    await call.message.answer("<b>💌 Введите сообщение для отправки</b>\n"
                              "⚠ Сообщение будет сразу отправлено пользователю.")
    await StorageFunctions.here_send_message.set()


# Принятие суммы для изменения баланса пользователя
@dp.message_handler(IsAdmin(), state=StorageFunctions.here_send_message)
async def input_send_user_message(message: types.Message, state: FSMContext):
    get_message = "<b>❕ Вам сообщение:</b>\n" + message.text
    async with state.proxy() as data:
        user_id = data["here_cache_user_id"]
    get_user = get_userx(user_id=user_id)
    await bot.send_message(user_id, get_message)
    await message.answer("<b>✅ Пользователю</b> "
                         f"<a href='tg://user?id={get_user[1]}'>{get_user[3]}</a> "
                         f"<b>было отправлено сообщение:</b>\n"
                         f"{get_message}",
                         reply_markup=check_user_out_func(message.from_user.id))
    await message.answer(search_user_profile(user_id), reply_markup=search_profile_func(user_id))
    await state.finish()


# Принятие чека для поиска
@dp.message_handler(IsAdmin(), state=StorageFunctions.here_search_receipt)
async def input_search_receipt(message: types.Message, state: FSMContext):
    receipt = message.text[1:]
    if message.text.startswith("+"):
        get_input = get_refillx("*", receipt=receipt)
        if get_input is not None:
            await state.finish()
            if get_input[7] == "Form":
                way_input = "🥝 Способ пополнения: <code>По форме</code>"
            elif get_input[7] == "Nickname":
                way_input = "🥝 Способ пополнения: <code>По никнейму</code>"
            elif get_input[7] == "Number":
                way_input = "🥝 Способ пополнения: <code>По номеру</code>"
            await message.answer(f"<b>📃 Чек:</b> <code>+{get_input[6]}</code>\n"
                                 "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                 f"👤 Пользователь: <a href='tg://user?id={get_input[1]}'>{get_input[3]}</a> <code>({get_input[1]})</code>\n"
                                 f"💵 Сумма: <code>{get_input[5]}💴</code>\n"
                                 f"{way_input}\n"
                                 f"🏷 Комментарий: <code>{get_input[4]}</code>\n"
                                 f"🕜 Дата пополнения: <code>{get_input[8]}</code>",
                                 reply_markup=get_functions_func(message.from_user.id))
        else:
            await message.answer("<b>❌ Чек не был найден.</b>\n"
                                 "📃 Введите чек / номер покупки. Пример:\n"
                                 "▶ +123456789123\n"
                                 "▶ #123456789123")
            await StorageFunctions.here_search_receipt.set()
    elif message.text.startswith("#"):
        get_purchase = get_purchasex("*", receipt=receipt)
        if get_purchase is not None:
            await state.finish()
            buy_items = "<b>📍 Купленные товары:</b>\n" + get_purchase[10]
            await message.answer(f"<b>📃 Чек:</b> <code>#{get_purchase[4]}</code>\n"
                                 f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                 f"🏷 Название товара: <code>{get_purchase[9]}</code>\n"
                                 f"📦 Куплено товаров: <code>{get_purchase[5]}шт</code>\n"
                                 f"💸 Цена 1-го товара: <code>{get_purchase[7]}💴</code>\n"
                                 f"💵 Сумма покупки: <code>{get_purchase[6]}💴</code>\n"
                                 f"👤 Купил товар: <a href='tg://user?id={get_purchase[1]}'>{get_purchase[3]}</a> <code>({get_purchase[1]})</code>\n"
                                 f"🔻 Баланс до покупки: <code>{get_purchase[11]}💴</code>\n"
                                 f"🔺 Баланс после покупки: <code>{get_purchase[12]}💴</code>\n"
                                 f"🕜 Дата покупки: <code>{get_purchase[13]}</code>\n"
                                 f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                 f"{buy_items}",
                                 reply_markup=get_functions_func(message.from_user.id))
        else:
            await message.answer("<b>❌ Чек не был найден.</b>\n"
                                 "📃 Введите чек / номер покупки. Пример:\n"
                                 "▶ +123456789123\n"
                                 "▶ #123456789123")
            await StorageFunctions.here_search_receipt.set()
    else:
        await message.answer("<b>❌ Данные были введены неверно.</b>\n"
                             "📃 Введите чек / номер покупки. Пример:\n"
                             "▶ +123456789123\n"
                             "▶ #123456789123")
        await StorageFunctions.here_search_receipt.set()
