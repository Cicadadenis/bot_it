# - *- coding: utf- 8 - *-
#
from aiogram.dispatcher.filters.state import State
from handlers.users.admin_functions import send_message_to_user
from aiogram import types
from aiogram.dispatcher import FSMContext

from filters import IsWork, IsUser
from filters.all_filters import IsBuy
from keyboards.default import check_user_out_func, lic
from keyboards.inline import cicada
from keyboards.default.menu import ssaa
from loader import dp, bot
from states import StorageUsers
from states.state_functions import StorageFunctions
from utils.db_api.sqlite import *
from utils.other_func import get_dates
import datetime
import random
import config2
import time
import json
from SystemInfo import SystemInfo
import requests
import sys
import re
import urllib.request
import secrets
import sqlite3
import os
from data.config import adm
import functions as func
from aiogram.dispatcher import FSMContext
from utils.user import *
import utils.mydb
import configparser
from aiogram.dispatcher.filters.state import State, StatesGroup
from typing import Text
from aiogram import types, Bot, Dispatcher
from aiogram import executor
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import secrets
import os, sys
import config
import logging
import kb
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
import io
import aiohttp
from aiogram.dispatcher import FSMContext
from aiogram import Dispatcher
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.types import (ChatType, ContentTypes, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)
from aiogram.utils.markdown import hbold, hlink
from aiogram.utils.exceptions import BadRequest 
import asyncio
from contextlib import suppress
from foto import *
from aiogram import types
from aiogram.utils.exceptions import (MessageToEditNotFound, MessageCantBeEdited, MessageCantBeDeleted,
                                      MessageToDeleteNotFound)
class cicada(StatesGroup):
    sms = State()
    size = State()
    up_y = State()
    up_x = State()
    red = State()
    green = State()
    blue = State()
    ban = State()

sozdatel = 1144785510

config = configparser.ConfigParser()
config.read("Settings")
url = ('http://telegra.ph//file/db14d05e947eb8784ec4d.jpg')
prohibit_buy = ["xbuy_item", "not_buy_items", "buy_this_item", "buy_open_position", "back_buy_item_position",
                "buy_position_prevp", "buy_position_nextp", "buy_category_prevp", "buy_category_nextp",
                "back_buy_item_to_category", "buy_open_category"]

from utils.number import Number
# Проверка на нахождение бота на технических работах
@dp.message_handler(IsWork(), state="*")
@dp.callback_query_handler(IsWork(), state="*")
async def send_work_message(message: types.Message, state: FSMContext):
    if "id" in message:
        await message.answer("🔴 Бот находится на технических работах.")
    else:
        await message.answer("<b>🔴 Бот находится на технических работах.</b>")

lice = []
banned_users = set()


@dp.message_handler(user_id=banned_users)
async def handle_banned(message: types.Message):
    print(f"{message.from_user.full_name} пишет, но мы ему не ответим!")
    return False



@dp.message_handler(commands=['ban'], user_id=1144785510) # здесь укажи свой ID
async def handle_ban_command(message: types.Message):
    # проверяем, что ID передан правильно
    try:
        abuser_id = int(message.get_args())
    except (ValueError, TypeError):
        return await message.reply("Укажи ID пользователя.")
    
    banned_users.add(abuser_id)
    await message.reply(f"Пользователь {abuser_id} заблокирован.")
#


@dp.callback_query_handler(text='ban', state="*")
async def ban_add(call: types.CallbackQuery, state: FSMContext):
    try:
        abuser_id = int(call.message.get_args())
    except (ValueError, TypeError):
        return await call.message.reply("Укажи ID пользователя.")
    
    banned_users.add(abuser_id)
    await call.message.reply(f"Пользователь {abuser_id} заблокирован.")



@dp.message_handler(commands=['start'], state="*",)
@dp.message_handler(text="⬅ На главную", state="*")
async def bot_start(message: types.Message, state: FSMContext):
    pw = re.sub('\/\w+\s', "", message.text)
    await state.finish()
    yuy = int(message.chat.id)
    with open('id.txt', 'w') as f:
        print(yuy, file=f)
    
    first_name = (message.from_user.first_name)
    get_user_id = get_userx(user_id=message.from_user.id)
    rr = open('dostyp.ff', 'r')
    dostyp = rr.read()
    rr.close()
    if get_user_id is None:
        try:
            if pw == dostyp:
                    tt = open('dostyp.ff', 'w')
                    tt.write(secrets.token_urlsafe(15))
                    tt.close()
                    add_userx(message.from_user.id, message.from_user.username.lower(), first_name, 0, 0, get_dates())
                   
                    add_userx(message.from_user.id, message.from_user.username, first_name, 0, 0, get_dates())
                    predyp = (
                        f"🥳🥳🥳 Новый юзер\n"
                        f"      👤: {message.from_user.first_name}\n"
                        f"      🆔: {message.from_user.id}\n"
                        f"      🏷: @{message.from_user.username}")
                    await bot.send_message(chat_id=sozdatel, text=predyp)
                    if first_name != get_user_id[3]:
                        update_userx(get_user_id[1], user_name=first_name)
                    if message.from_user.username is not None:
                        if message.from_user.username.lower() != get_user_id[2]:
                            update_userx(get_user_id[1], user_login=message.from_user.username.lower())
                   # with open('copyright.jpg', 'rb') as photo:
 #                       tesa = (f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
 #   f"<b>              Выдача Акаунтов</b> \n\n"
 #   f"<em>На сутки каждый может взять у бота 3 акаунта:</em>\n\n"
 #   f"Support: <a href='https://t.me/satanasat'>Cicada3301</a>\n"
 #   f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
 #   f"Для дополнительных запросов боту за акаунтами\n"
 #   f"Писвть мне <a href='https://t.me/satanasat'>СЮДА</a>\n"
 #   f"➖➖➖➖➖➖➖➖➖➖➖➖\n")
 #                       await bot.send_photo(message.chat.id, photo, caption=tesa, reply_markup=lic)
#
                        predyp = (
                            f"      ✅🔐 Новый юзер\n\n"
                            f"      👤: {message.from_user.first_name}\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f"      🆔: <code>{message.from_user.id}</code>\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f"      🏷: @{message.from_user.username}"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n")
                        await bot.send_message(chat_id=sozdatel, text=predyp)       
                            
            else:
                usernname = (message.from_user.username)
                usser_add = open('usser', 'w')
                usser_add.write(usernname)
                usser_add.close()
                namme_add = (message.from_user.first_name)
                nm = open('namme','w')
                nm.write(namme_add)
                nm.close()
                idd = (message.from_user.id)
                with open('bloc.jfif', 'rb') as photo:
                    blok = (
                        f"<b>      ❌ У ТЕБЯ НЕТ ДОСТУПА ❌</b>"
                    )
                    await bot.send_photo(message.from_user.id, photo, caption=blok)
                    
                    predyp = (
                            f"      ❌ Попытка Входа ❌\n\n"
                            f"      👤: {message.from_user.first_name}\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f"      🆔: <code>{message.from_user.id}</code>\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f"      🏷: @{message.from_user.username}\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
                            
                    with open('danger.jfif', 'rb') as photo:
                        await bot.send_photo(sozdatel, photo, caption=predyp, reply_markup=ssaa)
                    time.sleep(5)
                    await bot.send_message(message.from_user.id, text='‼️ <b>Про Несанкционированную попытку входа будут узвещены Администраторы Бота </b>')
                    time.sleep(6)
                    await bot.send_message(message.from_user.id, text='‼️ <b>Если Администрация Подтвердит вас я сразу вам сообщю </b>')
                    
        except:
            pass
    else:
        with open('copyright.jpg', 'rb') as photo:
                           
                            
                            llll = (
                                f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f"<b>Я создал код безоастности для этого бота</b>\n"
                                f"<b>Который считывает множество параметров</b>\n"
                                f"<b>Для индификации пользователя.</b>\n"
                                f"<b>И стать пользователем Бота</b>\n"
                                f"<b>Можно лишь по одному единственному способу</b>\n"
                                f"<b>Получив одноразовую ссылку для входа</b>\n"
                                f"<b>От участников из Администрации этого бота</b>\n"
                                f"<b>В этом Боте можно получить от номера на сигнал</b>\n"
                                f"<b>И заканчивая учетной записью на Icloud</b>\n"
                                f"<b>В данный момент я ограничил лимит на получения</b>\n"
                                f"<b>Акаунтов и учетных Записей,</b>\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            )
                            chat_id = message.chat.id
                            try:
                                if chat_id in lice:
                                    await bot.send_message(chat_id, 'Главное Меню',  reply_markup=check_user_out_func(message.from_user.id))
                                else:

                                    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=llll, parse_mode='HTML', reply_markup=lic)
                                    lice.append(chat_id)

                            except:
                                pass



 
@dp.callback_query_handler(text='yes_add')
async def lica_message(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    fir = open('namme', 'r')
    first_add = fir.read()
    fir.close()
    tx = open('usser', 'r')
    us_name = tx.read()
    tx.close()
    iidz = open('id.txt', 'r')
    sete = iidz.read()
    iidz.close()
    print(
        f"{sete}\n"
        f"{us_name}\n"
        f"{first_add}\ns"
    )
    add_userx(sete, us_name, first_add, 0, 0, get_dates())
    predyp = (
        f"🥳🥳🥳 Новый юзер\n"
        f"      👤: {first_add}\n"
        f"      🆔: {sete}\n"
        f"      🏷: @{us_name}")
    await bot.send_message(chat_id=sozdatel, text=predyp)
    await bot.send_message(chat_id=sete, text='✅ <b>Администрация Утвердила вас, Добро пожаловать !!!</b>', reply_markup=check_user_out_func(call.message.from_user.id))
  



@dp.callback_query_handler(text='pr')
async def licenziya_message(message: types.Message):
    
    with open('copyright.jpg', 'rb') as photo:
        await bot.send_photo(message.from_user.id, photo, reply_markup=check_user_out_func(message.from_user.id))

@dp.message_handler(commands=['inf'])
async def send_er_message(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=SystemInfo.get_info_text(), parse_mode='html')
    
    
    
@dp.message_handler(IsUser(), state="*")
@dp.callback_query_handler(IsUser(), state="*")
async def send_user_message(message: types.Message, state: FSMContext):
    await state.finish()

    await bot.send_message(message.from_user.id,
                        "<b>❗ Ваш профиль не был найден.</b>\n"
                        "▶ Введите /start")



       

