from utils.mydb import *
from utils.user import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from os import system
import config
import requests
import json
import time
import asyncio


class Number():

    def __init__(self):
        conn, cursor = connect()

        cursor.execute(f'SELECT * FROM numbers')
        self.numbers = cursor.fetchall()

    async def get_list_code(self, state=0):
        if state == 0:
            code_list = []

            for i in self.numbers:
                code_list.append(i[0])
        elif state == 1:
            code_list = ''

            for i in self.numbers:
                code_list += f'{i[0]} - {i[1]}\n'

        return code_list

    async def request_info_from_sms_activate(self, country):
        with open(f'docs/country_{country.split(":")[0]}.txt', 'r', encoding='UTF-8') as txt:
            return json.loads(txt.read())

    async def get_info_number(self, code, user_id):
        conn, cursor = connect()

        cursor.execute(f'SELECT * FROM numbers WHERE code = "{code}"')
        __service = cursor.fetchone()

        msg = f""" 
❕ Ваш баланс - {User(user_id).balance} руб
❕ В наличии:
➖➖➖➖➖➖➖➖
    """

        for i in range(2, len(__service)-1):
            if __service[i] == '0':
                break

            qty = await self.request_info_from_sms_activate(__service[i])
            ot2 = 'ot'

            msg += f'\n{await self.get_country_name(__service[i].split(":")[0])} | {qty[f"{code}_0"]}'

        return msg

    async def get_country_name(self, country_code):
        base = {
            '0': '🇷🇺 Россия',
            '1': '🇺🇦 Украина',
            '2': '🇰🇿 Казахстан',
            '51': '🇧🇾 Беларусь',
            '12': '🇺🇸 США',
            '15': '🇵🇱 Польша',
            '40': '🇺🇿 Узбекистан',
            '32': '🇷🇴 Румыния',
            '117': '🇵🇹 Португалия',
            '16': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 Англия',
            '86': '🇮🇹 Италия',
            '175': '🇦🇺 Австралия',
            '83': '🇧🇬 Болгария',
            '187': '🇺🇸 США',
            '56': '🇪🇸 Испания',
            '43': '🇩🇪 Германия',
            '36': '🇨🇦 Канада',
            '48': '🇳🇱 Нидерланды',
        }

        return base.get(country_code)

    async def get_menu(self, code):
        conn, cursor = connect()
        cursor.execute(f'SELECT * FROM numbers WHERE code = "{code}"')
        __service = cursor.fetchone()
        ot2 = 'ot'

        menu = types.InlineKeyboardMarkup(row_width=2)

        for i in range(2, len(__service)):
            if __service[i] == '0':
                break
            menu.add(
                types.InlineKeyboardButton(text=f'{await self.get_country_name(__service[i].split(":")[0])}',
                                           callback_data=f'buy_num:{code}:{__service[i].split(":")[0]}'),
            )

        menu.add(types.InlineKeyboardButton(text='🔙', callback_data='to_close'))

        return menu

    async def get_price(self, number_code, country):
        conn, cursor = connect()
        cursor.execute(f'SELECT * FROM numbers WHERE code = "{number_code}"')
        __service = cursor.fetchone()

        for i in range(2, len(__service) - 1):
            if __service[i].split(':')[0] == str(country):
                return float(__service[i].split(':')[1])

    async def buy(self, number_code, country):
        url = f'https://sms-activate.ru/stubs/handler_api.php?api_key={config.config(f"api_smsactivate")}&action=getNumber&service={number_code}&forward=0&operator=any&ref=123614&country={country}'

        response = requests.post(url)
        response = response.text

        return response

    async def buy_number(self, bot, number_code, country, user_id):
        response = await self.buy(number_code, country)

        status = 0
        operation_ID = 0
        number = 0

        try:
            status = response.split(':')[0]
            operation_ID = response.split(':')[1]
            number = response.split(':')[2]
            ot2 = 'ot'
        except:
            pass
        
        if str(status) == 'ACCESS_NUMBER':
            ot2 = 'ot'
            url2 = f'https://sms-activate.ru/stubs/handler_api.php?api_key={config.config("api_smsactivate")}&action=setStatus&status=1&id={operation_ID}'
            response2 = requests.post(url2)
            
            price = await self.get_price(number_code, country)
            User(user_id).update_balance(-price)

            status = True
        elif str(status) == 'NO_NUMBERS':
            status = False
        else:
            status = False

        if status:
            await bot.send_message(
                chat_id=user_id,
                text=f"""
Сервис: {await self.get_service_name(number_code)}
Ваш номер: {number}
Ожидайте прихода смс

<i>Если смс не прийдет через 3 минуты 30 секунд, то вам вернуться потраченные деньги за этот номер, аренда номера будет отменена!!!</i>""",
                parse_mode='html',
                reply_markup=await self.get_menu_number_cancel(operation_ID, price)#menu.number_cancel(resp[2], resp[3])
            )

            try:
                await self.number_logs(user_id, number_code, operation_ID, number, 'buy', price, time.time())
            except: pass

            chat = await bot.get_chat(user_id)

            try:
                await bot.send_message(chat_id=config.config("CHANNEL_ID2"),
                                 text=f'📱 {user_id}/{chat.username}/{chat.first_name} заказал номер {number}')
            except:
                pass

            conn, cursor = connect()

            cursor.execute(
                f'INSERT INTO wait_list_number VALUES ("{user_id}", "{operation_ID}", "{number}", "{number_code}", "{country}", "first", "{time.time()}","{price}")')
            conn.commit()

        else:
            await bot.send_message(
                chat_id=user_id,
                text=f'<i>На данный момент номеров нет, ожидайте пополнения!</i>',
                parse_mode='html'
            )

    async def get_service_name(self, number_code):
        conn, cursor = connect()
        cursor.execute(f'SELECT * FROM numbers WHERE code = "{number_code}"')
        __service = cursor.fetchone()

        return __service[1]

    async def get_menu_number_cancel(self, operation_ID, price):
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton(text='❌ Отменить', callback_data=f'number_cancel:{price}:{operation_ID}')
        )

        return markup

    async def number_logs(self, user_id, service, operation_id, number, status, price, date):
        conn, cursor = connect()

        cursor.execute(f'INSERT INTO number_logs VALUES ("{user_id}", "{service}", "{operation_id}", "{number}", "{status}", "{price}", "{date}")')
        conn.commit()

    @staticmethod
    async def check_sms(operation_ID):
        url = f'https://sms-activate.ru/stubs/handler_api.php?api_key={config.config(f"sms-activate.ru")}&action=getStatus&id={operation_ID}'

        response = requests.post(url)
        response = response.text

        return response

    async def get_sms(self, bot, operation_ID):
        response = await self.check_sms(operation_ID)

        try:
            status = response.split(':')[0]
            sms = response.split(':')[1]
        except:
            pass

        await self.get_data_operation(operation_ID)

        if str(status) == 'STATUS_OK':

            if self.status == 'second':
                try:
                    await self.number_logs(self.user_id, self.number_code, operation_ID, self.number, 'good_sms2', self.price, time.time())
                except:
                    pass

                await bot.send_message(
                    chat_id=self.user_id,
                    text=f'Номер: <code>{self.number}</code>\n'
                         f'ПОВТОРНЫЙ КОД: <code>{sms}</code>',
                    parse_mode='html'
                )
                await self.del_operation(operation_ID)
            else:
                try:
                    await self.number_logs(self.user_id, self.number_code, operation_ID, self.number, 'good_sms', self.price, time.time())
                except:
                    pass

                await bot.send_message(
                    chat_id=self.user_id,
                    text=f'Номер: <code>{self.number}</code>\n'
                         f'КОД: <code>{sms}</code>',
                    reply_markup=await self.get_buy_num_menu(operation_ID, self.number),
                    parse_mode='html')

                try:
                    await bot.send_message(
                        chat_id=config.config("CHANNEL_ID2"),
                        text=f'<code>{self.user_id}</code> Получил код(<code>{sms}</code>) для номера <code>{self.number}</code>',
                        parse_mode='html'
                    )
                except:
                    pass

                await self.set_status_operation(operation_ID, 'wait')

        else:
            if self.status == 'second':
                if time.time() - self.purchase_time >= 600:
                    try:
                        await self.number_logs(self.user_id, self.number_code, operation_ID, self.number, 'bad_sms2', self.price, time.time())
                    except:
                        pass

                    await bot.send_message(
                        chat_id=self.user_id,
                        text=f'Повторный код для номера <code>{self.number}</code> не пришел, работа с номером завершена',
                        parse_mode='html'
                    )

                    await self.number_cancel(operation_ID)
                    await self.del_operation(operation_ID)

                    try:
                        await bot.send_message(
                            chat_id=config.config("CHANNEL_ID2"),
                            text=f'Повторный код для номера <code>{self.number}</code> не пришел, <code>{self.user_id}</code> работа с номером завершена',
                            parse_mode='html'

                        )
                    except:
                        pass

            print(f'TIME | {User(self.user_id).username} = {time.time() - self.purchase_time}')

            if self.status == 'first':
                if time.time() - self.purchase_time >= 210:
                    if await self.number_cancel(operation_ID) == True:
                        try:
                            await self.number_logs(self.user_id, self.number_code, operation_ID, self.number, 'bad_sms', self.price,
                                                   time.time())
                        except:
                            pass

                        await bot.send_message(
                            chat_id=self.user_id,
                            text=f'Код для номера <code>{self.number}</code> не пришел, вам будут возвращены деньги',
                            parse_mode='html'
                        )

                        User(self.user_id).update_balance(self.price)

                    try:
                        await bot.send_message(
                            chat_id=config.config("CHANNEL_ID2"),
                            text=f'Код для номера <code>{self.number}</code> не пришел, <code>{self.user_id}</code> будут возвращены деньги',
                            parse_mode='html')
                    except:
                        pass

                    await self.del_operation(operation_ID)

    async def set_status_operation(self, operation_ID, status):
        conn, cursor = connect()

        cursor.execute(f'UPDATE wait_list_number SET status = "{status}" WHERE operation_ID = "{operation_ID}"')
        conn.commit()

    async def del_operation(self, operation_ID):
        conn, cursor = connect()

        cursor.execute(f'DELETE FROM wait_list_number WHERE operation_ID = "{operation_ID}"')
        conn.commit()

    async def get_data_operation(self, operation_ID):
        conn, cursor = connect()
        cursor.execute(f'SELECT * FROM wait_list_number WHERE operation_ID = "{operation_ID}"')
        operation = cursor.fetchone()

        self.user_id = operation[0]
        self.operation_ID = operation[1]
        self.number = operation[2]
        self.number_code = operation[3]
        self.country = operation[4]
        self.status = operation[5]
        self.purchase_time = operation[6]
        self.price = operation[7]

    async def get_buy_num_menu(self, operation_ID, number):
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton(text='✅ Завершить заказ', callback_data=f'num_end:{operation_ID}'),
            types.InlineKeyboardButton(text='🔂 Запросить еще смс', callback_data=f'num_req:{operation_ID}:{number}')
        )

        return markup

    async def number_cancel(self, operation_ID):
        url = f'https://sms-activate.ru/stubs/handler_api.php?api_key={config.config("api_smsactivate")}&action=setStatus&status=8&id={operation_ID}'
        response = requests.post(url)
 
        if response.text == 'BAD_STATUS':
            return False
        elif response.text == 'ACCESS_CANCEL':
            return True

    async def number_iteration(self, operation_ID):
        url = f'https://sms-activate.ru/stubs/handler_api.php?api_key={config.config("api_smsactivate")}&action=setStatus&status=3&id={operation_ID}'
        response = requests.post(url)

        return True

    async def buy_number_menu(self):
        conn, cursor = connect()

        cursor.execute(f'SELECT * FROM numbers')
        numbers = cursor.fetchall()

        markup = types.InlineKeyboardMarkup(row_width=2)

        x1 = 0
        x2 = 1
        try:
            for i in range(len(numbers)):
                markup.add(
                    types.InlineKeyboardButton(text=f'{numbers[x1][1]}',
                                               callback_data=f'{numbers[x1][0]}'),
                    types.InlineKeyboardButton(text=f'{numbers[x2][1]}',
                                               callback_data=f'{numbers[x2][0]}'),
                )
                x1 += 2
                x2 += 2
        except Exception as e:
            try:
                markup.add(
                    types.InlineKeyboardButton(text=f'{numbers[x1][1]}',
                                               callback_data=f'{numbers[x1][0]}'))
            except:
                return markup

        markup.add(
            types.InlineKeyboardButton(text='Выйти', callback_data='exit_to_menu')
        )

        return markup

    async def set_price(self, bot, chat_id, number_code, country, price):

        for i in self.numbers:
            if i[0] == number_code:
                for j in range(2, len(i)-1):
                    if i[j].split(':')[0] == country:
                        conn, cursor = connect()
                        cursor.execute(f'UPDATE numbers SET country{j-1} = "{country}:{price}" WHERE code = "{number_code}"')
                        conn.commit()

                        await bot.send_message(chat_id=chat_id, text=f'Вы изменили цену на {price} ₽')

                        return

        await bot.send_message(chat_id=chat_id, text='Сервис не найден')
   