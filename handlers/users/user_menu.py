# - *- coding: utf- 8 - *-
from keyboards.default.main_settings import get_settings_func
from typing import Text
from aiogram import types
from my_fake_useragent import UserAgent
import general as gen
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, message
import requests
from keyboards.inline.user_func import confirm_buy_items
from keyboards.inline.user_func import open_item_func
from keyboards.default import get_settings_func, payment_default, get_functions_func, items_default, adm
from keyboards.default import check_user_out_func, all_back_to_main_default
from keyboards.inline.cicada import soglasie
from keyboards.inline.inline_page import *
from loader import dp, bot
from states import state_url
from data.config import config
from states.state_users import *
from utils.other_func import  get_dates
from states.state_url import cicada
import datetime
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types.user import User
from Users.Users import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
import random
import config
from data.config import bot_description
import time
import os
import json
from keyboards.default.menu import reg_back, virtualsim
import pyshorteners
from data.config import sms_api

import secrets
import configparser
import re
from Users.Users import Admin
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from handlers.users.main_start import sozdatel
from handlers.users.cicada_menu import cicada
from keyboards.inline.cicada import gen_pass, uss
from keyboards.inline.user_profiles import get_user_profile
from keyboards.inline.user_inline import open_profile_inl

class cicada(StatesGroup):
    size = State()
    up_y = State()
    up_x = State()
    red = State()
    passw = State()
    capha = State()
    cicada_url = State()
    ip_up = State()
    probiv = State()



s = pyshorteners.Shortener()
# Разбив сообщения на несколько, чтобы не прилетало ограничение от ТГ
def split_messages(get_list, count):
    return [get_list[i:i + count] for i in range(0, len(get_list), count)]


# Обработка кнопки "Купить"
@dp.message_handler(text="🔐 Акаунты", state="*")
async def show_search(message: types.Message, state: FSMContext):
    await message.delete()
    await state.finish()
    get_categories = get_all_categoriesx()
    if len(get_categories) >= 1:
        get_kb = buy_item_open_category_ap(0)
        
        await message.answer("<b>🔐 Выберите нужный вам Акаунт:</b>", reply_markup=get_kb)
    else:
        await message.answer("<b>🔐 Акаунты в данное время отсутствуют.</b>")


@dp.message_handler(text='📶 virtualSim')
async def sim(message: types.Message):
    await message.answer('®️ VirtualSim', reply_markup=virtualsim)
    
# Обработка кнопки "Профиль"
@dp.message_handler(text="📱 Профиль", state="*")
async def show_profile(message: types.Message, state: FSMContext):
    await state.finish()
    await message.delete()
    await message.answer(get_user_profile(message.from_user.id), reply_markup=open_profile_inl)



     #   otmena = url2 = f'https://sms-activate.ru/stubs/handler_api.php?api_key={sms_api}&action=setStatus&status=8&id={operation_ID}'
     #   bak = requests.get(otmena)
     #   otve = bak.text
     #   await message.answer(f"Отмена Регистрации: {otve}")
#



##############################
################################

@dp.callback_query_handler  (text="bak", state="*")
async def bak(call: CallbackQuery, state: FSMContext):
    await message.answer('Вы вернулись в Главное Меню !!!',  reply_markup=get_functions_func(call.message.from_user.id))
###################################
##################################
@dp.callback_query_handler  (text="uurl", state="*")
async def reg_url(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.finish()
    await call.message.answer('Введите ссылку в таком формате <code>http://google.com/</code>')
    await cicada.cicada_url.set()

@dp.message_handler(state=cicada.cicada_url)
async def ssylka(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['cicada.cicada_url'] = str(f"{message.text}")
    await cicada.cicada_url.set()
    uurl = data['cicada.cicada_url']
    r = (requests.get(f'https://is.gd/create.php?format=simple&url={uurl}'))
    
    await message.answer('Шифруем вашу ссылку ожидайте ....')
    r2 = (requests.get(f"https://uni.su/api/?url={uurl}"))
    r3 = (requests.get(f"https://clck.ru/--?url={uurl}"))
    r4 = (requests.get(f"https://v.gd/create.php?format=simple&url={uurl}"))
    s = pyshorteners.Shortener()
    pr = (s.chilpit.short(uurl))
    pr8 = (s.osdb.short(uurl))
    pr9 = (s.dagd.short(message.text))
    s = pyshorteners.Shortener()
    pr1 = (s.qpsru.short(message.text))
    time.sleep(4)
    await message.answer(
        f"🔗 Готово! Вот ваши ссылки:\n\n"
    f"Ссылка №1️⃣: {r.text} \nСсылка №2️⃣: {r2.text} \nСсылка №3️⃣: {r3.text} \nСсылка №4️⃣: {r4.text} \nСсылка №5️⃣: {pr} \nСсылка №6️⃣: {pr9} \nСсылка №7️⃣: {pr1} \n\n<b>TOP-ССЫЛКА: {pr8}</b>", parse_mode='HTML',disable_web_page_preview = True)
    
@dp.callback_query_handler  (text="gen_pass", state="*")
async def gen_pass(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    await call.message.delete()
    password0 = secrets.token_hex(4)
    password1 = secrets.token_hex(6)
    password2 = secrets.token_hex(8)
    password3 = secrets.token_hex(10)
    password4 = secrets.token_hex(12)
    paroli = (
        f"<b>Пароли успешно сгенерировано:</b>\n\n"
        f"➖➖➖➖➖➖➖➖\n"
        f"<code>{password0}</code>\n"
        f"➖➖➖➖➖➖➖➖\n"
        f"<code>{password1}</code>\n"
        f"➖➖➖➖➖➖➖➖\n"
        f"<code>{password2}</code>\n"
        f"➖➖➖➖➖➖➖➖\n"
        f"<code>{password3}</code>\n"
        f"➖➖➖➖➖➖➖➖\n"
        f"<code>{password4}</code>")
    await bot.send_message(chat_id, text=paroli)


@dp.callback_query_handler  (text="proton")
async def send_danet(call: CallbackQuery):
    await call.message.answer('Зарегистрировать ProtonMail ?', reply_markup=soglasie)


@dp.callback_query_handler  (text="sig")
async def sssig(call: CallbackQuery):
    await call.answer("Времено Отключен для улучьшения кода")


@dp.callback_query_handler(text="nene")
async def send_danet(call: CallbackQuery):
    await call.message.delete() 
    await call.message.answer("Регистрация ProtonMail Отменена", reply_markup=check_user_out_func(call.message.from_user.id)) 


@dp.callback_query_handler(text="dada")
async def send_danet(call: CallbackQuery):
    await call.message.delete() 
    chat_id = call.message.chat.id
    nam = call.message.from_user.first_name
    
    kosh = (f"https://sms-activate.ru/stubs/handler_api.php?api_key={sms_api}&action=getBalance")
    den_kosh = requests.get(kosh)
    msg_ = den_kosh.text
    msg_s = msg_[15:]
    chat_id = call.message.chat.id
    
    await bot.send_message(chat_id=sozdatel, text=f"На счету: {msg_s} p")
    status = 0
    operation_ID = 0
    number = 0
    url = f'https://sms-activate.ru/stubs/handler_api.php?api_key={sms_api}&action=getNumber&service=dp&forward=0&operator=any&ref=123614&country=0'
    den = requests.get(url)
    
    if den.text == 'NO_BALANCE':
        await call.message.answer('В данный момент нет номеров')
        await bot.send_message(chat_id=sozdatel, text=f"Закончелись деньги на счету")
        pass
    st = den.text
    print(st)
    status = st.split(':')[0]
    operation_ID = st.split(':')[1]
    number = st.split(':')[2]
    await bot.send_message(chat_id=sozdatel, text=f"👤 Пользователь: {call.message.from_user.first_name} || {chat_id} || {call.message.from_user.username} 📲 Взял Номер {number}")
    if str(status) == 'ACCESS_NUMBER':
        ot2 = 'ot'
        url2 = f'https://sms-activate.ru/stubs/handler_api.php?api_key={sms_api}&action=setStatus&status=1&id={operation_ID}'
        response2 = requests.post(url2)
        status = True
    elif str(status) == 'NO_NUMBERS':
        status = False
    else:
        status = False
    if status:
            await call.message.answer(
                f"🎟  <b>Регистрация ProtonMail:</b>\n"
                f"➖➖➖➖➖➖➖➖➖\n"
                f"🌍  <b>Страна: Россия</b> 🇷🇺\n"
                f"➖➖➖➖➖➖➖➖➖\n"
                f"📲  <b>Номер:</b> <code>{number}</code>"
            )
            time.sleep(5)
            await call.message.answer('Ожидаю смс ....')


    url2 = f'https://sms-activate.ru/stubs/handler_api.php?api_key={sms_api}&action=getStatus&id={operation_ID}'
    cica = requests.post(url2)
    den2 = cica.text
    
    while True:
        url2 = f'https://sms-activate.ru/stubs/handler_api.php?api_key={sms_api}&action=getStatus&id={operation_ID}'
        cica = requests.post(url2)
        den2 = cica.text
        
        try:
            if den2[:9] == 'STATUS_OK':
                sms = den2[10:]
                print(sms)
                mas = (
                    f"✅ <b>Регистрация на номер: {number} Выполнена успешно</b>\n"
                    f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                    f"🔐 <b>Код подтверждения:   {sms}</b>\n"
                    f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                )
                await bot.send_message(chat_id, mas)
                break
        except:
            time.sleep(5)

@dp.callback_query_handler  (text="gen_proxy", state="*")
async def genene(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    await call.answer("❗В плижайшее время допишу")
    await call.answer("❗В плижайшее время допишу")
    await call.answer("❗В плижайшее время допишу")
    await call.answer("❗В плижайшее время допишу")
    await call.answer("❗В плижайшее время допишу")
    await call.answer("❗В плижайшее время допишу")
#######################
@dp.callback_query_handler  (text="gen_nick", state="*")
async def gen_name(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    await call.message.delete()
    line = random.choice(open('names.txt').readlines())
    line2 = random.choice(open('names.txt').readlines())
    line3 = random.choice(open('names.txt').readlines())
    line4 = random.choice(open('names.txt').readlines())
    line5 = random.choice(open('names.txt').readlines())
    await bot.send_message(chat_id=chat_id,  text=f'''
✅ <b>Ники</b> успешно сгенерирован:

<code>{line}</code>
<code>{line2}</code>
<code>{line3}</code>
<code>{line4}</code>
<code>{line5}</code>''')

###########################
@dp.callback_query_handler  (text="gen_agent", state="*")
async def gen_ag(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await bot.send_message(chat_id=call.message.chat.id, text=f'Привет!Выбери устройстра 📱💻🖥 ', reply_markup=uss)

"""
@dp.callback_query_handler  (text="uss_android", state="*")
async def gen_ag(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    """



@dp.callback_query_handler  (text="uss_windows", state="*")
async def link(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    await call.message.delete()
    ff = open('useragent.txt', 'w')
    ua = UserAgent(os_family = 'windows')
    res = ua.random()
    ua = UserAgent(os_family = 'windows')
    res1 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res2 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res3 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res4 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res5 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res6 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res7 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res8 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res9 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res10 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res11 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res12 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res13 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res14 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res15 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res16 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res17 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res18 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res19 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res20 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res21 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res22 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res23 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res24 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res25 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res26 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res27 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res28 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res29 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res30 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res31 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res32 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res33 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res34 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res35 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res36 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res37 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res38 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res39 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res40 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res41 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res42 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res43 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res44 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res45 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res46 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res47 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res48 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res49 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res50 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res51 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res52 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res54 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res55 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res56 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res57 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res58 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res59 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res60 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res61 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res62 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res63 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res64 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res65 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res66 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res67 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res68 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res69 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res70 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res71 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res72 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res73 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res74 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res75 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res76 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res77 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res78 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res79 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res80 = ua.random()
    ff.write(f'''✅ user-agent успешно Перехвачен:,\n\n
{res} 
{res1} 
{res2} 
{res3} 
{res4} 
{res5} 
{res6} 
{res7} 
{res8} 
{res9} 
{res10} 
{res11} 
{res12} 
{res13} 
{res14} 
{res15} 
{res16} 
{res17} 
{res18} 
{res19} 
{res20} 
{res21} 
{res22} 
{res23} 
{res24} 
{res25} 
{res26} 
{res27} 
{res28} 
{res29} 
{res30} 
{res31} 
{res32} 
{res33} 
{res34} 
{res35} 
{res36} 
{res37} 
{res38} 
{res39} 
{res40} 
{res41} 
{res42} 
{res43} 
{res44} 
{res45} 
{res46} 
{res47} 
{res48} 
{res49} 
{res50} 
{res51} 
{res52} 
{res55} 
{res54} 
{res55} 
{res56} 
{res57} 
{res58} 
{res59} 
{res60} 
{res61} 
{res62} 
{res63} 
{res64} 
{res65} 
{res66} 
{res67} 
{res68} 
{res69} 
{res70} 
{res71} 
{res72} 
{res73} 
{res74} 
{res75} 
{res76} 
{res77} 
{res78} 
{res79} 
{res80} ''')

    ff.close()
    f = open("useragent.txt","rb")
    titleus = (
        f"User-Agent Windows\n"
        f"Количество: 80 шт.")
    await bot.send_document(chat_id,f, caption=titleus)

@dp.callback_query_handler  (text="uss_linux", state="*")
async def link(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    await call.message.delete()
    ff = open('useragent.txt', 'w')
    ua = UserAgent(os_family = 'linux')
    res = ua.random()
    ua = UserAgent(os_family = 'linux')
    res1 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res2 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res3 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res4 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res5 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res6 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res7 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res8 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res9 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res10 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res11 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res12 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res13 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res14 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res15 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res16 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res17 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res18 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res19 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res20 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res21 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res22 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res23 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res24 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res25 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res26 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res27 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res28 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res29 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res30 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res31 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res32 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res33 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res34 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res35 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res36 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res37 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res38 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res39 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res40 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res41 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res42 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res43 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res44 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res45 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res46 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res47 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res48 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res49 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res50 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res51 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res52 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res54 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res55 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res56 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res57 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res58 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res59 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res60 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res61 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res62 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res63 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res64 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res65 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res66 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res67 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res68 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res69 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res70 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res71 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res72 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res73 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res74 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res75 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res76 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res77 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res78 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res79 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res80 = ua.random()
    ff.write(f'''✅ user-agent успешно Перехвачен:,\n\n
{res} 
{res1} 
{res2} 
{res3} 
{res4} 
{res5} 
{res6} 
{res7} 
{res8} 
{res9} 
{res10} 
{res11} 
{res12} 
{res13} 
{res14} 
{res15} 
{res16} 
{res17} 
{res18} 
{res19} 
{res20} 
{res21} 
{res22} 
{res23} 
{res24} 
{res25} 
{res26} 
{res27} 
{res28} 
{res29} 
{res30} 
{res31} 
{res32} 
{res33} 
{res34} 
{res35} 
{res36} 
{res37} 
{res38} 
{res39} 
{res40} 
{res41} 
{res42} 
{res43} 
{res44} 
{res45} 
{res46} 
{res47} 
{res48} 
{res49} 
{res50} 
{res51} 
{res52} 
{res55} 
{res54} 
{res55} 
{res56} 
{res57} 
{res58} 
{res59} 
{res60} 
{res61} 
{res62} 
{res63} 
{res64} 
{res65} 
{res66} 
{res67} 
{res68} 
{res69} 
{res70} 
{res71} 
{res72} 
{res73} 
{res74} 
{res75} 
{res76} 
{res77} 
{res78} 
{res79} 
{res80} ''')

    ff.close()
    f = open("useragent.txt","rb")
    titleus = (
        f"User-Agent Linux\n"
        f"Количество: 80 шт.")
    await bot.send_document(chat_id,f, caption=titleus)



@dp.callback_query_handler  (text="uss_ios", state="*")
async def gen_ios(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    await call.message.delete()
    ff = open('useragent.txt', 'w')
    ua = UserAgent(os_family = 'ios')
    res = ua.random()
    ua = UserAgent(os_family = 'ios')
    res1 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res2 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res3 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res4 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res5 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res6 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res7 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res8 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res9 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res10 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res11 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res12 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res13 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res14 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res15 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res16 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res17 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res18 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res19 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res20 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res21 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res22 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res23 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res24 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res25 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res26 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res27 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res28 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res29 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res30 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res31 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res32 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res33 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res34 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res35 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res36 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res37 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res38 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res39 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res40 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res41 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res42 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res43 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res44 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res45 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res46 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res47 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res48 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res49 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res50 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res51 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res52 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res54 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res55 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res56 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res57 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res58 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res59 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res60 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res61 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res62 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res63 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res64 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res65 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res66 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res67 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res68 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res69 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res70 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res71 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res72 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res73 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res74 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res75 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res76 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res77 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res78 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res79 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res80 = ua.random()
    ff.write(f'''✅ user-agent успешно Перехвачен:,\n\n
{res} 
{res1} 
{res2} 
{res3} 
{res4} 
{res5} 
{res6} 
{res7} 
{res8} 
{res9} 
{res10} 
{res11} 
{res12} 
{res13} 
{res14} 
{res15} 
{res16} 
{res17} 
{res18} 
{res19} 
{res20} 
{res21} 
{res22} 
{res23} 
{res24} 
{res25} 
{res26} 
{res27} 
{res28} 
{res29} 
{res30} 
{res31} 
{res32} 
{res33} 
{res34} 
{res35} 
{res36} 
{res37} 
{res38} 
{res39} 
{res40} 
{res41} 
{res42} 
{res43} 
{res44} 
{res45} 
{res46} 
{res47} 
{res48} 
{res49} 
{res50} 
{res51} 
{res52} 
{res55} 
{res54} 
{res55} 
{res56} 
{res57} 
{res58} 
{res59} 
{res60} 
{res61} 
{res62} 
{res63} 
{res64} 
{res65} 
{res66} 
{res67} 
{res68} 
{res69} 
{res70} 
{res71} 
{res72} 
{res73} 
{res74} 
{res75} 
{res76} 
{res77} 
{res78} 
{res79} 
{res80} ''')

    ff.close()
    f = open("useragent.txt","rb")
    titleus = (
        f"User-Agent IOS\n"
        f"Количество: 80 шт.")
    await bot.send_document(chat_id,f, caption=titleus)


@dp.callback_query_handler  (text="uss_android", state="*")
async def gen_andr(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    await call.message.delete()
    ff = open('useragent.txt', 'w')
    ua = UserAgent(os_family = 'android')
    res = ua.random()
    ua = UserAgent(os_family = 'android')
    res1 = ua.random()
    ua = UserAgent(os_family = 'android')
    res2 = ua.random()
    ua = UserAgent(os_family = 'android')
    res3 = ua.random()
    ua = UserAgent(os_family = 'android')
    res4 = ua.random()
    ua = UserAgent(os_family = 'android')
    res5 = ua.random()
    ua = UserAgent(os_family = 'android')
    res6 = ua.random()
    ua = UserAgent(os_family = 'android')
    res7 = ua.random()
    ua = UserAgent(os_family = 'android')
    res8 = ua.random()
    ua = UserAgent(os_family = 'android')
    res9 = ua.random()
    ua = UserAgent(os_family = 'android')
    res10 = ua.random()
    ua = UserAgent(os_family = 'android')
    res11 = ua.random()
    ua = UserAgent(os_family = 'android')
    res12 = ua.random()
    ua = UserAgent(os_family = 'android')
    res13 = ua.random()
    ua = UserAgent(os_family = 'android')
    res14 = ua.random()
    ua = UserAgent(os_family = 'android')
    res15 = ua.random()
    ua = UserAgent(os_family = 'android')
    res16 = ua.random()
    ua = UserAgent(os_family = 'android')
    res17 = ua.random()
    ua = UserAgent(os_family = 'android')
    res18 = ua.random()
    ua = UserAgent(os_family = 'android')
    res19 = ua.random()
    ua = UserAgent(os_family = 'android')
    res20 = ua.random()
    ua = UserAgent(os_family = 'android')
    res21 = ua.random()
    ua = UserAgent(os_family = 'android')
    res22 = ua.random()
    ua = UserAgent(os_family = 'android')
    res23 = ua.random()
    ua = UserAgent(os_family = 'android')
    res24 = ua.random()
    ua = UserAgent(os_family = 'android')
    res25 = ua.random()
    ua = UserAgent(os_family = 'android')
    res26 = ua.random()
    ua = UserAgent(os_family = 'android')
    res27 = ua.random()
    ua = UserAgent(os_family = 'android')
    res28 = ua.random()
    ua = UserAgent(os_family = 'android')
    res29 = ua.random()
    ua = UserAgent(os_family = 'android')
    res30 = ua.random()
    ua = UserAgent(os_family = 'android')
    res31 = ua.random()
    ua = UserAgent(os_family = 'android')
    res32 = ua.random()
    ua = UserAgent(os_family = 'android')
    res33 = ua.random()
    ua = UserAgent(os_family = 'android')
    res34 = ua.random()
    ua = UserAgent(os_family = 'android')
    res35 = ua.random()
    ua = UserAgent(os_family = 'android')
    res36 = ua.random()
    ua = UserAgent(os_family = 'android')
    res37 = ua.random()
    ua = UserAgent(os_family = 'android')
    res38 = ua.random()
    ua = UserAgent(os_family = 'android')
    res39 = ua.random()
    ua = UserAgent(os_family = 'android')
    res40 = ua.random()
    ua = UserAgent(os_family = 'android')
    res41 = ua.random()
    ua = UserAgent(os_family = 'android')
    res42 = ua.random()
    ua = UserAgent(os_family = 'android')
    res43 = ua.random()
    ua = UserAgent(os_family = 'android')
    res44 = ua.random()
    ua = UserAgent(os_family = 'android')
    res45 = ua.random()
    ua = UserAgent(os_family = 'android')
    res46 = ua.random()
    ua = UserAgent(os_family = 'android')
    res47 = ua.random()
    ua = UserAgent(os_family = 'android')
    res48 = ua.random()
    ua = UserAgent(os_family = 'android')
    res49 = ua.random()
    ua = UserAgent(os_family = 'android')
    res50 = ua.random()
    ua = UserAgent(os_family = 'android')
    res51 = ua.random()
    ua = UserAgent(os_family = 'android')
    res52 = ua.random()
    ua = UserAgent(os_family = 'android')
    res54 = ua.random()
    ua = UserAgent(os_family = 'android')
    res55 = ua.random()
    ua = UserAgent(os_family = 'android')
    res56 = ua.random()
    ua = UserAgent(os_family = 'android')
    res57 = ua.random()
    ua = UserAgent(os_family = 'android')
    res58 = ua.random()
    ua = UserAgent(os_family = 'android')
    res59 = ua.random()
    ua = UserAgent(os_family = 'android')
    res60 = ua.random()
    ua = UserAgent(os_family = 'android')
    res61 = ua.random()
    ua = UserAgent(os_family = 'android')
    res62 = ua.random()
    ua = UserAgent(os_family = 'android')
    res63 = ua.random()
    ua = UserAgent(os_family = 'android')
    res64 = ua.random()
    ua = UserAgent(os_family = 'android')
    res65 = ua.random()
    ua = UserAgent(os_family = 'android')
    res66 = ua.random()
    ua = UserAgent(os_family = 'android')
    res67 = ua.random()
    ua = UserAgent(os_family = 'android')
    res68 = ua.random()
    ua = UserAgent(os_family = 'android')
    res69 = ua.random()
    ua = UserAgent(os_family = 'android')
    res70 = ua.random()
    ua = UserAgent(os_family = 'android')
    res71 = ua.random()
    ua = UserAgent(os_family = 'android')
    res72 = ua.random()
    ua = UserAgent(os_family = 'android')
    res73 = ua.random()
    ua = UserAgent(os_family = 'android')
    res74 = ua.random()
    ua = UserAgent(os_family = 'android')
    res75 = ua.random()
    ua = UserAgent(os_family = 'android')
    res76 = ua.random()
    ua = UserAgent(os_family = 'android')
    res77 = ua.random()
    ua = UserAgent(os_family = 'android')
    res78 = ua.random()
    ua = UserAgent(os_family = 'android')
    res79 = ua.random()
    ua = UserAgent(os_family = 'android')
    res80 = ua.random()
    ff.write(f'''✅ user-agent успешно Перехвачен:,\n
{res} 
{res1} 
{res2} 
{res3} 
{res4} 
{res5} 
{res6} 
{res7} 
{res8} 
{res9} 
{res10} 
{res11} 
{res12} 
{res13} 
{res14} 
{res15} 
{res16} 
{res17} 
{res18} 
{res19} 
{res20} 
{res21} 
{res22} 
{res23} 
{res24} 
{res25} 
{res26} 
{res27} 
{res28} 
{res29} 
{res30} 
{res31} 
{res32} 
{res33} 
{res34} 
{res35} 
{res36} 
{res37} 
{res38} 
{res39} 
{res40} 
{res41} 
{res42} 
{res43} 
{res44} 
{res45} 
{res46} 
{res47} 
{res48} 
{res49} 
{res50} 
{res51} 
{res52} 
{res55} 
{res54} 
{res55} 
{res56} 
{res57} 
{res58} 
{res59} 
{res60} 
{res61} 
{res62} 
{res63} 
{res64} 
{res65} 
{res66} 
{res67} 
{res68} 
{res69} 
{res70} 
{res71} 
{res72} 
{res73} 
{res74} 
{res75} 
{res76} 
{res77} 
{res78} 
{res79} 
{res80} ''')
    ff.close()
    f = open("useragent.txt","rb")
    titleus = (
        f"User-Agent android\n"
        f"Количество: 80 шт.")
    await bot.send_document(chat_id,f, caption=titleus)   


# Обработка кнопки "FAQ"
@dp.message_handler(text="ℹ FAQ", state="*")
async def show_my_deals(message: types.Message, state: FSMContext):
    await state.finish()
    await message.delete()
    send_msg = bot_description
    if "{username}" in send_msg:
        send_msg = send_msg.replace("{username}", f"<b>{message.from_user.username}</b>")
    if "{user_id}" in send_msg:
        send_msg = send_msg.replace("{user_id}", f"<b>{message.from_user.id}</b>")
    if "{firstname}" in send_msg:
        send_msg = send_msg.replace("{firstname}", f"<b>{(message.from_user.first_name)}</b>")
    await message.answer(send_msg, disable_web_page_preview=True)


@dp.callback_query_handler  (text="ip", state="*")
async def reg_url(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.finish()
    await call.message.answer('Введите IP Адрес Жертвы')
    await cicada.ip_up.set()


@dp.message_handler(state=cicada.ip_up)
async def reg_uip(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['cicada.ip_up'] = message.text
            r = requests.get(f"https://api.ipdata.co/{message.text}?api-key=7149ffee49a432bb1c7557e3235afdf78a2d22fcdde3a4ecd7a5d5ca")
            data = json.loads(r.text)
            city = str(data['city'])
            region = str(data['region'])
            country_name = str(data['country_name'])
            country_code = str(data['country_code'])
            continent_name = str(data['continent_name'])
            continent_code = str(data['continent_code'])
            calling_code = str(data['calling_code'])
            latitude = str(data['latitude'])
            longitude = str(data['longitude'])
            postal = str(data['postal'])
            
            time_zone = str(data['time_zone']['name'])
            time_zone2 = str(data['time_zone']['current_time'])
            
            currency = str(data['currency']['name'])
            currency2 = str(data['currency']['code'])
            
            #languages = str(data['languages']['name']) Error = list indices must be integers or slices, not str
            
            await bot.send_message(message.chat.id, f'''<b> 🔎 Результат поиска:</b>

    <b>IP</b> - {message.text}

    ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    <b>Город</b>: <code>{city}</code> | <code>{region}</code>
    <b>Страна</b>: <code>{country_name} ({country_code})</code>
    <b>Часовой пояс</b>: <code>{time_zone}</code>
    <b>Код страны</b>: <code>+{calling_code}</code>
    <b>Широта</b>: <code>{latitude}</code> | <b>Долгота</b>: <code>{longitude}</code>
    <b>Почтовый индекс</b>: <code>{postal}</code>
    <b>Континет</b>: <code>{continent_name} ({continent_code})</code>
    ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    <b>Валюта</b>: <code>{currency} ({currency2})</code>
    <b>Точное время</b>: <code>{time_zone2}</code>
                            ''', parse_mode='HTML')
            #func.act_count_ip("add", message.chat.id,)
        except Exception as e:
            await bot.send_message(message.chat.id, 'Не верный айпи! Попробуйте еще раз')
            print(e)






# Обработка колбэка "Мои покупки"
@dp.callback_query_handler(text="my_buy", state="*")
async def show_referral(call: CallbackQuery, state: FSMContext):
    last_purchases = last_purchasesx(call.from_user.id)
    if len(last_purchases) >= 1:
        await call.message.delete()
        count_split = 0
        save_purchases = []
        for purchases in last_purchases:
            save_purchases.append(f"<b>📃 Код Выдачи:</b> <code>#{purchases[4]}</code>\n"
                                  f"▶ {purchases[9]} | {purchases[5]} шт \n"
                                  f"🕜 {purchases[13]}\n"
                                  f"<code>{purchases[10]}</code>")
        await call.message.answer("<b>ℹ️ Последние 10 запросов</b>\n"
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

        await call.message.answer(get_user_profile(call.from_user.id), reply_markup=open_profile_inl)
    else:
        await call.answer("❗ Ты еще не брал Акаунт(ы)")


################################################################################################
######################################### ПОКУПКА ТОВАРА #######################################
# Открытие категории для покупки
@dp.callback_query_handler(text_startswith="buy_open_category", state="*")
async def open_category_for_buy_item(call: CallbackQuery, state: FSMContext):
    category_id = int(call.data.split(":")[1])
    get_category = get_categoryx("*", category_id=category_id)
    get_positions = get_positionsx("*", category_id=category_id)

    get_kb = buy_item_item_position_ap(0, category_id)
    if len(get_positions) >= 1:
        await call.message.edit_text("<b>🔐 Выберите нужный вам Акаунт(ы):</b>",
                                     reply_markup=get_kb)
    else:
        await call.answer(f"❕ Акаунт(ы) в категории {get_category[2]} отсутствуют.")


# Вернутсья к предыдущей категории при покупке
@dp.callback_query_handler(text_startswith="back_buy_item_to_category", state="*")
async def back_category_for_buy_item(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("<b>🔐 Выберите нужный вам Акаунт(ы):</b>",
                                 reply_markup=buy_item_open_category_ap(0))


# Следующая страница категорий при покупке
@dp.callback_query_handler(text_startswith="buy_category_nextp", state="*")
async def buy_item_next_page_category(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])

    await call.message.edit_text("<b>🔐 Выберите нужный вам Акаунт(ы):</b>",
                                 reply_markup=buy_item_next_page_category_ap(remover))


# Предыдущая страница категорий при покупке
@dp.callback_query_handler(text_startswith="buy_category_prevp", state="*")
async def buy_item_prev_page_category(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])

    await call.message.edit_text("<b>🔐 Выберите нужный вам Акаунт(ы):</b>",
                                 reply_markup=buy_item_previous_page_category_ap(remover))


# Следующая страница позиций при покупке
@dp.callback_query_handler(text_startswith="buy_position_nextp", state="*")
async def buy_item_next_page_position(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])
    category_id = int(call.data.split(":")[2])

    await call.message.edit_text("<b>🔐 Выберите нужный вам Акаунт(ы):</b>",
                                 reply_markup=item_buy_next_page_position_ap(remover, category_id))


# Предыдущая страница позиций при покупке
@dp.callback_query_handler(text_startswith="buy_position_prevp", state="*")
async def buy_item_prev_page_position(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])
    category_id = int(call.data.split(":")[2])

    await call.message.edit_text("<b>🔐 Выберите нужный вам Акаунт(ы):</b>",
                                 reply_markup=item_buy_previous_page_position_ap(remover, category_id))


# Возвращение к страницам позиций при покупке товара
@dp.callback_query_handler(text_startswith="back_buy_item_position", state="*")
async def buy_item_next_page_position(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])
    category_id = int(call.data.split(":")[2])

    await call.message.delete()
    await call.message.answer("<b>🔐 Выберите нужный вам Акаунт(ы):</b>",
                              reply_markup=buy_item_item_position_ap(remover, category_id))


# Открытие позиции для покупки
@dp.callback_query_handler(text_startswith="buy_open_position", state="*")
async def open_category_for_create_position(call: CallbackQuery, state: FSMContext):
    position_id = int(call.data.split(":")[1])
    remover = int(call.data.split(":")[2])
    category_id = int(call.data.split(":")[3])

    get_position = get_positionx("*", position_id=position_id)
    get_category = get_categoryx("*", category_id=category_id)
    get_items = get_itemsx("*", position_id=position_id)

    send_msg = f"<b>🔐 Выбор Акаунта:</b>\n" \
               f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
               f"<b>📜 Категория:</b> <code>{get_category[2]}</code>\n" \
               f"<b>🏷 Название:</b> <code>{get_position[2]}</code>\n" \
               f"<b>📦 Количество:</b> <code>{len(get_items)}шт</code>\n" \
               f"<b>📜 Описание:</b>\n" \
               f"{get_position[4]}\n"
    if len(get_position[5]) >= 5:
        await call.message.delete()
        await call.message.answer_photo(get_position[5],
                                        send_msg,
                                        reply_markup=open_item_func(position_id, remover, category_id))
    else:
        await call.message.edit_text(send_msg,
                                     reply_markup=open_item_func(position_id, remover, category_id))


# Выбор кол-ва товаров для покупки
@dp.callback_query_handler(text_startswith="buy_this_item", state="*")
async def open_category_for_create_position(call: CallbackQuery, state: FSMContext):
    position_id = int(call.data.split(":")[1])

    get_items = get_itemsx("*", position_id=position_id)
    get_position = get_positionx("*", position_id=position_id)
    get_user = get_userx(user_id=call.from_user.id)
    if len(get_items) >= 1:
        if int(get_user[4]) >= int(get_position[3]):
            async with state.proxy() as data:
                data["here_cache_position_id"] = position_id
            await call.message.delete()
            await StorageUsers.here_input_count_buy_item.set()
            await call.message.answer(f"📦 <b>Введите количество Акаунтов для получения</b>\n"
                                      f"▶ От <code>1</code> до <code>3</code>\n"
                                      f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                      f"🏷 Название Акаунта: <code>{get_position[2]}</code>\n"
                                      f"❗❗❗ Вам Доступно: <code>{get_user[4]} шт</code>\n",
                                      reply_markup=all_back_to_main_default)
        else:
            await call.answer("❗ Лимит Исчерпан ❗Для поднятия лимита писать Админу"),
            await call.answer("❗ Для поднятия лимита писать Админу❗")
    else:
        await call.answer("🔐 Акаунтов нет в наличии.")


# Принятие кол-ва товаров для покупки
@dp.message_handler(state=StorageUsers.here_input_count_buy_item)
async def input_buy_count_item(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        position_id = data["here_cache_position_id"]
    get_items = get_itemsx("*", position_id=position_id)
    get_position = get_positionx("*", position_id=position_id)
    get_user = get_userx(user_id=message.from_user.id)

    if message.text.isdigit():
        get_count = int(message.text)
        amount_pay = int(get_position[3]) * get_count
        if len(get_items) >= 1:
            if 1 <= get_count <= len(get_items):
                if int(get_user[4]) >= amount_pay:
                    await state.finish()
                    delete_msg = await message.answer("<b>🔐 Акаунты подготовлены.</b>",
                                                      reply_markup=check_user_out_func(message.from_user.id))

                    await message.answer(f"<b>🔐 Получить Акаут(ы)?</b>\n"
                                         f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                         f"🏷 Название Акаунта: <code>{get_position[2]}</code>\n"
                                         f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                         f"▶ Количество Акаунтов: <code>{get_count} шт</code>\n",
                                         reply_markup=confirm_buy_items(position_id, get_count,
                                                                        delete_msg.message_id))
                else:
                    await message.answer(f"<b>❌ Лимит исчерпан (2 акаунта в сутки).</b>\n"
                                         f"<b>📦 Введите количество Акаунтов для выдачи лимит (3 акаунта в сутки)</b>\n"
                                         f"▶ От <code>1</code> до <code>2</code>\n"
                                         f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                         f"📦 Тебе доступно: <code>{get_user[4]} шт</code>\n"
                                         f"🏷 Название Акаунта: <code>{get_position[2]}</code>\n",
                                         reply_markup=all_back_to_main_default)
            else:
                await message.answer(f"<b>❌ Неверное количество Акаунтов.</b>\n"
                                     f"<b>📦 Введите количество Акаунтов для выдачи</b>\n"
                                     f"▶ От <code>1</code> до <code>2</code>\n"
                                     f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                     f"📦 Тебе доступно: <code>{get_user[4]} шт</code>\n"
                                     f"🏷 Название Акаунтов: <code>{get_position[2]}</code>\n",
                                     reply_markup=all_back_to_main_default)
        else:
            await state.finish()
            await message.answer("<b>❌ Акаунты который ты выбрал закончились</b>",
                                 reply_markup=check_user_out_func(message.from_user.id))
    else:
        await message.answer(f"<b>❌ Данные были введены неверно.</b>\n"
                             f"<b>📦 Введите количество Акаунтов для выдачи</b>\n"
                             f"▶ От <code>1</code> до <code>3</code>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"📦 Тебе доступно: <code>{get_user[4]} шт</code>\n"
                             f"🏷 Название Акаунтов: <code>{get_position[2]}</code>\n",
                             reply_markup=all_back_to_main_default)


# Отмена покупки товара
@dp.callback_query_handler(text_startswith="not_buy_items", state="*")
async def not_buy_this_item(call: CallbackQuery, state: FSMContext):
    message_id = call.data.split(":")[1]
    await call.message.delete()
    await bot.delete_message(call.message.chat.id, message_id)
    await call.message.answer("<b>☑ Ты отменили получение Акаунтов.</b>",
                              reply_markup=check_user_out_func(call.from_user.id))


# Согласие на покупку товара
@dp.callback_query_handler(text_startswith="xbuy_item:", state="*")
async def yes_buy_this_item(call: CallbackQuery, state: FSMContext):
    
    delete_msg = await call.message.answer("<b>🔄 Жди, Акаунты подготавливаются</b>")
    position_id = int(call.data.split(":")[1])
    get_count = int(call.data.split(":")[2])
    message_id = int(call.data.split(":")[3])

    await bot.delete_message(call.message.chat.id, message_id)
    await call.message.delete()

    get_items = get_itemsx("*", position_id=position_id)
    get_position = get_positionx("*", position_id=position_id)
    get_user = get_userx(user_id=call.from_user.id)
    amount_pay = int(get_position[3]) * get_count

    if 1 <= int(get_count) <= len(get_items):
        if int(get_user[4]) >= amount_pay:
            save_items, send_count, split_len = buy_itemx(get_items, get_count)

            if split_len <= 50:
                split_len = 70
            elif split_len <= 100:
                split_len = 50
            elif split_len <= 150:
                split_len = 30
            elif split_len <= 200:
                split_len = 10
            else:
                split_len = 3

            if get_count != send_count:
                amount_pay = int(get_position[3]) * send_count
                get_count = send_count

            random_number = [random.randint(100000000, 999999999)]
            passwd = list("ABCDEFGHIGKLMNOPQRSTUVYXWZ")
            random.shuffle(passwd)
            random_char = "".join([random.choice(passwd) for x in range(1)])
            receipt = random_char + str(random_number[0])
            buy_time = get_dates()

            await bot.delete_message(call.from_user.id, delete_msg.message_id)

            if len(save_items) <= split_len:
                send_message = "\n".join(save_items)
                await call.message.answer(f"<b>🔐 Твои Акаунты:</b>\n"
                                          f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                          f"{send_message}")
            else:
                await call.message.answer(f"<b>🔐 Твои Акаунты:</b>\n"
                                          f"➖➖➖➖➖➖➖➖➖➖➖➖➖")

                save_split_items = split_messages(save_items, split_len)
                for item in save_split_items:
                    send_message = "\n".join(item)
                    await call.message.answer(send_message)
            save_items = "\n".join(save_items)

            add_purchasex(call.from_user.id, call.from_user.username, call.from_user.first_name,
                          receipt, get_count, amount_pay, get_position[3], get_position[1], get_position[2],
                          save_items, get_user[4], int(get_user[4]) - amount_pay, buy_time, int(time.time()))
            update_userx(call.from_user.id, balance=get_user[4] - amount_pay)
            await call.message.answer(f"<b>🔐 Ты получил Акаунт(ы) ✅</b>\n"
                                      f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                      f"🏷 Название Акаунтов: <code>{get_position[2]}</code>\n"
                                      f"📦 Полученно Акаунтов: <code>{get_count}</code>\n"
                                      f"👤 Выданно: <a href='tg://user?id={get_user[1]}'>{get_user[3]}</a> <code>({get_user[1]})</code>\n"
                                      f"🕜 Дата Выдачи: <code>{buy_time}</code>",
                                      reply_markup=check_user_out_func(call.from_user.id))
        else:
            await call.message.answer("<b>❌ Лимит исчерпан (3 акаунта в сутки).</b>")
    else:
        await state.finish()
        await call.message.answer("<b>❌ Акаунты который ты выбрал закончились.</b>",
                                  check_user_out_func(call.from_user.id))
