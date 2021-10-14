# - *- coding: utf- 8 - *-
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageCantBeDeleted
from keyboards.default.main_settings import get_settings_func
from typing import Text
from aiogram import types
import general as gen
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, message
import requests
from keyboards.default import check_user_out_func
from keyboards.inline import *
from keyboards.inline.inline_page import *
from loader import dp, bot

from data.config import config
from states.state_users import *
from utils.other_func import  get_dates
from states.state_url import cicada
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from aiogram.types.user import User
from Users.Users import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
import time
from data.config import sms_api
from Users.Users import Admin
from handlers.users.main_start import sozdatel
from handlers.users.cicada_menu import cicada
from keyboards.default import check_user_out_func
from loader import dp


# Обработка всех колбэков которые потеряли стейты после перезапуска скрипта
@dp.callback_query_handler(text="...", state="*")
async def processing_missed_callback(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)


# Обработка всех колбэков которые потеряли стейты после перезапуска скрипта
#@dp.callback_query_handler(state="*")
#async def processing_missed_callback(call: CallbackQuery, state: FSMContext):
#    try:
#        await call.message.delete()
#    except MessageCantBeDeleted:
#        pass
#    await call.message.answer("<b>❌ Данные не были найдены из-за перезапуска скрипта.\n"
#                              "♻ Выполните действие заново.</b>",
#                              reply_markup=check_user_out_func(call.from_user.id))


# Обработка всех неизвестных сообщений

 

@dp.message_handler()
async def processing_missed_messages(message: types.Message):
    await message.answer("<b>♦ Неизвестная команда.</b>\n"
                         "▶ Введите /start")
