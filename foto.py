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




@dp.message_handler(text='📸 Штамп на фото')
async def foto_sh(message: types.Message):
    with open('copyright.jpg', 'rb') as photo:
        tesa = (f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
        f"<b>                 Штамп на фото \n       с полным функционалом</b>\n\n"
        f"<em>управления настройками:</em>\n\n"
          f"🖌 Размер текста\n"
          f"®️ Текст штампа\n"
          f"◀️ Отсту по горизонтали\n"
          f"🔼 Отступ по вертикали\n"
          f"📊 Любая цветовая гамма\n"
          f"💱 Подержка всех шрифтов\n\n\n"
          f"Support: <a href='https://t.me/satanasat'>Cicada3301</a>\n"
        f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
        f"Для смены шрифтов качаем любой понравившийся <a href='https://fonts-online.ru/fonts'>ТУТ</a>\n"
        f"И закидываем сам фаил шрифтов боту\n"
        f"➖➖➖➖➖➖➖➖➖➖➖➖\n")
        await bot.send_photo(message.from_user.id, photo, caption=tesa, parse_mode='html', reply_markup=kb.menu_default)


    @dp.callback_query_handler(text="t1", state='*')
    async def send_random_value(call: types.CallbackQuery, state: FSMContext):
        await state.finish()
        await call.message.answer("<b>Введите Текст для добавления Штампа:</b>", parse_mode='html')
        await cicada.sms.set()

    # Добавить Администратора
    @dp.message_handler(state=cicada.sms)
    async def sms_set(message: types.Message, state: FSMContext):
        chat_id = message.chat.id
        async with state.proxy() as data:
            data["cicada.sms"] = str(f"{message.text}")
        await cicada.sms.set()
        try:
            sms_up = data['cicada.sms']
            config2.edit_config('sms', sms_up)
            await state.finish()
            await message.answer(f'Штамп изменен на {sms_up}', reply_markup=kb.nazad)
        except:
            await bot.send_message(chat_id=chat_id,
                                    text=f'⚠️Ошибка\n\nПроверьте правописание команды', reply_markup=kb.nazad)
        

    @dp.callback_query_handler(text="t2", state='*')
    async def send_random_value(call: types.CallbackQuery, state: FSMContext):
        await state.finish()
        await call.message.answer("<b>Введите Цифреное значение для шрифта:</b>", parse_mode='html', reply_markup=kb.nazad)
        await cicada.size.set()

    # Добавить Администратора
    @dp.message_handler(state=cicada.size)
    async def size_set(message: types.Message, state: FSMContext):
        chat_id = message.chat.id
        async with state.proxy() as data:
            data["cicada.size"] = str(message.text)
        await cicada.size.set()
        try:
            size_up = data['cicada.size']
            config2.edit_config('ra', size_up)
            await state.finish()
            await message.answer(f'Размер шрифта изменен на {size_up}', reply_markup=kb.nazad)
        except:
            await bot.send_message(chat_id=chat_id,
                                    text=f'⚠️Ошибка\n\nПроверьте правописание команды', reply_markup=kb.nazad)

    @dp.callback_query_handler(text="t3", state='*')
    async def send_random_value(call: types.CallbackQuery, state: FSMContext):
        await state.finish()
        await call.message.answer("<b>Введите Цифреное значение для Отступа Y:</b>", parse_mode='html', reply_markup=kb.nazad)
        await cicada.up_y.set()

    # Добавить Администратора
    @dp.message_handler(state=cicada.up_y)
    async def up_y_set(message: types.Message, state: FSMContext):
        chat_id = message.chat.id
        async with state.proxy() as data:
            data["cicada.up_y"] = str(message.text)
        await cicada.up_y.set()
        try:
            up_y = data['cicada.up_y']
            config2.edit_config('gor', up_y)
            await state.finish()
            await message.answer(f'Отступ по вертикали изменен на {up_y}', reply_markup=kb.nazad)
        except:
            await bot.send_message(chat_id=chat_id,
                                    text=f'⚠️Ошибка\n\nПроверьте правописание команды', reply_markup=kb.nazad)

    @dp.callback_query_handler(text="t4", state='*')
    async def send_random_value(call: types.CallbackQuery, state: FSMContext):
        await state.finish()
        await call.message.answer("<b>Введите Цифреное значение Отступа X:</b>", parse_mode='html', reply_markup=kb.nazad)
        await cicada.up_x.set()

    # Добавить Администратора
    @dp.message_handler(state=cicada.up_x)
    async def up_x_set(message: types.Message, state: FSMContext):
        chat_id = message.chat.id
        async with state.proxy() as data:
            data["cicada.up_x"] = str(message.text)
        await cicada.up_x.set()
        try:
            up_x = data['cicada.up_x']
            config2.edit_config('ver', up_x)
            await state.finish()
            await message.answer(f'Отступ по вертикали изменен на {up_x}', reply_markup=kb.nazad)
        except:
            await bot.send_message(chat_id=chat_id,
                                    text=f'⚠️Ошибка\n\nПроверьте правописание команды', reply_markup=kb.nazad)


    @dp.callback_query_handler(text="t5", state='*')
    async def send_random_value(call: types.CallbackQuery, state: FSMContext):
        chat_id = call.message.chat.id
        cap_color = ("Введите Цвет в Любом формаре \nЛибо словом либо кодом\nНапример:\nСловом <code>red</code>\nКодом <code>#7CFC00</code>:")
        with open('colors.png', 'rb') as photo:
            await bot.send_photo(chat_id, photo, caption=cap_color, parse_mode='html')
        await cicada.red.set()

    # Добавить Администратора
    @dp.message_handler(state=cicada.red)
    async def red_set(message: types.Message, state: FSMContext):
        chat_id = message.chat.id
        async with state.proxy() as data:
            data["cicada.red"] = str(message.text)
        await cicada.red.set()
        try:
            red = data['cicada.red']
            config2.edit_config('r', red)
            await state.finish()
            await message.answer(f'Значение изменено на {red}', reply_markup=kb.nazad)
        except:
            await bot.send_message(chat_id=chat_id,
                                    text=f'⚠️Ошибка\n\nПроверьте правописание команды', reply_markup=kb.nazad)


    @dp.callback_query_handler(text="back", state='*')
    async def send_random_value(call: types.CallbackQuery, state: FSMContext):
        await call.message.answer('Главное Меню', reply_markup=kb.menu_default)


    @dp.callback_query_handler(text="rem", state='*')
    async def send_random_value(call: types.CallbackQuery, state: FSMContext):
        config2.create_config()
        await call.message.answer('Настройки установленны по умолчанию', reply_markup=kb.nazad)



    @dp.callback_query_handler(text="rem2")
    async def send_random_value(call: types.CallbackQuery):
        chat_id = call.message.chat.id
        r = config2.config('ra')
        shs = config2.config('sms')
        go = config2.config('gor')
        v = config2.config('ver')
        rr =  config2.config('r')
        nast = (
            f"🎟 Текущие Параметры 🎟"
            f"➖➖➖➖➖➖➖➖➖➖\n"
            f"®️ Текст штампа: {shs}\n"
            f"➖➖➖➖➖➖➖➖➖➖\n"
            f"🖌 Размер текста: {r}\n"
            f"➖➖➖➖➖➖➖➖➖➖\n"
            f"🔼 Отступ Вертикаль: {go}\n"
            f"➖➖➖➖➖➖➖➖➖➖\n"
            f"◀️ Отступ Горизонталь: {v}\n"
            f"➖➖➖➖➖➖➖➖➖➖\n"
            f"Цвет: {rr}\n"
            f"➖➖➖➖➖➖➖➖➖➖\n"
        )
        await bot.send_message(chat_id=chat_id, text=nast, parse_mode="HTML",
            reply_markup=kb.nazad)
        

        @dp.message_handler(content_types=["document"])
        async def document_handler(message: types.Message):
            try:
                if message.document.file_name[-3:] == 'ttf':
                    await message.document.download(destination="Carnivale.ttf")
                    await message.answer('Новые Шрифты загружены !', reply_markup=kb.nazad)
                else:
                    await message.answer('Неверный Формат Шрифтов\nШрифты имеют расширение .ttf\nОбразец (font.ttf)', reply_markup=kb.nazad)
            except:
                await message.answer('Неверный Формат Шрифтов')




    @dp.message_handler(content_types=["photo"])
    async def download_photo(message: types.Message, sleep_time: int = 5):
        chat_id = message.chat.id
        password = secrets.token_urlsafe(5)
        try:
            await message.photo[-1].download(destination=f"{password}cicada.jpg")
        except:
            await message.photo[-1].download(destination=f"{password}cicada.jpg")
        try:
            img = Image.open(f"{password}cicada.jpg")
        except:
            img = Image.open(f"{password}cicada.jpg")
        #with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        #   await message.delete()
        draw = ImageDraw.Draw(img)
        r = config2.config('ra')
        font = ImageFont.truetype("Carnivale.ttf", int(r))
        shs = config2.config('sms')
        v = config2.config('ver')
        go = config2.config('gor')
        vv = int(v)
        gg = int(go)
        rr =  config2.config('r')
        draw.text((vv, gg), shs, rr,font=font, align ="left")
        img.save(f'{password}.jpg')
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{password}cicada.jpg')
        os.remove(path)
        with io.open(f'{password}.jpg', 'rb') as file:
            form = aiohttp.FormData()
            form.add_field(
                name="file",
                value=file,
            )
            async with bot.session.post("https://telegra.ph/upload", data=form) as response:
                img_src = await response.json()

        link = "http://telegra.ph/" + img_src[0]["src"]
        with open(f'{password}.jpg', 'rb') as photo:
            await message.reply(f"✓ Изображение загружено \n{link} ", disable_web_page_preview=True) 
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{password}.jpg')
        os.remove(path)
    


    @dp.callback_query_handler(text="red")
    async def send_random_value(call: types.CallbackQuery):
        await call.message.answer('da')

    @dp.callback_query_handler(text="seting")
    async def send_random_value(call: types.CallbackQuery):
        chat_id = call.message.chat.id
        cap_seting = 'Меню настроеек Штампа'
        with open('copyright.jpg', 'rb') as photo:
            await bot.send_photo(chat_id, photo, caption=cap_seting, reply_markup=kb.menu_setings)